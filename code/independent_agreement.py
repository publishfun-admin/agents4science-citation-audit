"""Independent-coder agreement and sensitivity bound.

Scores the reference-strings-only sheets released for a human coder who is not connected to the study:
  data/adjudication/blind/independent_coder_sheet_A.csv  (64 items: the author's 64-item validation sheet without labels)
  data/adjudication/blind/independent_coder_sheet_B.csv  (45 items: a simple random sample of the 857 manual decisions)
once the CODER_CATEGORY column has been filled in (see INDEPENDENT_CODER_INSTRUCTIONS.md and CODER_STATEMENT.md).

For each sheet it reports raw agreement and Cohen's kappa, for the five categories and for fabricated-versus-not, against
(1) the first adjudicator's label, (2) the blind agent's label where the item was blind re-adjudicated and (3) the author's
coding (sheet A only; sheet B does not overlap the author's sheet). Sheet A is also reported per stratum.

From sheet B, a probability sample of the manual decisions, it estimates the coder's label given the first adjudicator's
label (three states: invented = NOT_FOUND, corrupted = EXISTS_CORRUPTED, other; Dirichlet posteriors with a Jeffreys
prior) and simulates relabelling every manual decision in the analysis, each independently given its first-adjudicator
state, to give a sensitivity bound for the detected counts: the 513 fabricated (286 invented) references, the paper-level
rates among reviewed submissions, the reference-level shares (denominators held at the detected analysis's values), the
paper-level metrics of the organisers' flag and the reference-level precision of the matched flagged examples.
The detected values are recomputed here from the released data as a self-check against paper/results_tables.md.

Writes data/dataset/independent_agreement.md and .json. Run from anywhere; N_SIM (default 4000) and SEED (default 1)."""
import csv, os, json, glob, collections, re
import numpy as np, unidecode
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'); os.chdir(ROOT)
BL = 'data/adjudication/blind/'
N_SIM = int(os.environ.get('N_SIM', 4000)); SEED = int(os.environ.get('SEED', 1))
VALID = {'EXISTS', 'WEB_RESOURCE_EXISTS', 'EXISTS_CORRUPTED', 'NOT_FOUND', 'WEB_RESOURCE_NOT_FOUND', 'PLACEHOLDER', 'UNADJUDICABLE'}
def raw(c): return (c or '').strip().upper().replace(' ', '_')
def col(c): return {'WEB_RESOURCE_EXISTS': 'EXISTS', 'WEB_RESOURCE_NOT_FOUND': 'NOT_FOUND', 'VERIFIED_(AUTOMATED)': 'EXISTS', 'VERIFIED': 'EXISTS', 'VERIFIED_URL': 'EXISTS'}.get(raw(c), raw(c))
def fab(c): return col(c) in ('NOT_FOUND', 'EXISTS_CORRUPTED')
def state(c): c = col(c); return 'NF' if c == 'NOT_FOUND' else ('EC' if c == 'EXISTS_CORRUPTED' else 'OTHER')
def norm(x): return re.sub(r'[^a-z0-9]+', ' ', unidecode.unidecode(str(x or '')).lower()).strip()
def kappa(pairs):
    n = len(pairs)
    if not n: return float('nan'), float('nan')
    cats = sorted({a for a, _ in pairs} | {b for _, b in pairs}); po = sum(a == b for a, b in pairs) / n
    pe = sum((sum(a == c for a, _ in pairs) / n) * (sum(b == c for _, b in pairs) / n) for c in cats)
    return po, (po - pe) / (1 - pe) if pe < 1 else float('nan')
def wilson(k, n, z=1.96):
    if not n: return (float('nan'), float('nan'))
    p = k / n; d = 1 + z * z / n; c = (p + z * z / (2 * n)) / d; h = z * ((p * (1 - p) / n + z * z / (4 * n * n)) ** 0.5) / d
    return (100 * (c - h), 100 * (c + h))
def kappa_ci(pairs, B=2000):
    rng = np.random.default_rng(0); ks = []
    for _ in range(B):
        idx = rng.integers(0, len(pairs), len(pairs)); ks.append(kappa([pairs[i] for i in idx])[1])
    ks = [k for k in ks if k == k]
    return (np.percentile(ks, 2.5), np.percentile(ks, 97.5)) if ks else (float('nan'), float('nan'))
