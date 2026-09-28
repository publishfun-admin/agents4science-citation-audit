const t0 = Date.now(); const sleep = ms => new Promise(r => setTimeout(r, ms));
const items = [{"n": 317, "id": "wLhQMbyF3y", "p": "/pdf/0af21d6de218ea2d8b1ae624987f88e7c8e67ed9.pdf"}, {"n": 318, "id": "sXgKlXfaBK", "p": "/pdf/20bbd5fd258a8838046ca30451a5414eae33ce2c.pdf"}, {"n": 319, "id": "DGDSlqtReN", "p": "/pdf/00da72d00f2b3f6da3f9774ecb5435ba57484a86.pdf"}, {"n": 320, "id": "YysFSiPQf7", "p": "/pdf/c53251dc7c7c2493f10703b4921b1dcddbf07b4c.pdf"}, {"n": 321, "id": "zTiOPZnpWv", "p": "/pdf/9ef8ab0433b93b85c5bcb808c05f1774b8035360.pdf"}, {"n": 322, "id": "98iucZYjap", "p": "/pdf/2d9adb5367690608ab4c9b697216f454cbac7d33.pdf"}, {"n": 323, "id": "bNP4BRONCE", "p": "/pdf/64ff1d9850b2258fddeeae20894f1ded62790106.pdf"}, {"n": 324, "id": "hnVumOzSK7", "p": "/pdf/38762d6399b2c59ee5fd21cbc21636c311267c80.pdf"}, {"n": 325, "id": "l5Wrcgyobp", "p": "/pdf/c99092c1eac460ecf41f5cd5de876a62af2ba441.pdf"}, {"n": 326, "id": "7qIGNFpf1C", "p": "/pdf/3bf4b0ac394fcfd5a06c6d141a079bdcf5c66229.pdf"}, {"n": 327, "id": "waBE0e7gx9", "p": "/pdf/3b624b7d6a8a59a899fcb161222fff27c532b280.pdf"}, {"n": 328, "id": "q15GkFTXbM", "p": "/pdf/6bf8dffc85e1ca5fcf66751ad6dc485c28ccc2c6.pdf"}];
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
'pdf chunk 24: ' + log.join(' | ') + ' :: ' + Math.round((Date.now()-t0)/1000) + 's'
