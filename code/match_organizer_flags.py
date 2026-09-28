"""Match the example references that the organizers' automated Related Work Check flagged ("could not be verified")
to our parsed reference entries, so their adjudication outcome gives the precision of the organizer flag (Q2a)."""
import json, glob, os, re, csv
import pandas as pd
from rapidfuzz import fuzz
from unidecode import unidecode

def norm(s): return re.sub(r'\s+', ' ', re.sub(r'[^a-z0-9 ]+', ' ', unidecode(str(s or '')).lower())).strip()

papers = pd.read_csv('data/dataset/papers.csv')
flags = []
for _, r in papers.iterrows():
    if isinstance(r.rw_flagged_examples, str):
        for ex in json.loads(r.rw_flagged_examples):
            m = re.match(r'^(.*?)\s+by\s+(.+)$', ex.strip())
            flags.append({'number': int(r.number), 'forum_id': r.forum_id, 'flag_text': ex.strip(), 'flag_title': (m.group(1) if m else ex).strip(' .'), 'flag_authors': (m.group(2) if m else '').strip(' .')})
print('organizer-flagged example references:', len(flags), 'in', len({f['number'] for f in flags}), 'papers')

entries = {}
for f in glob.glob('data/refs/*.verified.json'):
    stem = os.path.basename(f).replace('.verified.json', ''); m = re.match(r'^(\d+)_', stem)
    if not m: continue
    d = json.load(open(f))
    if isinstance(d, dict): entries[int(m.group(1))] = d.get('entries', [])

out = []
for fl in flags:
    ents = entries.get(fl['number'])
    if ents is None: out.append({**fl, 'matched_idx': None, 'match_score': None, 'entry_verdict': 'PAPER_NOT_PROCESSED'}); continue
    best, bs = None, 0
    for e in ents:
        if e.get('junk'): continue
        cand_t = e.get('title') or ''
        s = max(fuzz.token_set_ratio(norm(fl['flag_title']), norm(cand_t)) if cand_t else 0, fuzz.partial_ratio(norm(fl['flag_title']), norm(e.get('raw') or '')))
        if s > bs: best, bs = e, s
    out.append({**fl, 'matched_idx': best['idx'] if best and bs >= 80 else None, 'match_score': bs, 'entry_verdict': (best['verdict'] if best and bs >= 80 else 'NO_MATCH'), 'entry_title': (best.get('title') if best and bs >= 80 else None)})
df = pd.DataFrame(out)
os.makedirs('data/adjudication', exist_ok=True)
df.to_csv('data/adjudication/organizer_flags.csv', index=False)
proc = df[df.entry_verdict != 'PAPER_NOT_PROCESSED']
print('in processed papers:', len(proc), '| matched to an entry:', int((proc.matched_idx.notna()).sum()), '| entry verdicts:', proc.entry_verdict.value_counts().to_dict())
