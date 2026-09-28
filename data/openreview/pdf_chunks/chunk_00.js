const t0 = Date.now(); const sleep = ms => new Promise(r => setTimeout(r, ms));
const items = [{"n": 2, "id": "2p1CCmRoyr", "p": "/pdf/ab137484d6c58664934c07985619a0c2356128a1.pdf"}, {"n": 4, "id": "4lScdZY10w", "p": "/pdf/133b4df1181dee16728c6739a772d5cf1c10db4c.pdf"}, {"n": 5, "id": "IfxYFkJEHx", "p": "/pdf/e5bd5b5936ba0d368f63a34c4f6dd7a4a5055d99.pdf"}, {"n": 8, "id": "VadGlawKiC", "p": "/pdf/3aeb273d9410060a655ef8a9aebceac4084ec766.pdf"}, {"n": 11, "id": "yh6WeaOCoq", "p": "/pdf/81ab586e492a877def93b5ad19c82487485ac750.pdf"}, {"n": 12, "id": "QSIkBpEbPt", "p": "/pdf/2089a17a90fceb0743c99779838ba873e388a2e2.pdf"}, {"n": 13, "id": "q0qXOaBOIC", "p": "/pdf/eb222105cc8a1de6d4b9d1a0add2594ebeb88f3c.pdf"}, {"n": 15, "id": "84N1sbuEMC", "p": "/pdf/9cb0f1f7a11d390696bd472d60893f22f6943763.pdf"}, {"n": 16, "id": "Iu35dffCJZ", "p": "/pdf/dc830dde76a43cf5871dc7e7cc36e4affd53de58.pdf"}, {"n": 18, "id": "VP1OqJeeTA", "p": "/pdf/327386f550648d84d0d6c6e706976062bb3d684f.pdf"}, {"n": 19, "id": "e80OpBGaal", "p": "/pdf/31acc1fa692b163fd8e0aca5520c47ecc4c32a57.pdf"}, {"n": 20, "id": "sEnMMnlztf", "p": "/pdf/e080eba25fbb1026b2ecc9ddf885f2b0bf905335.pdf"}];
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
'pdf chunk 0: ' + log.join(' | ') + ' :: ' + Math.round((Date.now()-t0)/1000) + 's'
