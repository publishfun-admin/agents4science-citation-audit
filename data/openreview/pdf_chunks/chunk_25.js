const t0 = Date.now(); const sleep = ms => new Promise(r => setTimeout(r, ms));
const items = [{"n": 329, "id": "VUTIDJhvD3", "p": "/pdf/76593efb6b99acd4f12fb4c12f2fab4c461b8f16.pdf"}, {"n": 331, "id": "7k3i6JYvFo", "p": "/pdf/4606e901967288df39b2c25015cbbafa97a488ca.pdf"}, {"n": 332, "id": "eSlhdv8zUL", "p": "/pdf/1fcde57119a552d3cf2210eb406288032b59233b.pdf"}, {"n": 333, "id": "AhFsKmuaCb", "p": "/pdf/d8d063e05fb61bf113a7ef1f9b12e37fd7c5bc88.pdf"}, {"n": 334, "id": "2w5HypzUpN", "p": "/pdf/e22837b2e4fb54544c6710d3806abc1c2fd682e6.pdf"}, {"n": 337, "id": "NRaWmVVltg", "p": "/pdf/5182e032e20e053fce9eaf25a705aa36c135d879.pdf"}, {"n": 338, "id": "Wu0W5BJ7UR", "p": "/pdf/b86be9a3e25e69b067eabfb78abd1bece9b423c1.pdf"}, {"n": 339, "id": "cPgX9C2BHB", "p": "/pdf/0b68c3b60d4312783ddc4f2b8acef6677d8918c4.pdf"}, {"n": 340, "id": "ShWjvhAZGs", "p": "/pdf/a87959c923172f051180b0a77c91e66edac4eb60.pdf"}, {"n": 341, "id": "MH6zuzCAiH", "p": "/pdf/b7b18ca881af6f547a6eec9f46226354acfdd6a8.pdf"}, {"n": 342, "id": "Pqjg14gnAV", "p": "/pdf/35195e5da803c7edc8fb7769484b4bbe4cb99c3f.pdf"}, {"n": 343, "id": "mEbFdPy2oy", "p": "/pdf/1bdf757f5d20ec093cd0e86f8b5f06d074a833aa.pdf"}];
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
'pdf chunk 25: ' + log.join(' | ') + ' :: ' + Math.round((Date.now()-t0)/1000) + 's'
