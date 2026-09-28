// Executed in a Chrome tab on https://openreview.net . Fetches submission PDFs and posts them to the local receiver.
const t0 = Date.now(); const sleep = ms => new Promise(r => setTimeout(r, ms));
const j = async (u) => (await fetch(u, {credentials:'include'})).json();
const base = 'https://api2.openreview.net/notes?';
const groups = ['Conference','Conference/Rejected_Submission','Conference/Withdrawn_Submission','Conference/Desk_Rejected_Submission'];
let notes = [];
for (const v of groups) { const d = await j(base + 'content.venueid=Agents4Science/2025/' + v + '&limit=1000'); notes = notes.concat(d.notes||[]); await sleep(200); }
notes.sort((a,b) => a.number - b.number);
const CHUNK = 0, SIZE = 12;   // edited per call
const slice = notes.slice(CHUNK*SIZE, (CHUNK+1)*SIZE).filter(n => n.content.pdf && n.content.pdf.value);
const dt = new DataTransfer(); const log = [];
for (const n of slice) {
  try {
    let r = await fetch('https://openreview.net' + n.content.pdf.value, {credentials:'include'});
    if (r.status !== 200 || !(r.headers.get('content-type')||'').includes('pdf')) { r = await fetch('https://openreview.net/pdf?id=' + n.id, {credentials:'include'}); }
    const b = await r.blob();
    dt.items.add(new File([b], n.number + '_' + n.id + '.pdf', {type:'application/pdf'}));
    log.push(n.number + ':' + b.size);
  } catch(e) { log.push(n.number + ':ERR'); }
  await sleep(150);
}
const f = document.createElement('form'); f.method='POST'; f.enctype='multipart/form-data'; f.action='http://127.0.0.1:8765/upload'; f.target='_self';
const inp = document.createElement('input'); inp.type = 'file'; inp.name = 'pdfs'; inp.multiple = true; inp.files = dt.files; f.appendChild(inp);
document.body.appendChild(f); f.submit();
'pdf chunk ' + CHUNK + ': ' + log.join(' | ') + ' :: ' + Math.round((Date.now()-t0)/1000) + 's'