def stats(pairs):
    po, k = kappa(pairs); pb = [(fab(a), fab(b)) for a, b in pairs]; po2, k2 = kappa(pb)
    w1 = wilson(round(po * len(pairs)), len(pairs)); w2 = wilson(round(po2 * len(pairs)), len(pairs)); c1 = kappa_ci(pairs); c2 = kappa_ci(pb)
    return {'n': len(pairs), 'cat_pct': 100 * po, 'cat_ci': list(w1), 'cat_kappa': k, 'cat_kappa_ci': list(c1),
            'fab_pct': 100 * po2, 'fab_ci': list(w2), 'fab_kappa': k2, 'fab_kappa_ci': list(c2)}
def line(label, pairs, ci=False, key=None):
    """One report line; with ci=True adds Wilson and bootstrap intervals; with key=... stores the statistics in OUT['summary'][key]."""
    if key: OUT.setdefault('summary', {})[key] = stats(pairs)
    po, k = kappa(pairs); pb = [(fab(a), fab(b)) for a, b in pairs]; po2, k2 = kappa(pb)
    if not ci: return f'- Coder vs {label} (n={len(pairs)}): categories {100*po:.1f}% agreement (kappa {k:.2f}); fabricated-vs-not {100*po2:.1f}% (kappa {k2:.2f})'
    st = OUT['summary'][key] if key else stats(pairs); w1, w2, c1, c2 = st['cat_ci'], st['fab_ci'], st['cat_kappa_ci'], st['fab_kappa_ci']
    return (f'- Coder vs {label} (n={len(pairs)}): categories {100*po:.1f}% agreement (95% CI {w1[0]:.1f}-{w1[1]:.1f}; kappa {k:.2f}, bootstrap 95% CI {c1[0]:.2f}-{c1[1]:.2f}); '
            f'fabricated-vs-not {100*po2:.1f}% ({w2[0]:.1f}-{w2[1]:.1f}; kappa {k2:.2f}, {c2[0]:.2f}-{c2[1]:.2f})')

L = ['# Independent-coder agreement (auto-generated by code/independent_agreement.py)\n']; OUT = {}
def load_sheet(name):
    rows = list(csv.DictReader(open(BL + f'independent_coder_sheet_{name}.csv')))
    coded = {r['item']: r for r in rows if (r.get('CODER_CATEGORY') or '').strip()}
    bad = [i for i, r in coded.items() if raw(r['CODER_CATEGORY']) not in VALID]
    L.append(f'Sheet {name}: {len(coded)} of {len(rows)} items coded' + (f'; invalid categories in {bad}' if bad else ''))
    return {i: r for i, r in coded.items() if i not in bad}

# blind-agent labels by (submission number, normalised reference text), from the four released blind samples
blind = {}
for i in ['', '2', '3', '4']:
    decs = {d['id']: d['category'] for d in json.load(open(BL + f'blind_decisions{i}.json'))}
    for s in json.load(open(BL + f'blind_sample{i}.json')):
        if s['id'] in decs: blind[(s['key'].split(':')[0], norm(s['raw']))] = decs[s['id']]

# ---- sheet A: against the first adjudicator, the blind agent and the author's coding, overall and per stratum
A = load_sheet('A'); H = {r['item']: r for r in csv.DictReader(open(BL + 'human_coding_sheet.csv'))}
mapA = {m['coder_item']: m for m in json.load(open(BL + 'independent_coder_sheet_A_map.json'))}
if A:
    items = [(r, H[mapA[i]['sheet_item']]) for i, r in A.items()]
    L.append('\n## Sheet A (the 64-item sheet, reference strings only)\n')
    for label, key, sk in [('first adjudicator (or automated VERIFIED)', 'label_first_adjudicator', 'A_first'), ('blind agent', 'label_blind_agent', 'A_blind'), ("the author's coding", 'HUMAN_CATEGORY', 'A_author')]:
        for strat in ['all', 'manual (both strata)', 'manual-disputed', 'manual-agreed', 'automated (both strata)', 'auto-disputed', 'auto-agreed']:
            sel = [(r, h) for r, h in items if strat == 'all' or (strat.startswith('manual (') and h['stratum'].startswith('manual')) or (strat.startswith('automated (') and h['stratum'].startswith('auto')) or h['stratum'] == strat]
            if sel: L.append(line(f'{label}, {strat}', [(col(h[key]), col(r['CODER_CATEGORY'])) for r, h in sel], ci=(strat == 'all'), key=(sk if strat == 'all' else None)))
        L.append('')
    dis = [(r, h) for r, h in items if h['stratum'] == 'manual-disputed']
    side = collections.Counter('first' if col(r['CODER_CATEGORY']) == col(h['label_first_adjudicator']) else ('blind' if col(r['CODER_CATEGORY']) == col(h['label_blind_agent']) else 'neither') for r, h in dis)
    L.append(f"- On the {len(dis)} coded manual decisions where the agents disagreed, the coder agreed with the first adjudicator in {side['first']}, with the blind agent in {side['blind']}, with neither in {side['neither']}")
    autod = [(r, h) for r, h in items if h['stratum'] == 'auto-disputed']
    L.append(f"- On the {len(autod)} coded automated matches that the blind agent called corrupted or invented, the coder confirmed a defect (corrupted or invented) in {sum(fab(r['CODER_CATEGORY']) for r, h in autod)}")
    OUT['sheet_A'] = {i: {'coder': col(r['CODER_CATEGORY']), 'first': col(h['label_first_adjudicator']), 'blind': col(h['label_blind_agent']), 'author': col(h['HUMAN_CATEGORY']), 'stratum': h['stratum']} for (r, h), i in zip(items, A)}

