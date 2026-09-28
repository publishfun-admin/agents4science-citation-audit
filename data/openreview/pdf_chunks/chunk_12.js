const t0 = Date.now(); const sleep = ms => new Promise(r => setTimeout(r, ms));
const items = [{"n": 168, "id": "I7meDPJFy8", "p": "/pdf/14031abc4e516ad80dd1ea6da1f60d9006b7f1a1.pdf"}, {"n": 169, "id": "U9kGYbIito", "p": "/pdf/2f62d1d00fc78d37e2aed5bcc042fd81364122ea.pdf"}, {"n": 170, "id": "Q0oGPmOM8Q", "p": "/pdf/e618e029a1739703aeb266ae49bcc59fb2c408f0.pdf"}, {"n": 172, "id": "NDpRTCW3sM", "p": "/pdf/65f2dfe3cf3756abd8c34237c64e63920cd11c18.pdf"}, {"n": 173, "id": "gBmfD0QYPs", "p": "/pdf/4346edf329bce2876ddffb7767911b70011d6e3e.pdf"}, {"n": 174, "id": "aPsA4Qrwfj", "p": "/pdf/52caefa758bdfe600f3ee54faee34847308ae9a1.pdf"}, {"n": 175, "id": "oALqqvTcMt", "p": "/pdf/c995a19d6ba6ae94520d4a73cd754517bb7968cb.pdf"}, {"n": 176, "id": "EUSuMA1H98", "p": "/pdf/de8009b75957a7e8780d793e2bbe6b0456bd0e8e.pdf"}, {"n": 177, "id": "X0rpsv88au", "p": "/pdf/2feb0d385c49e32b414da5311b8b3efe8eebb9ce.pdf"}, {"n": 178, "id": "TaHeCGU69A", "p": "/pdf/514d1775ef1e1a281e3f1786fc9e2ec6e985453f.pdf"}, {"n": 179, "id": "xYUNkQ4vKK", "p": "/pdf/29da4f51d2f1be9559f41234da067a6e6c4d82b9.pdf"}, {"n": 180, "id": "TTPrLmI1xH", "p": "/pdf/cf3c565741d986e9aa7a7e2cb1c06cb76249f547.pdf"}];
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
'pdf chunk 12: ' + log.join(' | ') + ' :: ' + Math.round((Date.now()-t0)/1000) + 's'
