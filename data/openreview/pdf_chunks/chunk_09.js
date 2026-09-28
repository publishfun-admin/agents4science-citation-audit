const t0 = Date.now(); const sleep = ms => new Promise(r => setTimeout(r, ms));
const items = [{"n": 129, "id": "8Oydp7dGon", "p": "/pdf/085be792972975fc3efc48d873ac79778ad75651.pdf"}, {"n": 130, "id": "emsnDnmtYP", "p": "/pdf/824cfd56a956d85277243f8d054756dc2a0363d9.pdf"}, {"n": 131, "id": "fACySEnG2z", "p": "/pdf/13b1272fa189ed77552b77a38d86be00576a0d67.pdf"}, {"n": 132, "id": "BVisnzd9q9", "p": "/pdf/2684dbf1511575264a667101f72cd772a1106ebe.pdf"}, {"n": 133, "id": "7bPKcF3dTG", "p": "/pdf/97256d71a650bd060890e558f9c9fe7137a0090b.pdf"}, {"n": 134, "id": "O5EPivCxd2", "p": "/pdf/c59f6c726b785551663d8d74c00d0c9c83526f2b.pdf"}, {"n": 135, "id": "7TzkOum3Nu", "p": "/pdf/b15df3ac712181c5c8fc57203262a1e8f4c2aaaa.pdf"}, {"n": 136, "id": "W6LcN2cF9k", "p": "/pdf/0a131ca14c60564f44bebbffc5a218bbb5cdc4fb.pdf"}, {"n": 137, "id": "M3EvRA0gU4", "p": "/pdf/53838594cb6e8b5201d33f9e1ff8903602ddc27c.pdf"}, {"n": 139, "id": "88zyE3fJzQ", "p": "/pdf/fe8dd7ee07d87ac9cf7e7d3063143075b6fcfc9a.pdf"}, {"n": 140, "id": "Mf9vz9TjOr", "p": "/pdf/0ab6d959c9cc5c62c984397792f009673964f08d.pdf"}, {"n": 141, "id": "Yja2KMahOL", "p": "/pdf/a1dd5d756359b6d9ef35b2b9d805707a991e3db9.pdf"}];
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
'pdf chunk 9: ' + log.join(' | ') + ' :: ' + Math.round((Date.now()-t0)/1000) + 's'