# ---- sheet B: against the first adjudicator (all items) and the blind agent (items that were blind re-adjudicated)
B = load_sheet('B'); mapB = {m['coder_item']: m['key'] for m in json.load(open(BL + 'independent_coder_sheet_B_map.json'))}
dec = {(r['number'], int(r['idx'])): r for r in csv.DictReader(open('data/adjudication/decisions.csv'))}
conf = {s: collections.Counter() for s in ('NF', 'EC', 'OTHER')}
if B:
    L.append('\n## Sheet B (simple random sample of 45 manual decisions, reference strings only)\n')
    pf, pb = [], []
    for i, r in B.items():
        n, idx = mapB[i].split(':'); first = dec[(n, int(idx))]['category']
        pf.append((col(first), col(r['CODER_CATEGORY']))); conf[state(first)][state(r['CODER_CATEGORY'])] += 1
        b = blind.get((n, norm(r['reference_as_printed'])))
        if b: pb.append((col(b), col(r['CODER_CATEGORY'])))
    L.append(line('first adjudicator, all coded items', pf, ci=True, key='B_first'))
    for s in ('NOT_FOUND', 'EXISTS_CORRUPTED', 'EXISTS', 'PLACEHOLDER', 'UNADJUDICABLE'):
        sub = [p for p in pf if p[0] == s]
        if sub: L.append(f"  - first adjudicator {s} (n={len(sub)}): coder said " + ', '.join(f'{k} {v}' for k, v in collections.Counter(b for _, b in sub).most_common()))
    if pb: L.append(line('blind agent (items that were also blind re-adjudicated)', pb, ci=True, key='B_blind'))
    L.append("- The author's 64-item sheet and sheet B share no item, so no comparison with the author's coding is possible on sheet B")
    OUT['sheet_B'] = {'pairs_first': pf, 'pairs_blind': pb, 'confusion_first_to_coder': {s: dict(c) for s, c in conf.items()}}

# ---- population of manual decisions and the detected analysis (mirrors code/analysis.py)
papers = {r['number']: r for r in csv.DictReader(open('data/dataset/papers.csv'))}
ent = []   # one row per non-junk entry: number, idx, status
for f in sorted(glob.glob('data/refs/*.verified.json')):
    num = os.path.basename(f).split('_')[0]
    for e in json.load(open(f))['entries']:
        if e.get('junk'): continue
        d = dec.get((num, e['idx']))
        st = col(d['category']) if d else ('VERIFIED' if e['verdict'] in ('VERIFIED', 'VERIFIED_URL') else 'PENDING')
        if d and raw(d['category']) in ('PLACEHOLDER', 'UNADJUDICABLE'): st = raw(d['category'])
        ent.append((num, e['idx'], st, bool(d)))
manual = [k for k, x in enumerate(ent) if x[3]]
first_state = np.array([state(ent[k][2]) for k in manual])
pnum = np.array([x[0] for x in ent]); pidx = {n: j for j, n in enumerate(sorted(set(pnum)))}; pj = np.array([pidx[n] for n in pnum])
has_refs = np.zeros(len(pidx), bool); has_refs[[pj[k] for k, x in enumerate(ent) if x[2] != 'UNADJUDICABLE']] = True   # papers with >=1 adjudicable entry, as in analysis.py
reviewed = np.array([papers[n]['group'] in ('Conference', 'Rejected_Submission') for n in sorted(set(pnum))]) & has_refs
chk = np.array([papers[n]['related_work_check'] == 'True' for n in sorted(set(pnum))]) & reviewed
flag = np.array([float(papers[n]['rw_n_examples'] or 0) > 0 for n in sorted(set(pnum))])
n_ref_rev = sum(1 for x in ent if papers[x[0]]['group'] in ('Conference', 'Rejected_Submission') and x[2] != 'UNADJUDICABLE')
def fl(x):
    try: return float(x)
    except (TypeError, ValueError): return float('nan')
