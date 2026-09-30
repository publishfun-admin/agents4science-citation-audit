"""Submission-clustered bootstrap of the blind check of automatically verified entries.

SUFFIX selects the label set written by code/blind_checks.py: '' (blind agent), '_human' (the author's labels for the 29
coded entries) or '_coder' (the independent coder's labels). Resamples the submissions represented in the 180-entry
sample with replacement (B=4000), pools their entries, and reports percentile intervals for the crude corrupted and
invented shares and for the expected share of reviewed submissions carrying at least one corrupted or fabricated
reference when the crude corrupted rate is applied uniformly to each submission's automatically verified entries
(1 - (1-p)^n for submissions with no detected fabricated reference). Run from anywhere."""
import csv, os, collections, numpy as np, pandas as pd
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'); os.chdir(ROOT)
SUFFIX = os.environ.get('SUFFIX', ''); B = int(os.environ.get('B', 4000)); rng = np.random.default_rng(int(os.environ.get('SEED', 1)))
rows = list(csv.DictReader(open(f'data/adjudication/blind/blind_autoverified_sample{SUFFIX}.csv')))
by = collections.defaultdict(list)
for r in rows: by[r['key'].split(':')[0]].append(r['blind'])
subs = list(by); n = len(rows)
p = pd.read_csv('data/dataset/papers_final.csv'); rev = p[p.group.isin(['Conference', 'Rejected_Submission']) & p.n_refs.notna()]
nv = rev.n_verified.fillna(0).values; det = (rev.n_fab.fillna(0) > 0).values
def expected(pc): return float(np.mean(np.where(det, 1.0, 1 - (1 - pc) ** nv)))
cs, ns, es = [], [], []
for _ in range(B):
    pool = [l for s in rng.choice(subs, size=len(subs), replace=True) for l in by[s]]
    c = sum(l == 'EXISTS_CORRUPTED' for l in pool) / len(pool); f = sum(l == 'NOT_FOUND' for l in pool) / len(pool)
    cs.append(c); ns.append(f); es.append(expected(c))
c0 = sum(l == 'EXISTS_CORRUPTED' for l in rows and [r['blind'] for r in rows]) / n; f0 = sum(r['blind'] == 'NOT_FOUND' for r in rows) / n
print(f"labels{SUFFIX or ' (blind agent)'}: {n} entries from {len(subs)} submissions; corrupted {100*c0:.1f}% (clustered 95% CI {100*np.percentile(cs,2.5):.1f}-{100*np.percentile(cs,97.5):.1f}); "
      f"invented {100*f0:.1f}% ({100*np.percentile(ns,2.5):.1f}-{100*np.percentile(ns,97.5):.1f}); expected share of reviewed submissions with >=1 corrupted or fabricated reference "
      f"{100*expected(c0):.0f}% (95% interval {100*np.percentile(es,2.5):.0f}-{100*np.percentile(es,97.5):.0f}) against {100*det.mean():.1f}% detected")
