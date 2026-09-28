"""Parse a PDF's reference list with AnyStyle (CRF parser; Tsang & Keil) and normalise to a common record schema.

Each record: idx, raw, title, authors (family names), year, doi, arxiv, urls, container, parser='anystyle'.
"""
import json, os, re, subprocess, sys
from refs_extract import DOI_RX, ARXIV_RX, ARXIV_OLD_RX, URL_RX

ANYSTYLE = os.path.expanduser('~/.gem/ruby/2.6.0/bin/anystyle')

def _run(args):
    return subprocess.run([ANYSTYLE, *args], capture_output=True, text=True, timeout=600)

def _first(v):
    if isinstance(v, list): return v[0] if v else None
    return v

def parse_pdf(pdf):
    j = _run(['-f', 'json', 'find', pdf])
    r = _run(['-f', 'ref', 'find', pdf])
    recs, raws, fallback = [], [], False
    if j.returncode == 0 and j.stdout.strip():
        try: recs = json.loads(j.stdout)
        except Exception: recs = []
        raws = [l for l in r.stdout.split('\n') if l.strip()] if r.returncode == 0 else []
    if not recs:
        # fallback: heuristic segmentation, then anystyle `parse` on the raw strings
        from refs_extract import extract as _hx
        hx = _hx(pdf)
        raws = [e['raw'] for e in hx['entries']]
        if not raws:
            return {'pdf': pdf, 'error': 'no references found by anystyle-find or heuristic extractor', 'entries': []}
        import tempfile
        with tempfile.NamedTemporaryFile('w', suffix='.txt', delete=False) as tf:
            tf.write('\n'.join(raws)); tmp = tf.name
        pj = _run(['-f', 'json', 'parse', tmp])
        try: recs = json.loads(pj.stdout) if pj.returncode == 0 else []
        except Exception: recs = []
        fallback = True
        if len(recs) != len(raws): raws = []
    entries = []
    for i, rec in enumerate(recs):
        raw = raws[i] if i < len(raws) and len(raws) == len(recs) else None
        blob = raw or ' '.join(str(_first(v)) if not isinstance(v, list) else ' '.join(map(lambda x: x if isinstance(x, str) else json.dumps(x), v)) for v in rec.values())
        authors = []
        for a in (rec.get('author') or []):
            if isinstance(a, dict):
                fam = a.get('family') or a.get('literal') or ''
                if fam: authors.append(fam)
        date = _first(rec.get('date')) or ''
        ym = re.search(r'(19|20)\d{2}', str(date))
        doi = _first(rec.get('doi'))
        if doi: doi = re.sub(r'^(https?://)?(dx\.)?doi\.org/', '', doi, flags=re.I).rstrip('.,;')
        if not doi:
            m = DOI_RX.search(blob); doi = m.group(1).rstrip('.,;') if m else None
        arx = _first(rec.get('arxiv'))
        if not arx:
            m = ARXIV_RX.search(blob) or ARXIV_OLD_RX.search(blob); arx = m.group(1) if m else None
        urls = [u.rstrip('.,;') for u in (rec.get('url') or [])] + [u.rstrip('.,;') for u in URL_RX.findall(blob)]
        urls = list(dict.fromkeys(urls))
        junk = (not authors and not ym) or bool(re.match(r'^(table|figure|fig\.|appendix)\b', str(_first(rec.get('title')) or ''), re.I)) or (len(blob) < 20)
        entries.append({'junk': junk,
            'idx': i + 1, 'raw': raw or blob, 'title': _first(rec.get('title')),
            'authors': authors, 'year': int(ym.group(0)) if ym else None, 'doi': doi, 'arxiv': arx,
            'urls': urls, 'container': _first(rec.get('container-title')) or _first(rec.get('journal')),
            'type': _first(rec.get('type')), 'parser': 'anystyle-parse' if fallback else 'anystyle-find',
        })
    return {'pdf': pdf, 'n_entries': len(entries), 'entries': entries, 'fallback': fallback}

if __name__ == '__main__':
    for p in sys.argv[1:]:
        r = parse_pdf(p)
        print(json.dumps({k: v for k, v in r.items() if k != 'entries'}))
        for e in r['entries']:
            print(f"  [{e['idx']}] {e['year']} | {(e['authors'] or ['?'])[0]} | {e['title']!r:70.70} | doi={e['doi']} arxiv={e['arxiv']} urls={len(e['urls'])}")
