const t0 = Date.now(); const sleep = ms => new Promise(r => setTimeout(r, ms));
const items = [{"n": 194, "id": "wU35L1GZud", "p": "/pdf/05f546a560906d34ef6fd1e94a55e00ac86e3d1e.pdf"}, {"n": 195, "id": "MYEr4iPFMn", "p": "/pdf/8893a420d299fc5eb414c4c2582cd63d9d84f42f.pdf"}, {"n": 196, "id": "lWHSiQpRIr", "p": "/pdf/4dd9cda916872fab4d99a0953e53f3e578d1ec55.pdf"}, {"n": 197, "id": "N7Kh0K33Dk", "p": "/pdf/602bcf6779498a573a60da5425f18ff66d150ad6.pdf"}, {"n": 198, "id": "ge6aUTPvYE", "p": "/pdf/2a5a63835e24b98d254e683f12752f98b5c71912.pdf"}, {"n": 199, "id": "zYDXTzql3n", "p": "/pdf/6363a04b09327046415ae6dbebf5fd2d8de4ddb2.pdf"}, {"n": 200, "id": "L4arZChBJD", "p": "/pdf/a6170a548d5207a0c63746136a3aeeff1d878cc2.pdf"}, {"n": 201, "id": "ZpW3U6NkS7", "p": "/pdf/93f476a1fe4be4541d64cc694672e61f40e87775.pdf"}, {"n": 202, "id": "aubtELkhDi", "p": "/pdf/8ab04619438c2eedde4d822bcdf0d4bd6e797e73.pdf"}, {"n": 203, "id": "4UmxrtV7eY", "p": "/pdf/ce47edad5178eeca9b7723dfcb2a3688e328f624.pdf"}, {"n": 205, "id": "XjJeBSf7NB", "p": "/pdf/7594ba588d6dbb477da4830912a16deb3e7fd973.pdf"}, {"n": 206, "id": "6pr7BUGkLp", "p": "/pdf/a16111541a1eef1ac87cb603b29c867b932e4b93.pdf"}];
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
'pdf chunk 14: ' + log.join(' | ') + ' :: ' + Math.round((Date.now()-t0)/1000) + 's'
