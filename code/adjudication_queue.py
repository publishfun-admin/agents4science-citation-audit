"""Build the manual-adjudication queue: every non-junk UNVERIFIED reference with the context a human/agent needs."""
import json, glob, os, re, csv
rows = []
for f in sorted(glob.glob('data/refs/*.verified.json')):
    d = json.load(open(f)); stem = os.path.basename(f).replace('.verified.json', '')
    m = re.match(r'^(\d+)_([A-Za-z0-9_-]+)$', stem)
    if not m: continue
    for e in d.get('entries', []):
        if e.get('junk') or e['verdict'] != 'UNVERIFIED': continue
        best = None
        for x in e.get('evidence', []):
            if 'rec' in x:
                mt = x.get('metrics', {})
                cand = (x['rec'].get('title') or '', x['rec'].get('year'), x['rec'].get('first_author'), x['rec'].get('doi') or x['rec'].get('arxiv') or x['rec'].get('id'), round(mt.get('title_sim', 0)))
                if best is None or cand[4] > best[4]: best = cand
        rows.append({'number': int(m.group(1)), 'forum_id': m.group(2), 'idx': e['idx'], 'title': e.get('title'), 'first_author': (e.get('authors') or [None])[0],
                     'n_authors': len(e.get('authors') or []), 'year': e.get('year'), 'container': e.get('container'), 'doi': e.get('doi'), 'arxiv': e.get('arxiv'),
                     'urls': ' '.join(e.get('urls') or [])[:200], 'raw': (e.get('raw') or '')[:400], 'steps': ';'.join(x['step'] for x in e.get('evidence', [])),
                     'best_title': best[0][:150] if best else None, 'best_year': best[1] if best else None, 'best_author': best[2] if best else None, 'best_id': best[3] if best else None, 'best_sim': best[4] if best else None,
                     'verdict': '', 'category': '', 'evidence_url': '', 'note': ''})
os.makedirs('data/adjudication', exist_ok=True)
with open('data/adjudication/queue.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
print('queue rows:', len(rows), 'papers:', len({r['number'] for r in rows}))
import collections
print('steps distribution:', collections.Counter(r['steps'] for r in rows).most_common(6))
print('with DOI:', sum(1 for r in rows if r['doi']), '| with arXiv id:', sum(1 for r in rows if r['arxiv']), '| with URL:', sum(1 for r in rows if r['urls']), '| no title parsed:', sum(1 for r in rows if not r['title']))
