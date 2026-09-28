const t0 = Date.now(); const sleep = ms => new Promise(r => setTimeout(r, ms));
const items = [{"n": 267, "id": "FOEalkTyTi", "p": "/pdf/404051cb3dc944bbcb21fbd545ecb173c797c09e.pdf"}, {"n": 268, "id": "W9TBkcaRLJ", "p": "/pdf/8d8747670eac69c7822752275beb681d83def782.pdf"}, {"n": 269, "id": "MIjY6VNtY0", "p": "/pdf/cab9a610e9c6be20a11f9a4f8dde872ff2f8e5d4.pdf"}, {"n": 270, "id": "g01exn7g5d", "p": "/pdf/2be4704b1a0e0cd16909d60123a749d10a155dd7.pdf"}, {"n": 271, "id": "i0LXSoRHOf", "p": "/pdf/565870e63a39cbfea4b2f6e96e3a8dba65a7bebb.pdf"}, {"n": 272, "id": "2qm4sB6BbS", "p": "/pdf/64c9aeb6f79075854b8bd89c4c3df9ad6e4c6397.pdf"}, {"n": 273, "id": "ChY7h0UvEL", "p": "/pdf/bf61c1e938ce3babafec3aaa9e557eae4c4af410.pdf"}, {"n": 274, "id": "c0CGbHsC45", "p": "/pdf/1233579c7af40e8532de8230e7d04e2f39b46569.pdf"}, {"n": 275, "id": "5qYADa1lbX", "p": "/pdf/14ca2368ecfcb4d2e7f791d187667171aa926fde.pdf"}, {"n": 276, "id": "aMep22Wzw7", "p": "/pdf/dedb1f504d03e485741bb5dca0606fa76b75eb79.pdf"}, {"n": 277, "id": "U4q6HXFvKn", "p": "/pdf/46a0e75e03898c3f6d41bfce2c85a999f8a301b5.pdf"}, {"n": 278, "id": "rgpgukbeVf", "p": "/pdf/ff056083f9748a1858ee5e2ad91be0f7f63bfefa.pdf"}];
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
'pdf chunk 20: ' + log.join(' | ') + ' :: ' + Math.round((Date.now()-t0)/1000) + 's'
