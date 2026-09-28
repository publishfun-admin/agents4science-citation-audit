const t0 = Date.now(); const sleep = ms => new Promise(r => setTimeout(r, ms));
const items = [{"n": 231, "id": "3oCWrOf4Gj", "p": "/pdf/901b0b050a7d27562f5404ed81f42d63ba37b295.pdf"}, {"n": 232, "id": "Hp3rUCPI98", "p": "/pdf/439d34c75e7dfb623f24e2a5d380e302f78a45ba.pdf"}, {"n": 233, "id": "hv0EdHgQJP", "p": "/pdf/012da69b7756f99decc0836c4014c1ff5dc0ca68.pdf"}, {"n": 234, "id": "0peaDMOMk8", "p": "/pdf/c06dee3f1a6da225051c8cac699ecddb33b186b1.pdf"}, {"n": 235, "id": "EEvS0GRiKE", "p": "/pdf/0ec6941dc2d4d57afa9fca302bc27ac59a05a23b.pdf"}, {"n": 236, "id": "EJ8cQFi5cU", "p": "/pdf/c7297f8a4bfee647b1ed8c85a5b82ebf6d8e5679.pdf"}, {"n": 237, "id": "zP2eARUsK3", "p": "/pdf/dc8c118b152b143a4ad081baa74f8ded6dd4a8a4.pdf"}, {"n": 238, "id": "kreJgMPdtf", "p": "/pdf/c6d50b9597e2199d81c8df9fa2fcf06a11b5d68f.pdf"}, {"n": 239, "id": "5HqxSctSmB", "p": "/pdf/890cb543bca7a637110260e1625a1c9793806fe6.pdf"}, {"n": 240, "id": "NCoM0crFgB", "p": "/pdf/fa36dc2c56ebfe6251a626034e84bc64a7577a00.pdf"}, {"n": 241, "id": "UfNNqRSkAn", "p": "/pdf/8405fd1d8877e01285769cf40ca053749f8feefc.pdf"}, {"n": 242, "id": "pjpkEHH5YS", "p": "/pdf/cb69434e231e942426e8723a61478362034914a7.pdf"}];
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
'pdf chunk 17: ' + log.join(' | ') + ' :: ' + Math.round((Date.now()-t0)/1000) + 's'
