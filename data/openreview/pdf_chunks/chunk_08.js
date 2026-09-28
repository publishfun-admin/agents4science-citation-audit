const t0 = Date.now(); const sleep = ms => new Promise(r => setTimeout(r, ms));
const items = [{"n": 115, "id": "CpiOENQuoE", "p": "/pdf/6ebff2213e0f0efc1f45bf3d4d33acce6d682705.pdf"}, {"n": 116, "id": "nuMdhnLDxv", "p": "/pdf/43a64eec26de5277d6266fce965ee8d3a0b58b2b.pdf"}, {"n": 117, "id": "6QXrawkcrX", "p": "/pdf/094546c24994a40da106ab3dff36898610b72813.pdf"}, {"n": 118, "id": "AjTMGsbx9Q", "p": "/pdf/fd7aa7601fff3c927046e928e7c0ebd6f1e02bf5.pdf"}, {"n": 119, "id": "Fbc7TctYBi", "p": "/pdf/90115aa8ea7b84ea3af5878cb7b3be72fa6fd398.pdf"}, {"n": 120, "id": "80ABX86CsX", "p": "/pdf/7ee0db18000333ed21b820aad16d19957991d19e.pdf"}, {"n": 122, "id": "OG8sFxeNHv", "p": "/pdf/bc69b91c7a10c9a3c664065fe3bb7c11d3114882.pdf"}, {"n": 123, "id": "d2zQW3AMuH", "p": "/pdf/f3c7c93df39dc813f424cfddc16c2ff7788aef4b.pdf"}, {"n": 124, "id": "qWIhFYUDC4", "p": "/pdf/4cb5530d4b85cb97f9d218bd01e6edcb0fcc48e9.pdf"}, {"n": 126, "id": "gsoMCQeGeH", "p": "/pdf/93aa5c5115c8ca42591b4f2de8bf16a152b5778a.pdf"}, {"n": 127, "id": "n4MKPVeDXZ", "p": "/pdf/93bd2b83e7bbd55252bc25fcf571fffc13a8df86.pdf"}, {"n": 128, "id": "h3Cc1Dzrh6", "p": "/pdf/759a76d667e413a02582e51747c4d57c802250b1.pdf"}];
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
'pdf chunk 8: ' + log.join(' | ') + ' :: ' + Math.round((Date.now()-t0)/1000) + 's'
