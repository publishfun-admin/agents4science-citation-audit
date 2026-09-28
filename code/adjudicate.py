"""Manual adjudication helper.
  python code/adjudicate.py next N        -> print the next N pending entries (papers through the 2nd pass; accepted first)
  python code/adjudicate.py record        -> read a JSON list of decisions from stdin and append to data/adjudication/decisions.csv
  python code/adjudicate.py status        -> counts
Decision fields: key ("number:idx"), category, evidence_url, note."""
import sys, json, glob, os, re, csv, datetime
import pandas as pd
DEC = 'data/adjudication/decisions.csv'
FIELDS = ['number', 'forum_id', 'idx', 'category', 'evidence_url', 'note', 'title', 'first_author', 'year', 'adjudicated_by', 'date']
PRIORITY = {'Conference': 0, 'Rejected_Submission': 1, 'Withdrawn_Submission': 2, 'Desk_Rejected_Submission': 3}

def load_decisions():
    if not os.path.exists(DEC): return set()
    return {(int(r['number']), int(r['idx'])) for r in csv.DictReader(open(DEC))}

def pending():
    papers = pd.read_csv('data/dataset/papers.csv').set_index('number')
    done = load_decisions(); items = []
    for f in sorted(glob.glob('data/refs/*.verified.json')):
        m = re.match(r'^(\d+)_([A-Za-z0-9_-]+)\.verified\.json$', os.path.basename(f))
        if not m: continue
        d = json.load(open(f))
        if not isinstance(d, dict) or not d.get('second_pass'): continue
        n = int(m.group(1)); grp = papers.loc[n, 'group'] if n in papers.index else 'zz'
        for e in d.get('entries', []):
            if e.get('junk') or e.get('verdict') != 'UNVERIFIED' or (n, e['idx']) in done: continue
            best = None
            for x in e.get('evidence', []):
                if 'rec' in x:
                    mt = x.get('metrics', {}); s = round(mt.get('title_sim', 0))
                    if best is None or s > best[2]: best = (x['rec'].get('title') or '', x['rec'].get('year'), s, x['rec'].get('first_author'))
            t = e.get('title'); au = (e.get('authors') or [])
            q = (f'"{t}"' + (f' {au[0]}' if au else '')) if t and len(t) >= 8 else (e.get('raw') or '')[:140]
            items.append({'key': f"{n}:{e['idx']}", 'grp': PRIORITY.get(grp, 9), 'n': n, 'forum_id': m.group(2), 'idx': e['idx'], 'title': t, 'first_author': au[0] if au else None, 'n_auth': len(au),
                          'year': e.get('year'), 'container': e.get('container'), 'doi': e.get('doi'), 'arxiv': e.get('arxiv'), 'urls': (e.get('urls') or [])[:2], 'raw': (e.get('raw') or '')[:220],
                          'best': best, 'q': q})
    items.sort(key=lambda x: (x['grp'], x['n'], x['idx']))
    return items

