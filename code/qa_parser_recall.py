"""QA: parser recall on bracket-numbered reference lists = parsed non-junk entries / highest [n] marker in the reference section."""
import sys, glob, os, re, json, statistics; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from refs_anystyle import clean_layout_text, REFHEAD_RX
rows = []
for f in sorted(glob.glob('data/refs/*.verified.json')):
    d = json.load(open(f)); stem = os.path.basename(f).replace('.verified.json', '')
    if not isinstance(d, dict) or not d.get('entries'): continue
    pdf = f'data/openreview/pdfs/{stem}.pdf'
    if not os.path.exists(pdf): continue
    txt, _ = clean_layout_text(pdf); lines = txt.split('\n')
    idx = [i for i, l in enumerate(lines) if REFHEAD_RX.match(l)]
    if not idx: continue
    nums = [int(x) for x in re.findall(r'^\s*\[(\d{1,3})\]', '\n'.join(lines[idx[-1] + 1:]), flags=re.M)]
    if len(nums) >= 3: rows.append((stem, len([e for e in d['entries'] if not e.get('junk')]), max(nums)))
ratios = [r[1] / r[2] for r in rows]
print(f'bracket-numbered papers: {len(rows)}; parsed/max-marker median {statistics.median(ratios):.2f}, min {min(ratios):.2f}; papers below 0.9: {[r for r in rows if r[1] / r[2] < 0.9]}')
json.dump(rows, open('data/dataset/qa_parser_recall.json', 'w'))
