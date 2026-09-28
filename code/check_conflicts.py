"""List adjudicated entries whose automated verdict is now VERIFIED (e.g. verified by a later pass after the manual decision),
so the manual decision can be re-examined. Usage: python3 code/check_conflicts.py"""
import csv, glob, json, os
dec = {(r['number'], r['idx']): r for r in csv.DictReader(open('data/adjudication/decisions.csv'))}
n = 0
for f in sorted(glob.glob('data/refs/*.verified.json')):
    try: d = json.load(open(f))
    except Exception: continue
    num = os.path.basename(f).split('_')[0]
    for e in d.get('entries', []):
        r = dec.get((num, str(e['idx'])))
        if r and e.get('verdict') in ('VERIFIED', 'VERIFIED_URL') and r['category'] not in ('EXISTS', 'WEB_RESOURCE_EXISTS'):
            n += 1; m = e.get('match') or {}
            print(f"{num}:{e['idx']} manual={r['category']} auto={e.get('verdict')} via={e.get('via')} | cited: {(e.get('title') or '')[:70]} | matched: {(m.get('title') or '')[:70]} ({m.get('year')}, {m.get('first_author')})")
print(f'{n} conflicts')
