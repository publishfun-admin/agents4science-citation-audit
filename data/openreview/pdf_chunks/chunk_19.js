const t0 = Date.now(); const sleep = ms => new Promise(r => setTimeout(r, ms));
const items = [{"n": 255, "id": "Jxp7TqMCAi", "p": "/pdf/409ed3f49cd1049c19b7ba5f41a3149269980dab.pdf"}, {"n": 256, "id": "yXYEbPQp8x", "p": "/pdf/764044320bbffd9447c0778300c009a28808ea25.pdf"}, {"n": 257, "id": "X26I2fwt3f", "p": "/pdf/9ee99218caea0580b2fd949e6eb9af49376c2e3b.pdf"}, {"n": 258, "id": "BxscqmB9Rs", "p": "/pdf/e7544708fd6a00e5fb201d30f3ea905442f4facf.pdf"}, {"n": 259, "id": "c8L0vgerBs", "p": "/pdf/8d2324a063100c327cb031b9062ea5f6eb963cf1.pdf"}, {"n": 260, "id": "73EbNDKArc", "p": "/pdf/98002485c6c3f051bdf39097abb0adbbe4db7fd5.pdf"}, {"n": 261, "id": "tSkCiacKNK", "p": "/pdf/c5a1e9bc3be09ab4a26c6f3ed19fdbf2eb9c66f2.pdf"}, {"n": 262, "id": "Y3Mn3UkPcz", "p": "/pdf/f3263e81f119c507592934386faf7300ab41afca.pdf"}, {"n": 263, "id": "FYYCrBCTgk", "p": "/pdf/eefd16bb3a515cb4fab0febc7e2e851d270953c5.pdf"}, {"n": 264, "id": "u4i2vyJVqe", "p": "/pdf/6885c1b99e8ede364d782932adb065b804a2efaa.pdf"}, {"n": 265, "id": "HeVPOpanJT", "p": "/pdf/1e69dfab89a20e1d708eeddc91cb8be70b0a37d6.pdf"}, {"n": 266, "id": "r1s9sxQLE5", "p": "/pdf/2aab379d78b4c6d9776e9b5ece587593f1d8abc4.pdf"}];
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
'pdf chunk 19: ' + log.join(' | ') + ' :: ' + Math.round((Date.now()-t0)/1000) + 's'
