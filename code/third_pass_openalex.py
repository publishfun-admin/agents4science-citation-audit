"""Deferred OpenAlex pass: waits until the OpenAlex free budget is available again, then re-queries OpenAlex for every
non-junk UNVERIFIED entry that has a parsed title, in files that have completed the second pass. Marks files with
'openalex_pass': True. Entries verified here get via='openalex_pass3'."""
import os, sys, json, glob, time, urllib.request
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('SHARD', 'p3')
import refs_verify as rv

def budget_ok():
    try:
        req = urllib.request.Request('https://api.openalex.org/works?search=test&per-page=1', headers={'User-Agent': rv.UA})
        with urllib.request.urlopen(req, timeout=20) as r: return r.status == 200
    except Exception: return False

while not budget_ok():
    print('OpenAlex budget not available; sleeping 15 min', flush=True); time.sleep(900)
print('OpenAlex available; starting third pass', flush=True)
idle = 0
while True:
    todo = []
    for f in sorted(glob.glob('data/refs/*.verified.json')):
        try: d = json.load(open(f))
        except Exception: continue
        if isinstance(d, dict) and d.get('second_pass') and not d.get('openalex_pass'): todo.append((f, d))
    if not todo:
        idle += 1
        if idle > 40: break
        time.sleep(60); continue
    idle = 0
    for f, d in todo:
        n = 0
        for e in d.get('entries', []):
            if e.get('junk') or e.get('verdict') != 'UNVERIFIED' or not e.get('title'): continue
            for c in rv.openalex_search(e['title']):
                ok, m = rv._accept_parsed(c, e)
                if ok: e.update({'verdict': 'VERIFIED', 'via': 'openalex_pass3', 'match': c, 'metrics': m}); n += 1; break
        d['openalex_pass'] = True
        json.dump(d, open(f, 'w'), indent=1); rv._save_cache()
        print(f"{os.path.basename(f)}: +{n} via OpenAlex (3rd pass)", flush=True)
        if rv._blocked_until.get('api.openalex.org', 0) > time.time():
            print('OpenAlex budget exhausted again; waiting', flush=True); time.sleep(900)
