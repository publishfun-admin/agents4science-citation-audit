"""Tiny local HTTP receiver: the browser (on openreview.net) POSTs fetched JSON/PDF bytes here so they land on disk.
Binds to 127.0.0.1 only. CORS restricted to https://openreview.net. Paths are sanitised to data/openreview/."""
import http.server, json, os, re, sys, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'openreview')
ALLOWED_ORIGINS = {'https://openreview.net', 'https://api2.openreview.net'}

class H(http.server.BaseHTTPRequestHandler):
    def _cors(self):
        o = self.headers.get('Origin', '')
        if o in ALLOWED_ORIGINS:
            self.send_header('Access-Control-Allow-Origin', o)
            self.send_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type, X-Name')
    def do_OPTIONS(self):
        self.send_response(204); self._cors(); self.end_headers()
    def do_GET(self):
        u = urllib.parse.urlparse(self.path)
        if u.path == '/progress':
            n = {d: len(os.listdir(os.path.join(ROOT, d))) for d in os.listdir(ROOT) if os.path.isdir(os.path.join(ROOT, d))}
            body = json.dumps(n).encode()
        else:
            body = b'{"ok":true}'
        self.send_response(200); self._cors(); self.send_header('Content-Type', 'application/json'); self.send_header('Content-Length', str(len(body))); self.end_headers(); self.wfile.write(body)
    def do_POST(self):
        u = urllib.parse.urlparse(self.path)
        q = urllib.parse.parse_qs(u.query)
        name = (q.get('name') or [''])[0]
        name = re.sub(r'[^A-Za-z0-9_./-]', '_', name).lstrip('/').replace('..', '_')
        n = int(self.headers.get('Content-Length', 0))
        data = self.rfile.read(n)
        if not name or n == 0:
            self.send_response(400); self._cors(); self.end_headers(); return
        path = os.path.join(ROOT, name); os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'wb') as f: f.write(data)
        body = json.dumps({'ok': True, 'name': name, 'size': n}).encode()
        self.send_response(200); self._cors(); self.send_header('Content-Type', 'application/json'); self.send_header('Content-Length', str(len(body))); self.end_headers(); self.wfile.write(body)
    def log_message(self, fmt, *args):
        sys.stderr.write('%s %s\n' % (self.address_string(), fmt % args))

if __name__ == '__main__':
    os.makedirs(ROOT, exist_ok=True)
    http.server.ThreadingHTTPServer(('127.0.0.1', 8765), H).serve_forever()
