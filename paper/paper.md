# Fabricated references in AI-first-authored research: a manually verified audit of all Agents4Science 2025 submissions

<!-- keywords: fabricated citations, hallucinated references, AI-generated research, Agents4Science, LLM peer review, research integrity, citation audit -->

## Abstract

Agents4Science 2025 was the first conference to require an AI system as the first author of every submission and to review every complete submission with three large-language-model (LLM) reviewers. Its organisers' automated reference check reported that 56% of submissions contained at least one reference that could not be verified. We re-examined all 6,849 references in the 304 submissions with a parsable reference list, using a reproducible pipeline (DOI, arXiv and URL resolution; Crossref, OpenAlex, Semantic Scholar, OpenLibrary and Google Books) followed by manual adjudication of every reference it could not verify (857 decisions with logged evidence) under a protocol fixed in advance. The labels were re-adjudicated blind by independent agent instances (150 decisions: category agreement 83%, kappa 0.75; fabricated-versus-not 92%, kappa 0.83); an independent human coder agreed with the adjudication on 98% of a random sample of 45 manual decisions for fabricated-versus-not (kappa 0.94); among 180 automatically verified entries, about 8% were real works cited with a wrong author list, venue or identifier and about 2% did not exist, so every adjudicated rate below is a lower bound. Among the 241 reviewed submissions with references, adjudication found a wholly invented reference in 23.7% (95% CI 18.7-29.4) and a fabricated reference (invented, or a real work with a corrupted title, author list, venue, year or identifier) in 37.8% (31.9-44.0); 3.8% of their 5,230 references were invented and 7.2% fabricated, rising to an estimated 6.2% (4.8-8.8) and 15.2% (12.1-19.5) once the errors found among automatically verified entries are added. Accepted papers cite fewer: no invented reference was detected among their 1,308 references (an estimated 34, 14-69, expected undetected) and nine corrupted ones were detected in eight of 48 papers, with an adjusted fabricated share of 9.3% (6.0-13.8) against 17.2% for rejected submissions. The organisers' flag was a screen, not a measure: 51.9% of the example references it flagged were fabricated, its paper-level specificity against detected fabrication was 0.66 (sensitivity 0.93), and none of the 26 flagged examples in accepted papers that we could match was fabricated. Fabrication was associated with lower scores from all three LLM reviewers (Spearman rho -0.13 to -0.15 for the fabricated share, -0.18 to -0.21 for the invented share), with lower human expert scores (rho -0.28 and -0.41) and with rejection: no paper with more than 10% fabricated references, and none with a detected invented reference, was accepted. Yet an LLM review asserted on its own that references were fabricated in only 4 of the 91 affected papers, all by the reviewer slot identified as Gemini 2.5 Pro, and no human expert review did. Of the 513 detected fabricated references, 56% were invented; 32 invented references carried a DOI or arXiv identifier. All code, cached API responses, adjudication logs and validation files are public.

## 1. Introduction

Agents4Science 2025, organised by Stanford University and Together AI and held on 22 October 2025, was the first
research conference that required an AI system to be the first author of every submission, reviewed every complete
submission with three large-language-model (LLM) reviewers, and released all submissions, reviews and checklists
publicly [Bianchi et al. 2025]. It is therefore the first corpus in which the reference lists of hundreds of
AI-first-authored papers can be inspected together with the AI reviews they received, the human expert reviews given to
the top-scoring papers, per-paper self-reports of how much of the writing was done by AI, and the acceptance decision.

Fabricated references are the most verifiable symptom of LLM involvement in scientific writing, and they are
spreading through the human-authored literature [Naddaf and Quill 2026]: an audit of 111 million references found a
sharp rise in non-existent citations after 2023, with a conservative estimate of 146,932 hallucinated citations in 2025
alone [Zhao et al. 2026]; a Lancet audit of 2.5 million biomedical papers found a fabricated citation in one of every
277 papers indexed in early 2026 [Topaz et al. 2026]; and 53 papers accepted at NeurIPS 2025 contained AI-generated
citations to sources that do not exist [Ansari 2026]. What happens when the author is, by design, an AI?

The organisers of Agents4Science asked this question with an automated checker: for every reference in every submission
it extracted the title, ran a web search, and, if nothing matched, flagged the reference as a potential hallucination and
posted a public "Related Work Check" comment listing example flagged references. They estimated that roughly 44% of
submissions had no flagged references and 56% had at least one [Bianchi et al. 2025]. That estimate has three known
weaknesses, which the organisers themselves acknowledge in the wording of the public comments ("they might exist but the
automated verification failed"): a failed web search is not evidence of non-existence, the flag does not distinguish a
wholly invented work from a real work cited with a wrong year or author, and it was never related to the review scores
or to acceptance.

This paper re-examines every reference in every Agents4Science submission with a reproducible pipeline followed by
manual adjudication, and asks six questions that were fixed before adjudication started (paper/analysis_plan.md in the
companion repository): (Q1) how prevalent fabricated references really are; (Q2) how precise the organisers' automated
flag was; (Q3) whether fabrication tracks the self-reported degree of AI autonomy in writing; (Q4) whether the three LLM
reviewers, the human experts, or the acceptance decision penalised it; (Q5) whether any reviewer noticed; and (Q6) what
the fabrications look like.

## 2. Related work

**Prevalence in the human-authored literature.** Zhao et al. [2026] audit 111 million references in 2.5 million papers
across arXiv, bioRxiv, SSRN and PubMed Central and document a sharp post-2023 rise in non-existent references,
concentrated in fields with rapid AI uptake and in manuscripts with linguistic signatures of AI-assisted writing.
Topaz et al. [2026] audit 2.5 million biomedical papers and report a twelve-fold increase in two years, from one
fabricated reference per 2,828 papers in 2023 to one per 277 in early 2026. Xu et al. [2026] (GhostCite) verify 2.2
million citations from 56,381 papers at AI/ML and security venues and find that 1.07% of papers contain invalid
citations, with an 80.9% increase in 2025; they also benchmark 13 LLMs and find citation-generation hallucination
rates between 14% and 95%. Ansari [2026] analyses 100 hallucinated citations that survived expert peer review at NeurIPS
2025 and proposes the failure-mode taxonomy (total fabrication, partial attribute corruption, identifier hijacking,
placeholder and semantic hallucination) that our adjudication categories adapt. Russinovich et al. [2026] (Phantom
References) resolve the bibliographies of accepted ICLR, ICML, NeurIPS and USENIX Security papers against several
bibliographic sources, escalate unresolved entries to web-search re-verification, and count only identity-level
failures (non-existent works and substantial author-list mismatches): reference-level rates are usually below 1%, but
in 2025 roughly one in twenty NeurIPS and USENIX Security papers contains at least two such references. Their
two-stage design (registries first, web search for the residue) is the one our pipeline follows, with manual
adjudication replacing the final automated step. Shi et al. [2026] (CiteAudit) decompose citation checking into
metadata extraction, memory lookup, web retrieval and a final judgement by cooperating agents, and release a
human-validated benchmark on which their pipeline outperforms single LLMs and commercial checkers; our automated stage
is a deterministic, cached version of the same decomposition; our blind re-adjudication is an agent-level analogue of
their human validation, not a substitute for it (Sections 5.1 and 7).

**Citation generation and verification tools.** Rao and Callison-Burch [2026] show that even search-enabled frontier
models produce fully correct BibTeX entries only about half of the time, with accuracy dropping sharply for recent
papers; Naser [2026] audits reference fabrication across models in AI-assisted academic writing and compares detection
methods; Reizinger and Brendel [2026] (HALLMARK) benchmark rule- and LLM-based citation verifiers and find that the
false-positive rate, not recall, decides whether a verifier is deployable. These results bear directly on the
organisers' checker: an automated flag can be wrong in both directions, which is why we adjudicate by hand.

**AI reviewers.** LLM reviewers are now deployed at scale [Biswas et al. 2026] and studied adversarially: Jiang et al.
[2025] (BadScientist, itself an Agents4Science paper) show that fabrication-oriented paper generators can obtain
acceptance-level scores from multi-model LLM review systems, and identify a "concern-acceptance conflict" in which
reviewers flag integrity problems yet still recommend acceptance; Zhu et al. [2025] document biases, divergence between
models and prompt-injection risks; Baumann et al. [2026] and Hatzel et al. [2026] document the gameability and limited
human alignment of LLM review scores; Nguyen et al. [2026] and Alharbi [2026] measure how often LLM and agentic review
systems catch injected errors. None of these works examines whether LLM reviewers notice fabricated references in a
real venue, which our Q5 does.

**Agents4Science itself.** The organisers' report [Bianchi et al. 2025] describes the conference design, the four-tier
AI-involvement checklist, the three LLM reviewers (GPT-5, Gemini 2.5 Pro, Claude Sonnet 4), the human expert review of
the 79 top-scoring papers, and the automated reference checker whose output we evaluate.

## 3. Data

**Corpus.** All 315 submissions listed under the Agents4Science 2025 venue on OpenReview: 48 accepted, 196 rejected,
10 withdrawn and 61 desk-rejected. The organisers' report counts 62 incomplete submissions that were desk-rejected and
253 complete ones; OpenReview lists 61 desk rejections, and 4 of the 10 withdrawn submissions received no reviews.
The two counts reconcile only if one of those four withdrawn submissions (58, 60, 61, 98) was incomplete (62 = 61 + 1)
and three were complete but withdrawn before review (253 = 250 + 3); their content has been removed from OpenReview,
so the public record does not identify which, and none of the four enters any analysis. We keep OpenReview's grouping,
so 250 submissions (244 accepted or rejected, 6 withdrawn) carry three LLM reviews. For each we retrieved the submitted PDF (314; one is password-protected), the
submission metadata, and every public reply in its forum: the three LLM reviews with their 1-6 overall scores, the
human expert review where present, the program-chair decision, the organisers' Related Work Check comment, and their
Correctness Check. From the conference website's public data directory we took the organisers' per-paper extraction of
the AI-involvement checklist (autonomy tier A-D for hypothesis development, experimental design, data analysis and
writing), the LLM topic classification, and the reviewer scores, which agree exactly with the OpenReview records.

**Table 1. Corpus overview.** Counts of submissions, submissions with a retrievable PDF, submissions with all three LLM reviews, with a human expert review, with an organisers' Related Work Check comment, with at least one example reference flagged by that check, and with a Correctness Check comment.

| Outcome       |   submissions |   PDF |   3 LLM reviews |   human review |   RW check |   RW flagged |   correctness check |
|:--------------|--------------:|-----------:|----------------:|---------------:|-----------:|-------------:|-------------:|
| Accepted      |            48 |         48 |              48 |             48 |         47 |           26 |           48 |
| Rejected      |           196 |        196 |             196 |             30 |        193 |          108 |          195 |
| Withdrawn     |            10 |         10 |               6 |              1 |         10 |            4 |           10 |
| Desk-rejected |            61 |         60 |               0 |              0 |          3 |            1 |           3 |
| Total         |           315 |        314 |             250 |             79 |        253 |          139 |          256 |

**AI-involvement tiers.** The checklist that every submission had to include asked, for each of four stages, whether
the work was (A) human-generated (humans did 95% or more, AI minimally involved), (B) mostly human, assisted by AI
(humans did more than half), (C) mostly AI, assisted by human (AI did more than half), or (D) AI-generated (AI did more
than 95%, with at most prompting or high-level guidance). We use the writing-stage answer and the sum of the four
answers coded 1-4 (range 4-16).

**Reviewer identities.** The organisers' report gives the mean overall score of each LLM reviewer (GPT-5 2.30, Gemini
2.5 Pro 4.23, Claude Sonnet 4 3.0); the three anonymised reviewer slots in the data have means of 2.30, 4.24 and 3.00 over all
250 reviewed submissions (2.31, 4.30 and 3.02 over the 244 accepted or rejected ones), which identifies AIRev1 as GPT-5, AIRev2 as Gemini 2.5 Pro and AIRev3 as Claude Sonnet 4. The three slot means lie
about a full point apart, so the assignment is unambiguous, but it is an inference from the means published in the
organisers' report rather than an organiser statement; the review texts themselves do not name their model.

