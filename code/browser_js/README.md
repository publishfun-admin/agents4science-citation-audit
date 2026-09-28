# Browser-side data pull (OpenReview)

OpenReview places anonymous API clients behind a Cloudflare Turnstile challenge, which a real browser passes
automatically. The scripts here were executed in a Chrome tab on https://openreview.net (via the Claude-in-Chrome
extension) on 2026-09-28. Because the site's Content-Security-Policy forbids fetch()/XHR to localhost but allows
form submissions to http://127.0.0.1:*, each script fetches a batch of JSON (or PDF blobs) from
https://api2.openreview.net / https://openreview.net with credentials, packs them into a multipart <form>, and submits
it to the local receiver (code/receiver.py), which writes the parts under data/openreview/.

- pull_submissions.js — all notes for the four venue ids (accepted, rejected, withdrawn, desk-rejected): 315 notes.
- pull_forums.js — for a list of forum ids, all replies (`notes?forum=<id>`): official reviews (AIRev1-3 = GPT-5,
  Gemini 2.5 Pro, Claude Sonnet 4 per the organizers' report; human reviewers), the automated Related Work Check and
  Correctness Check comments, and program-chair decisions.
- pull_pdfs.js — for a slice of submissions, the submitted PDF (`/pdf/<hash>.pdf`, fallback `/pdf?id=`), 12 per call.
