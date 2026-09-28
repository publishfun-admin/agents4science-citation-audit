const t0 = Date.now(); const sleep = ms => new Promise(r => setTimeout(r, ms));
const items = [{"n": 219, "id": "W967XG1NBG", "p": "/pdf/25dbdf94d8898b3e9ab9ab62a3a49c32a60b1b11.pdf"}, {"n": 220, "id": "G5jK2OMT2q", "p": "/pdf/9db0c04b7157a50bfb47a87f4852117fae342c08.pdf"}, {"n": 221, "id": "xE6L2AQLex", "p": "/pdf/cc5bc69458b71df4c58456a72b8e3a6011965057.pdf"}, {"n": 222, "id": "b7exZpS4vy", "p": "/pdf/33ea58e5c235f8853eaa99931f4746ec03c5d97d.pdf"}, {"n": 223, "id": "NULs9ucJpz", "p": "/pdf/ebdc7493eda7a1df71928ac061dd8efac9bfe75c.pdf"}, {"n": 224, "id": "88lrbJ8PTe", "p": "/pdf/b1628d6feef4c0fc410c43e0a0035718810829f5.pdf"}, {"n": 225, "id": "1g8lpVSLZ1", "p": "/pdf/5fd6ff9e978896994022779b05410b88036f6846.pdf"}, {"n": 226, "id": "Jfx32wFUXq", "p": "/pdf/5d4fbcf007ed7a2113bee097d8329156b5109764.pdf"}, {"n": 227, "id": "pmfF7wwX6W", "p": "/pdf/85b01ac303ed8ed7c9e6ac275435d78ed4f1dc90.pdf"}, {"n": 228, "id": "GitkwMobgt", "p": "/pdf/c75073f909a3e1f0261153c57bb6d161f09889a6.pdf"}, {"n": 229, "id": "j24USL1xKd", "p": "/pdf/1c27903206d64169041b4b775e3d1d504cee4b1f.pdf"}, {"n": 230, "id": "8DzD2zITNi", "p": "/pdf/4ecf68b9b75ebc474bb08b3b6fda4a6be3f297ff.pdf"}];
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
'pdf chunk 16: ' + log.join(' | ') + ' :: ' + Math.round((Date.now()-t0)/1000) + 's'
