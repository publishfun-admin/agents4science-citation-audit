const t0 = Date.now(); const sleep = ms => new Promise(r => setTimeout(r, ms));
const items = [{"n": 142, "id": "CT9ffLinm8", "p": "/pdf/aa8f28edfa9cdba66307c3775c1eaad68a0df56f.pdf"}, {"n": 143, "id": "WGm2RSJSRI", "p": "/pdf/6f774dba8020e0a054c1688b1d7fa6c96604f7f8.pdf"}, {"n": 144, "id": "DiditQVw1f", "p": "/pdf/a974d789860ca99f67771f37a14c74edce97d75d.pdf"}, {"n": 145, "id": "vUJOhgV3zh", "p": "/pdf/6fcf0407f96090e7f9abf3dff731d27758a6e62d.pdf"}, {"n": 146, "id": "EWYarfMZU2", "p": "/pdf/36dd00f16cc35422c22ebcc50ccc962befadeb78.pdf"}, {"n": 147, "id": "N6zS6EgzTw", "p": "/pdf/5aff1a83050cc6cd460520af6d652872788479be.pdf"}, {"n": 148, "id": "4GS2ThfKZl", "p": "/pdf/e2a930679d50c175d79c3854569cc63ea4bd67c8.pdf"}, {"n": 149, "id": "5Hit4lIpkl", "p": "/pdf/d85cd1e4fc87dfdefe807536539177a389a3e478.pdf"}, {"n": 150, "id": "VuEXcpLp29", "p": "/pdf/757d024a02d2d1e7a820192a0f5bc9d78233dccf.pdf"}, {"n": 151, "id": "B6ZrLXou3u", "p": "/pdf/e69f4511cc2047931ea5590cb850677d6b0d606a.pdf"}, {"n": 152, "id": "neQWbqbgSs", "p": "/pdf/e1f1323807697b2892b5b29c5e7e73510ad2a1ab.pdf"}, {"n": 155, "id": "3agwfP3euK", "p": "/pdf/c19ff5fd4aa8bcf1d4a3b16a02ac9567ff875df0.pdf"}];
const dt = new DataTransfer(); const log = [];
for (const it of items) {
  try {
    let r = await fetch('https://openreview.net' + it.p, {credentials:'include'});
    if (r.status !== 200 || !(r.headers.get('content-type')||'').includes('pdf')) { r = await fetch('https://openreview.net/pdf?id=' + it.id, {credentials:'include'}); }
    const b = await r.blob();
    dt.items.add(new File([b], it.n + '_' + it.id + '.pdf', {type:'application/pdf'}));
    log.push(it.n + ':' + b.size);
  } catch(e) { log.push(it.n + ':ERR'); }
  await sleep(120);
}
const f = document.createElement('form'); f.method='POST'; f.enctype='multipart/form-data'; f.action='http://127.0.0.1:8765/upload'; f.target='_self';
const inp = document.createElement('input'); inp.type = 'file'; inp.name = 'pdfs'; inp.multiple = true; inp.files = dt.files; f.appendChild(inp);
document.body.appendChild(f); f.submit();
'pdf chunk 10: ' + log.join(' | ') + ' :: ' + Math.round((Date.now()-t0)/1000) + 's'
