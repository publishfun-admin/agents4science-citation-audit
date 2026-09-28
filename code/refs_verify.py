"""Verify reference entries against bibliographic databases (Crossref, OpenAlex, arXiv, DBLP) and URL liveness.

Deterministic, cached, rate-limited. Produces a verdict per entry with the evidence used, so that the
manual adjudication step only has to look at UNVERIFIED entries.
"""
import json, os, re, sys, time, urllib.request, urllib.parse, urllib.error, xml.etree.ElementTree as ET
from rapidfuzz import fuzz
from unidecode import unidecode

UA = 'publishfun-firstpaper-research/0.1 (mailto:admin@publish.fun)'
CACHE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'cache', 'api_cache.json')
_cache = json.load(open(CACHE_PATH)) if os.path.exists(CACHE_PATH) else {}
_last = {}
GAPS = {'api.crossref.org': 0.3, 'api.openalex.org': 0.15, 'export.arxiv.org': 3.2, 'dblp.org': 1.0, 'doi.org': 0.3}

def _save_cache():
    json.dump(_cache, open(CACHE_PATH, 'w'))

def http(url, headers=None, kind='json', max_tries=3, timeout=25):
    key = url
    if key in _cache: return _cache[key]
    host = urllib.parse.urlparse(url).netloc
    wait = 3
    for attempt in range(max_tries):
        gap = GAPS.get(host, 0.5) - (time.time() - _last.get(host, 0))
        if gap > 0: time.sleep(gap)
        req = urllib.request.Request(url, headers={'User-Agent': UA, **(headers or {})})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                _last[host] = time.time()
                body = r.read().decode('utf-8', 'replace')
                try:
                    val = json.loads(body) if kind == 'json' else body
                except Exception:
                    _cache[key] = None; return None
                _cache[key] = val
                if len(_cache) % 25 == 0: _save_cache()
                return val
        except urllib.error.HTTPError as e:
            _last[host] = time.time()
            if e.code == 404: _cache[key] = None; return None
            if e.code in (429, 500, 502, 503, 504): time.sleep(wait); wait = min(wait * 2, 20); continue
            _cache[key] = None; return None
        except Exception:
            _last[host] = time.time(); time.sleep(wait); wait *= 2
    return None

def norm(s):
    s = unidecode(str(s or '')).lower()
    s = re.sub(r'[^a-z0-9 ]+', ' ', s)
    return re.sub(r'\s+', ' ', s).strip()

STOP = set('the a an of and in on for to with by from at as is are be via its into over under toward towards using'.split())
def title_match(title, entry):
    """Return (containment, partial_ratio): share of informative title tokens found in the entry, and fuzzy partial ratio."""
    t, e = norm(title), norm(entry)
    toks = [w for w in t.split() if len(w) >= 3 and w not in STOP]
    if not toks: return 0.0, 0
    etoks = set(e.split())
    cont = sum(1 for w in toks if w in etoks) / len(toks)
    return cont, fuzz.partial_ratio(t, e) if len(t) >= 12 else 0

def surname_in_entry(name, entry):
    if not name: return None
    return norm(name).split()[-1] in set(norm(entry).split()) if norm(name) else None

# ---------- sources ----------
def crossref_doi(doi):
    d = http('https://api.crossref.org/works/' + urllib.parse.quote(doi, safe=''))
    if not d: return None
    m = d['message']
    return _cr_rec(m)

def _cr_rec(m):
    y = None
    for k in ('published-print', 'published-online', 'issued', 'created'):
        dp = (m.get(k) or {}).get('date-parts')
        if dp and dp[0] and dp[0][0]: y = dp[0][0]; break
    auth = m.get('author') or []
    return {'source': 'crossref', 'doi': m.get('DOI'), 'title': (m.get('title') or [''])[0],
            'year': y, 'first_author': (auth[0].get('family') if auth else None),
            'container': (m.get('container-title') or [''])[0], 'type': m.get('type'), 'score': m.get('score')}

