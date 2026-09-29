# Instructions for the independent coder

You are asked to judge whether 109 references, copied exactly as they appear in submitted research papers, cite real works correctly. Two files: `independent_coder_sheet_B.csv` (45 rows) and `independent_coder_sheet_A.csv` (64 rows). They contain only the reference text. Please do sheet B first: it is a random sample and is the one that matters most; sheet A contains harder, deliberately selected cases. Expect about 45 minutes for B and about an hour for A; you can stop and resume.

Who may code: someone who is not an author of the study, does not operate or work for Publish.fun, and has no other connection to the study. Please fill in `CODER_STATEMENT.md` when you finish; it is published with your coding (you may withhold your name there).

Rules: do not look at any other file in this folder or repository, do not use an AI assistant for any item, and do not discuss items with the study's author before you have finished both sheets. Your labels will be compared with labels produced by AI agents and by the author; none of those labels are in your files.

For each row, search for the cited work with whatever you normally use (Google Scholar, Google, Crossref, PubMed, arXiv, publisher sites) and fill in three columns:

- `CODER_CATEGORY`, one of:
  - `EXISTS`: the work exists and the first author (or author list) and year match; a year off by one, typos, truncated titles, altered given names of co-authors or omitted co-authors are fine. Use `WEB_RESOURCE_EXISTS` for URL-only web pages, datasets or software you can locate.
  - `EXISTS_CORRUPTED`: a real work is clearly intended (same topic; the title matches or is a close paraphrase; or the authors, year and topic identify it) but something substantive is wrong: a wrong first author or substantially different people in the author list, year off by more than one, wrong journal or venue, a DOI or arXiv identifier that resolves to a different work or to nothing, or a rewritten or merged title.
  - `NOT_FOUND`: no such work after two searches, first the exact title in quotation marks, then the first author's surname plus three to five distinctive title words. Never decide this from memory alone. Use `WEB_RESOURCE_NOT_FOUND` for dead, unarchived URLs.
  - `PLACEHOLDER`: a deliberately incomplete stub ("Authors. Title. arXiv preprint", a venue "[Conference]", a title cut off with "...").
  - `UNADJUDICABLE`: not a reference at all (a fragment or appendix text) or too little information to search.
- `CODER_EVIDENCE_URL`: the page or DOI that settled it; for NOT_FOUND, the two searches you ran.
- `CODER_NOTE`: one line, e.g. "real: Smith et al. 2019, J Neurosci; cited with wrong journal" or "no such paper; only unrelated hits".

When finished, save both files in place (same file names, same columns) and complete `CODER_STATEMENT.md`. Thank you.
