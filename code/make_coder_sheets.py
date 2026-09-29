"""Builds the reference-strings-only sheets for an independent human coder (run once; the released sheets were made with this
script and seed 20261005). Sheet A: the 64 items of data/adjudication/blind/human_coding_sheet.csv in a new random order with new
ids and no labels (map in independent_coder_sheet_A_map.json). Sheet B: a simple random sample of 45 of the manual decisions in
data/adjudication/decisions.csv, reference strings only (map in independent_coder_sheet_B_map.json). Run from the repository root.
Re-running overwrites the sheets, so do not run it after a coder has filled them in."""
import os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
import csv, json, glob, random
random.seed(20261005)
BL='data/adjudication/blind/'
# Sheet A: the 64 items, reference strings only, new random order and ids
rows=list(csv.DictReader(open(BL+'human_coding_sheet.csv')))
order=list(range(len(rows))); random.shuffle(order)
mapA=[]
with open(BL+'independent_coder_sheet_A.csv','w',newline='') as f:
    w=csv.writer(f); w.writerow(['item','reference_as_printed','CODER_CATEGORY','CODER_EVIDENCE_URL','CODER_NOTE'])
    for j,i in enumerate(order,1):
        w.writerow([f'A{j:02d}', rows[i]['reference_as_printed'], '', '', '']); mapA.append({'coder_item':f'A{j:02d}','sheet_item':rows[i]['item'],'key':rows[i]['key']})
json.dump(mapA, open(BL+'independent_coder_sheet_A_map.json','w'), indent=1)
# Sheet B: simple random sample of 45 of the 857 manual decisions, reference strings only
dec=list(csv.DictReader(open('data/adjudication/decisions.csv')))
ent={}
for fpath in glob.glob('data/refs/*.verified.json'):
    num=fpath.split('/')[-1].split('_')[0]
    for e in json.load(open(fpath))['entries']: ent[(num,e['idx'])]=e['raw']
pool=[r for r in dec if (r['number'],int(r['idx'])) in ent]
sample=random.sample(pool,45); mapB=[]
with open(BL+'independent_coder_sheet_B.csv','w',newline='') as f:
    w=csv.writer(f); w.writerow(['item','reference_as_printed','CODER_CATEGORY','CODER_EVIDENCE_URL','CODER_NOTE'])
    for j,r in enumerate(sample,1):
        w.writerow([f'B{j:02d}', ent[(r['number'],int(r['idx']))], '', '', '']); mapB.append({'coder_item':f'B{j:02d}','key':f"{r['number']}:{r['idx']}"})
json.dump(mapB, open(BL+'independent_coder_sheet_B_map.json','w'), indent=1)
print('sheet A:', len(mapA), 'items | sheet B:', len(mapB), 'items (SRS of', len(pool), 'manual decisions, seed 20261005)')
