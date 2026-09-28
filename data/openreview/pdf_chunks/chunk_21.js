const t0 = Date.now(); const sleep = ms => new Promise(r => setTimeout(r, ms));
const items = [{"n": 279, "id": "aSlhaqLbL1", "p": "/pdf/fc830a315075feeffb2bfa3458bb222ded344acc.pdf"}, {"n": 280, "id": "gC3D2ESSyK", "p": "/pdf/521037328af4df7687b86343bc0ed0bddcc441fb.pdf"}, {"n": 281, "id": "qSmh66KJR4", "p": "/pdf/f9a01858ecd0bb8d191bbed59bd0b30f748b1677.pdf"}, {"n": 282, "id": "ioHldPPWKK", "p": "/pdf/5708df3fba3e07924b28fb91918149d348a30403.pdf"}, {"n": 283, "id": "nRK2lFl77R", "p": "/pdf/86fc1b1353b073c1dc4cadec3295842d7b196511.pdf"}, {"n": 284, "id": "7MPstNz66e", "p": "/pdf/f9bdf4bce606f7b089bb459cad91f2d7d867749c.pdf"}, {"n": 286, "id": "udPANfLJBW", "p": "/pdf/8058cb5090b234df221d0e438c8ae6cd588198f0.pdf"}, {"n": 287, "id": "4nrWtE6oZ9", "p": "/pdf/78192599c59a0385e26e62292703f918f1d8e20c.pdf"}, {"n": 288, "id": "3Y2ZEQiZFx", "p": "/pdf/f3a0e7a1a535d8c0f2df31395fe9959423f9c918.pdf"}, {"n": 289, "id": "ExGHHgTM2p", "p": "/pdf/f471ba88f36480827538236f2ca6b79358a9d5da.pdf"}, {"n": 290, "id": "ud9cRk9yBM", "p": "/pdf/bb2044c17a131b75f41304412975c044d694dc42.pdf"}, {"n": 291, "id": "LqukdleDgU", "p": "/pdf/423f7ce78bc9c7b8d42a435e0a883df48a55d68b.pdf"}];
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
'pdf chunk 21: ' + log.join(' | ') + ' :: ' + Math.round((Date.now()-t0)/1000) + 's'