P = sorted(set(pnum)); llm = np.array([[fl(papers[n][c]) for c in ('airev1', 'airev2', 'airev3')] for n in P]); human = np.array([fl(papers[n]['human_score']) for n in P])
accepted = np.array([papers[n]['group'] == 'Conference' for n in P]) & has_refs
n_adj = np.bincount(pj, np.array([x[2] != 'UNADJUDICABLE' for x in ent]), minlength=len(pidx)).astype(float)
from scipy.stats import spearmanr
def rho(x, y, m):
    m = m & ~np.isnan(y)
    return float(spearmanr(x[m], y[m]).correlation) if m.sum() > 2 else float('nan')
of = [(r['number'], int(float(r['matched_idx']))) for r in csv.DictReader(open('data/adjudication/organizer_flags.csv')) if r['matched_idx']]
epos = {(x[0], x[1]): k for k, x in enumerate(ent)}
matched = [epos[k] for k in of if k in epos and ent[epos[k]][2] != 'PENDING']
def summarise(st_manual):
    """st_manual: array of states ('NF','EC','OTHER') for the manual decisions, in the order of `manual`."""
    isf = np.zeros(len(ent), bool); isn = np.zeros(len(ent), bool)
    isf[manual] = np.isin(st_manual, ['NF', 'EC']); isn[manual] = st_manual == 'NF'
    cf = np.bincount(pj, isf, minlength=len(pidx)); cn = np.bincount(pj, isn, minlength=len(pidx)); pf = cf > 0; pn = cn > 0
    sf = np.divide(cf, n_adj, out=np.zeros_like(cf), where=n_adj > 0); sn = np.divide(cn, n_adj, out=np.zeros_like(cn), where=n_adj > 0)
    tp = int((flag & pf & chk).sum()); fn = int((~flag & pf & chk).sum()); fp = int((flag & ~pf & chk).sum()); tn = int((~flag & ~pf & chk).sum())
    n = tp + fn + fp + tn; po = (tp + tn) / n; pe = ((tp + fp) * (tp + fn) + (fn + tn) * (fp + tn)) / n ** 2
    return {'fabricated_refs': int(isf.sum()), 'invented_refs': int(isn.sum()),
            'reviewed_papers_fab_pct': 100 * pf[reviewed].mean(), 'reviewed_papers_inv_pct': 100 * pn[reviewed].mean(),
            'reviewed_ref_fab_pct': 100 * sum(isf[k] for k in range(len(ent)) if reviewed[pj[k]]) / n_ref_rev,
            'reviewed_ref_inv_pct': 100 * sum(isn[k] for k in range(len(ent)) if reviewed[pj[k]]) / n_ref_rev,
            'flag_sensitivity': tp / (tp + fn), 'flag_specificity': tn / (tn + fp), 'flag_kappa': (po - pe) / (1 - pe),
            'flag_example_precision_pct': 100 * float(isf[matched].mean()),
            'rho_fab_llm1': rho(sf, llm[:, 0], reviewed), 'rho_fab_llm2': rho(sf, llm[:, 1], reviewed), 'rho_fab_llm3': rho(sf, llm[:, 2], reviewed),
            'rho_inv_llm1': rho(sn, llm[:, 0], reviewed), 'rho_inv_llm2': rho(sn, llm[:, 1], reviewed), 'rho_inv_llm3': rho(sn, llm[:, 2], reviewed),
            'rho_fab_human': rho(sf, human, reviewed), 'rho_inv_human': rho(sn, human, reviewed),
            'accepted_with_invented': int((pn & accepted).sum()), 'accepted_with_fab_share_gt10': int(((sf > 0.10) & accepted).sum())}
det = summarise(first_state)
L.append('\n## Detected values recomputed from the released data (self-check against paper/results_tables.md)\n')
L.append(f"- Manual decisions in the analysis: {len(manual)} (invented {int((first_state=='NF').sum())}, corrupted {int((first_state=='EC').sum())}); reviewed submissions {int(reviewed.sum())}, with an organiser check {int(chk.sum())}; matched flagged examples {len(matched)}")
L.append('- ' + '; '.join((f'{k} {v:.2f}' if (k.startswith('flag_') and not k.endswith('pct')) or k.startswith('rho_') else f'{k} {v:.1f}') if isinstance(v, float) else f'{k} {v}' for k, v in det.items()))
OUT['detected'] = det

