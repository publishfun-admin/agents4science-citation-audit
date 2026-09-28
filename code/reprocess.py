"""Re-parse and re-verify specific papers with the current parser (e.g. after a parser fix).
Usage: python3 code/reprocess.py <stem> [<stem> ...]   (stem = '13_q0qXOaBOIC')
Overwrites data/refs/<stem>.verified.json without the second_pass / arxiv_repass flags so the later passes re-run."""
import os, sys, json, time
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('SHARD', 'p_re'); os.environ.setdefault('SKIP_DBLP', '1')
from refs_anystyle import parse_pdf
from refs_verify import verify_parsed_paper, _save_cache
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
for stem in sys.argv[1:]:
    t = time.time(); pdf = os.path.join(ROOT, 'data', 'openreview', 'pdfs', stem + '.pdf')
    try:
        parsed = parse_pdf(pdf)
        res = verify_parsed_paper(parsed, do_arxiv_search=False) if parsed.get('entries') else []
        out = {'pdf': os.path.basename(pdf), 'n_entries': len(parsed.get('entries', [])), 'fallback': parsed.get('fallback'), 'error': parsed.get('error'),
               'linenumbers_stripped': parsed.get('linenumbers_stripped'), 'two_column': parsed.get('two_column'), 'parser_version': parsed.get('parser_version'),
               'reprocessed': True, 'entries': res}
        json.dump(out, open(os.path.join(ROOT, 'data', 'refs', stem + '.verified.json'), 'w'), indent=1); _save_cache()
        print(f"{stem}: entries={out['n_entries']} {dict(Counter(e['verdict'] for e in res))} two_column={out['two_column']} {time.time()-t:.0f}s", flush=True)
    except Exception as ex:
        print(f"{stem}: ERROR {ex}", flush=True)
