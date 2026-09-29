"""QA: parser recall for non-bracket reference lists. For each paper, classify the reference-section style (bracket [n],
number-dot "n.", author-year) from the plain pdftotext text and compare the number of parsed non-junk entries with the
number of year tokens in the section (an upper-bound proxy for the number of entries). Also counts parsed entries that
contain two or more year tokens (merged entries). Writes data/dataset/qa_recall_authoryear.json and prints a summary."""
import glob, json, re, subprocess, numpy as np
YEAR = re.compile(r'\b(?:19[5-9]\d|20[0-2]\d)\b'); BRACK = re.compile(r'^\s*\[\d+\]'); NUMDOT = re.compile(r'^\s*\d{1,3}\.\s+\S')
HEAD = re.compile(r'^\s*(?:\d+\.?\s*)?(references|bibliography|reference list|works cited)\s*$', re.I)
CHK = re.compile(r'(Agents4Science AI Involvement Checklist|AI Involvement Checklist|NeurIPS Paper Checklist|^\s*Checklist\s*$|^\s*Appendix|^\s*Supplementary)', re.I | re.M)
MULTI = re.compile(r'(?:\(\s*(?:19|20)\d\d[a-z]?\s*\)|,\s*(?:19|20)\d\d[a-z]?\s*[.;]|\b(?:19|20)\d\d[a-z]?\.\s)')
rows = []
for f in sorted(glob.glob('data/refs/*.verified.json')):
    stem = f.split('/')[-1].replace('.verified.json', ''); d = json.load(open(f))
    ents = [e for e in d['entries'] if not e.get('junk')]
    if not ents: continue
    txt = subprocess.run(['pdftotext', '-q', f'data/openreview/pdfs/{stem}.pdf', '-'], capture_output=True, text=True).stdout
    lines = txt.split('\n'); idx = [i for i, l in enumerate(lines) if HEAD.match(l)]
    merged = sum(1 for e in ents if len(MULTI.findall(e['raw'])) >= 2)
    if not idx: rows.append({'stem': stem, 'parsed': len(ents), 'year_tokens': None, 'kind': 'nohead', 'merged_entries': merged, 'parser': d.get('fallback')}); continue
    sec = '\n'.join(lines[idx[-1] + 1:]); m = CHK.search(sec); sec = sec[:m.start()] if m else sec
    sl = [l for l in sec.split('\n') if l.strip()]
    kind = 'bracket' if sum(1 for l in sl if BRACK.match(l)) >= 3 else ('numdot' if sum(1 for l in sl if NUMDOT.match(l)) >= 3 else 'authoryear')
    rows.append({'stem': stem, 'parsed': len(ents), 'year_tokens': len(YEAR.findall(sec)), 'kind': kind, 'merged_entries': merged, 'parser': d.get('fallback')})
json.dump(rows, open('data/dataset/qa_recall_authoryear.json', 'w'), indent=1)
for kind in ('authoryear', 'numdot'):
    r = [x for x in rows if x['kind'] == kind and x['year_tokens']]
    if not r: continue
    rat = np.array([x['parsed'] / x['year_tokens'] for x in r])
    print(f"{kind} lists: {len(r)} | parsed/year-tokens median {np.median(rat):.2f}, q25 {np.quantile(rat, .25):.2f}, q10 {np.quantile(rat, .1):.2f}, min {rat.min():.2f} | papers < 0.8: {sum(rat < 0.8)} | merged entries remaining: {sum(x['merged_entries'] for x in r)} in {sum(1 for x in r if x['merged_entries'])} papers")
print('kinds:', {k: sum(1 for x in rows if x['kind'] == k) for k in ('bracket', 'numdot', 'authoryear', 'nohead')}, '| merged entries in all lists:', sum(x['merged_entries'] for x in rows))
