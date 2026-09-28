"""Phase 1: match each Agents4Science paper title to Semantic Scholar; Phase 2: fetch its references."""
import sys, json, os, csv, re, time
sys.path.insert(0, os.path.dirname(__file__))
import s2_client as s2
from rapidfuzz import fuzz

def norm(t): return re.sub(r'[^a-z0-9 ]+', ' ', (t or '').lower()).strip()

papers = {}
for row in csv.DictReader(open('data/a4s_site/papers_with_ids.csv')):
    pid = row['paper_id']
    if pid not in papers: papers[pid] = row
os.makedirs('data/s2_refs', exist_ok=True)
out = open('data/s2_match.jsonl', 'a')
done = set()
if os.path.exists('data/s2_match.jsonl'):
    for line in open('data/s2_match.jsonl'):
        try: done.add(json.loads(line)['paper_id'])
        except: pass
time.sleep(12)  # let the foreground test finish first
for pid, row in papers.items():
    if pid in done: continue
    title = row['title']
    d = s2.get('/paper/search/match', {'query': title, 'fields': 'title,externalIds,referenceCount,openAccessPdf,publicationDate,venue'})
    rec = {'paper_id': pid, 'title': title, 'match': None, 'sim': None}
    if d and d.get('data'):
        m = d['data'][0]
        sim = fuzz.ratio(norm(title), norm(m.get('title')))
        rec.update({'match': m, 'sim': sim})
        if sim >= 90 and m.get('paperId'):
            refs = s2.get(f"/paper/{m['paperId']}/references", {'fields': 'title,year,authors,externalIds,venue,publicationDate', 'limit': 500})
            json.dump(refs, open(f"data/s2_refs/{pid}.json", 'w'))
            rec['n_refs'] = len(refs.get('data', [])) if refs and 'data' in refs else None
    out.write(json.dumps(rec) + '\n'); out.flush()
    print(pid, rec['sim'], rec.get('n_refs'), flush=True)
print('DONE', flush=True)
