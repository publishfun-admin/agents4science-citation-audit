const t0 = Date.now(); const sleep = ms => new Promise(r => setTimeout(r, ms));
const items = [{"n": 88, "id": "2ZikSF7mMI", "p": "/pdf/0bd3289960a8d36fed3343ffa12187ec95577b35.pdf"}, {"n": 89, "id": "RknuLtI8bF", "p": "/pdf/a19bb9786db31f971bc2662971273eb8815764ad.pdf"}, {"n": 91, "id": "AzOkqwsTXo", "p": "/pdf/ae50059249f82a4311de820c5f7de256fa6450bb.pdf"}, {"n": 92, "id": "TXPUEX280M", "p": "/pdf/9fc7dd0fbc1ddba21a9078fe211f95a907079eb5.pdf"}, {"n": 95, "id": "DePdMeXCxy", "p": "/pdf/36601b8eed27b1cd3f3df5db5488bbc435d4b8c2.pdf"}, {"n": 96, "id": "hreVjQIgyt", "p": "/pdf/2c506b1785f0ac52dd32d113e43dfab239c16b9a.pdf"}, {"n": 97, "id": "QfcCWkfzgP", "p": "/pdf/d696560cca649ba1cca57f67b255e04a394864df.pdf"}, {"n": 98, "id": "Wyt9peeYrm", "p": "/pdf/53bf27b2721400bc60f50224e6e06afc359ba8c3.pdf"}, {"n": 99, "id": "GnCbMGnE6F", "p": "/pdf/db574eb7baf32d0dba39a1d3c853deb8e19f070c.pdf"}, {"n": 100, "id": "6Sg1kouJmP", "p": "/pdf/3ec28d7b2d37211d7cf77559b9036205c2151f9f.pdf"}, {"n": 101, "id": "QXyeIJ9PQ3", "p": "/pdf/d9202a051590f8115544ac1e259d41c3be25f298.pdf"}, {"n": 102, "id": "h1smCvJcxI", "p": "/pdf/608a3fa1f6efa64b0db3f313477108bbb5067b8f.pdf"}];
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
'pdf chunk 6: ' + log.join(' | ') + ' :: ' + Math.round((Date.now()-t0)/1000) + 's'
