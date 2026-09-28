const t0 = Date.now(); const sleep = ms => new Promise(r => setTimeout(r, ms));
const items = [{"n": 181, "id": "yvk5HRVGQr", "p": "/pdf/f6a1b2e9ddf62cfd4262e0926c4fdb4b788f8ede.pdf"}, {"n": 182, "id": "aOLM3NmX5V", "p": "/pdf/4e90cc6aa94679a41c3976bc3152bf1496f9e105.pdf"}, {"n": 183, "id": "NiUl3EkvIW", "p": "/pdf/935a0387830e114babdb1736689582bb87d15ae3.pdf"}, {"n": 184, "id": "VYz9u0R5CD", "p": "/pdf/a48774f6c65ca3e01da54be9c1fe198e46cf5d99.pdf"}, {"n": 185, "id": "NJnEz4xw6u", "p": "/pdf/58ad147bcce33de2d4cbc32c056650547d86c077.pdf"}, {"n": 186, "id": "KUp89TfOZE", "p": "/pdf/21d7335679e4575f1a948d66b40a893fb4081afb.pdf"}, {"n": 187, "id": "z6HofiQC33", "p": "/pdf/2a67152840137af871c1e95f97416645a36b9623.pdf"}, {"n": 188, "id": "cNGI9La4Ks", "p": "/pdf/102b2bf7b92668592fb7dbd9186e048aaad78557.pdf"}, {"n": 189, "id": "mkV1Y15uP8", "p": "/pdf/ba2658d38057c089453c0c36bcdba12ac97bfd55.pdf"}, {"n": 191, "id": "FAz5XxIfP3", "p": "/pdf/6fee6c1d18df31e5d54ad44ac0d51225479ce2d0.pdf"}, {"n": 192, "id": "1lP8cufEsT", "p": "/pdf/12c5369e871ed6123e12094592a9edf18f73c14c.pdf"}, {"n": 193, "id": "xEjie6Puap", "p": "/pdf/1a57d56b33ce7e91164479f220e46202ee27173d.pdf"}];
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
'pdf chunk 13: ' + log.join(' | ') + ' :: ' + Math.round((Date.now()-t0)/1000) + 's'
