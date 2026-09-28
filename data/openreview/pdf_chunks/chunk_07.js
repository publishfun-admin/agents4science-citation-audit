const t0 = Date.now(); const sleep = ms => new Promise(r => setTimeout(r, ms));
const items = [{"n": 103, "id": "ZdUb8xFQD5", "p": "/pdf/ad4375798fac9386ae889437ccf17157a359f98b.pdf"}, {"n": 104, "id": "NYJJoGFtr2", "p": "/pdf/c97761c6503882ec2f3bcf85dc9761f931a11c4b.pdf"}, {"n": 105, "id": "bQV35LlBuP", "p": "/pdf/cbf4004c8016c830c3883f84591b7415d75d33be.pdf"}, {"n": 106, "id": "fHUl3imA7t", "p": "/pdf/7918a8d62b23470c65b2c2da3608242191f4b3f4.pdf"}, {"n": 107, "id": "UBPZSdsztb", "p": "/pdf/93d6621b834320a295222f3d84a36925899292a3.pdf"}, {"n": 108, "id": "pv8Y7F2FjR", "p": "/pdf/c78122066448a5c18f91057ed44ec9defbe7c822.pdf"}, {"n": 109, "id": "KQX70xNaL6", "p": "/pdf/fdb3b500841d3961a9ee6825c7e64ede2e3de367.pdf"}, {"n": 110, "id": "VONPKc9hae", "p": "/pdf/74bf54dab9752df3e41425f176fce5ac446e2ea9.pdf"}, {"n": 111, "id": "ary6ztIHwA", "p": "/pdf/664cf07c6f51e80f741184ffe2ed5654df33c6a7.pdf"}, {"n": 112, "id": "q9pyhsYHBk", "p": "/pdf/98c14ed6ebf4890684d4c3873cec6538fcfc591f.pdf"}, {"n": 113, "id": "Er3RbV9XZt", "p": "/pdf/87ff39ee3b68518528234de58150aee666530561.pdf"}, {"n": 114, "id": "mFTp8xzMRE", "p": "/pdf/1e5b6242473d675835bcdbdc20fa4dacc7be8ca5.pdf"}];
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
'pdf chunk 7: ' + log.join(' | ') + ' :: ' + Math.round((Date.now()-t0)/1000) + 's'
