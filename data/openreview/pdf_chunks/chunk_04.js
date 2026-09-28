const t0 = Date.now(); const sleep = ms => new Promise(r => setTimeout(r, ms));
const items = [{"n": 62, "id": "O9SCxDji5A", "p": "/pdf/cecf0de3c22fbf3094d4ca46558202f61227d851.pdf"}, {"n": 63, "id": "4JsCVsg8Pj", "p": "/pdf/5c27720ef6848536a81b9b3c5fc289b5b06ad3c6.pdf"}, {"n": 64, "id": "heYWeCpOlS", "p": "/pdf/17173ba9a4cd9d01ccf80464a81b0f6b2d987f23.pdf"}, {"n": 65, "id": "YxgXwd9lxM", "p": "/pdf/4fc528d0a0f0a12e89e9d894ebd701ce32de449c.pdf"}, {"n": 66, "id": "s4gTj3fOIo", "p": "/pdf/e319ffa74f170b37fa4209dec5e318ea297e5e56.pdf"}, {"n": 68, "id": "yAxNWUdyxb", "p": "/pdf/89bb5415ec9fe5f8e67498b5274cbe3b2e873185.pdf"}, {"n": 69, "id": "CUkjqutmHr", "p": "/pdf/634c2d55f67fa4d3f04d59062a87d3947aece995.pdf"}, {"n": 70, "id": "BtwfpDb1OO", "p": "/pdf/c86e40a577f67068564988d88b020f5ed3b490ac.pdf"}, {"n": 71, "id": "m0hH80gZmx", "p": "/pdf/8a662ba9829e4111cad1957d4dbeb4769b2b5bba.pdf"}, {"n": 72, "id": "Q8XbQybxbG", "p": "/pdf/67a33cf1e24086fa4873b477925fc194aadddf2c.pdf"}, {"n": 73, "id": "GwIqpSITr9", "p": "/pdf/96162d1013f737e09948cf70246bf3b2586a80ee.pdf"}, {"n": 74, "id": "vlkjLwVoOI", "p": "/pdf/0f73b2bfa35697fab25193df0d22a77a70de0d3f.pdf"}];
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
'pdf chunk 4: ' + log.join(' | ') + ' :: ' + Math.round((Date.now()-t0)/1000) + 's'