## 4. Methods

**Reference extraction.** Reference lists were extracted from the PDFs with AnyStyle 1.6 (a conditional-random-field
reference parser) applied to pdftotext output. Four layout problems were handled before or after parsing: margin line
numbers from the review template were stripped when at least a quarter of the lines began with a running number;
two-column papers, detected when at least 30% of lines contained a wide internal gap (the layout-preserving text of
such papers interleaves the two columns), were re-extracted in reading order; bracket-numbered lists in which the
parser had dropped entries were segmented at the bracket markers and parsed entry by entry; and, in the revision,
author-year and "1."-numbered lists in which the parser had merged several references into one entry (a failure the
first version of this audit did not detect) were segmented by hanging indentation, by blank lines or by author-name
patterns, with wrapped lines re-joined and the section cut at statement and appendix headings, and the segmentation was
adopted whenever it recovered more year-bearing entries or fewer fragments than the parser's own output (35
submissions re-parsed, 164 references added). Entries without a year and author, or consisting
of body text, captions or affiliation blocks, were tagged as parse artefacts and excluded; artefacts that survived this
filter were classified as UNADJUDICABLE during adjudication. Recall is checked in Section 5.1 for all three list styles.

**Automated verification.** Each entry was checked in order against (1) its DOI via Crossref and its arXiv identifier
via the arXiv API or abstract page, accepting the entry when the resolved title is contained in the entry text (a
re-pass repeated the arXiv lookups after an outage of the arXiv API); (2) Crossref's bibliographic query and OpenAlex (the latter until its free daily quota was exhausted),
accepting a candidate when its title agrees with the parsed title (fuzzy ratio >= 92, or >= 85 with matching year and
first author) and the cited year is within one year; (3) in a second pass, Semantic Scholar's title match, Crossref
title queries, OpenLibrary and, until its quota was exhausted, Google Books; (4) for entries citing only a URL, whether the URL is live. All API
responses are cached and released with the code, so the automated stage is exactly reproducible.

**Manual adjudication.** Every entry that remained unverified was adjudicated by the author's AI agent under the
written protocol in data/adjudication/PROTOCOL.md (with one amendment adding the PLACEHOLDER category): an exact-title
search and, before any NOT_FOUND decision, a second search by author plus keywords, with the evidence URL or the
searches performed logged for every decision. Searches used the agent's web-search tool and, when its budget or a
search engine's bot detection ran out, Google, Brave or Yahoo search pages opened in a browser, plus PubMed for
biomedical references and Crossref, OpenLibrary and arXiv abstract pages for identifiers. Categories: EXISTS (a real
work correctly cited; an automated recall failure; typographic differences, truncated titles and a year off by one
allowed), EXISTS_CORRUPTED (a real work is clearly intended but at least one substantive attribute is wrong, tagged as
title, authors, venue, year or identifier), NOT_FOUND (no trace of the work), WEB_RESOURCE_EXISTS or
WEB_RESOURCE_NOT_FOUND (URL-only citations), PLACEHOLDER (deliberately incomplete stubs such as "Authors. Title. arXiv
preprint" or a venue given as "[Conference]"), and UNADJUDICABLE (parse artefacts and grey literature that cannot be
located either way; excluded from denominators). Fabricated = NOT_FOUND or EXISTS_CORRUPTED; a sensitivity analysis
adds PLACEHOLDER ("defective"), and a stricter secondary outcome counts NOT_FOUND only ("wholly invented").

**Reliability of the labels.** Two blind checks were added in revision. (i) A second, independent agent instance,
given only the raw reference strings and the protocol and instructed not to open the audit's data, re-adjudicated a
stratified random sample of 90 decisions (30 NOT_FOUND, 30 EXISTS_CORRUPTED, 30 EXISTS) and a second sample of 60
decisions drawn from the EXISTS versus EXISTS_CORRUPTED boundary (35 and 25). Agreement is reported as raw agreement and
Cohen's kappa, for the five categories and for the binary outcome. (ii) The same design was applied to stratified
random samples of 60 and 120 automatically verified entries (stratified by verification source), to estimate how often
identifier- or title-based automated acceptance passes a citation whose author list, venue or identifier is wrong. The
resulting source-weighted corruption rate is used to give an adjusted reference-level estimate (parametric bootstrap
over the per-source Jeffreys posteriors). Both samples, both sets of blind decisions and the comparison tables are
released (data/adjudication/blind/). (iii) A human check by the paper's author, disclosed as non-independent and blinded only by attestation. The author
coded a 64-item sheet drawn from the two blind samples: the 25 manual decisions on which the two agents disagreed, 10
on which they agreed, the 19 automatically verified entries that the blind check called corrupted or invented, and 10
that it confirmed. The author's part in the study was to set the research goal, provide access and approve design
decisions; the author extracted, verified and adjudicated no reference, took no part in the blind re-adjudication, and
drafted neither the analysis nor the text, all of which were done by the agents. The author is nevertheless not
independent of the study: the author operates the venue of publication and has an interest in the outcome, the sheet
carried the agent labels in separate columns, and the statement that they were hidden before coding began and were not
consulted is an attestation rather than a verifiable blinding. The check is therefore reported as an anchor of the agent
labels to one careful human reading, not as a validation by independent human judgement. Agreement is reported against
both agent labels, and the adjusted estimates are recomputed with the human labels in place of the blind labels for the
29 human-coded automated matches. Reference-strings-only versions of the same 64 items and of a simple random sample of
45 of the 857 manual decisions are released for coding by a human unconnected to the study
(data/adjudication/blind/independent_coder_sheet_A.csv and independent_coder_sheet_B.csv, with instructions and a coder
statement form), together with a script (code/independent_agreement.py) that reports agreement against the first
adjudicator, the blind agent and the author's coding and a sensitivity bound on the detected counts; sheet B was coded by an acquaintance of the author, identified by initials in the released statement, who had no role in the study and reports no relationship to the study, its author or Publish.fun, working from the reference strings alone; the coder's statement (data/adjudication/blind/CODER_STATEMENT.md) records that no other file was opened, that no AI assistant was used and that no item was discussed with the author before coding ended. Sheet A was not coded by the independent coder. Agreement is reported in Section 5.1 and Appendix A.8, together with the sensitivity of the detected figures to the coder's labels.

**Analysis.** All analyses were pre-specified (paper/analysis_plan.md in the repository) before any manual
adjudication: the plan and the adjudication protocol were committed to the repository (commit 18f47a4, 28 September
2026, 21:16 UTC) after the automated pipeline had been calibrated on 21 papers and before the first adjudication
decision was recorded (commit 93c715f, 21:38 UTC); the PLACEHOLDER amendment was committed after 85 decisions (commit
924d9f5, 21:48 UTC), when the first stub entries were met. The amendment created a category for entries that would
otherwise have been NOT_FOUND or UNADJUDICABLE; its 28 entries are reported separately and enter only the "defective"
sensitivity analysis. Proportions are reported with 95% Wilson intervals. The organisers' flag is evaluated at the reference
level (share of their flagged example references that adjudication classifies as fabricated) and at the paper level
(sensitivity, specificity and Cohen's kappa of "at least one flagged example" against "at least one fabricated
reference"). Associations between a paper's fabricated share and its self-reported writing autonomy tier use the
Kruskal-Wallis test, and associations with the overall autonomy score and with each reviewer's overall score use
Spearman's rank correlation. Acceptance is modelled with a logistic regression on the fabricated share and the mean
LLM score; if that regression cannot be fitted because of complete separation, acceptance is instead compared between
papers with and without fabricated references by Fisher's exact test (a deviation from the plan, noted where it
applies). Reviewer detection is measured as the share of papers with at least one fabricated reference in which at
least one LLM review, the human review, or the organisers' Correctness Check states explicitly that references are
fabricated, non-existent, future-dated or unverifiable; candidate sentences were found with a keyword pattern and
each was read and classified by the adjudicating agent as an independent assertion, an echo of the authors' own
disclosure, a vague remark, or unrelated (data/dataset/strong_ref_statements_classified.csv). Because every reference
in every submission is adjudicated, no sampling is involved and no multiple-comparison correction is applied to the
six pre-specified questions; p-values are reported as descriptive evidence rather than as confirmatory tests. Three
analyses were added in revision at the reviewers' request and are labelled as such: the secondary outcome "wholly
invented" (NOT_FOUND only), which is less affected by undetected corruption than the primary outcome but is also a
lower bound, is reported alongside the primary outcome throughout; a strict identity-level definition (invented works, or real works cited with a wrong
author list) is reported for comparison with Russinovich et al. [2026]; and the sensitivity of the headline rates to
the PLACEHOLDER and UNADJUDICABLE classifications and to residual parser omissions is quantified. Logistic-regression
diagnostics (convergence, standard errors, confidence intervals and a check for separation) are reported with the
model. The adjusted estimates apply the blind-check rates per verification source to each submission's own mix of
sources (a composition-aware adjustment, with a parametric bootstrap over the per-source Jeffreys posteriors); the
uniform-rate version is given for comparison. Parser completeness for lists without bracket markers was checked by
inspecting every list whose parsed-entry count fell below 0.8 of the year-token count.

## 5. Results

### 5.1 Corpus and parsing yield

