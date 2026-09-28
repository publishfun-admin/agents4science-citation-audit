const t0 = Date.now(); const sleep = ms => new Promise(r => setTimeout(r, ms));
const items = [{"n": 292, "id": "EwXxI9mF4d", "p": "/pdf/ffb9bccaf19c462995137f5399fc131f9f2e6771.pdf"}, {"n": 293, "id": "WAbHXkmBIn", "p": "/pdf/b625b1543f34a774c89cb7a6085287b5582e9e68.pdf"}, {"n": 295, "id": "Ka1WYEwLdC", "p": "/pdf/fb79a623b2e6799781436c15fdb70b423960bffc.pdf"}, {"n": 296, "id": "w7c1rotw9I", "p": "/pdf/2aeb4ad12d4a550a8a58de12655146160cbcc292.pdf"}, {"n": 297, "id": "51ri0E84gG", "p": "/pdf/0b0709b64a82578d5b430d507942d204fa4c6e26.pdf"}, {"n": 298, "id": "KjkhwoXbYK", "p": "/pdf/063f85f363754d738a2c7dfa2898d289df061d68.pdf"}, {"n": 299, "id": "si22iakiB5", "p": "/pdf/a7416dc29f874f8510f48cc3b945e8ef3e1df18f.pdf"}, {"n": 300, "id": "cK8YYMc65B", "p": "/pdf/7129828329e62f517291940c806f4789dbd39e40.pdf"}, {"n": 301, "id": "KnkFyU8BmD", "p": "/pdf/0ece9fe08057b5a2aa75af5db5513ddc2cdf0caf.pdf"}, {"n": 302, "id": "diwnmHfFNE", "p": "/pdf/938441db4d7bcad3d971ca27f00c690500c55b46.pdf"}, {"n": 303, "id": "maMnVCHl8J", "p": "/pdf/c8e397648b145d63e907f81ba657b3529c68c6cd.pdf"}, {"n": 304, "id": "aK9JwuE29c", "p": "/pdf/d99161acf15c21261a069dc61dc2a112f9f3237a.pdf"}];
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
'pdf chunk 22: ' + log.join(' | ') + ' :: ' + Math.round((Date.now()-t0)/1000) + 's'
