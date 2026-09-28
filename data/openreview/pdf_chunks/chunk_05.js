const t0 = Date.now(); const sleep = ms => new Promise(r => setTimeout(r, ms));
const items = [{"n": 75, "id": "XAe1uIBVsk", "p": "/pdf/16c928f16e8ea2a0ef873e126dd8103a7ccc4ded.pdf"}, {"n": 76, "id": "6jqcouwCay", "p": "/pdf/ce23ace9f5ed3a6444b55a3fbdd2fa1fd45365df.pdf"}, {"n": 77, "id": "if6RZty9HK", "p": "/pdf/a46d300280ac67bdb672331ef8c251b74bd23ac8.pdf"}, {"n": 78, "id": "Q7PjM5RFXV", "p": "/pdf/21cd881f0f528b5a68610784abc107d39de9fa81.pdf"}, {"n": 80, "id": "oo7VhdqAMB", "p": "/pdf/5b5feb6e6981a7962887813c4ffdc2f357588fdb.pdf"}, {"n": 81, "id": "Kb5tkksOcN", "p": "/pdf/2f43d124bf1c0f68e1854bce45164342313e184e.pdf"}, {"n": 82, "id": "oUvoYRXNFE", "p": "/pdf/608a8d42c60d7b916721cf2b0e1c0152865c4f9a.pdf"}, {"n": 83, "id": "k5hVY6qj5R", "p": "/pdf/674477e5664b7f8b6e86b5e0e486bf993e02b1fa.pdf"}, {"n": 84, "id": "D04PbaE5X3", "p": "/pdf/34c4f521782a3b9a3524d3ea4c7ec4fada6505d6.pdf"}, {"n": 85, "id": "zXS7K9s1MQ", "p": "/pdf/64b69780af68e4296123f8a3039e7029cc4e030e.pdf"}, {"n": 86, "id": "AZlE3BPVCR", "p": "/pdf/cf77290269c9c438ce225c1e6ff2309086e507db.pdf"}, {"n": 87, "id": "0duEYeqUZw", "p": "/pdf/f751f4dcf165baf56a8014b70f01084320905891.pdf"}];
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
'pdf chunk 5: ' + log.join(' | ') + ' :: ' + Math.round((Date.now()-t0)/1000) + 's'
