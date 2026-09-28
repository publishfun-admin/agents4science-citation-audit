"""Extract and segment the reference list of a scholarly PDF (deterministic heuristics).

Pipeline: pdftotext -> locate the References section -> segment into entries -> extract identifiers.
Everything is rule-based so that the audit can be reproduced exactly.
"""
import re, subprocess, sys, json

HEAD_RX = re.compile(r'^\s*(?:\d+\s+)?(references|bibliography|reference list|works cited)\s*:?\s*$', re.I)
STOP_RX = re.compile(r'^\s*(?:appendix|appendices|a\.?\s+appendix|supplementary|supplemental|checklist|neurips paper checklist|agents4science.*checklist|ai involvement|a\s+additional|acknowledg)', re.I)
DOI_RX = re.compile(r'\b(10\.\d{4,9}/[^\s"<>]+)', re.I)
ARXIV_RX = re.compile(r'(?:arxiv[:\s,]*(?:preprint\s*)?(?:abs/)?|arxiv\.org/(?:abs|pdf)/)(\d{4}\.\d{4,5})(v\d+)?', re.I)
ARXIV_OLD_RX = re.compile(r'arxiv[:\s/]*([a-z\-]+(?:\.[A-Z]{2})?/\d{7})', re.I)
URL_RX = re.compile(r'https?://[^\s<>"\)\]]+', re.I)
YEAR_RX = re.compile(r'\b((?:19|20)\d{2})[a-z]?\b')

def pdf_to_text(pdf_path):
    out = subprocess.run(['pdftotext', '-enc', 'UTF-8', pdf_path, '-'], capture_output=True, text=True)
    return out.stdout

def find_references_section(text):
    lines = text.split('\n')
    starts = [i for i, l in enumerate(lines) if HEAD_RX.match(l.strip()) and len(l.strip()) < 40]
    if not starts:
        return None, None
    start = starts[-1] if len(starts) > 1 and (len(lines) - starts[-1]) > 15 else starts[0]
    # choose the heading that is followed by the largest reference-looking block
    best = None
    for s in starts:
        block = lines[s+1:]
        end = len(lines)
        for j, l in enumerate(block):
            if STOP_RX.match(l.strip()) and j > 3:
                end = s + 1 + j; break
        sec = '\n'.join(lines[s+1:end])
        score = len(YEAR_RX.findall(sec))
        if best is None or score > best[0]:
            best = (score, s, end)
    _, s, end = best
    return '\n'.join(lines[s+1:end]), (s, end)

def _clean(s):
    s = s.replace('\x0c', ' ')
    s = re.sub(r'-\n(?=[a-z])', '', s)          # de-hyphenate line breaks
    s = re.sub(r'\s*\n\s*', ' ', s)
    return re.sub(r'\s+', ' ', s).strip()

def segment_entries(section):
    """Return list of raw entry strings."""
    sec = section.replace('\x0c', '\n')
    # remove page headers/footers that look like lone page numbers
    sec = re.sub(r'\n\s*\d{1,3}\s*\n', '\n', sec)
    # style 1: [n] numbered
    if len(re.findall(r'(?m)^\s*\[\d{1,3}\]', sec)) >= 3:
        parts = re.split(r'(?m)^\s*(?=\[\d{1,3}\])', sec)
        ents = [_clean(p) for p in parts if re.match(r'\s*\[\d{1,3}\]', p)]
        return [re.sub(r'^\[\d{1,3}\]\s*', '', e) for e in ents]
    # style 2: "n." numbered at line start
    if len(re.findall(r'(?m)^\s*\d{1,3}\.\s+\S', sec)) >= 3:
        parts = re.split(r'(?m)^\s*(?=\d{1,3}\.\s+\S)', sec)
        ents = [_clean(p) for p in parts if re.match(r'\s*\d{1,3}\.\s+\S', p)]
        return [re.sub(r'^\d{1,3}\.\s*', '', e) for e in ents]
    # style 3: author-year with hanging indent or blank-line separation
    if '\n\n' in sec.strip() and len(sec.strip().split('\n\n')) >= 3:
        blocks = [b for b in sec.strip().split('\n\n') if b.strip()]
        ents = [_clean(b) for b in blocks]
        # merge blocks that do not look like entry starts (no capitalised surname + year)
        merged = []
        for e in ents:
            if merged and not re.match(r'^[A-Z][^\d]{0,80}?(?:\(?(?:19|20)\d{2}\)?|,)', e):
                merged[-1] += ' ' + e
            else:
                merged.append(e)
        return merged
    # style 4: line-based heuristic: new entry starts with "Surname, I." pattern at line start
    lines = [l for l in sec.split('\n')]
    ents, cur = [], ''
    start_rx = re.compile(r'^(?:[A-Z][A-Za-z\'\-]+,\s*(?:[A-Z]\.|[A-Z][a-z]+)|[A-Z][a-z]+\s+[A-Z][A-Za-z\'\-]+,)')
    for l in lines:
        if start_rx.match(l.strip()) and cur and YEAR_RX.search(cur):
            ents.append(_clean(cur)); cur = l
        else:
            cur += '\n' + l
    if cur.strip(): ents.append(_clean(cur))
    return [e for e in ents if len(e) > 15]

def extract_ids(entry):
    doi = DOI_RX.search(entry)
    arx = ARXIV_RX.search(entry) or ARXIV_OLD_RX.search(entry)
    urls = URL_RX.findall(entry)
    years = [int(y) for y in YEAR_RX.findall(entry)]
    return {
        'doi': doi.group(1).rstrip('.,;') if doi else None,
        'arxiv': (arx.group(1) if arx else None),
        'urls': [u.rstrip('.,;') for u in urls],
        'year': (max(set(years), key=years.count) if years else None),
    }

def extract(pdf_path):
    text = pdf_to_text(pdf_path)
    section, span = find_references_section(text)
    if section is None:
        return {'pdf': pdf_path, 'error': 'no references section found', 'entries': []}
    entries = segment_entries(section)
    return {'pdf': pdf_path, 'n_entries': len(entries), 'span': span,
            'entries': [dict(idx=i+1, raw=e, **extract_ids(e)) for i, e in enumerate(entries)]}

if __name__ == '__main__':
    for p in sys.argv[1:]:
        r = extract(p)
        print(json.dumps({k: v for k, v in r.items() if k != 'entries'}))
        for e in r['entries']:
            print(f"  [{e['idx']}] doi={e['doi']} arxiv={e['arxiv']} year={e['year']} :: {e['raw'][:160]}")