def crossref_biblio(q, rows=5):
    d = http('https://api.crossref.org/works?' + urllib.parse.urlencode({'query.bibliographic': q[:500], 'rows': rows, 'select': 'DOI,title,author,issued,container-title,score,type,published-print,published-online,created'}))
    if not d: return []
    return [_cr_rec(m) for m in d['message']['items']]

def openalex_search(q, per_page=5):
    d = http('https://api.openalex.org/works?' + urllib.parse.urlencode({'search': q[:300], 'per-page': per_page, 'select': 'id,doi,title,publication_year,authorships,primary_location,type'}))
    if not d: return []
    out = []
    for w in d.get('results', []):
        a = w.get('authorships') or []
        fa = (a[0].get('author') or {}).get('display_name') if a else None
        src = ((w.get('primary_location') or {}).get('source') or {}).get('display_name')
        out.append({'source': 'openalex', 'id': w.get('id'), 'doi': w.get('doi'), 'title': w.get('title') or '', 'year': w.get('publication_year'), 'first_author': fa, 'container': src, 'type': w.get('type')})
    return out

def arxiv_by_id(aid):
    body = http('https://export.arxiv.org/api/query?' + urllib.parse.urlencode({'id_list': aid, 'max_results': 1}), kind='text')
    if not body: return None
    ns = {'a': 'http://www.w3.org/2005/Atom'}
    root = ET.fromstring(body)
    e = root.find('a:entry', ns)
    if e is None or e.findtext('a:title', '', ns).strip() == 'Error': return None
    title = ' '.join(e.findtext('a:title', '', ns).split())
    if not title: return None
    auth = [x.findtext('a:name', '', ns) for x in e.findall('a:author', ns)]
    pub = e.findtext('a:published', '', ns)
    return {'source': 'arxiv', 'arxiv': aid, 'title': title, 'year': int(pub[:4]) if pub else None, 'first_author': auth[0] if auth else None}

def arxiv_title_search(q):
    words = re.findall(r'[A-Za-z0-9]{3,}', q)[:8]
    if len(words) < 3: return []
    body = http('https://export.arxiv.org/api/query?' + urllib.parse.urlencode({'search_query': ' AND '.join('ti:' + w for w in words), 'max_results': 5}), kind='text')
    if not body: return []
    ns = {'a': 'http://www.w3.org/2005/Atom'}
    out = []
    for e in ET.fromstring(body).findall('a:entry', ns):
        title = ' '.join(e.findtext('a:title', '', ns).split())
        auth = [x.findtext('a:name', '', ns) for x in e.findall('a:author', ns)]
        pub = e.findtext('a:published', '', ns)
        aid = e.findtext('a:id', '', ns).split('/abs/')[-1]
        out.append({'source': 'arxiv', 'arxiv': aid, 'title': title, 'year': int(pub[:4]) if pub else None, 'first_author': auth[0] if auth else None})
    return out

def dblp_search(q):
    d = http('https://dblp.org/search/publ/api?' + urllib.parse.urlencode({'q': q[:200], 'format': 'json', 'h': 5}), max_tries=1, timeout=15)
    if not d: return []
    out = []
    for h in (d.get('result', {}).get('hits', {}).get('hit') or []):
        i = h.get('info', {})
        au = i.get('authors', {}).get('author')
        if isinstance(au, dict): au = [au]
        fa = au[0].get('text') if au else None
        out.append({'source': 'dblp', 'title': (i.get('title') or '').rstrip('.'), 'year': int(i['year']) if i.get('year') else None, 'first_author': fa, 'container': i.get('venue'), 'doi': i.get('doi')})
    return out

