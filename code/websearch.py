"""Minimal Bing web search via HTML scraping (fallback when the session's WebSearch budget is exhausted).
Usage: python3 code/websearch.py "query" ["query" ...]  -> prints title | url / snippet for the top results.
Cached in data/cache/websearch_cache.json; 1.5 s gap between requests."""
import sys, re, html, json, os, time, urllib.parse, urllib.request
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36"
CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'cache', 'websearch_cache.json')
try: _cache = json.load(open(CACHE))
except Exception: _cache = {}
_last = [0.0]
def strip(s): return html.unescape(re.sub(r'<[^>]+>', '', s)).strip()
def search(q, n=8):
    if q in _cache: return _cache[q]
    gap = 1.5 - (time.time() - _last[0])
    if gap > 0: time.sleep(gap)
    url = 'https://www.bing.com/search?setlang=en&q=' + urllib.parse.quote(q)
    req = urllib.request.Request(url, headers={'User-Agent': UA, 'Accept-Language': 'en-US,en;q=0.9'})
    try:
        with urllib.request.urlopen(req, timeout=30) as r: s = r.read().decode('utf-8', 'replace')
    except Exception as ex:
        return [{'error': str(ex)}]
    _last[0] = time.time()
    out = []
    for it in re.findall(r'<li class="b_algo".*?</li>', s, flags=re.S)[:n]:
        m = re.search(r'<h2[^>]*>\s*<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', it, flags=re.S)
        sn = re.search(r'<p class="b_lineclamp[^"]*"[^>]*>(.*?)</p>|<div class="b_caption"[^>]*>.*?<p[^>]*>(.*?)</p>', it, flags=re.S)
        if not m: continue
        out.append({'title': strip(m.group(2)), 'url': m.group(1), 'snippet': strip((sn.group(1) or sn.group(2)) if sn else '')})
    _cache[q] = out
    json.dump(_cache, open(CACHE, 'w'))
    return out
if __name__ == '__main__':
    for q in sys.argv[1:]:
        print(f'\n### {q}')
        res = search(q)
        if not res: print('  (no results)')
        for r in res:
            if 'error' in r: print('  ERROR', r['error']); continue
            print(f"  - {r['title'][:110]} | {r['url'][:110]}\n      {r['snippet'][:220]}")
