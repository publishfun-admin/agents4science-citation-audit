const t0 = Date.now(); const sleep = ms => new Promise(r => setTimeout(r, ms));
const items = [{"n": 21, "id": "Vwoz7Sgb0k", "p": "/pdf/ed7cfc109c6a4b1fb6b07bac66724d743a34d0f4.pdf"}, {"n": 22, "id": "ycBbvnXPfB", "p": "/pdf/384883684fa60f3f72f82d104b15c407f6615336.pdf"}, {"n": 23, "id": "71C5p8pm6s", "p": "/pdf/90731a32f1aa6626c580d1b984299c41ea4b5c94.pdf"}, {"n": 24, "id": "bqBTWmNhGL", "p": "/pdf/5d0bfdf8d24bd78df29dd1949f0e4ee5ce3be5c0.pdf"}, {"n": 26, "id": "suQWzY4lrG", "p": "/pdf/05396a26c2e0456710ceb70f4fe7eb100fc2d033.pdf"}, {"n": 27, "id": "Ko7tXcuAoV", "p": "/pdf/3db7da5654aeafc884508863a3d1bce7bae60ea2.pdf"}, {"n": 28, "id": "3qFtGLGyO3", "p": "/pdf/01c1eccd3ce5fa1b7a69a416582831f14265b443.pdf"}, {"n": 29, "id": "yNUrcUJ4Is", "p": "/pdf/dabb4999269f4826e24fa591c099347e098e3318.pdf"}, {"n": 30, "id": "HMCif97Xd4", "p": "/pdf/ac8418aa863b40712e525ce5f2b4ed882dd9fdde.pdf"}, {"n": 32, "id": "e6e8Snzkpo", "p": "/pdf/002902607d0792a8cb4369386370dac084797af1.pdf"}, {"n": 33, "id": "FHyiXZKQ6o", "p": "/pdf/70a246a0d3786ff025d2b0d2670ae37072d994a1.pdf"}, {"n": 34, "id": "p6A3I9b1wf", "p": "/pdf/c7c7c9f4806c02035e2cac8159f0cd76c9a4c241.pdf"}];
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
'pdf chunk 1: ' + log.join(' | ') + ' :: ' + Math.round((Date.now()-t0)/1000) + 's'
