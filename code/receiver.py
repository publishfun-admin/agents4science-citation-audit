"""Local receiver for browser-fetched OpenReview data.

OpenReview's CSP forbids fetch()/XHR to localhost but allows <form action="http://127.0.0.1:*">, so the page submits a
multipart form: text fields named  json:<relative/path>  are written verbatim; file parts are written under their
field name's directory. Binds to 127.0.0.1:8765 only; every path is sanitised into data/openreview/.
"""
import http.server, json, os, re, sys, urllib.parse
from email.parser import BytesParser
from email.policy import default as email_default
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'openreview'))

def safe(name):
    name = re.sub(r'[^A-Za-z0-9_./-]', '_', name or '').replace('..', '_').lstrip('/')
    return name

class H(http.server.BaseHTTPRequestHandler):
    def _reply(self, code, body, ctype='text/html'):
        b = body.encode() if isinstance(body, str) else body
        self.send_response(code); self.send_header('Content-Type', ctype); self.send_header('Content-Length', str(len(b))); self.end_headers(); self.wfile.write(b)
    def do_GET(self):
        u = urllib.parse.urlparse(self.path)
        if u.path == '/progress':
            n = {}
            for d, _, files in os.walk(ROOT):
                rel = os.path.relpath(d, ROOT)
                if files: n[rel] = len(files)
            return self._reply(200, json.dumps(n), 'application/json')
        return self._reply(200, '<html><body>receiver ok</body></html>')
    def do_POST(self):
        n = int(self.headers.get('Content-Length', 0))
        raw = self.rfile.read(n)
        ctype = self.headers.get('Content-Type', '')
        saved = []
        if ctype.startswith('multipart/form-data'):
            msg = BytesParser(policy=email_default).parsebytes(b'Content-Type: ' + ctype.encode() + b'\r\nMIME-Version: 1.0\r\n\r\n' + raw)
            for part in msg.iter_parts():
                fname = part.get_filename()
                field = part.get_param('name', header='content-disposition') or ''
                payload = part.get_payload(decode=True)
                if fname:
                    rel = safe(os.path.join(field or 'files', fname))
                elif field.startswith('json:'):
                    rel = safe(field[5:])
                else:
                    continue
                path = os.path.join(ROOT, rel); os.makedirs(os.path.dirname(path), exist_ok=True)
                with open(path, 'wb') as f: f.write(payload or b'')
                saved.append({'path': rel, 'size': len(payload or b'')})
        else:
            u = urllib.parse.urlparse(self.path); q = urllib.parse.parse_qs(u.query)
            rel = safe((q.get('name') or ['blob.bin'])[0]); path = os.path.join(ROOT, rel)
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, 'wb') as f: f.write(raw)
            saved.append({'path': rel, 'size': n})
        sys.stderr.write('saved %s\n' % json.dumps(saved)); sys.stderr.flush()
        return self._reply(200, '<html><body><pre id="saved">' + json.dumps(saved) + '</pre></body></html>')
    def log_message(self, fmt, *args): pass

if __name__ == '__main__':
    os.makedirs(ROOT, exist_ok=True)
    http.server.ThreadingHTTPServer(('127.0.0.1', 8765), H).serve_forever()