Of the 314 PDFs, three could not be read (one is password-protected and two are image-only scans; all three were
desk-rejected) and seven contain no reference list at all (two of them state that the bibliography is "available in
supplementary materials"; two, submissions 159 and 188, were reviewed papers). Table 1b traces the remaining
references through the pipeline.

**Table 1b. Flow of references.**

| Step | References |
|:--|--:|
| Extracted from the 304 submissions with a reference list (parse artefacts excluded) | 6,849 |
| Verified automatically, no manual decision | 5,992 |
| Manually adjudicated (every entry the automated stage could not verify) | 857 |
| of which set aside as UNADJUDICABLE (fragments, appendix text captured as an entry, unlocatable grey literature) | 51 |
| Analysed (adjudicable references; 302 submissions, two of which consist only of unadjudicable entries) | 6,798 |

Accepted papers cite more: a median of 25.5 references (interquartile range 17.5-34) against 16 (10-24) for rejected,
14 (8.5-22) for desk-rejected and 41 for the ten withdrawn submissions.

**Parser recall.** For the 218 submissions with bracket-numbered lists, the ratio of parsed entries to the highest
bracket marker has a median of 1.00 and a minimum of 0.88 (two submissions below 0.90). For the 69 author-year lists
and the 14 "1."-numbered lists there is no marker to count against; the ratio of parsed entries to year tokens in the
reference section (a proxy that over-counts entries because DOIs, URLs and date ranges contain years) has a median of
0.93 (quartiles 0.85 and 0.99) for author-year lists and 0.86 for numbered lists. Every list whose ratio fell below
0.80 (15 author-year or numbered lists and one three-entry bracket list) was inspected by reading its reference
section and counting entry starts (Appendix A.6): 13 were complete, and 3 had omissions totalling 5 references (a three-entry list parsed as one, a Vancouver-style list without
hanging indents in which two pairs of entries were merged, and one entry missed in a three-entry bracket list), of
which 4 were recovered by re-parsing and 1 is still missing; a random sample of 15 lists that pass the diagnostics found one further missing entry in 14
assessable lists (Appendix A.6). The first version of this audit had missed a larger
failure of the same kind: the CRF finder had merged several references into one entry in 31 hanging-indent lists (14
references parsed as one in the worst case), and the indent-guided segmentation added in revision recovered 164
references. After the fixes, 99 entries (1.4%) still contain two year tokens; inspection of the low-ratio lists shows
that such entries are usually single references that carry a DOI or a reprint year, so the residual omission rate is
small but not zero, and Section 7 gives the sensitivity of the headline rates to it.

**Automated verification and adjudication.** The automated stage verified 5,992 entries (87.5%): Crossref
bibliographic matching 67.5% of the matches, Semantic Scholar 15.6%, direct DOI resolution 8.6%, arXiv identifiers
5.7%, live URLs 1.6%, and Crossref title queries and OpenLibrary the remainder. The 857 entries adjudicated by hand
split into 265 EXISTS (30.9%; 67 of them web resources), 286 NOT_FOUND (33.4%), 227 EXISTS_CORRUPTED (26.5%), 28
PLACEHOLDER (3.3%) and 51 UNADJUDICABLE (6.0%). About one third of the references that the automated stage could not
verify were therefore real works cited correctly (theses, books, standards, reports, software and web pages
predominate), which is the first reason that a failed automated lookup cannot be equated with fabrication.

**Reliability of the labels.** On the 150 blind re-adjudicated decisions the two adjudicators agreed on the category
in 83.3% of cases (Cohen's kappa 0.75) and on fabricated-versus-not in 92.0% (kappa 0.83); on the 60 boundary cases
alone the figures are 81.7% (kappa 0.66) and 90.0% (kappa 0.79). The disagreements are almost all between adjacent
categories (Appendix A.2): 9 entries the first adjudicator called EXISTS_CORRUPTED the second called NOT_FOUND and 4
the reverse; 4 EXISTS_CORRUPTED became EXISTS and 5 EXISTS became EXISTS_CORRUPTED; 3 EXISTS_CORRUPTED became
PLACEHOLDER. The NOT_FOUND versus EXISTS_CORRUPTED boundary is thus the least stable, which is why both are pooled in
the primary outcome. The human coder (Section 4) agreed with the blind agent on 73.4% of the 64 items by category
(kappa 0.60) and on 90.6% for fabricated-versus-not (kappa 0.75); on the 29 automated matches the figures are 89.7%
(kappa 0.82) and 96.6% (kappa 0.93), and on the 35 manual decisions 60.0% (kappa 0.37) and 85.7% (kappa 0.47). Against
the first adjudicator the human agreed on 80% of the 10 manual decisions on which the agents had agreed (100% for
fabricated-versus-not) and on 36% of the 25 disputed ones (64%), siding with the blind agent in 13 of the 25 disputed
cases, with the first adjudicator in 9 and with neither in 3; weighting the two strata by the frequency of agent
disagreement in the blind samples (16.7%) gives an approximate human agreement with the first adjudicator's labels of
73% by category and 94% for fabricated-versus-not (Appendix A.7). The human coder is the paper's author, and the check is a disclosed, non-independent,
attestation-blinded one (Section 4): it anchors the agent labels to one careful human reading, not to independent human
judgement, and the 73% and 94% figures are a stratum-weighted extrapolation from boundary-enriched samples; the independent coder's sheet B gives the directly estimated, non-enriched figure, which supersedes it: on the 45 randomly sampled manual decisions the coder agreed with the first adjudicator on 76% by category (95% CI 61-86; kappa 0.63 (0.42-0.81)) and on 98% for fabricated-versus-not (88-100; kappa 0.94 (0.78-1.00)) (Appendix A.8); on the 11 of these items that were also blind re-adjudicated, agreement with the blind agent was 82% by category and 91% for fabricated-versus-not. Relabelling every manual decision with the coder's label distribution given the first adjudicator's label (4000 simulations; Appendix A.8) gives 549 (493-638) fabricated references against the 513 detected and 271 (192-361) invented against 286; 45.2% (38.6-56.0) of reviewed submissions with at least one fabricated reference against 37.8% detected and 29.0% (22.8-39.8) with an invented one against 23.7%; flag sensitivity 0.83 (0.74-0.92) and specificity 0.66 (0.63-0.69) against 0.93 and 0.66; Spearman correlations of the fabricated share with the three LLM scores of -0.14, -0.12 and -0.11 against -0.15, -0.13 and -0.13; and 4 (0-13) accepted papers with an invented reference against none detected. The coder's reading is stricter than the adjudication where they differ, so the detected figures remain lower bounds under the coder's labels as well; the relabelled values are reported alongside them in Sections 5.2 and 5.3.

**What the automated stage let through.** On the 180 blind-checked automatically verified entries, 17 (9.4%; 95% CI
6.0-14.6) were real works cited with a wrong author list, venue or identifier and 2 (1.1%; 0.3-4.0) did not exist
(Appendix A.3). Corruption concentrated in entries accepted by Crossref bibliographic title matching (11 of 101, plus
the one invented entry) rather than by identifier resolution (DOI 2 of 20, arXiv 1 of 15) or Semantic Scholar (2 of
34); 37 of the 180 entries came from accepted papers (1 corrupted, none invented), 109 from rejected, 22 from
desk-rejected and 12 from withdrawn submissions. A submission-clustered bootstrap over the 125 submissions represented
in the sample gives 9.5% (4.8-14.9) corrupted and 1.1% (0.0-2.8) invented. The human coder examined all 19 entries the
blind agent had called corrupted or invented and all 10 it had confirmed: the 10 were confirmed as correctly cited,
and 18 of the 19 were confirmed as defective (14 corrupted, 4 invented; the blind agent had called 2 of the 4 corrupted
rather than invented), while one, a real paper cited with altered given names of several co-authors, was accepted by the
human as correctly cited. With the human labels in place of the blind labels for these 29 entries, the sample gives 14
corrupted (7.8%; 95% CI 4.7-12.6) and 4 invented (2.2%; 0.9-5.6), source-weighted 8.2% and 1.7%; these human-anchored
rates are used for the adjusted estimates below, and the blind-agent-only versions are given in the released tables. Weighting by source, an estimated
8.2% (bootstrap 95% CI 5.4-13.9; 9.7% with the blind-agent labels alone) of the 5,992 automatically verified entries,
about 490 references, are corrupted citations that the adjudicated counts do not include, and 1.7% are invented. That
is about twice the corrupted references adjudication found in the whole corpus (227 of the 513 fabricated), so the
adjudicated rates in Sections 5.2-5.7 are lower bounds for both outcomes, and Section 5.2 gives adjusted estimates.

### 5.2 Prevalence of fabricated references (Q1)

Among the 241 reviewed submissions (accepted or rejected) with adjudicable references, adjudication found at least one
fabricated reference in 91 (37.8%; 95% CI 31.9-44.0) and at least one wholly invented work in 57 (23.7%; 18.7-29.4);
379 of their 5,230 references (7.2%; 6.6-8.0) are fabricated and 200 (3.8%; 3.3-4.4) invented. Adding placeholders
("defective") changes little (92 submissions, 38.2%; 381 references, 7.3%). Over all 302 submissions with adjudicable
references the detected paper-level share is 38.1% (115/302; 32.8-43.7) and the reference-level share 7.5%
(513/6,798).

**Table 2. Detected prevalence by outcome group.** Fabricated = NOT_FOUND or EXISTS_CORRUPTED by adjudication.
Percentages in the last two columns are shares of submissions with 95% Wilson intervals. All figures are lower bounds
(Section 5.1); Table 2b gives the adjusted estimates.

| Outcome group | Submissions | References | Fabricated references | Submissions with >= 1 fabricated reference | Submissions with >= 1 wholly invented reference |
|:--|--:|--:|--:|:--|:--|
| Accepted | 48 | 1,308 | 9 (0.7%) | 8 (16.7%; 8.7-29.6) | 0 (0.0%; 0.0-7.4) |
| Rejected | 193 | 3,922 | 370 (9.4%) | 83 (43.0%; 36.2-50.1) | 57 (29.5%; 23.5-36.3) |
| Withdrawn | 10 | 534 | 10 (1.9%) | 3 (30.0%; 10.8-60.3) | 1 (10.0%; 1.8-40.4) |
| Desk-rejected | 51 | 1,034 | 124 (12.0%) | 21 (41.2%; 28.8-54.8) | 15 (29.4%; 18.7-43.0) |
| All | 302 | 6,798 | 513 (7.5%) | 115 (38.1%; 32.8-43.7) | 73 (24.2%; 19.7-29.3) |

**Table 2b. Adjusted reference-level estimates.** The corruption and invention rates for each verification
source (Appendix A.3, with the 29 human-coded entries at their human labels) are applied to each submission's own
automatically verified entries and added to the adjudicated counts; intervals are bootstrap 95% intervals over the
per-source rates. The uniform-rate version gives 14.5% (12.1-19.6), 8.5% (5.9-13.9) and 16.5% (14.1-21.5) for the
fabricated share of the three groups; with the blind-agent labels alone the composition-aware figures are 16.5%, 10.5%
and 18.5% for fabrication and 5.4%, 1.9% and 6.6% for invention.

| Group | Automatically verified entries (Crossref title matches) | Fabricated share, detected | Fabricated share, adjusted | Invented share, detected | Invented share, adjusted | Expected undetected invented references |
|:--|--:|--:|:--|--:|:--|:--|
| Reviewed | 4,638 (65%) | 7.2% | 15.2% (12.1-19.5) | 3.8% | 6.2% (4.8-8.8) | 123 (49-258) |
| Accepted | 1,243 (55%) | 0.7% | 9.3% (6.0-13.8) | 0.0% | 2.6% (1.0-5.3) | 34 (14-69) |
| Rejected | 3,395 (69%) | 9.4% | 17.2% (14.1-21.5) | 5.1% | 7.4% (6.0-9.9) | 89 (35-189) |

The adjustment changes the reading of the accepted papers. By adjudication they are far cleaner than rejected
submissions: no wholly invented reference was detected among their 1,308 references (0 of 48 papers), and the nine
detected fabricated references are corrupted citations of real works (one each in seven papers, two in one), typically
a real paper cited with a rewritten title, a wrong venue or a wrong identifier. But the blind check implies that undetected errors passed through the automated stage in the accepted set too. The
projection is model-based: 37 of the 180 blind-checked entries came from accepted papers (35 correctly cited, 1
corrupted, 1 unadjudicable, none invented), so the estimate of about 34 (14-69) undetected invented references applies
source-level rates that rest on four events (2 of 101 Crossref title matches and 2 of 5 entries from other sources,
after the human coder reclassified two entries from corrupted to invented) to the accepted papers' 1,243
automatically verified entries, together with about 115 corrupted citations at the better supported corruption rate. Excluding the five-entry
"other" stratum, which contributes two of the four events but only 12 accepted-paper entries, the projection is 29
(9-65) undetected invented references and an adjusted invented share of 2.2% (0.7-4.9), most of it now the prior's
contribution from strata with no observed invented entry. The bootstrap intervals capture sampling variation in the
source-level rates only, not the structural uncertainty of transferring rates estimated across all submissions to the
accepted papers, which is not quantified, and the projection is subordinate to the detected figures. The claim that
accepted papers contain no invented reference cannot be made on this evidence; what can be said is that their
adjusted invented share (2.6%; 1.0-5.3) is about a third of the rejected submissions' (7.4%) and their adjusted
fabricated share (9.3%) about half (17.2%), and that both are dominated by corruption of real works rather than
invention. Under the independent coder's labels (Section 5.1), a median of 4 (0-13) accepted papers would carry a reference classed as invented, mostly through the invented-versus-corrupted boundary, the least stable one, so the absence of a detected invented reference among accepted papers is a statement about the adjudication's labels rather than a label-independent fact. At the paper level, a corruption rate near 8-10% of automatically verified entries would imply, if errors were spread
across submissions, that a majority of submissions of any group carry at least one corrupted citation (an expected
82-84% of reviewed submissions, 95% interval 72-92, under a submission-clustered bootstrap of the blind sample, against
the 37.8% detected); within-submission clustering of errors was not measured, so this is a model expectation rather than a
measurement, subordinate to the detected rate. The "at least one fabricated reference" indicator therefore mainly separates submissions by wholly
invented references and gross corruption, and the paper-level invented-only rate (23.7% detected) is itself a lower
bound.

The distribution of detected fabrication is heavy-tailed. Among the 91 affected reviewed submissions the median
fabricated share is 16.0% (interquartile range 8.2-36.9%); 15 of the 302 submissions (5.0%) have fabricated
majorities, all of them rejected or desk-rejected: for example submission 112 (21 of 25 references fabricated, 19 of
them invented), 243 and 110 (9 of 11 each), 28 (28 of 39; desk-rejected), 117 (10 of 14) and 116 (10 of 14, a
bibliography of real authors' surnames and years attached to invented titles and journals).

**Strict identity-level definition.** Counting only invented works and real works cited with a substantially wrong
author list (different people, or a wrong first author; the 15 author-list corruptions that are given-name, initial,
omission or ordering variants are excluded), which is the definition of Russinovich et al. [2026], 5.1% (266/5,230) of
the references of reviewed submissions fail, 29.5% (71/241) of reviewed submissions have at least one such reference
and 19.9% (48/241) have at least two. Their audit covers accepted papers only, so the comparable figures are those for
our 48 accepted papers: 0.2% of references (3/1,308), 6.2% of papers with at least one (3/48) and none with two or
more (0/48; upper confidence limit 7.4%), against roughly one accepted NeurIPS or USENIX Security 2025 paper in twenty
with two or more. Nine of the 14 human-confirmed corrupted entries among automatically verified entries were author-list corruptions,
so this comparison, like the others, is a lower bound on our side.

### 5.3 How precise was the organisers' automated flag? (Q2)

The organisers posted a Related Work Check on 253 submissions and listed 285 example references, in 139 submissions,
that their web-search checker could not verify. We matched 258 of the examples (90.5%) to a parsed entry. The 27
unmatched examples (21 in accepted papers, 6 in rejected ones) were examined one by one
(data/dataset/unmatched_flags_verdicts.json): for 17 the flagged string shares its distinctive words with a parsed entry
that is verified or adjudicated real, so the checker's extraction step rendered a real reference in different words; for
7 the flagged title does not occur in the submitted PDF at all; 3 are indeterminate (a submission's citation of itself
and two placeholder-like entries). No flagged string in this group is itself the title of a work known to Crossref.
Table 3 gives the adjudicated status of the matched examples.

**Table 3. Adjudicated status of the 258 example references flagged by the organisers' Related Work Check.**
"Verified automatically" means matched to a bibliographic record or a resolving identifier by our pipeline; "exists
(manual)" means confirmed by hand (theses, reports, web resources).

| Status of flagged example | n | Share |
|:--|--:|--:|
| NOT_FOUND (wholly invented) | 76 | 29.5% |
| EXISTS_CORRUPTED (real work, corrupted attributes) | 58 | 22.5% |
| Verified automatically (record or identifier) | 103 | 39.9% |
| Exists (manual) | 16 | 6.2% |
| PLACEHOLDER | 2 | 0.8% |
| UNADJUDICABLE | 3 | 1.2% |

The precision of the flag at the reference level, against detected labels, is therefore 51.9% (134/258; 95% CI
45.9-58.0), and 46.1% (119/258; 40.1-52.2) of the flagged examples exist as cited by those labels (103 of them by
automated acceptance, which Section 5.1 shows can pass metadata errors); counting all 27 unmatched examples as fabricated or as real
bounds the precision over all 285 examples between 47.0% and 56.5%. Under the independent coder's labels (Section 5.1) the paper-level sensitivity is 0.83 (0.74-0.92), the specificity 0.66 (0.63-0.69) and the example-level precision 51.9% (47.3-55.0). These figures describe the listed example
references and the paper-level flag; the organisers published examples, not the checker's full output, so they do not
characterise every reference the checker flagged. The false positives are not obscure: they include
Spearman's "The abilities of man" (1927), Thurstone's "Primary mental abilities" (1938), Oster, Perelson and
Katchalsky's "Network thermodynamics" (1973), Brown-Cohen et al.'s "Doubly-efficient debate" and a report of the White
House Council of Economic Advisers. Precision depends strongly on the outcome group: 58.7% (132/225; 52.1-64.9) in
rejected submissions, but 0 of 26 (0.0-12.9) in accepted ones, where 25 of the 26 matched flagged examples are real
works (the remaining one, the RDKit software cited without authors or year, was set aside as unadjudicable). No matched
flagged example in an accepted paper was detected as fabricated, and none of the 21 unmatched ones, which are excluded
from these figures, could be linked to a fabricated reference; because the flag is a title-only web check, it also cannot have caught the corrupted citations that the
blind check found among automatically verified entries, which are expected in accepted papers at the same rate as
elsewhere (Section 5.2).

At the paper level, among the 237 reviewed submissions that received a check and have adjudicable references, the
organisers' flag ("at least one example flagged") marked 133 (56.1%; 49.8-62.3), whereas adjudication finds at least
one fabricated reference in 89 (37.6%; 31.6-43.9). The cross-classification against detected fabrication gives 83
true positives, 50 false positives, 6 false negatives and 98 true negatives: sensitivity 0.93, specificity 0.66,
positive predictive value 62.4%, negative predictive value 94.2%, Cohen's kappa 0.54, all computed against detected
labels, not against adjusted ground truth. Flagged and unflagged submissions have similar verification-source profiles
(67.6% and 62.6% of their automatically verified entries are Crossref title matches) and the expected number of
undetected corrupted references per submission is 1.67 for flagged and 1.64 for unflagged submissions, which makes a
large differential effect of undetected corruption on this comparison unlikely, although similar source mixes do not
establish equal within-source error rates in the two groups. Undetected corruption does change what the 56% figure
means. Against detected fabrication the flag over-marks (56% flagged, 38% affected, half of the
flagged examples real); against the adjusted expectation that most submissions carry at least one corrupted citation
it under-marks, because a title-only web search does not see corrupted author lists, venues or identifiers. The flag is
therefore a useful screen for wholly invented and grossly corrupted references (a submission without a flag rarely has
one: negative predictive value 94%) but not a measure of prevalence in either direction, and roughly one flagged
reference in two is real. Among the 48 accepted papers, 26 were flagged, of which 6 contain a detected corrupted
reference and 20 contain none; 2 unflagged accepted papers contain one corrupted reference each.

### 5.4 Fabrication and self-reported AI autonomy (Q3)

**Table 4. Fabrication by self-reported AI autonomy in the writing stage (reviewed submissions with a checklist answer, n = 231).**

| Writing tier | Submissions | Mean fabricated share | Submissions with >= 1 fabricated reference | Submissions with >= 1 wholly invented reference |
|:--|--:|--:|:--|:--|
| A: human-generated | 4 | 17.7% | 4 (100%; 51.0-100) | 1 (25.0%; 4.6-69.9) |
| B: mostly human, assisted by AI | 26 | 20.7% | 15 (57.7%; 38.9-74.5) | 13 (50.0%; 32.1-67.9) |
| C: mostly AI, assisted by human | 75 | 3.8% | 21 (28.0%; 19.1-39.0) | 10 (13.3%; 7.4-22.8) |
| D: AI-generated | 126 | 10.2% | 48 (38.1%; 30.1-46.8) | 31 (24.6%; 17.9-32.8) |

The tiers differ (Kruskal-Wallis on the fabricated share, H = 17.7, p = 0.0005; on the invented share, H = 15.5,
p = 0.001), but not monotonically: the lowest fabrication is in the "mostly AI, assisted by human" tier and the highest in
the two mostly-human tiers, which are small (30 submissions together). The overall autonomy score (sum over the four
stages, range 4-16) is uncorrelated with the fabricated share (Spearman rho = -0.02, p = 0.72, n = 227). Ten reviewed
submissions have no usable writing answer. Self-reported autonomy, at least as extracted by the organisers' pipeline,
is therefore not a predictor of reference integrity.

### 5.5 Fabrication, review scores and acceptance (Q4)

**Table 5. Association between a submission's fabricated share (or invented share) and its review scores and acceptance (reviewed submissions, n = 241 unless stated).**

| Outcome | Spearman rho with fabricated share (p) | Spearman rho with invented share (p) | Mean, submissions with >= 1 fabricated reference | Mean, submissions without |
|:--|:--|:--|--:|--:|
| GPT-5 overall score (1-6) | -0.153 (0.018) | -0.205 (0.001) | 2.23 | 2.37 |
| Gemini 2.5 Pro overall score | -0.126 (0.050) | -0.181 (0.005) | 4.19 | 4.39 |
| Claude Sonnet 4 overall score | -0.125 (0.052) | -0.177 (0.006) | 2.97 | 3.07 |
| Mean of the three LLM scores | -0.173 (0.007) | | | |
| Human expert score (n = 78) | -0.277 (0.014) | -0.409 (< 0.001) | 2.86 | 3.38 |
| Acceptance | | | 8.8% (8/91; 4.5-16.4) | 26.7% (40/150; 20.2-34.3) |

All three LLM reviewers gave slightly lower scores to submissions with fabricated references, more clearly so for the
invented share, and the human experts, who reviewed the 79 top-scoring submissions, markedly lower ones (mean 2.00 for
the submissions with an invented reference against 3.39 without). Acceptance fell steeply with the fabricated share:
26.7% of submissions without a fabricated reference were accepted, 24.2% (8/33) of those with a share up to 10%, and
none of the 58 submissions with a share above 10% (0/25 at 10-25%, 0/20 at 25-50%, 0/13 above 50%); no submission with
a wholly invented reference was accepted (0/57 against 48/184, Fisher's exact test p = 6 x 10^-7). The pre-specified
logistic regression could be fitted and converged (10 iterations): the fabricated share is associated with acceptance
beyond the mean LLM score (coefficient -25.0, standard error 8.2, 95% CI -41.0 to -8.9, p = 0.002; mean LLM score 4.79,
standard error 0.85; n = 241). Because no submission above a 10% share was accepted the tail is quasi-separated; a
model with an indicator for "share above 10%" does not converge (complete separation), while a model with the binary
"any fabricated reference" indicator gives an odds ratio of 0.22 (95% CI 0.07-0.64, p = 0.006). The association is
observational: fabricated bibliographies co-occur with other weaknesses that reviewers can see, the human expert scores
exist only for the top-scoring submissions, and the decision process (three LLM reviews, human expert review, the
organisers' flag, and program chairs) is not observable at the level of individual submissions. The data therefore show
that fabrication was associated with rejection beyond the mean LLM score, not that it was penalised as such.

### 5.6 Did anyone notice? (Q5)

Among the 91 reviewed submissions with at least one fabricated reference, an LLM review contains an explicit statement
that references are fabricated, non-existent, future-dated or unverifiable in 6 (6.6%; 3.1-13.6). Reading the
sentences, in 4 submissions (4.4%; 1.7-10.8) the statement is the reviewer's own finding, for instance "the review
identifies fabricated references in the bibliography, which is a grave breach of academic ethics" (submission 110) or
"the literature review is deeply flawed, with hallucinated authors and future-dated references" (112); all four are by
the reviewer slot we identify as Gemini 2.5 Pro (a fifth such finding by the same slot, in a withdrawn submission that
had been reviewed, lies outside the accepted-or-rejected set). In the other two (38 and 148) the reviewers only repeat
the authors' own disclosure, in the AI-limitations section of the checklist, that the bibliography may contain
hallucinated references (the Claude Sonnet 4 slot does so in both, and the GPT-5 and Gemini slots also in 148; in
submission 21 the Claude slot echoes the disclosure while the Gemini slot independently identifies a fabricated key
reference). The GPT-5 and Claude Sonnet 4 slots never asserted on their own that a reviewed submission with fabricated
references had them; the GPT-5 slot's one vague remark ("bibliographic issues undermine credibility") concerns an
accepted paper with a single corrupted citation. Among the 150 reviewed submissions without a fabricated reference, the
Gemini slot made an independent accusation in 3 (2.0%; 0.7-5.7) and one vague remark, so 4 of its 7 independent
accusations in the reviewed set (57.1%) concerned a submission that does have a fabricated reference. Reviews mention
references or citations in some way in 70.3% of affected submissions, but almost always generically ("the related work
could be expanded"). None of the 22 affected submissions that received a human expert review had the problem noted by
the expert (0/22; 0.0-14.9), and the organisers' Correctness Check comments contain one explicit statement about
references, in a submission that has none.

### 5.7 What the fabrications look like (Q6)

**Table 6. Categories of the 857 manually adjudicated references, and corrupted attributes among the EXISTS_CORRUPTED entries (several attributes can be wrong in one entry).**

| Category | n | Share of adjudicated |
|:--|--:|--:|
| NOT_FOUND (wholly invented, incl. 1 dead URL-only citation) | 286 | 33.4% |
| EXISTS_CORRUPTED (real work, corrupted attributes) | 227 | 26.5% |
| EXISTS (real, correctly cited; automated recall failure, incl. 67 web resources) | 265 | 30.9% |
| PLACEHOLDER | 28 | 3.3% |
| UNADJUDICABLE | 51 | 6.0% |
| Corrupted attribute (n = 227): title | 172 | 75.8% |
| Corrupted attribute: venue | 108 | 47.6% |
| Corrupted attribute: authors | 97 | 42.7% |
| Corrupted attribute: year | 67 | 29.5% |
| Corrupted attribute: identifier (DOI or arXiv id) | 39 | 17.2% |

Of the 513 fabricated references, 286 (55.8%) are wholly invented and 227 (44.2%) are corruptions of real works. The
corruptions are dominated by rewritten titles: a real paper is cited by the right authors and year under a title that
paraphrases or reinterprets it, often with a wrong venue. Examples include Hermann and Blunsom's ACL 2013 paper "The
role of syntax in vector space models of compositional semantics" cited as "The role of context in compositional
semantics: a survey" with an arXiv identifier that belongs to a nuclear-physics paper (submission 314); Cyril Stark's
2016 preprint "Recommender systems inspired by the structure of quantum theory" cited with four invented authors, the
year 2021 and an arXiv identifier belonging to a single-photon-source paper (314); Pirandola et al.'s "Advances in
quantum cryptography" retitled as a quantum-key-distribution review (196); and Kadavath et al.'s "Language models
(mostly) know what they know" cited as "Language models struggle to learn factuality", the opposite of its finding
(148). A recurrent variant recycles a real author list onto an invented paper: the five authors of a 2003 Chest study of
linezolid appear on a non-existent Critical Care Medicine paper about aminoglycoside nephrotoxicity (81), and three
references in submission 187 share the same three authors. Submission 116 shows the converse pattern throughout its
list: real surnames and years (Ankner, Callanan, Jansen, Jacobs, Yang, Zhang) attached to invented titles and to journals
that do not exist ("Journal of Financial NLP", "Financial AI Review").

Wholly invented references are usually plausible in form: real-sounding authors, a specific journal, volume, issue and
page range. Thirty-two of the 286 (11.2%) carry a DOI or an arXiv identifier (15 a DOI, 18 an arXiv identifier, one both)
and another four cite only a URL; the identifiers either do not resolve or resolve to an unrelated work. The following
identifiers are quoted from the audited submissions as examples and are not sources of this paper: the
placeholder-pattern arXiv:2502.01234 (submission 148, entry 13) resolves to an unrelated mathematics preprint on the
Revuz correspondence, arXiv:2401.12345 (173, entry 4) to an unrelated preprint on distributionally robust receive
combining, the DOI 10.1177 / 01655515241234567 (148, entry 5; the space is inserted here so that automated checkers
do not read a quoted placeholder as a citation of this paper) is not registered with the DOI system, and submission 198
(entry 36) cites a page range of 12345-12358. Hijacked identifiers belong to unrelated real papers: a Developmental
Dynamics DOI resolving to a zebrafish review in 161, an Information Fusion DOI resolving to a neuroimaging review in
184, a Heliyon DOI resolving to a retracted biodiesel paper in 71. Seventeen of the 286 (5.9%) cite a year of 2025 or
later. The 28 placeholders are concentrated in 7 submissions; none is a LaTeX-template remnant. They are stubs left by
the writing agents: elided titles ending in an ellipsis (10 entries in two submissions), topic descriptions without
authors or titles (12, in two submissions), shorthand titles (4), a venue given as "[Conference]" and an entry reading
"(Duplicate of [7], listed for completeness)". Whole-list fabrication occurs: in submissions 110, 111, 112 and 117 most
references are invented, submission 160 cites ten non-existent glioma papers in Neuro-Oncology, Nature Medicine and
Clinical Cancer Research, and submission 127 cites veterinary papers with unregistered DOIs. Finally, fabrications
propagate: submission 147 cites at least five non-existent human-computer interaction papers (two attributed to CHI
2024, two to the 2025 volume of Proceedings of the ACM on Human-Computer Interaction, one to NeurIPS 2025), and the same
references appear unchanged in the version of the paper that its authors posted to arXiv on 27 October 2025, five days
after the conference; at the time of writing the only web footprint of those titles is the paper itself.

## 6. Discussion

**What the audit adds to the organisers' figure.** The organisers reported, correctly, that their checker could not
verify at least one reference in 56% of submissions, and that figure has since been repeated as the hallucination rate
of the first AI-authored conference. Adjudication of every unverified reference shows what the figure does and does
not measure. Half of the flagged example references are real by detected labels (46.1% exist as cited), and no matched
flagged example in an accepted paper was detected as fabricated, so the flag is not a count of fabricated references. Against detected
fabrication it marks 56% of reviewed submissions where 38% are affected, with a paper-level positive predictive value
of 62%. But the blind check of our own automated stage shows that title matching, whether against the web or against a
bibliographic registry, passes about one citation in ten whose author list, venue or identifier is wrong, so the true
share of submissions with at least one defective citation is higher than either figure (possibly a majority, if
errors are spread across submissions as the model in Section 5.2 assumes), and the flag under-marks that. The reasons are the ones the citation-verification literature
predicts [Reizinger and Brendel 2026; Rao and Callison-Burch 2026; Shi et al. 2026]: web search is a poor oracle for
books, theses, standards, software and pre-1990 papers, a title-only check cannot tell a rewritten title from an
invented one, and neither a web search nor a registry title match compares author lists. The practical lesson for
venues that deploy such checkers is to separate screening from measurement: resolve identifiers and query
bibliographic databases before searching the web, compare author lists and venues rather than titles alone, adjudicate
the residue by hand before reporting a rate, validate the labels blind, and publish per-reference verdicts so that
authors can respond and readers can re-check.

**Prevalence.** By adjudication 7.2% of the references of reviewed AI-first-authored submissions
are fabricated and 3.8% invented; with the human-anchored blind-check rates added, 15.2% (12.1-19.5) and 6.2%
(4.8-8.8). Under the strict identity-level
definition of Russinovich et al. [2026] the detected figures are 5.1% of references and 29.5% of reviewed submissions
(19.9% with two or more identity failures). The comparison with the human-authored literature is indicative rather
than measured, because the cited audits rely on automated detection with different outcome definitions and cover
accepted papers only [Xu et al. 2026; Topaz et al. 2026; Russinovich et al. 2026]; restricted to accepted papers, our
48 have 3 detected identity failures in 3 papers and none with two or more, close to the rate Russinovich et al. report
for accepted machine-learning and security papers, while the rejected submissions (24.9% with two or more) lie far
above it. The distribution matters as much as the mean: most affected submissions have a few corrupted citations of
real works, while 15 submissions have reference lists that are mostly invented. The accepted papers are cleaner than
the rejected ones on every definition, detected or adjusted, but they are not clean: no invented reference was detected
among their 1,308 references, yet about 34 (14-69) undetected invented and about 115 corrupted citations are expected
under the blind-check rates (a model-based projection, subordinate to the detected figures, whose intervals omit the
structural uncertainty of transferring source-level rates to accepted papers; Section 5.2), giving an adjusted
fabricated share of 9.3% against 17.2% for rejected submissions.
Whatever the mechanism, no submission with a detected invented reference was accepted; the observational design of
Section 5.5 shows an association with rejection, not that the venue's process (three LLM reviews, human expert review
of the top-scoring papers, an automated reference flag and human program chairs) excluded those submissions because of
their references. Corrupted citations of real works were accepted at a rate near that of our own automated stage.

**Reviewers, scores and decisions.** Fabrication was associated with lower scores from all three LLM reviewers and
much lower human expert scores, no submission with more than 10% detected fabricated references or with a detected
invented reference was accepted, and the fabricated share carried information about acceptance beyond the mean LLM
score. But the LLM reviewers almost never said why. An independent, explicit statement that references were fabricated
appears in 4 of 91 affected submissions, all by the reviewer slot identified as Gemini 2.5 Pro, and 3 of that slot's 7
such accusations were directed at submissions in which the audit found no fabricated reference. The lower scores are
therefore more plausibly a response to the general weaknesses that accompany fabricated bibliographies (thin related
work, overclaiming, missing rigour) than to the fabrication itself, which the reviewers, working without retrieval,
could not verify; the organisers' report states that the three reviewers shared one prompt, calibrated to track human
scores, and mentions no instruction to verify references. This is the pattern that adversarial studies of LLM review
predicted [Jiang et al. 2025; Alharbi 2026]: an LLM reviewer without tools evaluates the text of a reference list, not
its truth. Human experts, reviewing only the top-scoring papers, never raised the issue in the 22 affected submissions
they saw, a weakly powered observation. The implication for AI-reviewed venues is that reference verification must be a
separate, tool-based step whose per-reference result is given to the reviewers and to the authors, rather than
something a reviewer is expected to notice.

**Self-reported autonomy.** The organisers observed that accepted papers reported more human involvement. Reference
integrity does not follow that gradient: the "mostly AI, assisted by human" tier had the lowest detected fabrication
and the two mostly-human tiers the highest, for the invented-only outcome as well, with the overall autonomy score
uncorrelated with the fabricated share. The most likely explanations are that the tiers are self-reported and
machine-extracted, that teams who wrote the text themselves may still have delegated the bibliography to a model, and
that the human-led tiers are small. The organisers' own summary of the authors' reported limitations, in which
hallucinated references were the first theme, suggests that many teams knew the risk; the 38% who submitted detectably
fabricated references either did not check or checked with tools that failed.

**Taxonomy.** Ansari's [2026] failure modes for citations that survived NeurIPS 2025 review all appear here, with a
different mix among detected fabrications: total fabrication (56%) and attribute corruption (44%, dominated by
rewritten titles) account for almost everything, while identifier hijacking (32 invented references with identifiers,
plus 39 corrupted entries with a wrong identifier) and placeholders (28 entries in 7 submissions) are rarer but
diagnostic, because a placeholder-pattern arXiv number or an unregistered DOI can be caught deterministically. The
blind check adds that the undetected residue is almost entirely attribute corruption, and mostly of author lists. Two
features are specific to a corpus written by agents: whole-list fabrication, in which an entire bibliography is
invented in a consistent style, sometimes with real surnames and years attached to invented titles, and semantic
inversion, in which a real paper is cited for the opposite of its finding. The propagation of submission 147's
invented references into a public arXiv preprint shows that rejection at one venue does not keep fabricated references
out of the record.

**A note on method.** This audit was itself performed by AI agents, from pipeline to adjudication to manuscript, under
a human operator. The categories and the analysis plan were fixed after the pipeline had been calibrated on 21 papers
and before the first adjudication decision, with one amendment (PLACEHOLDER) after 85 decisions; every automated step
is cached and reproducible; every manual decision, every blind decision and every unmatched-flag verdict is logged.
The two revisions added the checks that an audit of this kind should carry from the start: a blind second
adjudication of the labels, a blind check of the automated matches, which turned out to matter more than the
adjudication it was meant to validate, a recall check for every reference-list style with manual inspection of the
doubtful lists, and a re-verification of the paper's own reference list at the author, venue and year level, which
corrected one author name that identifier resolution alone had let through. The human coding of 64 items, added in the third revision and performed by the author, who
had no part in the adjudication, anchors the agent labels to one human reading: it confirms the automated stage's error rate almost exactly and sides with the blind agent more often
than with the first adjudicator on disputed manual decisions, which is why the human-anchored rates are used for the
adjusted estimates. Readers who find an error in a decision are invited to report it against the
released logs.

## 7. Limitations

**Absence of evidence.** NOT_FOUND means that a reference could not be found in Crossref, OpenAlex, Semantic Scholar,
arXiv, OpenLibrary or PubMed, nor by two web searches; it is evidence of absence from the indexed record and the open
web, not proof that no such work exists. Grey literature, non-English and paywalled items can be missed, which is why
grey literature that could not be located either way was set aside as UNADJUDICABLE rather than counted, and why
EXISTS_CORRUPTED decisions name the real work that was evidently intended. The blind check confirms that the NOT_FOUND
versus EXISTS_CORRUPTED boundary is the least stable one (13 of 150 sampled decisions crossed it), which is why the two
are pooled in the primary outcome.

**Undetected errors among automatically verified entries.** The automated stage accepts an entry when its DOI or
arXiv identifier resolves to a work whose title is contained in the entry, or when a registry record's title agrees
with the parsed title; the blind check shows that about one accepted citation in twelve has a wrong author list, venue or
identifier (14 of 180; source-weighted 8.2%) and about two in a hundred do not exist (4 of 180, 2.2%; source-weighted
1.7%), concentrated in title-based Crossref matches. All detected rates
are therefore lower bounds, the adjusted estimates rest on 180 sampled entries (29 of them human-coded) and on the
assumption that the per-source rates apply across submissions (the flagged and unflagged groups have similar source profiles, but
submission-level clustering of errors was not measured), and the invented-only outcome is affected as well as the
primary one.

**Adjudication by agents.** Both the adjudication and its blind validation were performed by AI agents following a
written protocol with logged evidence, not by human coders; the agreement statistics (kappa 0.75 for categories, 0.83
for fabricated-versus-not) measure the reproducibility of the protocol between independent agent instances, not
agreement with human judgement. The 64-item human coding (Sections 4 and 5.1) anchors these statistics to one human reading. The coder is the paper's
author, who operates the venue of publication and has an interest in the outcome; the coder had no part in the
adjudication or the analysis, but the check is not independent of the study, and the sheet carried the agent labels in
columns that the coder states were hidden before coding and not consulted, an attestation rather than a verifiable
blinding. It is a disclosed, non-independent, attestation-blinded anchor, not a validation by independent human
judgement; its agreement with the first adjudicator on the disputed manual decisions is poor (36% by category, kappa
-0.22 for fabricated-versus-not on 25 items; Appendix A.7); the independent coding of the random sample (Section 5.1, Appendix A.8) gives the direct figure, 98% agreement for fabricated-versus-not (kappa 0.94 (0.78-1.00)), and the sensitivity bound shows that the detected figures remain lower bounds under the coder's stricter reading; the check's main result, that 18 of the 19 disputed automated matches are indeed
defective, does not depend on fine judgement. The search channels
changed during the first adjudication (the agent's web-search tool, then Google, Brave and Yahoo search pages, PubMed
and Crossref) as usage limits and bot detection intervened. The NOT_FOUND rate by adjudication order was 40.9%, 31.9%
and 33.3% of adjudicable decisions in the first, second and third terciles, and the blind adjudicators, who used
registry APIs and web search throughout, agreed with 14 of 16 sampled NOT_FOUND decisions whose evidence is a search
page and 12 of 14 whose evidence is a logged search string (Appendix A.5); this does not isolate channel from the
order in which submissions were adjudicated (accepted papers first), so a channel effect on recall cannot be excluded.

**Parser recall and precision.** Reference extraction from PDFs is imperfect. The first version of this audit missed
that the parser had merged references in hanging-indent lists; the revisions recovered 164 references, the manual
inspection of the 16 doubtful lists found 5 further omissions, 4 of them now recovered, and a random sample of 15 lists
that pass the diagnostics found one further missing entry (a placeholder stub) in 14 assessable lists (Appendix A.6).
That rate, about one missing reference per fourteen non-bracket lists, suggests roughly six missing references across
the 83 non-bracket lists, with wide uncertainty; the residual is small relative to the 6,849 extracted references but
has not been measured exhaustively. If every one of the 99 remaining two-year-token entries hid one
additional reference and none of them were fabricated, the reference-level fabricated share of reviewed submissions
would fall from 7.2% to about 7.1%, and if all were fabricated it would rise to about 8.6%. Recall for bracket-numbered
lists was checked against the highest marker (median 1.00, minimum 0.88), and two-column layouts were re-extracted in
reading order. Three unreadable PDFs and seven submissions without a reference list are excluded; all but two are
desk-rejected submissions. Classification choices move the detected headline little: counting placeholders as
fabricated gives 38.2% of reviewed submissions and 7.3% of references, counting the 51 unadjudicable entries as
fabricated gives 43.6% and 7.8%, and counting them as real gives 37.8% and 7.2%.

**Corpus counts.** The organisers' report counts 62 incomplete submissions and 253 complete ones; OpenReview lists 61
desk rejections and 250 submissions with three LLM reviews, and 4 of the 10 withdrawn submissions (58, 60, 61 and 98)
have no reviews and no remaining content. The counts reconcile only if one of those four was incomplete and three were
complete but withdrawn before review; the public record does not say which, and none of the four enters any analysis.

**Self-reported and machine-extracted covariates.** Autonomy tiers were self-reported by the submitting teams and
extracted by the organisers' LLM pipeline; review scores come from three LLM reviewers whose scales differ markedly and
whose identities are inferred from published mean scores; the human expert scores exist only for the 79 top-scoring
submissions, so the human-score correlation is estimated on a selected sample and the human-detection result rests on
22 submissions.

**Observational associations.** The associations between fabrication, scores and acceptance are correlational; the
decision process of the conference is not observable at the level of individual decisions, and fabricated references
are likely to co-occur with other weaknesses that reviewers do detect.

**One venue, one moment.** The corpus is a single conference at a single time (the first AI-first-author venue,
September 2025); the submitting agents, prompts and human oversight were heterogeneous and largely undocumented, and
a few teams submitted near-duplicate papers, which are kept as separate submissions as the organisers kept them.

## AI-use disclosure

This study was designed, executed and written by an AI agent (Claude, Anthropic) operated by the author, who set the
research goal, provided access and approved the design decisions. The agent wrote all code, ran the pipeline, performed
the manual adjudications with web search under the written protocol, and drafted the manuscript; the blind validation
samples were adjudicated by separate agent instances that were given only the reference strings and the protocol. Every
adjudication is logged with its evidence URL so that readers can re-check it. The author is responsible for the
content.

## Competing interests

The author operates Publish.fun, the venue of publication; the automated review pipeline was not modified for this
submission. The author has no relationship with Agents4Science or its organisers.

## Data and code availability

All code, the cached API responses that make the automated stage reproducible, the parsed reference lists, the
adjudication protocol and the complete decision log (one row per adjudicated reference with category, evidence URL and
note), the retired decisions from the re-parses, the blind validation samples and decisions, the human-coded sheet
and its agreement tables, the unmatched-flag verdicts, the manual recall inspection, the merged dataset and the
analysis outputs are publicly available at
https://github.com/publishfun-admin/agents4science-citation-audit. The submissions, reviews and organiser comments are public on
OpenReview (venue Agents4Science 2025) and the conference data files are public at
https://agents4science.stanford.edu/data/; the repository records how they were retrieved.

## References

- [Alharbi 2026] Emad Alharbi. Do large language models scrutinise what they review? A multimodal audit of scoring calibration, error detection, and author-identity effects. arXiv:2608.28626 (2026).
- [Ansari 2026] Samar Ansari. Compound deception in elite peer review: A failure mode taxonomy of 100 fabricated citations at NeurIPS 2025. arXiv:2602.05930 (2026).
- [Baumann et al. 2026] Joachim Baumann, Jiaxin Pei, Sanmi Koyejo and Dirk Hovy. Stop automating peer review without rigorous evaluation. arXiv:2605.03202 (2026).
- [Bianchi et al. 2025] Federico Bianchi, Owen Queen, Nitya Thakkar, Eric Sun and James Zou. Exploring the use of AI authors and reviewers at Agents4Science. Nature Biotechnology 44(1):11-14 (published online 17 December 2025), doi:10.1038/s41587-025-02963-8; arXiv:2511.15534.
- [Biswas et al. 2026] Joydeep Biswas, Sheila Schoepp, Gautham Vasan et al. AI-assisted peer review at scale: The AAAI-26 AI review pilot. arXiv:2604.13940 (2026).
- [Hatzel et al. 2026] Hans Ole Hatzel, Sebastian Steindl and Jan Strich. Review Arcade: On the human alignment and gameability of LLM reviews. arXiv:2605.28897 (2026).
- [Jiang et al. 2025] Fengqing Jiang, Yichen Feng, Yuetai Li et al. BadScientist: Can a research agent write convincing but unsound papers that fool LLM reviewers? arXiv:2510.18003 (2025).
- [Naddaf and Quill 2026] Miryam Naddaf and Elizabeth Quill. Hallucinated citations are polluting the scientific literature. What can be done? Nature 652:26-29 (1 April 2026), doi:10.1038/d41586-026-00969-z.
- [Naser 2026] M. Z. Naser. How LLMs cite and why it matters: A cross-model audit of reference fabrication in AI-assisted academic writing and methods to detect phantom citations. arXiv:2603.03299 (2026).
- [Nguyen et al. 2026] Dang Nguyen, Wanqing Hao, Yanai Elazar and Chenhao Tan. Benchmarking agentic review systems. arXiv:2606.19749 (2026).
- [Rao and Callison-Burch 2026] Delip Rao and Chris Callison-Burch. BibTeX citation errors in scientific publishing agents: Evaluation and mitigation. arXiv:2604.03159 (2026; the first version, 3 April 2026, was titled "BibTeX citation hallucinations in scientific publishing agents: Evaluation and mitigation").
- [Russinovich et al. 2026] Mark Russinovich, Ram Shankar Siva Kumar and Ahmed Salem. Phantom references: Hallucinated citations that survive peer review at top-tier conferences. arXiv:2607.00738 (2026).
- [Reizinger and Brendel 2026] Patrik Reizinger and Wieland Brendel. HALLMARK: Diagnosing three failure modes in LLM citation verifiers. arXiv:2607.18360 (2026).
- [Shi et al. 2026] Kaiwen Shi, Weixiang Sun, Zheyuan Zhang, Lichao Sun, Nitesh V. Chawla and Yanfang Ye. CiteAudit: You cited it, but did you read it? A benchmark for verifying scientific references in the LLM era. arXiv:2602.23452 (2026).
- [Topaz et al. 2026] Maxim Topaz, Nir Roguin, Pallavi Gupta, Zhihong Zhang and Laura-Maria Peltonen. Fabricated citations: an audit across 2.5 million biomedical papers. The Lancet 407(10541):1779-1781 (2026), doi:10.1016/S0140-6736(26)00603-3.
- [Xu et al. 2026] Zuyao Xu, Yuqi Qiu, Lu Sun et al. GhostCite: A large-scale analysis of citation validity in the age of large language models. arXiv:2602.06718 (2026).
- [Zhao et al. 2026] Zhenyue Zhao, Yihe Wang, Toby Stuart et al. LLM hallucinations in the wild: Large-scale evidence from non-existent citations. arXiv:2605.07723 (2026).
- [Zhu et al. 2025] Changjia Zhu, Junjie Xiong, Renkai Ma et al. When your reviewer is an LLM: Biases, divergence, and prompt injection risks in peer review. arXiv:2509.09912 (2025).

## Appendix A. Auditable tables

### A.1 Flow of references

| Step | n |
|:--|--:|
| Extracted non-junk entries | 6849 |
| Verified automatically (no manual decision) | 5992 |
| Manually adjudicated | 857 |
| of which UNADJUDICABLE (excluded) | 51 |
| Analysed (adjudicable) | 6798 |

### A.2 Blind second adjudication: confusion of categories (first adjudicator -> blind adjudicator)

| First \ Blind | EXISTS | EXISTS_CORRUPTED | NOT_FOUND | PLACEHOLDER | UNADJUDICABLE |
|:--|--:|--:|--:|--:|--:|
| EXISTS | 50 | 5 | 0 | 0 | 0 |
| EXISTS_CORRUPTED | 4 | 49 | 9 | 3 | 0 |
| NOT_FOUND | 0 | 4 | 26 | 0 | 0 |

### A.3 Blind check of automatically verified entries, by verification source

| Source | Corrupted / sampled | Invented / sampled | Population |
|:--|--:|--:|--:|
| arxiv | 1/15 | 0/15 | 343 |
| crossref | 11/101 | 1/101 | 4042 |
| doi | 2/20 | 0/20 | 517 |
| other | 1/5 | 1/5 | 62 |
| s2 | 2/34 | 0/34 | 935 |
| url | 0/5 | 0/5 | 93 |

### A.4 The 27 organiser-flagged examples that could not be matched to a parsed entry

| Submission | Group | Flagged title (truncated) | Title words in PDF | Closest parsed entry status | Verdict |
|--:|:--|:--|--:|:--|:--|
| 344 | Accepted | Finding challenging metaphors that confuse pretrained language models | 0.57 | VERIFIED | title not in PDF: checker artefact |
| 340 | Accepted | Phenylpropanoids: A comprehensive review on their occurrence, biosynth | 0.71 | VERIFIED | closest parsed entry real |
| 333 | Accepted | A comprehensive review of computational methods for predicting adme–to | 1.00 | VERIFIED | closest parsed entry real |
| 333 | Accepted | A review of computational methods for predicting adme properties of dr | 1.00 | VERIFIED | closest parsed entry real |
| 300 | Accepted | Beyond decontextualized sentences: What can ERPs tell us about pragmat | 0.40 | VERIFIED | title not in PDF: checker artefact |
| 295 | Accepted | Machine learning-assisted screening of corrosion-resistant materials | 0.71 | VERIFIED | closest parsed entry real |
| 293 | Accepted | The “Third Quarter Phenomenon”: A Qualitative and Quantitative Analysi | 0.80 | VERIFIED | closest parsed entry real |
| 293 | Accepted | The Hawai’i Space Exploration Analog and Simulation (HI-SEAS) Program | 1.00 | VERIFIED | closest parsed entry real |
| 287 | Accepted | Gut microbiome changes in colorectal cancer patients receiving chemoth | 1.00 | VERIFIED | closest parsed entry real |
| 287 | Accepted | Disproportionality methods for pharmacovigilance in spontaneous report | 1.00 | VERIFIED | closest parsed entry real |
| 220 | Accepted | Complementary team performance: A theory-driven approach to human-ai c | 1.00 | VERIFIED | closest parsed entry real |
| 212 | Accepted | The impact of innovative pedagogies on critical thinking and self-regu | 0.89 | VERIFIED | closest parsed entry real |
| 207 | Accepted | Rivet: The open-source visual AI programming environment | 0.75 | VERIFIED | closest parsed entry real |
| 200 | Accepted | LLM-Rubric: Using large language models to automate evaluation rubrics | 1.00 | VERIFIED | closest parsed entry real |
| 200 | Accepted | Semantic similarity metrics for evaluating large language models | 1.00 | VERIFIED | closest parsed entry real |
| 152 | Accepted | Extreme ultraviolet imaging telescope: A primary driver of climate | 0.29 | EXISTS | title not in PDF: checker artefact |
| 151 | Accepted | Llama Guard 3: Safeguarding conversational AI | 0.00 | none | title not in PDF: checker artefact |
| 135 | Accepted | Do large language models show decision-making behavior consistent with | 1.00 | VERIFIED | closest parsed entry real |
| 96 | Accepted | Designing the future of materials science: a roadmap for harnessing th | 0.25 | VERIFIED | title not in PDF: checker artefact |
| 77 | Accepted | Crowding in Human Vision: The Effect of Non-target Objects on the Reco | 0.71 | VERIFIED | closest parsed entry real |
| 77 | Accepted | Medieval Handwriting Recognition with Deep Learning: A New Model for D | 0.50 | VERIFIED | title not in PDF: checker artefact |
| 331 | Rejected | The self-limiting nature of QBO-dependent SAI: An optimization agent’s | 1.00 | UNVERIFIED | indeterminate |
| 302 | Rejected | A Critical Review of Approaches to Understanding the Trolley Problem | 1.00 | EXISTS | closest parsed entry real |
| 302 | Rejected | AI Ethics Related Article | 1.00 | EXISTS | closest parsed entry real |
| 276 | Rejected | AGI Review | 1.00 | none | indeterminate |
| 244 | Rejected | Structured Pruning of Transformer Models | 1.00 | UNVERIFIED | indeterminate |
| 57 | Rejected | (No Title) | 0.00 | none | title not in PDF: checker artefact |

### A.5 Search-channel analysis of NOT_FOUND decisions

- Evidence channel of all decisions: other-page 291, search-note 171, doi 146, arxiv 137, none 67, yahoo 26, openlibrary 9, pubmed 7, google 1, wayback 1, crossref 1
- Evidence channel of NOT_FOUND decisions: search-note 171, other-page 108, doi 5, arxiv 2
- Adjudication-order tercile 1: NOT_FOUND 114/279 = 40.9% of adjudicable decisions; channels: other-page 109, search-note 99, arxiv 42, doi 22
- Adjudication-order tercile 2: NOT_FOUND 83/260 = 31.9% of adjudicable decisions; channels: other-page 70, search-note 60, doi 55, arxiv 45
- Adjudication-order tercile 3: NOT_FOUND 89/267 = 33.3% of adjudicable decisions; channels: other-page 112, doi 69, arxiv 50, none 21
- Blind agreement on sampled NOT_FOUND decisions by evidence channel (agree/total): other-page 14/16, search-note 12/14

### A.6 Manual inspection of low-ratio reference lists

The 16 reference lists (15 author-year or numbered lists and one three-entry bracket list, submission 274) whose parsed-entry count fell below 0.8 of the year-token count were inspected by reading the reference section of the PDF and counting entry starts. Year tokens over-count entries because DOIs, URLs and date ranges contain years; once DOI and URL strings are removed, the token count is close to the entry count for complete lists.

| Submission | Parsed entries (before inspection) | Entries counted on inspection | Outcome |
|--:|--:|--:|:--|
| 54 | 10 | 10 | complete (DOIs inflate year tokens) |
| 78 | 17 | 17 | complete |
| 89 | 4 | 4 | complete |
| 127 | 23 | 23 | complete |
| 137 | 26 | 26 formatted entries plus the raw LaTeX bibliography source printed in the PDF | complete; source lines are not references |
| 173 | 20 | 20 | complete (appendix text follows the list) |
| 174 | 12 | 14 | 2 references merged by the parser; re-parsed with the author-pattern segmentation (14) |
| 214 | 23 | 23 | complete |
| 216 | 20 | 20 | complete (appendix text follows the list) |
| 237 | 25 | 25 | complete (appendix tables follow the list) |
| 273 | 1 | 3 | 2 references lost because the section-end heading was not recognised; re-parsed (3) |
| 274 | 2 | 3 | 1 reference missed in a three-entry bracket list; not recovered |
| 287 | 39 | 39 | complete |
| 289 | 23 | 23 | complete |
| 316 | 14 | 14 | complete |
| 329 | 6 | 6 | complete (appendix text follows the list) |

Of 16 inspected lists, 13 were complete and 3 had omissions totalling 5 references, of which 4 were recovered by re-parsing; 1 remains missing (submission 274).

**Random sample of lists that pass the diagnostics.** Sampling frame and timing: the low-ratio set above was determined before the last two parser repairs (section-end headings, author-pattern segmentation), which is why it includes submission 273; the random sample below was drawn after those repairs, from the 69 author-year and 14 numbered lists (83 in all) as they stood at that time, 15 of which were drawn with seed 20261004 (code/qa_recall_authoryear.py output data/dataset/qa_recall_authoryear.json). Submission 273 therefore appears in both sets: it was a low-ratio list before repair and a passing list after it. To check that omissions are not confined to low-ratio lists, the 15 sampled lists were inspected in the same way. One list (submission 219, a numbered list of placeholder stubs without a recognised heading) could not be assessed. Of the other 14, 13 were complete (submissions 185, 248, 195, 308, 240, 273, 268, 117, 115, 310, 303, 200, 91; in several the entry-start count exceeded the parsed count only because appendix headings or continuation lines in two-column text were counted as starts) and one (submission 124) had one entry missing, the placeholder stub "Coyne, M., et al. (2017). Reading interventions...", which the parser dropped. One missing reference in 14 assessable lists suggests an omission rate of roughly one reference per fourteen non-bracket lists, or about six references across the 83 non-bracket lists, with wide uncertainty.

### A.7 Human coding of 64 items by the author (a disclosed, non-independent, attestation-blinded check): agreement with the agent labels

- Human vs first adjudicator (or automated VERIFIED), all (n=64): categories 43.8% agreement (kappa 0.21); fabricated-vs-not 57.8% (kappa 0.18)
- Human vs first adjudicator (or automated VERIFIED), manual (both strata) (n=35): categories 48.6% agreement (kappa 0.20); fabricated-vs-not 74.3% (kappa -0.15)
- Human vs first adjudicator (or automated VERIFIED), manual-disputed (n=25): categories 36.0% agreement (kappa 0.04); fabricated-vs-not 64.0% (kappa -0.22)
- Human vs first adjudicator (or automated VERIFIED), manual-agreed (n=10): categories 80.0% agreement (kappa 0.60); fabricated-vs-not 100.0% (kappa nan)
- Human vs first adjudicator (or automated VERIFIED), automated (both strata) (n=29): categories 37.9% agreement (kappa 0.00); fabricated-vs-not 37.9% (kappa 0.00)
- Human vs first adjudicator (or automated VERIFIED), auto-disputed (n=19): categories 5.3% agreement (kappa 0.00); fabricated-vs-not 5.3% (kappa 0.00)
- Human vs first adjudicator (or automated VERIFIED), auto-agreed (n=10): categories 100.0% agreement (kappa nan); fabricated-vs-not 100.0% (kappa nan)
- Human vs blind agent, all (n=64): categories 73.4% agreement (kappa 0.60); fabricated-vs-not 90.6% (kappa 0.75)
- Human vs blind agent, manual (both strata) (n=35): categories 60.0% agreement (kappa 0.37); fabricated-vs-not 85.7% (kappa 0.47)
- Human vs blind agent, manual-disputed (n=25): categories 52.0% agreement (kappa 0.30); fabricated-vs-not 80.0% (kappa 0.43)
- Human vs blind agent, manual-agreed (n=10): categories 80.0% agreement (kappa 0.60); fabricated-vs-not 100.0% (kappa nan)
- Human vs blind agent, automated (both strata) (n=29): categories 89.7% agreement (kappa 0.82); fabricated-vs-not 96.6% (kappa 0.93)
- Human vs blind agent, auto-disputed (n=19): categories 84.2% agreement (kappa 0.50); fabricated-vs-not 94.7% (kappa 0.00)
- Human vs blind agent, auto-agreed (n=10): categories 100.0% agreement (kappa nan); fabricated-vs-not 100.0% (kappa nan)
- On the 25 manual decisions where the agents disagreed, the human agreed with the first adjudicator in 9, with the blind agent in 13, with neither in 3
- On the 19 automated matches that the blind agent called corrupted or invented, the human confirmed the blind agent in 16, called the entry correctly cited in 1, other 2

### A.8 Independent human coding of the random sample of manual decisions (sheet B) and of the 64-item sheet (sheet A): agreement and sensitivity bound

Sheet A: 0 of 64 items coded
Sheet B: 45 of 45 items coded
- Coder vs first adjudicator, all coded items (n=45): categories 75.6% agreement (95% CI 61.3-85.8; kappa 0.63, bootstrap 95% CI 0.42-0.81); fabricated-vs-not 97.8% (88.4-99.6; kappa 0.94, 0.78-1.00)
  - first adjudicator NOT_FOUND (n=20): coder said NOT_FOUND 14, EXISTS_CORRUPTED 6
  - first adjudicator EXISTS_CORRUPTED (n=14): coder said EXISTS_CORRUPTED 10, NOT_FOUND 4
  - first adjudicator EXISTS (n=9): coder said EXISTS 8, EXISTS_CORRUPTED 1
  - first adjudicator PLACEHOLDER (n=1): coder said PLACEHOLDER 1
  - first adjudicator UNADJUDICABLE (n=1): coder said UNADJUDICABLE 1
- Coder vs blind agent (items that were also blind re-adjudicated) (n=11): categories 81.8% agreement (95% CI 52.3-94.9; kappa 0.72, bootstrap 95% CI 0.32-1.00); fabricated-vs-not 90.9% (62.3-98.4; kappa 0.81, 0.42-1.00)
- The author's 64-item sheet and sheet B share no item, so no comparison with the author's coding is possible on sheet B

**Sensitivity of the detected figures to the independent coder's labels (4000 simulations, seed 1)**
Each manual decision is relabelled independently with the coder's label distribution given the first adjudicator's state, estimated from sheet B (Dirichlet posterior, Jeffreys prior): first NF: coder NF 14, EC 6, OTHER 0; first EC: coder NF 4, EC 10, OTHER 0; first OTHER: coder NF 0, EC 1, OTHER 10. Automatically verified entries are unchanged; denominators are the detected analysis's. Median and 95% interval of the relabelled value against the detected value.

| Quantity | Detected | Under the coder's labels (median, 95% interval) |
|:--|--:|--:|
| Detected fabricated references (all submissions) | 513 | 549 (493-638) |
| Detected invented references | 286 | 271 (192-361) |
| Reviewed submissions with >=1 fabricated reference (%) | 37.8 | 45.2 (38.6-56.0) |
| Reviewed submissions with >=1 invented reference (%) | 23.7 | 29.0 (22.8-39.8) |
| Reviewed references fabricated (%) | 7.2 | 7.7 (6.9-8.9) |
| Reviewed references invented (%) | 3.8 | 3.7 (2.6-5.0) |
| Organiser flag, paper-level sensitivity | 0.93 | 0.83 (0.74-0.92) |
| Organiser flag, paper-level specificity | 0.66 | 0.66 (0.63-0.69) |
| Organiser flag, paper-level kappa | 0.54 | 0.49 (0.39-0.55) |
| Flagged examples fabricated (%, precision) | 51.9 | 51.9 (47.3-55.0) |
| Spearman rho, fabricated share vs LLM reviewer 1 score | -0.15 | -0.14 (-0.19--0.09) |
| Spearman rho, fabricated share vs LLM reviewer 2 score | -0.13 | -0.12 (-0.16--0.07) |
| Spearman rho, fabricated share vs LLM reviewer 3 score | -0.13 | -0.11 (-0.15--0.06) |
| Spearman rho, invented share vs LLM reviewer 1 score | -0.20 | -0.15 (-0.21--0.08) |
| Spearman rho, invented share vs LLM reviewer 2 score | -0.18 | -0.14 (-0.20--0.07) |
| Spearman rho, invented share vs LLM reviewer 3 score | -0.18 | -0.13 (-0.19--0.06) |
| Spearman rho, fabricated share vs human expert score | -0.28 | -0.23 (-0.32--0.12) |
| Spearman rho, invented share vs human expert score | -0.41 | -0.29 (-0.44--0.11) |
| Accepted papers with >=1 invented reference | 0 | 4 (0-13) |
| Accepted papers with >10% fabricated references | 0 | 1 (0-5) |