def url_status(url):
    key = 'HEAD ' + url
    if key in _cache: return _cache[key]
    st = None
    for method in ('HEAD', 'GET'):
        try:
            req = urllib.request.Request(url, method=method, headers={'User-Agent': 'Mozilla/5.0 (research; +mailto:admin@publish.fun)'})
            with urllib.request.urlopen(req, timeout=20) as r: st = r.status; break
        except urllib.error.HTTPError as e:
            st = e.code
            if method == 'HEAD' and e.code in (403, 405): continue
            break
        except Exception: st = 'error'
    _cache[key] = st; return st

# ---------- title guess ----------
def guess_title(entry):
    """Heuristic: quoted segment, else the longest sentence-like segment between periods with >=4 words and no 'et al'."""
    m = re.search(r'[“"]([^”"]{12,})[”"]', entry)
    if m: return m.group(1).strip(' .,')
    segs = [s.strip() for s in re.split(r'(?<=[a-z0-9\)\?])\.\s+(?=[A-Z])', entry)]
    segs = [s for s in segs if len(s.split()) >= 4 and 'et al' not in s.lower() and not re.search(r'\b(19|20)\d{2}\b', s[:6])]
    segs = [re.sub(r'^\d{4}[a-z]?\.?\s*', '', s) for s in segs]
    if not segs: return None
    # prefer segments without many commas (author lists have many commas) and not starting with 'In '
    segs = sorted(segs, key=lambda s: (s.count(',') > 3, s.lower().startswith('in '), -len(s)))
    return segs[0].strip(' .,')

# ---------- verdict ----------
def _accept(cand, entry_raw, year, strict=True):
    cont, pr = title_match(cand.get('title', ''), entry_raw)
    y = cand.get('year'); year_ok = (year is None or y is None or abs(int(y) - int(year)) <= 1)
    fa_ok = surname_in_entry(cand.get('first_author'), entry_raw)
    ok = (cont >= 0.85 and pr >= 85 and (year_ok or fa_ok)) or (cont >= 0.95 and year_ok) or (cont >= 0.75 and pr >= 90 and year_ok and fa_ok)
    return ok, {'containment': round(cont, 3), 'partial_ratio': pr, 'year_ok': year_ok, 'first_author_ok': fa_ok}

def verify_entry(e, do_arxiv_search=True):
    raw, year = e['raw'], e.get('year')
    ev = []
    # 1) DOI
    if e.get('doi'):
        rec = crossref_doi(e['doi'])
        if rec:
            ok, m = _accept(rec, raw, year)
            if ok: return {'verdict': 'VERIFIED', 'via': 'doi', 'match': rec, 'metrics': m, 'evidence': ev}
            ev.append({'step': 'doi_resolves_title_mismatch', 'rec': rec, 'metrics': m})
        else:
            ev.append({'step': 'doi_not_resolvable', 'doi': e['doi']})
    # 2) arXiv id
    if e.get('arxiv'):
        rec = arxiv_by_id(e['arxiv'])
        if rec:
            ok, m = _accept(rec, raw, year)
            if ok: return {'verdict': 'VERIFIED', 'via': 'arxiv_id', 'match': rec, 'metrics': m, 'evidence': ev}
            ev.append({'step': 'arxiv_id_resolves_title_mismatch', 'rec': rec, 'metrics': m})
        else:
            ev.append({'step': 'arxiv_id_not_found', 'arxiv': e['arxiv']})
    # 3) Crossref bibliographic
    best = None
    for c in crossref_biblio(raw):
        ok, m = _accept(c, raw, year)
        if ok: return {'verdict': 'VERIFIED', 'via': 'crossref_biblio', 'match': c, 'metrics': m, 'evidence': ev}
        if best is None or m['containment'] > best[1]['containment']: best = (c, m)
    if best: ev.append({'step': 'crossref_best_reject', 'rec': best[0], 'metrics': best[1]})
    # 4) OpenAlex + DBLP on the title guess (and on the raw string for OpenAlex)
    tg = guess_title(raw)
    for q in ([tg] if tg else []) + [raw]:
        for c in openalex_search(q):
            ok, m = _accept(c, raw, year)
            if ok: return {'verdict': 'VERIFIED', 'via': 'openalex', 'match': c, 'metrics': m, 'evidence': ev, 'title_guess': tg}
    if tg:
        for c in dblp_search(tg):
            ok, m = _accept(c, raw, year)
            if ok: return {'verdict': 'VERIFIED', 'via': 'dblp', 'match': c, 'metrics': m, 'evidence': ev, 'title_guess': tg}
        if do_arxiv_search:
            for c in arxiv_title_search(tg):
                ok, m = _accept(c, raw, year)
                if ok: return {'verdict': 'VERIFIED', 'via': 'arxiv_search', 'match': c, 'metrics': m, 'evidence': ev, 'title_guess': tg}
    # 5) URL-only resources (software, datasets, web pages)
    urls = [u for u in e.get('urls', []) if not re.search(r'doi\.org|arxiv\.org', u)]
    if urls:
        sts = {u: url_status(u) for u in urls[:3]}
        if any(s == 200 for s in sts.values()):
            return {'verdict': 'VERIFIED_URL', 'via': 'url', 'url_status': sts, 'evidence': ev, 'title_guess': tg}
        ev.append({'step': 'urls_not_live', 'url_status': sts})
    return {'verdict': 'UNVERIFIED', 'evidence': ev, 'title_guess': tg}

