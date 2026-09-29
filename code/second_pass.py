"""Second automated pass over UNVERIFIED references: Semantic Scholar title match, Crossref query.title, OpenLibrary (books),
Google Books (books). Rewrites data/refs/*.verified.json in place (verdict VERIFIED with via=s2|crossref_title|openlibrary|googlebooks).
Runs continuously: polls for verified.json files that have not had a second pass (flag 'second_pass' in the file)."""
import os, sys, json, glob, time, re, urllib.parse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('SHARD', 'p2')
import refs_verify as rv
from rapidfuzz import fuzz

def s2_match(title):
    d = rv.http('https://api.semanticscholar.org/graph/v1/paper/search/match?' + urllib.parse.urlencode({'query': title[:300], 'fields': 'title,year,authors,externalIds,venue'}), max_tries=4, timeout=30)
    if not d or not d.get('data'): return []
    out = []
    for m in d['data']:
        au = m.get('authors') or []
        out.append({'source': 's2', 'id': m.get('paperId'), 'title': m.get('title') or '', 'year': m.get('year'), 'first_author': au[0]['name'] if au else None, 'container': m.get('venue'), 'ext': m.get('externalIds')})
    return out

def crossref_title(title, author=None):
    q = {'query.title': title[:300], 'rows': 5, 'select': 'DOI,title,author,issued,container-title,score,type,published-print,published-online,created'}
    if author: q['query.author'] = author
    d = rv.http('https://api.crossref.org/works?' + urllib.parse.urlencode(q))
    return [rv._cr_rec(m) for m in d['message']['items']] if d else []

def openlibrary(title, author=None):
    q = {'title': title[:200], 'limit': 5, 'fields': 'title,author_name,first_publish_year,key'}
    if author: q['author'] = author
    d = rv.http('https://openlibrary.org/search.json?' + urllib.parse.urlencode(q), max_tries=2, timeout=30)
    out = []
    for doc in (d or {}).get('docs', []):
        out.append({'source': 'openlibrary', 'id': doc.get('key'), 'title': doc.get('title') or '', 'year': doc.get('first_publish_year'), 'first_author': (doc.get('author_name') or [None])[0]})
    return out

def googlebooks(title, author=None):
    if os.environ.get('SKIP_GBOOKS') == '1': return []   # daily quota exhausted; skip
    q = 'intitle:' + title[:150] + (' inauthor:' + author if author else '')
    d = rv.http('https://www.googleapis.com/books/v1/volumes?' + urllib.parse.urlencode({'q': q, 'maxResults': 5}), max_tries=2, timeout=30)
    out = []
    for it in (d or {}).get('items', []):
        vi = it.get('volumeInfo', {})
        y = (vi.get('publishedDate') or '')[:4]
        out.append({'source': 'googlebooks', 'id': it.get('id'), 'title': (vi.get('title') or '') + (': ' + vi['subtitle'] if vi.get('subtitle') else ''), 'year': int(y) if y.isdigit() else None, 'first_author': (vi.get('authors') or [None])[0]})
    return out

BOOKISH = re.compile(r'press|springer|wiley|elsevier|routledge|mcgraw|pearson|academic|publish|books?\b|edition|handbook|textbook|isbn', re.I)

def second_pass_entry(e):
    t = e.get('title'); au = (e.get('authors') or [None])[0]
    if not t or len(t) < 8: return None
    for name, cands in (('s2', s2_match(t)), ('crossref_title', crossref_title(t, au))):
        for c in cands:
            ok, m = rv._accept_parsed(c, e)
            if ok: return {'verdict': 'VERIFIED', 'via': name, 'match': c, 'metrics': m}
    raw = e.get('raw') or ''
    if BOOKISH.search(raw) or (e.get('container') and BOOKISH.search(e['container'])) or not e.get('container'):
        for name, cands in (('openlibrary', openlibrary(t, au)), ('googlebooks', googlebooks(t, au))):
            for c in cands:
                ok, m = rv._accept_parsed(c, e)
                if ok: return {'verdict': 'VERIFIED', 'via': name, 'match': c, 'metrics': m}
    return None

def main():
    idle = 0
    while True:
        files = [f for f in sorted(glob.glob('data/refs/*.verified.json')) if time.time() - os.path.getmtime(f) > 15]
        todo = []
        for f in files:
            try: d = json.load(open(f))
            except Exception: continue
            if not isinstance(d, dict): continue
            if not d.get('second_pass'):
                stem_no = int(os.path.basename(f).split('_')[0]) if os.path.basename(f).split('_')[0].isdigit() else 0
                sh = os.environ.get('SHARD', '0'); sh = int(sh) if sh.isdigit() else 0
                if stem_no % int(os.environ.get('NSHARDS', 1)) == sh: todo.append((f, d))
        if not todo:
            if os.environ.get('ONCE'): break
            idle += 1
            if idle > 40 and len(files) >= 310: break
            time.sleep(30); continue
        idle = 0
        for f, d in todo:
            n_new = 0; t0 = time.time()
            for e in d.get('entries', []):
                if e.get('junk') or e.get('verdict') != 'UNVERIFIED': continue
                try:
                    r = second_pass_entry(e)
                except Exception as ex:
                    r = None
                if r:
                    e.update(r); e['second_pass_hit'] = True; n_new += 1
            d['second_pass'] = True
            json.dump(d, open(f, 'w'), indent=1)
            rv._save_cache()
            print(f"{os.path.basename(f)}: +{n_new} verified in 2nd pass ({time.time()-t0:.0f}s)", flush=True)

if __name__ == '__main__':
    main()
