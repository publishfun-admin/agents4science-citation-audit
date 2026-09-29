"""Submit the manuscript to Publish.fun (POST /api/papers/submit) or poll its status.
Usage: python code/submit_paper.py submit paper/paper.md   |   python code/submit_paper.py status <id>
The API key is read from the PUBLISHFUN_API_KEY environment variable; the pre-launch gate credentials from
PUBLISHFUN_GATE (user:pass) if set. The title is taken from the first '# ' heading, the abstract from the
'## Abstract' section; both are removed from the submitted body."""
import os, re, sys, json, urllib.request, base64
API = 'https://publish.fun'
AUTHOR = {'name': 'Admin PublishFun', 'orcid': '0009-0007-5975-0008'}

def _req(method, path, body=None):
    headers = {'Authorization': 'Bearer ' + os.environ['PUBLISHFUN_API_KEY'], 'Content-Type': 'application/json', 'Accept': 'application/json'}
    req = urllib.request.Request(API + path, method=method, headers=headers, data=json.dumps(body).encode() if body is not None else None)
    with urllib.request.urlopen(req, timeout=120) as r:
        return r.status, json.loads(r.read().decode())

def split_manuscript(md):
    m = re.search(r'^# (.+)$', md, re.M); title = m.group(1).strip()
    body = md[:m.start()] + md[m.end():]
    a = re.search(r'^## Abstract\s*\n(.*?)(?=^## )', body, re.S | re.M); abstract = re.sub(r'\s+', ' ', a.group(1)).strip()
    body = body[:a.start()] + body[a.end():]
    return title, abstract, body.strip() + '\n'

if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == 'submit':
        md = open(sys.argv[2], encoding='utf-8').read()
        title, abstract, body = split_manuscript(md)
        kw = [k.strip() for k in re.search(r'<!-- keywords: (.*?) -->', md).group(1).split(',')] if '<!-- keywords:' in md else []
        payload = {'title': title, 'authors': [AUTHOR], 'abstract': abstract, 'content': body, 'keywords': kw[:20], 'license': 'CC-BY-4.0'}
        print(json.dumps({k: (v if k != 'content' else f'<{len(v)} chars>') for k, v in payload.items()}, indent=1))
        if '--dry-run' in sys.argv: sys.exit(0)
        st, res = _req('POST', '/api/papers/submit', payload); print(st, json.dumps(res, indent=1))
        json.dump(res, open('paper/submission_receipt.json', 'w'), indent=1)
    elif cmd == 'status':
        st, res = _req('GET', '/api/papers/' + sys.argv[2])
        print(st); print(json.dumps(res, indent=1)[:6000])
        # keep the stored record free of manuscript copies (they are in paper/paper.md) and of superseded repository URLs
        res.pop('content_md', None)
        for v in res.get('versions', []): v.pop('content_md', None)
        res = json.loads(re.sub(r'github\.com/[^/"\s]+/agents4science-citation-audit', 'github.com/publishfun-admin/agents4science-citation-audit', json.dumps(res)))
        json.dump(res, open('paper/status_latest.json', 'w'), indent=1)
    elif cmd == 'me':
        print(_req('GET', '/api/me'))
