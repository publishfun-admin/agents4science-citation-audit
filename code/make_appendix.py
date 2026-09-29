"""Assemble the manuscript appendix (auditable tables) from the released analysis outputs and print it as Markdown."""
import json, os, re, csv, collections
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
rt = open(os.path.join(ROOT, 'paper/results_tables.md')).read()
def section(md, head):
    m = re.search(r'^## ' + re.escape(head) + r'.*?\n(.*?)(?=^## |\Z)', md, re.S | re.M); return m.group(1).strip() if m else ''
out = ['## Appendix A. Auditable tables\n', '### A.1 Flow of references\n', section(rt, 'Flow of references'), '']
bc = open(os.path.join(ROOT, 'data/dataset/blind_checks.md')).read()
out += ['### A.2 Blind second adjudication: confusion of categories (first adjudicator -> blind adjudicator)\n']
conf = re.search(r'Confusion \(first adjudicator -> blind\): (.*)', bc).group(1)
pairs = [(a.split('->')[0].strip(), a.split('->')[1].split(':')[0].strip(), int(a.split(':')[-1])) for a in conf.split(';')]
cats = ['EXISTS', 'EXISTS_CORRUPTED', 'NOT_FOUND', 'PLACEHOLDER', 'UNADJUDICABLE']; M = collections.defaultdict(int)
for a, b, c in pairs: M[(a, b)] += c
out += ['| First \\ Blind | ' + ' | '.join(cats) + ' |', '|:--|' + '--:|' * len(cats)]
for a in cats:
    if any(M[(a, b)] for b in cats): out.append(f'| {a} | ' + ' | '.join(str(M[(a, b)]) for b in cats) + ' |')
out += ['', '### A.3 Blind check of automatically verified entries, by verification source\n']
src = re.search(r'- By source: (.*)', bc).group(1)
out += ['| Source | Corrupted / sampled | Invented / sampled | Population |', '|:--|--:|--:|--:|']
for part in src.split(';'):
    m = re.match(r'\s*(\w+): (\d+)/(\d+) corrupted, (\d+)/(\d+) not found \(population (\d+)\)', part)
    if m: out.append(f'| {m.group(1)} | {m.group(2)}/{m.group(3)} | {m.group(4)}/{m.group(5)} | {m.group(6)} |')
out += ['', '### A.4 The 27 organiser-flagged examples that could not be matched to a parsed entry\n', '| Submission | Group | Flagged title (truncated) | Title words in PDF | Closest parsed entry status | Verdict |', '|--:|:--|:--|--:|:--|:--|']
for o in json.load(open(os.path.join(ROOT, 'data/dataset/unmatched_flags_verdicts.json'))):
    out.append(f"| {o['number']} | {str(o['group']).replace('_Submission','').replace('Conference','Accepted')} | {o['flag_title'][:70].replace('|','/')} | {o['title_words_in_pdf']:.2f} | {o['closest_status'] or 'none'} | {o['verdict']} |")
out += ['', '### A.5 Search-channel analysis of NOT_FOUND decisions\n', open(os.path.join(ROOT, 'data/dataset/channel_analysis.md')).read().split('\n', 1)[1].strip(), '']
out += ['### A.6 Manual inspection of low-ratio reference lists\n', open(os.path.join(ROOT, 'data/dataset/manual_recall_inspection.md')).read().strip() if os.path.exists(os.path.join(ROOT, 'data/dataset/manual_recall_inspection.md')) else '(see data/dataset/manual_recall_inspection.md)', '']
hp = os.path.join(ROOT, 'data/dataset/human_agreement.md')
if os.path.exists(hp):
    out += ['### A.7 Human coding of 64 items by the author (a disclosed, non-independent, attestation-blinded check): agreement with the agent labels\n']
    for line in open(hp).read().split('\n'):
        if line.startswith('- Human vs') or line.startswith('- On the'): out.append(line)
    out.append('')
ip = os.path.join(ROOT, 'data/dataset/independent_agreement.md')
if os.path.exists(ip) and '## Sheet B' in open(ip).read():
    txt = open(ip).read()
    out += ['### A.8 Independent human coding of the random sample of manual decisions (sheet B) and of the 64-item sheet (sheet A): agreement and sensitivity bound\n']
    for line in txt.split('\n'):
        if line.startswith('Sheet ') or line.startswith('- Coder vs') or line.startswith('  - first adjudicator') or line.startswith("- The author's") or line.startswith('- On the'): out.append(line)
    if '## Sensitivity' in txt:
        head, rest = txt.split('## Sensitivity', 1)[1].split('\n', 1)
        out += ['', '**Sensitivity' + head.rstrip() + '**', rest.strip()]
    out.append('')
print('\n'.join(out))
