const t0 = Date.now(); const sleep = ms => new Promise(r => setTimeout(r, ms));
const items = [{"n": 305, "id": "PYqvzvr5F7", "p": "/pdf/6da6509d96ce97891fd62dbd3c3eca951e65568f.pdf"}, {"n": 306, "id": "3PWDmzgjbb", "p": "/pdf/22155ad9b2b33f365e29f6d0c76c1b55ebc6498c.pdf"}, {"n": 307, "id": "AL5YBk5JXP", "p": "/pdf/b02031acf21a058da04d8e7d0531a69c1d3b35c4.pdf"}, {"n": 308, "id": "S8uzdZvStA", "p": "/pdf/4585f678e2431dd9bf68f382b8e6f6d1ea5556fa.pdf"}, {"n": 309, "id": "6b5kZtfwIH", "p": "/pdf/bc5d84bdbd6821b6cffd0f8d471afb11f6c803df.pdf"}, {"n": 310, "id": "7dJ7BFv9AT", "p": "/pdf/3a61c99d23faac4b7521c9595feb29a6087069c0.pdf"}, {"n": 311, "id": "IH6LV3uUTG", "p": "/pdf/d57d645fdec79a9ea61cbea79906bb984e6b6743.pdf"}, {"n": 312, "id": "gArBKNBVyN", "p": "/pdf/846b16b3b6762a4ef8f21933cbef49281059a6cc.pdf"}, {"n": 313, "id": "bBpCWzZ6wm", "p": "/pdf/60c392b1cd76c3fa20f2c91e99a6d3f5e7672957.pdf"}, {"n": 314, "id": "814MdsPtZq", "p": "/pdf/558902e2c75e60156fb7ae311d53dc1d79366d4c.pdf"}, {"n": 315, "id": "wVn3uPvm9W", "p": "/pdf/c3a5083e3e5eff5b3e8390e2969e0979fb29cda1.pdf"}, {"n": 316, "id": "qkVgd25Ngh", "p": "/pdf/470cf87ae623c29aee9c86dfa72c38693b9ccb90.pdf"}];
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
'pdf chunk 23: ' + log.join(' | ') + ' :: ' + Math.round((Date.now()-t0)/1000) + 's'
