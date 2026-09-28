"""Aggregate per-reference verification results into per-paper statistics and merge with paper metadata.
Writes data/dataset/refs_long.csv (one row per reference) and data/dataset/papers_refs.csv (one row per paper)."""
import json, glob, os, re
import pandas as pd

def main():
    papers = pd.read_csv('data/dataset/papers.csv')
    rows = []
    for f in sorted(glob.glob('data/refs/*.verified.json')):
        stem = os.path.basename(f).replace('.verified.json', '')
        m = re.match(r'^(\d+)_([A-Za-z0-9_-]+)$', stem)
        if not m: continue
        number, fid = int(m.group(1)), m.group(2)
        d = json.load(open(f))
        if d.get('error') and not d.get('entries'):
            rows.append({'number': number, 'forum_id': fid, 'idx': None, 'verdict': 'PAPER_ERROR', 'error': d['error']}); continue
        for e in d['entries']:
            rows.append({'number': number, 'forum_id': fid, 'idx': e['idx'], 'junk': bool(e.get('junk')), 'verdict': e['verdict'], 'via': e.get('via'),
                         'title': e.get('title'), 'first_author': (e.get('authors') or [None])[0], 'year': e.get('year'), 'doi': e.get('doi'), 'arxiv': e.get('arxiv'),
                         'has_url': bool(e.get('urls')), 'raw': (e.get('raw') or '')[:300], 'likely_match': ((e.get('likely_match') or {}).get('title') if e.get('likely_match') else None),
                         'parser': e.get('parser')})
    long = pd.DataFrame(rows)
    os.makedirs('data/dataset', exist_ok=True)
    long.to_csv('data/dataset/refs_long.csv', index=False)
    ok = long[(long.verdict != 'PAPER_ERROR') & (~long.junk.fillna(False))]
    per = ok.groupby(['number', 'forum_id']).agg(n_refs=('idx', 'size'), n_verified=('verdict', lambda s: s.isin(['VERIFIED', 'VERIFIED_URL']).sum()),
                                                 n_unverified=('verdict', lambda s: (s == 'UNVERIFIED').sum())).reset_index()
    per['share_unverified'] = per.n_unverified / per.n_refs
    merged = papers.merge(per, on=['number', 'forum_id'], how='left')
    merged.to_csv('data/dataset/papers_refs.csv', index=False)
    done = merged[merged.n_refs.notna()]
    print('papers processed:', len(done), '| refs:', int(done.n_refs.sum()), '| verified:', int(done.n_verified.sum()), '| unverified:', int(done.n_unverified.sum()))
    print('paper-level: share with >=1 unverified:', round(float((done.n_unverified > 0).mean()), 3))
    print('by group:\n', done.groupby('group').agg(n=('number', 'size'), refs=('n_refs', 'sum'), unv=('n_unverified', 'sum'), any_unv=('n_unverified', lambda s: (s > 0).mean().round(3))))
    return merged

if __name__ == '__main__':
    main()
