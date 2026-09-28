# Pre-specified analysis plan (written 2026-09-28, before any manual adjudication and before aggregate results were inspected beyond pipeline calibration on 21 papers)

## Corpus
All 315 submissions to Agents4Science 2025 (OpenReview), i.e. 48 accepted, 196 rejected, 10 withdrawn and 61 desk-rejected
records; 314 have a PDF (one is password-protected and excluded). Primary analysis population: the 253 complete
submissions that were reviewed (accepted + rejected, plus any withdrawn submission that received reviews); desk-rejected
submissions are reported separately.

## Unit of analysis and outcome
- Reference = one entry in a paper's reference list as segmented by AnyStyle (junk/parse artefacts excluded).
- Verified = matched to a bibliographic record (DOI/arXiv resolution, Crossref, OpenAlex, DBLP, arXiv, Semantic Scholar,
  OpenLibrary, Google Books) or to a live URL, under pre-set title/year/author agreement thresholds; or adjudicated EXISTS.
- Fabricated (primary outcome) = adjudicated NOT_FOUND or EXISTS_CORRUPTED. Secondary: NOT_FOUND only (total fabrication).
- Paper-level outcome: share of fabricated references, and indicator ">= 1 fabricated reference".

## Questions and tests (all two-sided, alpha = 0.05, 95% Wilson intervals for proportions, bootstrap for differences)
Q1 Prevalence: reference-level and paper-level fabricated shares, overall and by outcome group.
Q2 Organizer flag validity: (a) among the example references the organizers' automated check posted as "could not be
   verified", the share adjudicated fabricated (precision of the flag); (b) paper-level agreement between the organizer
   flag (>= 1 flagged example) and our ">= 1 fabricated" indicator (sensitivity, specificity, kappa).
Q3 Correlates of fabrication (paper level): self-reported AI autonomy in the writing stage (A-D) and overall (sum of
   stages), outcome group, primary topic; Spearman correlation and Kruskal-Wallis across autonomy tiers.
Q4 Review outcomes: association of fabricated share with each LLM reviewer's overall score (Spearman), with the human
   expert score (79 papers), and with acceptance (logistic regression: accepted ~ fabricated share + mean LLM score).
Q5 Reviewer detection: share of papers with >= 1 fabricated reference in which any LLM review, the human review, or the
   organizers' Correctness Check contains an explicit statement that references are fabricated/non-existent/unverifiable
   (regex from code/review_scan; manually confirmed for the matched sentences).
Q6 Taxonomy: distribution of adjudication categories; for NOT_FOUND entries, whether they carry a DOI/arXiv identifier
   (identifier hijacking) and whether the cited year is after the reviewer models' knowledge cutoffs.

## Sampling for manual adjudication
All automatically unverified references in accepted papers are adjudicated. If the remaining queue (rejected, withdrawn,
desk-rejected) exceeds 600 entries, a simple random sample of 600 (numpy seed 20260928) is adjudicated and prevalence in
those groups is estimated with sampling weights; the sampling frame is saved in data/adjudication/SAMPLE.md.

## What is NOT claimed
Adjudication cannot prove non-existence; NOT_FOUND means no trace was found by the protocol at adjudication time. The
audit does not distinguish LLM-generated from human-generated errors; it measures reference integrity of submissions to a
venue that required AI first authorship.