if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == 'next':
        N = int(sys.argv[2]); its = pending()
        print(f"pending total: {len(its)}")
        for it in its[:N]:
            print(f"\n[{it['key']}] {it['year']} | {it['first_author']} (+{max(it['n_auth']-1,0)}) | title={it['title']!r} | in={it['container']!r} | doi={it['doi']} arxiv={it['arxiv']} urls={it['urls']}")
            print(f"   raw: {it['raw']}")
            if it['best']: print(f"   nearest db hit: {it['best'][0][:100]!r} ({it['best'][1]}, {it['best'][3]}, sim {it['best'][2]})")
            print(f"   Q: {it['q']}")
    elif cmd == 'record':
        rows = json.load(sys.stdin); done = load_decisions(); new = 0
        papers = pd.read_csv('data/dataset/papers.csv').set_index('number')
        info = {}
        for f in glob.glob('data/refs/*.verified.json'):
            m = re.match(r'^(\d+)_([A-Za-z0-9_-]+)\.verified\.json$', os.path.basename(f))
            if not m: continue
            d = json.load(open(f))
            if isinstance(d, dict):
                for e in d.get('entries', []): info[(int(m.group(1)), e['idx'])] = (m.group(2), e.get('title'), (e.get('authors') or [None])[0], e.get('year'))
        exists = os.path.exists(DEC)
        with open(DEC, 'a', newline='') as f:
            w = csv.DictWriter(f, fieldnames=FIELDS)
            if not exists: w.writeheader()
            for r in rows:
                n, idx = map(int, r['key'].split(':'))
                if (n, idx) in done: continue
                fid, t, au, y = info.get((n, idx), (None, None, None, None))
                w.writerow({'number': n, 'forum_id': fid, 'idx': idx, 'category': r['category'], 'evidence_url': r.get('evidence_url', ''), 'note': r.get('note', ''), 'title': t, 'first_author': au, 'year': y,
                            'adjudicated_by': 'claude-fable-5.1 (web search)', 'date': datetime.date.today().isoformat()}); new += 1
        print(f"recorded {new} decisions; total {len(load_decisions())}")
    elif cmd == 'propagate':
        # copy each decision to pending entries in other papers with the same normalised title + year (duplicate submissions)
        import unidecode
        def norm(x): return re.sub(r'[^a-z0-9]+', ' ', unidecode.unidecode(str(x or '')).lower()).strip()
        dec = list(csv.DictReader(open(DEC))); done = load_decisions()
        by_key = {}
        for r in dec:
            if r['title'] and len(norm(r['title'])) > 15: by_key[(norm(r['title']), str(r['year']))] = r
        its = pending(); rows = []
        for it in its:
            k = (norm(it['title']), str(it['year']))
            if k in by_key and (it['n'], it['idx']) not in done:
                src = by_key[k]; rows.append({'key': it['key'], 'category': src['category'], 'evidence_url': src['evidence_url'], 'note': f"[propagated from {src['number']}:{src['idx']}] " + (src['note'] or '')})
        if rows:
            with open(DEC, 'a', newline='') as f:
                w = csv.DictWriter(f, fieldnames=FIELDS)
                papers = pd.read_csv('data/dataset/papers.csv').set_index('number')
                info = {}
                for fpath in glob.glob('data/refs/*.verified.json'):
                    m = re.match(r'^(\d+)_([A-Za-z0-9_-]+)\.verified\.json$', os.path.basename(fpath))
                    if not m: continue
                    d = json.load(open(fpath))
                    if isinstance(d, dict):
                        for e in d.get('entries', []): info[(int(m.group(1)), e['idx'])] = (m.group(2), e.get('title'), (e.get('authors') or [None])[0], e.get('year'))
                for r in rows:
                    n, idx = map(int, r['key'].split(':')); fid, t, au, y = info.get((n, idx), (None, None, None, None))
                    w.writerow({'number': n, 'forum_id': fid, 'idx': idx, 'category': r['category'], 'evidence_url': r['evidence_url'], 'note': r['note'], 'title': t, 'first_author': au, 'year': y, 'adjudicated_by': 'propagated (identical entry)', 'date': datetime.date.today().isoformat()})
        print(f"propagated {len(rows)} decisions")
    elif cmd == 'update':
        # overwrite category/evidence_url/note for existing decisions; JSON list on stdin with key + fields to change; note_append appends
        ups = {r['key']: r for r in json.load(sys.stdin)}
        rows = list(csv.DictReader(open(DEC))); n = 0
        for r in rows:
            k = f"{r['number']}:{r['idx']}"
            if k in ups:
                u = ups[k]
                for f_ in ('category', 'evidence_url', 'note'):
                    if f_ in u: r[f_] = u[f_]
                if 'note_append' in u: r['note'] = (r['note'] or '') + ' ' + u['note_append']
                r['date'] = datetime.date.today().isoformat(); n += 1
        with open(DEC, 'w', newline='') as f:
            w = csv.DictWriter(f, fieldnames=FIELDS); w.writeheader(); w.writerows(rows)
        print(f"updated {n} decisions")
    elif cmd == 'second_queue':
        # NOT_FOUND decisions still marked "[2nd search pending]": print an alternative (author + distinctive words) query
        import unidecode
        N = int(sys.argv[2]) if len(sys.argv) > 2 else 20
        rows = [r for r in csv.DictReader(open(DEC)) if r['category'] == 'NOT_FOUND' and '[2nd search pending]' in (r['note'] or '')]
        print(f"second-search pending: {len(rows)}")
        STOP = set('the a an of and in on for to with by from at as is are be via its into over under toward towards using based approach study analysis learning model models system systems method methods data deep neural network networks'.split())
        for r in rows[:N]:
            words = [w for w in re.findall(r'[A-Za-z][A-Za-z-]{3,}', unidecode.unidecode(r['title'] or '')) if w.lower() not in STOP][:5]
            print(f"[{r['number']}:{r['idx']}] {r['first_author']} {r['year']} | {r['title']!r:80.80} | Q2: {r['first_author'] or ''} {' '.join(words)}")
    elif cmd == 'status':
        its = pending(); done = load_decisions()
        print(f"pending: {len(its)} | decided: {len(done)}")
        if os.path.exists(DEC):
            df = pd.read_csv(DEC); print(df.category.value_counts().to_dict())
