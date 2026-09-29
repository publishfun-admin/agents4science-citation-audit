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

LINENUM_RX = re.compile(r'^(\s*)\d{1,3}(\s{2,})')
CHECKLIST_RX = re.compile(r'^\s*(?:\d+\s+)?(?:neurips paper checklist|agents4science(?: ai involvement)? checklist|checklist|ai involvement checklist|appendix [a-z][:.]?\s*checklist)\s*$', re.I)
REFHEAD_RX = re.compile(r'^\s*(?:\d+\s+)?(references|bibliography)\s*$', re.I)

TWOCOL_RX = re.compile(r'\S.{9,}?\s{5,}\S')   # text, wide gap, text on one line

def clean_layout_text(pdf):
    """pdftotext -layout, with review-template margin line numbers stripped and the trailing checklist removed."""
    txt = subprocess.run(['pdftotext', '-layout', '-enc', 'UTF-8', pdf, '-'], capture_output=True, text=True).stdout
    lines = txt.split('\n'); nonempty = [l for l in lines if l.strip()]
    numbered = sum(1 for l in nonempty if re.match(r'^\s*\d{1,3}\s{2,}\S', l))
    # review-template margin numbers: many lines start with a 1-3 digit number AND those numbers run consecutively
    nums = [int(m.group(1)) for l in nonempty for m in [re.match(r'^\s*(\d{1,3})\s{2,}\S', l)] if m]
    consecutive = sum(1 for a, b in zip(nums, nums[1:]) if b == a + 1)
    stripped = (numbered / max(len(nonempty), 1) >= 0.25) or consecutive >= 30
    if stripped: lines = [LINENUM_RX.sub(r'\1\2', l) for l in lines]
    refidx = [i for i, l in enumerate(lines) if REFHEAD_RX.match(l)]
    if refidx:
        start = refidx[-1]
        for i in range(start + 1, len(lines)):
            if CHECKLIST_RX.match(lines[i]): lines = lines[:i]; break
    # two-column papers: -layout interleaves the columns (most lines carry text, a wide gap, then more text),
    # which garbles every reference. Detect that at document level and use pdftotext's reading-order output instead.
    gapped = sum(1 for l in nonempty if TWOCOL_RX.search(l))
    two_col = len(nonempty) >= 50 and gapped / len(nonempty) >= 0.3
    if two_col:
        raw = subprocess.run(['pdftotext', '-enc', 'UTF-8', pdf, '-'], capture_output=True, text=True).stdout
        rl = raw.split('\n')
        if stripped: rl = [l for l in rl if not re.match(r'^\s*\d{1,3}\s*$', l)]
        ridx2 = [i for i, l in enumerate(rl) if REFHEAD_RX.match(l)]
        if ridx2:
            for i in range(ridx2[-1] + 1, len(rl)):
                if CHECKLIST_RX.match(rl[i]): rl = rl[:i]; break
        lines = rl
    return '\n'.join(lines), stripped, two_col

YEARTOK_RX = re.compile(r'\b(?:19[5-9]\d|20[0-2]\d)[a-z]?\b')

def _join_lines(ls):
    out = ''
    for l in ls:
        t = l.strip()
        if not t: continue
        if out.endswith('-') and t[:1].islower(): out = out[:-1] + t
        else: out = (out + ' ' + t) if out else t
    return out

