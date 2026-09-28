"""Layout-aware reference segmentation using pdftotext -layout indentation (for author-year / hanging-indent styles).

Strategy: extract the references section from the -layout text; an entry starts on a line whose indentation
equals the block's minimum indentation and is followed by more-indented continuation lines. Two-column pages are
handled by cropping each column separately (pdftotext -x/-W) so indentation stays meaningful.
"""
import re, subprocess, statistics, sys
from refs_extract import HEAD_RX, STOP_RX, YEAR_RX, _clean, extract_ids

def _pdftotext(pdf, extra=()):
    return subprocess.run(['pdftotext', '-enc', 'UTF-8', '-layout', *extra, pdf, '-'], capture_output=True, text=True).stdout

def _page_count(pdf):
    out = subprocess.run(['pdfinfo', pdf], capture_output=True, text=True).stdout
    m = re.search(r'Pages:\s+(\d+)', out); return int(m.group(1)) if m else 0

def _page_size(pdf):
    out = subprocess.run(['pdfinfo', pdf], capture_output=True, text=True).stdout
    m = re.search(r'Page size:\s+([\d.]+) x ([\d.]+)', out); return (float(m.group(1)), float(m.group(2))) if m else (612.0, 792.0)

def _is_two_column(layout_text):
    lines = [l for l in layout_text.split('\n') if len(l.strip()) > 40]
    if len(lines) < 20: return False
    hits = sum(1 for l in lines if re.search(r'\S\s{6,}\S', l[len(l)//4: 3*len(l)//4]))
    return hits / len(lines) > 0.45

def layout_text(pdf):
    """Return -layout text; if the document is two-column, return column-wise text page by page."""
    full = _pdftotext(pdf)
    if not _is_two_column(full):
        return full
    w, h = _page_size(pdf); n = _page_count(pdf)
    parts = []
    for p in range(1, n + 1):
        for x0 in (0, int(w / 2)):
            parts.append(_pdftotext(pdf, ('-f', str(p), '-l', str(p), '-x', str(x0), '-y', '0', '-W', str(int(w / 2) + 1), '-H', str(int(h)))))
    return '\n'.join(parts)

def references_block(text):
    lines = text.split('\n')
    starts = [i for i, l in enumerate(lines) if HEAD_RX.match(l.strip()) and len(l.strip()) < 40]
    if not starts: return None
    best = None
    for s in starts:
        end = len(lines)
        for j, l in enumerate(lines[s+1:]):
            if STOP_RX.match(l.strip()) and j > 3: end = s + 1 + j; break
        sec = lines[s+1:end]
        score = len(YEAR_RX.findall('\n'.join(sec)))
        if best is None or score > best[0]: best = (score, sec)
    return best[1] if best else None

def segment_by_indent(lines):
    body = [l for l in lines if l.strip()]
    if len(body) < 3: return []
    indents = [len(l) - len(l.lstrip(' ')) for l in body]
    base = min(indents)
    # continuation indent must be visibly larger than base for at least 30% of lines
    deeper = [i for i in indents if i > base + 1]
    if len(deeper) < 0.3 * len(body): return []
    entries, cur = [], None
    for l, ind in zip(body, indents):
        s = l.strip()
        if re.fullmatch(r'\d{1,3}', s): continue          # page numbers
        if ind <= base + 1:
            if cur: entries.append(cur)
            cur = s
        else:
            cur = (cur + '\n' + s) if cur else s
    if cur: entries.append(cur)
    out = [_clean(e) for e in entries]
    # merge fragments that clearly are not entry starts (no letters / very short)
    merged = []
    for e in out:
        if merged and (len(e) < 25 or not re.search(r'[A-Za-z]{3}', e)):
            merged[-1] += ' ' + e
        else:
            merged.append(e)
    return merged

def extract_layout(pdf):
    txt = layout_text(pdf)
    blk = references_block(txt)
    if blk is None: return {'pdf': pdf, 'error': 'no references section (layout)', 'entries': []}
    # strip numbering if present so that indentation logic works uniformly
    ents = segment_by_indent(blk)
    ents = [re.sub(r'^\[?\d{1,3}[\]\.]\s*', '', e) for e in ents]
    return {'pdf': pdf, 'n_entries': len(ents), 'entries': [dict(idx=i+1, raw=e, **extract_ids(e)) for i, e in enumerate(ents)]}

if __name__ == '__main__':
    import json
    for p in sys.argv[1:]:
        r = extract_layout(p)
        print(json.dumps({k: v for k, v in r.items() if k != 'entries'}))
        for e in r['entries']: print(f"  [{e['idx']}] {e['raw'][:150]}")