def verify_paper(extracted, do_arxiv_search=True):
    out = []
    for e in extracted['entries']:
        v = verify_entry(e, do_arxiv_search=do_arxiv_search)
        out.append({**e, **v})
    _save_cache()
    return out

if __name__ == '__main__':
    sys.path.insert(0, os.path.dirname(__file__))
    from refs_extract import extract
    for p in sys.argv[1:]:
        ex = extract(p)
        res = verify_paper(ex)
        from collections import Counter
        print(p, Counter(r['verdict'] for r in res))
        for r in res:
            tag = r['verdict'] + ('/' + r['via'] if r.get('via') else '')
            print(f"  [{r['idx']}] {tag:24s} {r['raw'][:110]}")
            if r['verdict'] == 'UNVERIFIED':
                print(f"        title_guess={r.get('title_guess')!r}; evidence={[x['step'] for x in r['evidence']]}")


# ---------- title-aware verification (AnyStyle records) ----------
def _title_sim(a, b):
    na, nb = norm(a), norm(b)
    if not na or not nb: return 0
    return max(fuzz.ratio(na, nb), fuzz.token_set_ratio(na, nb) if abs(len(na) - len(nb)) < 40 else 0)

def _accept_parsed(cand, e):
    """Candidate matches a parsed entry if titles agree strongly and year/author do not contradict."""
    t = e.get('title') or ''
    sim = _title_sim(cand.get('title', ''), t) if t else 0
    cont, pr = title_match(cand.get('title', ''), e['raw'])
    y, ey = cand.get('year'), e.get('year')
    year_ok = (ey is None or y is None or abs(int(y) - int(ey)) <= 1)
    fa = cand.get('first_author')
    fa_ok = None
    if fa and e.get('authors'):
        fa_ok = norm(fa).split()[-1] in {norm(a).split()[-1] for a in e['authors'] if norm(a)}
    elif fa:
        fa_ok = surname_in_entry(fa, e['raw'])
    ok = ((sim >= 92 and (year_ok or fa_ok)) or (sim >= 85 and year_ok and fa_ok) or
          (cont >= 0.9 and pr >= 90 and year_ok and (fa_ok is not False)))
    return ok, {'title_sim': sim, 'containment': round(cont, 3), 'partial_ratio': pr, 'year_ok': year_ok, 'first_author_ok': fa_ok}