def _indent_guided(text, n_found):
    """Segment the reference section at entry starts identified by hanging indentation (or by blank lines).
    Returns (recs, raws) when the segmentation yields more entries than the finder and parses cleanly, else (None, None)."""
    lines = text.split('\n')
    ridx = [i for i, l in enumerate(lines) if REFHEAD_RX.match(l)]
    if not ridx: return None, None
    sec = lines[ridx[-1] + 1:]
    for i, l in enumerate(sec):
        if CHECKLIST_RX.match(l): sec = sec[:i]; break
    keep = [l for l in sec if not re.fullmatch(r'\s*\d{1,3}\s*', l)]          # drop bare page numbers
    nonempty = [l for l in keep if l.strip()]
    if len(nonempty) < 6: return None, None
    if sum(1 for l in nonempty if re.match(r'^\s*\[\d{1,3}\]', l)) >= 3: return None, None   # bracket lists: finder + marker path
    indents = [len(l) - len(l.lstrip(' ')) for l in nonempty]
    from collections import Counter
    cnt = Counter(indents)

    def finish(chunks):
        for _pass in range(3):   # re-join chunks that were split inside one entry (an entry can be split over three lines)
            merged = []
            for c in chunks:
                if merged:
                    prev = merged[-1]; last = prev.split()[-1] if prev.split() else ''
                    open_ended = prev.endswith('-') or re.search(r'[,:(]$', prev) or (re.fullmatch(r'[a-z]+', last) is not None and last not in ('al',))
                    cont = c[:1].islower() or re.match(r'^\d+\s*[-\u2013]\s*\d+\.?$', c) or len(c) < 16 or (not YEARTOK_RX.search(prev) and (len(c) < 60 or not re.search(r'[.)\]/0-9]$', prev) or YEARTOK_RX.search(c)))
                    if open_ended or cont:
                        merged[-1] = (prev[:-1] + c) if prev.endswith('-') and c[:1].islower() else (prev + ' ' + c); continue
                merged.append(c)
            done = len(merged) == len(chunks); chunks = merged
            if done: break
        chunks = [re.sub(r'^\d{1,3}\.\s+', '', c) for c in chunks if len(c) > 15]
        run = 0   # the list ends where chunks stop carrying years (appendices, figure captions, checklists)
        for i, c in enumerate(chunks):
            run = 0 if YEARTOK_RX.search(c) else run + 1
            if run >= 3: chunks = chunks[:i - 2]; break
        return chunks

    def score(ch):   # candidate quality: share of chunks with a year, then count
        wy = sum(1 for c in ch if YEARTOK_RX.search(c)); return (wy >= 0.85 * len(ch) and len(ch) >= 3, wy)
    cands = []
    for base in sorted(v for v, c in cnt.items() if c >= 3):          # try each plausible entry-start indent
        for tol in (0, 1):                                              # continuation lines may sit 1 space in, or more
            is_start = [ind <= base + tol for ind in indents]
            if sum(is_start) < 3 or sum(1 for x in is_start if not x) < 0.25 * len(indents): continue
            chunks, cur = [], []
            for l, st in zip(nonempty, is_start):
                if st and cur: chunks.append(_join_lines(cur)); cur = []
                cur.append(l)
            if cur: chunks.append(_join_lines(cur))
            cands.append(finish(chunks))
    blocks, cur = [], []                                                # blank-line separated blocks
    for l in keep:
        if l.strip(): cur.append(l)
        elif cur: blocks.append(_join_lines(cur)); cur = []
    if cur: blocks.append(_join_lines(cur))
    cands.append(finish(blocks))
    cands = [c for c in cands if score(c)[0]]
    chunks = max(cands, key=lambda c: (score(c)[1], -len(c))) if cands else []
    if len(chunks) < 3: return None, None
    withyear = sum(1 for c in chunks if YEARTOK_RX.search(c)); frag = len(chunks) - withyear
    n_found_year, n_found_frag = n_found if isinstance(n_found, tuple) else (n_found, 10**6)
    if withyear < n_found_year or (withyear == n_found_year and frag >= n_found_frag): return None, None   # adopt only if it recovers more entries or fewer fragments than the finder
    import tempfile as _tf
    with _tf.NamedTemporaryFile('w', suffix='.txt', delete=False) as tf2:
        tf2.write('\n'.join(chunks)); tmp2 = tf2.name
    pj = _run(['-f', 'json', 'parse', tmp2])
    try: recs2 = json.loads(pj.stdout) if pj.returncode == 0 and pj.stdout.strip() else []
    except Exception: recs2 = []
    if len(recs2) == len(chunks): return recs2, chunks
    recs2 = []   # anystyle split or dropped a line: parse chunk by chunk so records stay aligned with the raw strings
    for c in chunks:
        with _tf.NamedTemporaryFile('w', suffix='.txt', delete=False) as tf3:
            tf3.write(c); tmp3 = tf3.name
        pc = _run(['-f', 'json', 'parse', tmp3])
        try: rc = json.loads(pc.stdout) if pc.returncode == 0 and pc.stdout.strip() else []
        except Exception: rc = []
        recs2.append(rc[0] if rc else {'title': None})
    return recs2, chunks

