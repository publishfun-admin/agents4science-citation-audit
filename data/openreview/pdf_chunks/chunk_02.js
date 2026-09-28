const t0 = Date.now(); const sleep = ms => new Promise(r => setTimeout(r, ms));
const items = [{"n": 37, "id": "soMxckukqT", "p": "/pdf/daa6a3720ac0f953bd1a7178de13b4867597ae29.pdf"}, {"n": 38, "id": "ONQPEgMGqn", "p": "/pdf/fbb3d12b1cc1869e2768942277d29117f5f58cde.pdf"}, {"n": 39, "id": "j9wKyda3jy", "p": "/pdf/cfdfc07078e39b919a74a000f0216ceb8bfe6416.pdf"}, {"n": 40, "id": "d7Uvmmpo0z", "p": "/pdf/95c74f97082b39b661ed055d491d0827bac8a5dd.pdf"}, {"n": 41, "id": "bu89SNurwn", "p": "/pdf/dcd02162e031763f4949d4632d8b55bd6f270a0d.pdf"}, {"n": 42, "id": "3O31o6AKpG", "p": "/pdf/934781f613659f77e726c9e109d7ed874ea96bdb.pdf"}, {"n": 44, "id": "wprP6MbBYd", "p": "/pdf/c407340c04fd898872f36829861b1f6bcd8431df.pdf"}, {"n": 45, "id": "SSQqerDh9A", "p": "/pdf/d243af7d79cbf22f471d582c95d7ef83467d0691.pdf"}, {"n": 46, "id": "x7qlIDcw0P", "p": "/pdf/358b6172077e931bf75ea9bc933e12300228ef65.pdf"}, {"n": 47, "id": "Vw2BtXeizW", "p": "/pdf/63a5ba56c71493070e3d26bb0725b86a0dc33fb0.pdf"}, {"n": 48, "id": "qVYG9fJb8B", "p": "/pdf/d4bed004abcb660c6a47223dfa987ea82d58d8e0.pdf"}, {"n": 49, "id": "fxL6eFPsd1", "p": "/pdf/3234be7aa0beb54b2fbdaf83dddfe5fdae766217.pdf"}];
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
'pdf chunk 2: ' + log.join(' | ') + ' :: ' + Math.round((Date.now()-t0)/1000) + 's'
