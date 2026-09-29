"""Characterise the organiser-flagged example references that could not be matched to a parsed entry:
does the flagged title occur in the submitted PDF (word overlap), what is the closest parsed entry and its status,
and does Crossref know a work with the flagged title. Writes data/dataset/unmatched_flags_verdicts.json and prints a table."""
import csv, glob, json, os, re, subprocess, sys, time, urllib.parse, urllib.request
import pandas as pd
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
def norm(s): return re.sub(r'[^a-z0-9 ]', ' ', str(s).lower())
def get(url):
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'refs-audit/1.0'}), timeout=25) as h: return h.read().decode('utf-8', 'replace')
    except Exception as ex: return 'ERR ' + str(ex)
def crossref_title(title):
    t = get('https://api.crossref.org/works?rows=1&query.bibliographic=' + urllib.parse.quote(title[:250]))
    if t.startswith('ERR'): return None, 0.0
    items = json.loads(t)['message']['items']
    if not items: return None, 0.0
    it = items[0]; tt = (it.get('title') or [''])[0]
    import difflib; return f"{tt[:90]} | {', '.join((a.get('family') or '') for a in it.get('author', [])[:2])} | {(it.get('issued', {}).get('date-parts') or [[None]])[0][0]}", difflib.SequenceMatcher(None, norm(title), norm(tt)).ratio()
dec = {(r['number'], int(r['idx'])): r['category'] for r in csv.DictReader(open(os.path.join(ROOT, 'data/adjudication/decisions.csv')))}
ent = {}
for f in glob.glob(os.path.join(ROOT, 'data/refs/*.verified.json')):
    num = os.path.basename(f).split('_')[0]
    for e in json.load(open(f))['entries']: ent[(num, e['idx'])] = e
of = pd.read_csv(os.path.join(ROOT, 'data/adjudication/organizer_flags.csv')); um = of[of.matched_idx.isna()]
papers = pd.read_csv(os.path.join(ROOT, 'data/dataset/papers.csv'))[['number', 'group']]; grp = dict(zip(papers.number.astype(int), papers.group))
out = []
for _, r in um.iterrows():
    num = str(int(r.number)); title = str(r.flag_title) if not pd.isna(r.flag_title) else str(r.flag_text).split(' by ')[0]
    pdf = glob.glob(os.path.join(ROOT, f'data/openreview/pdfs/{num}_*.pdf'))
    txt = norm(re.sub(r'-\n', '', subprocess.run(['pdftotext', '-q', pdf[0], '-'], capture_output=True, text=True).stdout)) if pdf else ''
    words = [w for w in norm(title).split() if len(w) >= 6]; frac = (sum(1 for w in words if w in txt) / len(words)) if words else 0.0
    best = (0, None)
    for (n, i), e in ent.items():
        if n != num: continue
        sh = sum(1 for w in words if w in norm(e.get('raw', '')))
        if sh > best[0]: best = (sh, i)
    st = None
    if best[1]: st = dec.get((num, best[1]), ent[(num, best[1])].get('verdict'))
    cr, agree = crossref_title(title); time.sleep(1.1)
    verdict = ('flagged title matches a real work (Crossref)' if agree >= 0.85 else ('title not in PDF: checker artefact' if frac < 0.6 else ('closest parsed entry real' if st in ('VERIFIED', 'VERIFIED_URL', 'EXISTS', 'WEB_RESOURCE_EXISTS') else 'indeterminate')))
    out.append({'number': int(num), 'group': grp.get(int(num)), 'flag_title': title[:120], 'title_words_in_pdf': round(frac, 2), 'closest_entry': best[1], 'closest_shared_words': best[0], 'closest_status': st, 'crossref_top': cr, 'crossref_agree': round(agree, 2), 'verdict': verdict})
    print(f"{num:>4} {grp.get(int(num), '')[:9]:9} | {title[:55]:55} | inPDF {frac:.2f} | entry {best[1]} {st} | CR {agree:.2f} | {verdict}")
json.dump(out, open(os.path.join(ROOT, 'data/dataset/unmatched_flags_verdicts.json'), 'w'), indent=1)
import collections; print('summary:', dict(collections.Counter(o['verdict'] for o in out)), '| accepted:', sum(1 for o in out if o['group'] == 'Conference'))
