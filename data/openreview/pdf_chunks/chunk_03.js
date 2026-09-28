const t0 = Date.now(); const sleep = ms => new Promise(r => setTimeout(r, ms));
const items = [{"n": 50, "id": "isNfx9ujE9", "p": "/pdf/1fccfe74769eed97378332f4ee53d0df4bfd63ea.pdf"}, {"n": 51, "id": "m5WvKvws5G", "p": "/pdf/64fca2b74e831cfc6f26ee621ba408e590ddbc3a.pdf"}, {"n": 52, "id": "fblkYm5Xeq", "p": "/pdf/ca1c202905a5ff48a89688fa2561e3e6c664ef85.pdf"}, {"n": 53, "id": "SF7BjKnqdh", "p": "/pdf/01814f65acfc5871679a2b6094c73dd7a0ec3a37.pdf"}, {"n": 54, "id": "tOysXqyjnm", "p": "/pdf/38da754f9a08f28e43e003e7f0a8145f5fd16d6b.pdf"}, {"n": 55, "id": "cCq2FThv5r", "p": "/pdf/dd82e5fd9b26a80575dd879b39f2f342a33e7c71.pdf"}, {"n": 56, "id": "xB2bCxRacM", "p": "/pdf/09a629669c4757e792f3981cfb5b34993424d213.pdf"}, {"n": 57, "id": "7nTxMexDE3", "p": "/pdf/957560e163ee7144387b8f5002c5deb3f8982277.pdf"}, {"n": 58, "id": "im8tT8Hpfu", "p": "/pdf/bfce737089283fb122c8fa4dfff40f740a6f5175.pdf"}, {"n": 59, "id": "njhOgQGqgV", "p": "/pdf/b0254b1090b6c81e5699e71dd8e8de7d0623599e.pdf"}, {"n": 60, "id": "AgIg43zlmi", "p": "/pdf/958f359597e23591e49fa7005affce2f908a9673.pdf"}, {"n": 61, "id": "hcIWKyWq2h", "p": "/pdf/3a4e3116225e08a2574bbfccea1b0e5299c6339b.pdf"}];
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
'pdf chunk 3: ' + log.join(' | ') + ' :: ' + Math.round((Date.now()-t0)/1000) + 's'
