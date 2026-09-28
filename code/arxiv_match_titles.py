"""Find arXiv versions of Agents4Science papers by title search (arXiv API, polite 3.5 s spacing)."""
import csv, json, os, re, time, urllib.parse, urllib.request, xml.etree.ElementTree as ET
from rapidfuzz import fuzz
NS = {'a': 'http://www.w3.org/2005/Atom'}
def norm(t): return re.sub(r'[^a-z0-9 ]+', ' ', (t or '').lower()).strip()
papers = {}
for row in csv.DictReader(open('data/a4s_site/papers_with_ids.csv')):
    papers.setdefault(row['paper_id'], row)
done = set()
if os.path.exists('data/arxiv_match.jsonl'):
    for line in open('data/arxiv_match.jsonl'):
        try: done.add(json.loads(line)['paper_id'])
        except: pass
out = open('data/arxiv_match.jsonl', 'a')
for pid, row in papers.items():
    if pid in done: continue
    title = row['title']
    q = ' AND '.join(f'ti:{w}' for w in re.findall(r'[A-Za-z0-9]{3,}', title)[:10]) or 'ti:' + norm(title)
    url = 'https://export.arxiv.org/api/query?' + urllib.parse.urlencode({'search_query': q, 'max_results': 5})
    rec = {'paper_id': pid, 'title': title, 'best': None, 'sim': None}
    for attempt in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'publishfun-firstpaper-research/0.1 (mailto:admin@publish.fun)'}), timeout=60) as r:
                root = ET.fromstring(r.read())
            best = None
            for e in root.findall('a:entry', NS):
                t = ' '.join((e.findtext('a:title', '', NS) or '').split())
                sim = fuzz.ratio(norm(title), norm(t))
                if best is None or sim > best['sim']:
                    best = {'sim': sim, 'title': t, 'id': e.findtext('a:id', '', NS), 'published': e.findtext('a:published', '', NS), 'updated': e.findtext('a:updated', '', NS)}
            if best: rec.update({'best': best, 'sim': best['sim']})
            break
        except Exception as ex:
            time.sleep(10 * (attempt + 1))
    out.write(json.dumps(rec) + '\n'); out.flush()
    print(pid, rec['sim'], (rec['best'] or {}).get('id'), flush=True)
    time.sleep(3.5)
print('DONE', flush=True)
