"""Minimal Semantic Scholar Graph API client with polite retry/backoff (no API key)."""
import json, time, sys, urllib.parse, urllib.request, urllib.error

BASE = "https://api.semanticscholar.org/graph/v1"
UA = "publishfun-firstpaper-research/0.1 (mailto:admin@publish.fun)"
MIN_GAP = 3.5          # seconds between requests
_last = [0.0]

def get(path, params=None, max_tries=8):
    url = BASE + path + ("?" + urllib.parse.urlencode(params) if params else "")
    wait = 5
    for attempt in range(max_tries):
        gap = MIN_GAP - (time.time() - _last[0])
        if gap > 0: time.sleep(gap)
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                _last[0] = time.time()
                return json.loads(r.read().decode())
        except urllib.error.HTTPError as e:
            _last[0] = time.time()
            if e.code == 404: return None
            if e.code == 429 or e.code >= 500:
                time.sleep(wait); wait = min(wait * 2, 90); continue
            raise
        except Exception:
            _last[0] = time.time(); time.sleep(wait); wait = min(wait * 2, 90)
    return {"_error": "gave up", "url": url}
