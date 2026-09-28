const t0 = Date.now(); const sleep = ms => new Promise(r => setTimeout(r, ms));
const items = [{"n": 207, "id": "295UNarKmq", "p": "/pdf/cb7e14e3fb8311a451978ba1c2977e2716769090.pdf"}, {"n": 208, "id": "CQ8MenNpW4", "p": "/pdf/f56fd01bd9c0cc71a9ed8b09f9b74532ce0eb7ca.pdf"}, {"n": 209, "id": "k1jcU6HZta", "p": "/pdf/74088c4c02b3d0a243f96c55bd673bf1beedc08d.pdf"}, {"n": 210, "id": "xQG4Ten4mf", "p": "/pdf/9e29ee76879ce72c2ac88e51d267ca78fc5d99c2.pdf"}, {"n": 211, "id": "k3NZexoWr6", "p": "/pdf/8680ddf2c6eb7ab9eb80292de5ad519ec82669ce.pdf"}, {"n": 212, "id": "0d3Nloe9pB", "p": "/pdf/d0a26c38101228f47bf71a197ce934d7bcc2e4bb.pdf"}, {"n": 213, "id": "hjEsIk0Nux", "p": "/pdf/5aea4181406879877b936df55a2e3962b623f5b7.pdf"}, {"n": 214, "id": "ma5tU8LXiI", "p": "/pdf/f4b8681f8fb5bb5b0d0eb850b2c46bcc9d03810e.pdf"}, {"n": 215, "id": "5cqTODhW4g", "p": "/pdf/f5cf9ae67df672ac88d9eb5fed46e36c4ecb190f.pdf"}, {"n": 216, "id": "L5gDfr4GdF", "p": "/pdf/23823822a9da6cd26826d3e99d69fc4b7c0b4533.pdf"}, {"n": 217, "id": "wWqcNQF7dH", "p": "/pdf/ff0a0d05d042a60fd4a9d431c92e7bfd43b2241b.pdf"}, {"n": 218, "id": "LENY7OWxmN", "p": "/pdf/b549e316e888007797eaf08853c7ac9724bef016.pdf"}];
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
'pdf chunk 15: ' + log.join(' | ') + ' :: ' + Math.round((Date.now()-t0)/1000) + 's'
