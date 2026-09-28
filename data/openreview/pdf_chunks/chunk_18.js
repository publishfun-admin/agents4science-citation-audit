const t0 = Date.now(); const sleep = ms => new Promise(r => setTimeout(r, ms));
const items = [{"n": 243, "id": "vXVQbDoYbP", "p": "/pdf/5d79ad1d861f6dc29c3b065691cb2438e9b501a8.pdf"}, {"n": 244, "id": "TX4BUsNGsA", "p": "/pdf/a3d20066ca88fbf0b1663697434c2ac4099d53f1.pdf"}, {"n": 245, "id": "UlGjJrW88p", "p": "/pdf/9df1437c4a4d117429c20a037a64e71ed137a05b.pdf"}, {"n": 246, "id": "x8R9TaMNv3", "p": "/pdf/e7086553e9474ddfb38489a25d50172b335fd309.pdf"}, {"n": 247, "id": "pdszjkhuRv", "p": "/pdf/42f497acd2fdd1171eb11a7eb916df199056b38a.pdf"}, {"n": 248, "id": "7zAuPR82do", "p": "/pdf/d285532e1db6a040d17a5a4a4df27a9550d706d1.pdf"}, {"n": 249, "id": "ugUrc5yVxG", "p": "/pdf/0411eedc8cce2f8ed549dba3780eb7a261d1b941.pdf"}, {"n": 250, "id": "k0u2RT8JT7", "p": "/pdf/3be4831bfb10a2eaaf95730496f9c0d9241c5587.pdf"}, {"n": 251, "id": "I9plFigPxl", "p": "/pdf/aadf9e8414a5f9af6da5efccf62f61a11e3657b2.pdf"}, {"n": 252, "id": "8V0TGsJHg4", "p": "/pdf/e7882c70cb3a54d4901c0d196ea3d9afe5a196d6.pdf"}, {"n": 253, "id": "EgfDyJhr3P", "p": "/pdf/7107bf6400ddfc503633e9313c693cd66ff65d6b.pdf"}, {"n": 254, "id": "ZHFdsEbBVu", "p": "/pdf/8f3ab317e03050456e9cef3e766c24b8a690aaa2.pdf"}];
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
'pdf chunk 18: ' + log.join(' | ') + ' :: ' + Math.round((Date.now()-t0)/1000) + 's'
