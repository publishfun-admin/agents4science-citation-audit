# Manual adjudication protocol (fixed before adjudication began, 2026-09-28)

Unit: one reference entry that the automated pipeline (AnyStyle parse -> DOI/arXiv resolution -> Crossref, OpenAlex,
DBLP, arXiv title search -> second pass: Semantic Scholar, Crossref title query, OpenLibrary, Google Books -> URL liveness)
could not verify. Adjudication is performed by the AI agent (Claude) using web search, with the evidence URL logged for
every decision, so that any reader can re-check any row.

Search procedure (stop as soon as a category is established):
1. Exact-title web search (title in quotes). If the entry has no parsed title, search the raw string's most specific phrase.
2. If no hit: search first-author surname + 3-5 distinctive title words; then first author + year + venue.
3. If still nothing: mark NOT_FOUND. A NOT_FOUND verdict therefore means "no trace of a work with this title (or a close
   variant) by these authors exists in Google-indexed web, Crossref, OpenAlex, DBLP, arXiv, Semantic Scholar, OpenLibrary or
   Google Books at adjudication time".

Categories (mutually exclusive; adapted from the failure-mode taxonomy of Compound Deception, arXiv:2602.05930):
- EXISTS            - a work with this title exists and the listed first author (or author list) and year match (+-1) or
                      differ only by typographic/format issues. Counted as NOT fabricated (automated recall failure).
- EXISTS_CORRUPTED  - a real work is clearly intended (title matches or is a close paraphrase) but at least one
                      substantive attribute is wrong: wrong author(s), year off by >1, wrong venue/journal, wrong or
                      hijacked DOI/arXiv identifier, or a title that merges/alters the real title. Counted as a
                      fabricated attribute (partial fabrication).
- NOT_FOUND         - no such work can be found (total fabrication).
- WEB_RESOURCE      - the entry is a web page, dataset, software repository, standard, or report; it is EXISTS if the
                      resource is found (by URL or name), otherwise NOT_FOUND.
- UNADJUDICABLE     - too little information to search (e.g. parser produced no usable title/author), or the entry is a
                      parsing artefact (not a reference). Excluded from denominators.

Rules:
- Search the web, not memory. Never mark NOT_FOUND on the basis of the adjudicator's prior knowledge alone.
- Log: verdict, category, evidence_url (the page that establishes the verdict; for NOT_FOUND the search-results URL),
  and a one-line note.
- Sampling: all unverified entries in accepted papers are adjudicated; for the remaining groups a simple random sample is
  drawn if the queue exceeds the budget (the sampling frame and seed are recorded in adjudication/SAMPLE.md).

## Amendment 1 (2026-09-28, after 85 adjudications): PLACEHOLDER category
Some reference lists contain entries that are deliberately incomplete pointers rather than citations, e.g.
"Browder, D. M., et al. (2008). Literacy outcomes..." with a trailing ellipsis and no title, venue or identifier
(the "placeholder hallucination" type of the Compound Deception taxonomy). Such entries cannot be adjudicated as a
specific work. They are recorded as PLACEHOLDER, reported separately, excluded from the primary fabricated share
(NOT_FOUND + EXISTS_CORRUPTED), and included in a sensitivity analysis of "defective references"
(fabricated + placeholder). They remain in the denominator of references.