def verify_parsed(e, do_arxiv_search=True):
    ev = []
    def done(via, rec, m): return {'verdict': 'VERIFIED', 'via': via, 'match': rec, 'metrics': m, 'evidence': ev}
    def id_ok(rec):
        # an identifier that resolves to a work whose title is contained in the raw entry is decisive
        ok, m = _accept_parsed(rec, e)
        if ok: return True, m
        cont, pr = title_match(rec.get('title', ''), e['raw'])
        if cont >= 0.9 or pr >= 95: return True, {**m, 'containment': round(cont, 3), 'partial_ratio': pr, 'rule': 'id+raw_containment'}
        return False, m
    if e.get('doi'):
        rec = crossref_doi(e['doi'])
        if rec:
            ok, m = id_ok(rec)
            if ok: return done('doi', rec, m)
            ev.append({'step': 'doi_resolves_title_mismatch', 'rec': rec, 'metrics': m})
        else: ev.append({'step': 'doi_not_resolvable', 'doi': e['doi']})
    if e.get('arxiv'):
        rec = arxiv_by_id(e['arxiv'])
        if rec:
            ok, m = id_ok(rec)
            if ok: return done('arxiv_id', rec, m)
            rec1 = arxiv_by_id(e['arxiv'].split('v')[0] + 'v1') if not re.search(r'v\d+$', e['arxiv']) else None
            if rec1 and rec1.get('title') != rec.get('title'):
                ok1, m1 = id_ok(rec1)
                if ok1: return done('arxiv_id_v1', rec1, {**m1, 'note': 'title matches an earlier arXiv version'})
            ev.append({'step': 'arxiv_id_resolves_title_mismatch', 'rec': rec, 'metrics': m})
        else: ev.append({'step': 'arxiv_id_not_found', 'arxiv': e['arxiv']})
    t = e.get('title')
    q_parts = [t] if t else []
    if e.get('authors'): q_parts.append(e['authors'][0])
    if e.get('year'): q_parts.append(str(e['year']))
    q = ' '.join(q_parts) if q_parts else e['raw']
    best = None
    for c in crossref_biblio(q if t else e['raw']):
        ok, m = _accept_parsed(c, e)
        if ok: return done('crossref', c, m)
        if best is None or m['title_sim'] > best[1]['title_sim']: best = (c, m)
    if best: ev.append({'step': 'crossref_best_reject', 'rec': best[0], 'metrics': best[1]})
    if t:
        for c in openalex_search(t):
            ok, m = _accept_parsed(c, e)
            if ok: return done('openalex', c, m)
        for c in dblp_search(t):
            ok, m = _accept_parsed(c, e)
            if ok: return done('dblp', c, m)
        if do_arxiv_search:
            for c in arxiv_title_search(t):
                ok, m = _accept_parsed(c, e)
                if ok: return done('arxiv_search', c, m)
    else:
        for c in openalex_search(e['raw']):
            ok, m = _accept_parsed(c, e)
            if ok: return done('openalex_raw', c, m)
    urls = [u for u in e.get('urls', []) if not re.search(r'doi\.org|arxiv\.org', u)]
    if urls:
        sts = {u: url_status(u) for u in urls[:3]}
        if any(s == 200 for s in sts.values()):
            return {'verdict': 'VERIFIED_URL', 'via': 'url', 'url_status': sts, 'evidence': ev}
        ev.append({'step': 'urls_not_live', 'url_status': sts})
    likely = None
    for x in ev:
        m = x.get('metrics') or {}
        if 'rec' in x and m.get('title_sim', 0) >= 70 and m.get('first_author_ok') and m.get('year_ok'):
            likely = x['rec']
    return {'verdict': 'UNVERIFIED', 'evidence': ev, 'likely_match': likely}

def verify_parsed_paper(parsed, do_arxiv_search=True):
    out = []
    for e in parsed['entries']:
        out.append({**e, **verify_parsed(e, do_arxiv_search=do_arxiv_search)})
    _save_cache()
    return out
