"""Re-resolve arXiv identifiers for UNVERIFIED entries whose lookup failed during the arXiv API outage.
Purges cached empty responses, waits until the API answers, then retries arxiv_by_id (and the v1 fallback) for every
non-junk UNVERIFIED entry with an arXiv id whose evidence says 'arxiv_id_not_found'. Falls back to scraping the
arxiv.org/abs page's citation meta tags if the API keeps failing. Marks files with 'arxiv_repass': True."""
import os, sys, json, glob, time, re, urllib.request, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('SHARD', 'p4')
import refs_verify as rv

def abs_page(aid):
    try:
        req = urllib.request.Request(f'https://arxiv.org/abs/{aid}', headers={'User-Agent': rv.UA})
        with urllib.request.urlopen(req, timeout=30) as r: s = r.read().decode('utf-8', 'replace')
    except Exception: return None
    t = re.search(r'<meta name="citation_title" content="([^"]+)"', s); a = re.findall(r'<meta name="citation_author" content="([^"]+)"', s); d = re.search(r'<meta name="citation_date" content="(\d{4})', s)
    if not t: return None
    return {'source': 'arxiv_abs', 'arxiv': aid, 'title': html.unescape(t.group(1)), 'year': int(d.group(1)) if d else None, 'first_author': html.unescape(a[0]) if a else None}

def api_ok():
    r = rv.arxiv_by_id('2005.01643')
    return bool(r and 'Offline Reinforcement Learning' in r.get('title', ''))

# purge cached empty bodies for arXiv
for k in [k for k, v in list(rv._cache.items()) if 'export.arxiv.org' in k and (v is None or v == '')]:
    del rv._cache[k]
use_api = api_ok(); print('arXiv API usable:', use_api, flush=True)
idle = 0
while True:
    todo = []
    for f in sorted(glob.glob('data/refs/*.verified.json')):
        try: d = json.load(open(f))
        except Exception: continue
        if isinstance(d, dict) and d.get('second_pass') and not d.get('arxiv_repass'): todo.append((f, d))
    if not todo:
        idle += 1
        if idle > 40: break
        time.sleep(60); continue
    idle = 0
    for f, d in todo:
        n = 0
        for e in d.get('entries', []):
            if e.get('junk') or e.get('verdict') != 'UNVERIFIED' or not e.get('arxiv'): continue
            if not any(x.get('step') == 'arxiv_id_not_found' for x in e.get('evidence', [])): continue
            rec = rv.arxiv_by_id(e['arxiv']) if use_api else None
            if rec is None: rec = abs_page(e['arxiv']); time.sleep(3)
            if not rec: continue
            ok, m = rv._accept_parsed(rec, e)
            cont, pr = rv.title_match(rec.get('title', ''), e['raw'])
            if ok or cont >= 0.9 or pr >= 95:
                e.update({'verdict': 'VERIFIED', 'via': 'arxiv_id_repass', 'match': rec, 'metrics': {**m, 'containment': round(cont, 3), 'partial_ratio': pr}}); n += 1
            else:
                e['evidence'] = [x for x in e['evidence'] if x.get('step') != 'arxiv_id_not_found'] + [{'step': 'arxiv_id_resolves_title_mismatch', 'rec': rec, 'metrics': m}]
        d['arxiv_repass'] = True
        json.dump(d, open(f, 'w'), indent=1); rv._save_cache()
        print(f"{os.path.basename(f)}: +{n} via arXiv repass", flush=True)
