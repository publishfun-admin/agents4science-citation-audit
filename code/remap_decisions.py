"""After re-parsing papers with a new parser version, remap existing manual decisions (keyed number:idx) to the new entry
indices by matching the normalised raw reference string. Decisions whose raw string no longer corresponds to exactly one
entry (e.g. entries that were previously merged) are retired to data/adjudication/retired_decisions.csv and the entries
re-enter the adjudication queue if still unverified.
Usage: python3 code/remap_decisions.py <stem> [<stem> ...]   (old parse must be saved in $OLD_DIR, default data/refs_v3/<stem>.verified.json)"""
import csv, glob, json, os, re, sys, unidecode
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
DEC = os.path.join(ROOT, 'data', 'adjudication', 'decisions.csv'); RET = os.path.join(ROOT, 'data', 'adjudication', 'retired_decisions.csv')
def norm(x): return re.sub(r'[^a-z0-9]+', ' ', unidecode.unidecode(str(x or '')).lower()).strip()
rows = list(csv.DictReader(open(DEC))); fields = rows[0].keys()
kept, retired, moved = [], [], 0
stems = sys.argv[1:]
nums = {s.split('_')[0] for s in stems}
new_by_num = {}
for s in stems:
    d = json.load(open(os.path.join(ROOT, 'data', 'refs', s + '.verified.json')))
    new_by_num[s.split('_')[0]] = {norm(e['raw']): e['idx'] for e in d['entries']}
old_by_num = {}
for s in stems:
    p = os.path.join(ROOT, os.environ.get('OLD_DIR', 'data/refs_v3'), s + '.verified.json')
    if os.path.exists(p):
        d = json.load(open(p)); old_by_num[s.split('_')[0]] = {e['idx']: norm(e['raw']) for e in d['entries']}
for r in rows:
    n = r['number']
    if n not in nums: kept.append(r); continue
    old_raw = old_by_num.get(n, {}).get(int(r['idx']))
    new_idx = new_by_num[n].get(old_raw) if old_raw else None
    if new_idx is None:  # try prefix match: new entry raw is the start of the old (merged) raw -> keep only if the decision note names it? no: retire
        retired.append(r); continue
    if new_idx != int(r['idx']): moved += 1
    r = dict(r); r['idx'] = str(new_idx); kept.append(r)
with open(DEC, 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(kept)
exists = os.path.exists(RET)
with open(RET, 'a', newline='') as f:
    w = csv.DictWriter(f, fieldnames=fields)
    if not exists: w.writeheader()
    w.writerows(retired)
print(f"kept {len(kept)} (moved {moved}) | retired {len(retired)} decisions for {len(stems)} papers")