def parse_pdf(pdf):
    import tempfile
    text, stripped, two_col = clean_layout_text(pdf)
    with tempfile.NamedTemporaryFile('w', suffix='.txt', delete=False) as tf:
        tf.write(text); txtpath = tf.name
    j = _run(['-f', 'json', 'find', txtpath])
    r = _run(['-f', 'ref', 'find', txtpath])
    recs, raws, fallback = [], [], False
    if j.returncode == 0 and j.stdout.strip():
        try: recs = json.loads(j.stdout)
        except Exception: recs = []
        raws = [l for l in r.stdout.split('\n') if l.strip()] if r.returncode == 0 else []
    # marker-guided path: bracket-numbered lists where the finder dropped entries
    try:
        lines = text.split('\n')
        ridx = [i for i, l in enumerate(lines) if REFHEAD_RX.match(l)]
        if ridx:
            sec = lines[ridx[-1] + 1:]
            starts = [i for i, l in enumerate(sec) if re.match(r'^\s*\[\d{1,3}\]', l)]
            if len(starts) >= 3 and len(recs) < 0.9 * len(starts):
                entries_raw = []
                for a, b in zip(starts, starts[1:] + [len(sec)]):
                    chunk = ' '.join(x.strip() for x in sec[a:b] if x.strip())
                    chunk = re.sub(r'^\[\d{1,3}\]\s*', '', chunk)
                    if len(chunk) > 15: entries_raw.append(chunk)
                import tempfile as _tf
                with _tf.NamedTemporaryFile('w', suffix='.txt', delete=False) as tf2:
                    tf2.write('\n'.join(entries_raw)); tmp2 = tf2.name
                pj = _run(['-f', 'json', 'parse', tmp2])
                recs2 = json.loads(pj.stdout) if pj.returncode == 0 and pj.stdout.strip() else []
                if len(recs2) == len(entries_raw) and len(recs2) > len(recs):
                    recs, raws, fallback = recs2, entries_raw, 'marker-guided'
    except Exception:
        pass
    # indent-guided path (parser v4): hanging-indent or blank-line-separated lists (author-year, "1." numbered)
    # where the finder merged several references into one entry
    try:
        if fallback != 'marker-guided':
            n_year = sum(1 for r0 in recs if re.search(r'(19|20)\d{2}', str(_first(r0.get('date')) or '')))
            n_frag = len(recs) - n_year
            recs2, entries_raw = _indent_guided(text, (n_year, n_frag))
            if recs2 is not None:
                recs, raws, fallback = recs2, entries_raw, 'indent-guided'
    except Exception:
        pass
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
            'type': _first(rec.get('type')), 'parser': ('anystyle-marker-guided' if fallback == 'marker-guided' else ('anystyle-indent-guided' if fallback == 'indent-guided' else ('anystyle-parse' if fallback else 'anystyle-find'))),
        })
    return {'pdf': pdf, 'n_entries': len(entries), 'entries': entries, 'fallback': fallback, 'linenumbers_stripped': stripped, 'two_column': two_col, 'parser_version': 4}

if __name__ == '__main__':
    for p in sys.argv[1:]:
        r = parse_pdf(p)
        print(json.dumps({k: v for k, v in r.items() if k != 'entries'}))
        for e in r['entries']:
            print(f"  [{e['idx']}] {e['year']} | {(e['authors'] or ['?'])[0]} | {e['title']!r:70.70} | doi={e['doi']} arxiv={e['arxiv']} urls={len(e['urls'])}")
