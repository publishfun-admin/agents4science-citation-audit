const t0 = Date.now(); const sleep = ms => new Promise(r => setTimeout(r, ms));
const items = [{"n": 156, "id": "qoKZuu16dk", "p": "/pdf/973640436e72c0497ce6ac53649f1fbae33ea99c.pdf"}, {"n": 157, "id": "E2XBNokxDy", "p": "/pdf/ece91dd731ee4d1d446485a9b3e481bba9f7316b.pdf"}, {"n": 158, "id": "RocBBSeKW5", "p": "/pdf/207ec0c480ba962f9681197f5b49b54520e605f5.pdf"}, {"n": 159, "id": "qCGHmXvgWh", "p": "/pdf/a2ae876da4ee8c43e7a866003e474bc0182614ef.pdf"}, {"n": 160, "id": "wpYnS2qBBX", "p": "/pdf/4e24bcee6ffc7b40697156695dcd8c62735a25fb.pdf"}, {"n": 161, "id": "h40Nyr36om", "p": "/pdf/3c568a7196107964f4c728c81303a9307c1919fd.pdf"}, {"n": 162, "id": "3Ik03urmXD", "p": "/pdf/f2595781c66e40c8c1ca2ed505844598ca2cac91.pdf"}, {"n": 163, "id": "Xh0s29VtbH", "p": "/pdf/df059b620dd89f367370d173e116b6632b228cec.pdf"}, {"n": 164, "id": "9uMgJR2mBc", "p": "/pdf/68215ae080deb8f32f7824a1fb52c8677acdd10b.pdf"}, {"n": 165, "id": "sVaRgmH8FE", "p": "/pdf/f3cd178d8c06cf7f8366fbce32590442348603d5.pdf"}, {"n": 166, "id": "5yxNX2pmhJ", "p": "/pdf/46dd3d56496048d38c47ee9bc28c881b6ba092d3.pdf"}, {"n": 167, "id": "Oirsciu0hZ", "p": "/pdf/c6b6d09b30a8eb3f5d495c8d63cf605ec1ab11af.pdf"}];
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
'pdf chunk 11: ' + log.join(' | ') + ' :: ' + Math.round((Date.now()-t0)/1000) + 's'
