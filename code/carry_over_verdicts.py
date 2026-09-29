"""After re-parsing, carry over automated VERIFIED verdicts from the previous parse (data/refs_v3) to entries of the
new parse whose raw text is identical, when the new run left them UNVERIFIED (API outages or quota exhaustion during the
re-run must not turn previously verified entries into adjudication work). Usage: python3 code/carry_over_verdicts.py <stem>..."""
import json, os, re, sys, unidecode
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
def norm(x): return re.sub(r'[^a-z0-9]+', ' ', unidecode.unidecode(str(x or '')).lower()).strip()
tot = 0
for stem in sys.argv[1:]:
    po, pn = os.path.join(ROOT, 'data', 'refs_v3', stem + '.verified.json'), os.path.join(ROOT, 'data', 'refs', stem + '.verified.json')
    if not (os.path.exists(po) and os.path.exists(pn)): continue
    old = json.load(open(po)); new = json.load(open(pn))
    om = {norm(e['raw']): e for e in old['entries'] if e.get('verdict') in ('VERIFIED', 'VERIFIED_URL')}
    n = 0
    for e in new['entries']:
        o = om.get(norm(e['raw']))
        if o and e.get('verdict') == 'UNVERIFIED' and not e.get('junk'):
            for k in ('verdict', 'via', 'match', 'metrics', 'evidence', 'second_pass_hit', 'title_guess'):
                if k in o: e[k] = o[k]
            e['carried_over_from'] = 'parser_v3_run'; n += 1
    if n:
        json.dump(new, open(pn, 'w'), indent=1)
    print(f"{stem}: carried over {n} verified verdicts"); tot += n
print('total carried over:', tot)
