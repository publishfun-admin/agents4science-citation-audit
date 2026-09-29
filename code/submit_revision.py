"""Submit a revision to Publish.fun: POST /api/papers/<id>/revisions with the full revised body and a response letter.
Usage: python code/submit_revision.py <paper_id> paper/paper.md paper/response_letter_round1.md [--dry-run]
The title and abstract are split off exactly as in submit_paper.py; they are sent as extra fields in case the API accepts them."""
import os, re, sys, json, urllib.request, urllib.error
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from submit_paper import split_manuscript, API
pid, md_path, letter_path = sys.argv[1], sys.argv[2], sys.argv[3]
md = open(md_path, encoding='utf-8').read(); title, abstract, body_noabs = split_manuscript(md)
# the revision endpoint does not update the stored abstract: keep the Abstract section inside the body so reviewers see the current one
body = re.sub(r'^# .+\n', '', md, count=1).strip() + '\n'
letter = open(letter_path, encoding='utf-8').read()
payload = {'content': body, 'response_letter': letter, 'abstract': abstract, 'title': title}
print(json.dumps({k: (v if k in ('title',) else f'<{len(v)} chars>') for k, v in payload.items()}, indent=1))
if '--dry-run' in sys.argv: sys.exit(0)
def post(p):
    req = urllib.request.Request(API + f'/api/papers/{pid}/revisions', method='POST', data=json.dumps(p).encode(),
        headers={'Authorization': 'Bearer ' + os.environ['PUBLISHFUN_API_KEY'], 'Content-Type': 'application/json', 'Accept': 'application/json'})
    try:
        with urllib.request.urlopen(req, timeout=120) as r: return r.status, json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()[:2000]
st, res = post(payload)
if st >= 400:
    print('first attempt', st, res); st, res = post({'content': body, 'response_letter': letter})
print(st, json.dumps(res, indent=1)[:3000] if not isinstance(res, str) else res)
json.dump({'status': st, 'response': res}, open('paper/revision_receipt.json', 'w'), indent=1)