# ---- sensitivity bound from sheet B
if B and sum(sum(c.values()) for c in conf.values()) >= 10:
    rng = np.random.default_rng(SEED); S = ('NF', 'EC', 'OTHER'); sims = collections.defaultdict(list)
    idx_by = {s: np.where(first_state == s)[0] for s in S}
    for _ in range(N_SIM):
        st = np.empty(len(manual), dtype=object)
        for s in S:
            p = rng.dirichlet([conf[s][t] + 0.5 for t in S]); st[idx_by[s]] = rng.choice(S, size=len(idx_by[s]), p=p)
        for k, v in summarise(st).items(): sims[k].append(v)
    OUT['n_sim'] = N_SIM; OUT['confusion'] = {s_: {t: conf[s_][t] for t in S} for s_ in S}
    L.append(f'\n## Sensitivity of the detected figures to the independent coder\'s labels ({N_SIM} simulations, seed {SEED})\n')
    L.append("Each manual decision is relabelled independently with the coder's label distribution given the first adjudicator's state, "
             'estimated from sheet B (Dirichlet posterior, Jeffreys prior): ' + '; '.join(f"first {s}: coder " + ', '.join(f'{t} {conf[s][t]}' for t in S) for s in S) + '. '
             'Automatically verified entries are unchanged; denominators are the detected analysis\'s. Median and 95% interval of the relabelled value against the detected value.\n')
    L.append('| Quantity | Detected | Under the coder\'s labels (median, 95% interval) |\n|:--|--:|--:|')
    names = {'fabricated_refs': 'Detected fabricated references (all submissions)', 'invented_refs': 'Detected invented references', 'reviewed_papers_fab_pct': 'Reviewed submissions with >=1 fabricated reference (%)',
             'reviewed_papers_inv_pct': 'Reviewed submissions with >=1 invented reference (%)', 'reviewed_ref_fab_pct': 'Reviewed references fabricated (%)', 'reviewed_ref_inv_pct': 'Reviewed references invented (%)',
             'flag_sensitivity': 'Organiser flag, paper-level sensitivity', 'flag_specificity': 'Organiser flag, paper-level specificity', 'flag_kappa': 'Organiser flag, paper-level kappa', 'flag_example_precision_pct': 'Flagged examples fabricated (%, precision)',
             'rho_fab_llm1': 'Spearman rho, fabricated share vs LLM reviewer 1 score', 'rho_fab_llm2': 'Spearman rho, fabricated share vs LLM reviewer 2 score', 'rho_fab_llm3': 'Spearman rho, fabricated share vs LLM reviewer 3 score',
             'rho_inv_llm1': 'Spearman rho, invented share vs LLM reviewer 1 score', 'rho_inv_llm2': 'Spearman rho, invented share vs LLM reviewer 2 score', 'rho_inv_llm3': 'Spearman rho, invented share vs LLM reviewer 3 score',
             'rho_fab_human': 'Spearman rho, fabricated share vs human expert score', 'rho_inv_human': 'Spearman rho, invented share vs human expert score',
             'accepted_with_invented': 'Accepted papers with >=1 invented reference', 'accepted_with_fab_share_gt10': 'Accepted papers with >10% fabricated references'}
    OUT['sensitivity'] = {}
    for k, nm in names.items():
        a = np.array(sims[k]); f = (lambda v: f'{v:.0f}') if k.endswith('_refs') or k.startswith('accepted_') else ((lambda v: f'{v:.2f}') if (k.startswith('flag_') and not k.endswith('pct')) or k.startswith('rho_') else (lambda v: f'{v:.1f}'))
        L.append(f'| {nm} | {f(det[k])} | {f(np.median(a))} ({f(np.percentile(a, 2.5))}-{f(np.percentile(a, 97.5))}) |')
        OUT['sensitivity'][k] = {'detected': det[k], 'median': float(np.median(a)), 'lo': float(np.percentile(a, 2.5)), 'hi': float(np.percentile(a, 97.5))}
elif B: L.append('\n(Too few sheet-B items coded for a sensitivity bound.)')
else: L.append('\nSheet B is not coded yet: no sensitivity bound.')
open('data/dataset/independent_agreement.md', 'w').write('\n'.join(L) + '\n'); json.dump(OUT, open('data/dataset/independent_agreement.json', 'w'), indent=1, default=str)
print('\n'.join(L))
