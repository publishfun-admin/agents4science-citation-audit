"""Background worker: parse + verify every PDF that appears in data/openreview/pdfs/, writing data/refs/<stem>.verified.json.
Idempotent: skips PDFs that already have an output. Polls every 20 s; exits after 30 idle polls once >= 300 outputs exist."""
import os, sys, time, json, glob, traceback
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from refs_anystyle import parse_pdf
from refs_verify import verify_parsed_paper
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
PDFS = os.path.join(ROOT, 'data', 'openreview', 'pdfs'); OUT = os.path.join(ROOT, 'data', 'refs'); os.makedirs(OUT, exist_ok=True)
SHARD, NSHARDS = int(os.environ.get('SHARD', 0)), int(os.environ.get('NSHARDS', 1))
idle = 0
while True:
    todo = []
    for p in sorted(glob.glob(os.path.join(PDFS, '*.pdf'))):
        stem = os.path.basename(p)[:-4]
        if stem == 't' or os.path.exists(os.path.join(OUT, stem + '.verified.json')): continue
        try:
            if int(stem.split('_')[0]) % NSHARDS != SHARD: continue
        except ValueError: continue
        if time.time() - os.path.getmtime(p) < 5: continue   # still being written
        todo.append((p, stem))
    if not todo:
        idle += 1
        if idle > 30 and len(glob.glob(os.path.join(OUT, '*.verified.json'))) >= 300: break
        time.sleep(20); continue
    idle = 0
    for p, stem in todo:
        t0 = time.time()
        try:
            parsed = parse_pdf(p)
            res = verify_parsed_paper(parsed) if parsed.get('entries') else []
            json.dump({'pdf': os.path.basename(p), 'n_entries': parsed.get('n_entries', 0), 'fallback': parsed.get('fallback'), 'error': parsed.get('error'), 'entries': res},
                      open(os.path.join(OUT, stem + '.verified.json'), 'w'), indent=1)
            from collections import Counter
            c = Counter(r['verdict'] for r in res if not r.get('junk'))
            print(f"{stem}: entries={parsed.get('n_entries',0)} {dict(c)} {time.time()-t0:.0f}s", flush=True)
        except Exception as e:
            print(f"{stem}: ERROR {e}", flush=True); traceback.print_exc()
            json.dump({'pdf': os.path.basename(p), 'error': f'worker exception: {e}', 'entries': []}, open(os.path.join(OUT, stem + '.verified.json'), 'w'))
