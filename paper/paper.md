# Fabricated references in AI-first-authored research: a manually verified audit of all Agents4Science 2025 submissions

<!-- keywords: fabricated citations, hallucinated references, AI-generated research, Agents4Science, LLM peer review, research integrity, citation audit -->

## Abstract

Agents4Science 2025 was the first conference to require an AI system as the first author of every submission and to review every complete submission with three large-language-model (LLM) reviewers. Its organisers' automated reference check reported that 56% of submissions contained at least one reference that could not be verified. We re-examined all 6,685 references in the 304 submissions with a parsable reference list, using a reproducible verification pipeline (DOI, arXiv and URL resolution; Crossref, OpenAlex, Semantic Scholar, OpenLibrary and Google Books) followed by manual adjudication of every reference it could not verify (821 decisions, each with logged evidence) under a protocol fixed before adjudication began. Among the 241 reviewed submissions with references, 36.9% (95% CI 31.1–43.2) contained at least one fabricated reference (a non-existent work, or a real work cited with a corrupted title, author list, venue, year or identifier) and 7.1% of their 5,090 references were fabricated; 14 submissions had fabricated majorities. Accepted papers were almost clean: none of their 1,251 references was wholly invented, and 8 corrupted references were spread over 7 of 48 papers. The organisers' flag was a useful screen but a poor measure: only 51.8% of the example references it flagged were fabricated, its paper-level specificity was 0.66 (sensitivity 0.94), and none of the 25 flagged examples in accepted papers was fabricated. Fabrication was associated with lower scores from all three LLM reviewers (Spearman rho between -0.13 and -0.16), with lower human expert scores (rho = -0.31) and with rejection: no paper with more than 10% fabricated references was accepted, and the fabricated share predicted acceptance beyond the mean LLM score. Yet reviewers rarely said so: an LLM review asserted on its own that references were fabricated in 4 of the 89 affected papers (all four by Gemini 2.5 Pro), and no human expert review did. Self-reported AI autonomy in writing did not predict fabrication monotonically. Of the 496 fabricated references, 57% were wholly invented and 43% were real works with corrupted attributes; 29 non-existent references carried a DOI or an arXiv identifier that resolves to an unrelated work or to nothing, and one submission's invented references were carried unchanged into its later arXiv preprint. All code, cached API responses and adjudication logs are released.

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
adjudication replacing the final automated step.

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
10 withdrawn and 61 desk-rejected. For each we retrieved the submitted PDF (314; one is password-protected), the
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
250 reviewed submissions (2.31, 4.30 and 3.02 over the 244 accepted or rejected ones), which identifies AIRev1 as GPT-5, AIRev2 as Gemini 2.5 Pro and AIRev3 as Claude Sonnet 4.

## 4. Methods

**Reference extraction.** Reference lists were extracted from the PDFs with AnyStyle 1.6 (a conditional-random-field
reference parser) applied to pdftotext output. Three layout problems were handled before parsing: margin line numbers
from the review template were stripped when at least a quarter of the lines began with a running number; two-column
papers, detected when at least 30% of lines contained a wide internal gap (the layout-preserving text of such papers
interleaves the two columns), were re-extracted in reading order; and bracket-numbered lists in which the parser had
dropped entries were segmented at the bracket markers and parsed entry by entry. Entries without a year and author, or
consisting of body text, captions or affiliation blocks, were tagged as parse artefacts and excluded; artefacts that
survived this filter were classified as UNADJUDICABLE during adjudication.

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

**Analysis.** All analyses were pre-specified (paper/analysis_plan.md in the repository) before any manual
adjudication. Proportions are reported with 95% Wilson intervals. The organisers' flag is evaluated at the reference
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
six pre-specified questions; p-values are reported as descriptive evidence rather than as confirmatory tests.

## 5. Results

### 5.1 Corpus and parsing yield

Of the 314 PDFs, three could not be read (one is password-protected and two are image-only scans; all three were
desk-rejected) and seven contain no reference list at all (two of them state that the bibliography is "available in
supplementary materials"; two, submissions 159 and 188, were reviewed papers). The remaining 304 submissions yielded
6,685 reference entries after parse artefacts were excluded. Adjudication set aside 43 entries as UNADJUDICABLE
(fragments of split entries, and grey literature that could not be located either way), leaving 6,642 adjudicable
references in 302 submissions (two submissions consisted only of unadjudicable entries). For the 218 submissions with
bracket-numbered lists, the ratio of parsed entries to the highest bracket marker had a median of 1.00 and a minimum of
0.88 (two submissions below 0.90), so the denominators are close to complete. Accepted papers cite more: a median of 24
references (interquartile range 16-33) against 15 (10-24) for rejected, 14 (9-21) for desk-rejected and 41 (29-72) for
the ten withdrawn submissions.

The automated stage verified 5,864 entries (87.7%). Crossref bibliographic matching accounted for about two thirds of
the automated matches, Semantic Scholar for a sixth, direct DOI resolution for 8%, arXiv identifiers for 4%, live URLs
for 1.5%, and Crossref title queries, OpenLibrary and arXiv search for the remainder. The 821 entries that were
adjudicated by hand (every entry unverified at the end of the automated stage; a handful were also matched by the later
arXiv re-pass and are counted by their manual category) split into 254 EXISTS (30.9%), 281 NOT_FOUND (34.2%), 215
EXISTS_CORRUPTED (26.2%), 28 PLACEHOLDER (3.4%) and 43 UNADJUDICABLE (5.2%). In other words, about one third of the
references that the automated stage could not verify were real works cited correctly (theses, books, standards,
reports, software and web pages predominate), which is the first reason that a failed automated lookup cannot be
equated with fabrication.

### 5.2 Prevalence of fabricated references (Q1)

Among the 241 reviewed submissions (accepted or rejected) with adjudicable references, 89 (36.9%; 95% CI 31.1-43.2)
cite at least one fabricated reference, and 361 of their 5,090 references (7.1%; 6.4-7.8) are fabricated. Restricting
the outcome to wholly invented works (NOT_FOUND only) gives 57 submissions (23.7%; 18.7-29.4) and 194 references
(3.8%); adding placeholders ("defective") changes little: 90 submissions (37.3%) and 363 references (7.1%). Over all
302 submissions with adjudicable references the paper-level share is 37.4% (113/302; 32.1-43.0) and the reference-level
share 7.5% (496/6,642; 6.9-8.1).

**Table 2. Prevalence by outcome group.** Fabricated = NOT_FOUND or EXISTS_CORRUPTED. Percentages in the last two
columns are shares of submissions with 95% Wilson intervals.

| Outcome group | Submissions | References | Fabricated references | Submissions with >= 1 fabricated reference | Submissions with >= 1 wholly invented reference |
|:--|--:|--:|--:|:--|:--|
| Accepted | 48 | 1,251 | 8 (0.6%) | 7 (14.6%; 7.2-27.2) | 0 (0.0%; 0.0-7.4) |
| Rejected | 193 | 3,839 | 353 (9.2%) | 82 (42.5%; 35.7-49.5) | 57 (29.5%; 23.5-36.3) |
| Withdrawn | 10 | 531 | 11 (2.1%) | 3 (30.0%; 10.8-60.3) | 1 (10.0%; 1.8-40.4) |
| Desk-rejected | 51 | 1,021 | 124 (12.1%) | 21 (41.2%; 28.8-54.8) | 15 (29.4%; 18.7-43.0) |
| All | 302 | 6,642 | 496 (7.5%) | 113 (37.4%; 32.1-43.0) | 73 (24.2%; 19.7-29.3) |

The distribution is heavy-tailed. Among the 89 affected reviewed submissions the median fabricated share is 16.7%
(interquartile range 9.1-37.5%); 14 of the 302 submissions (4.6%) have fabricated majorities, all of them rejected or
desk-rejected: for example submission 112 (21 of 25 references fabricated, 19 of them non-existent), 243 and 110 (9 of
11 each), 28 (28 of 39; desk-rejected) and 148 (21 of 39). At the other end, the accepted papers are almost clean: none
of their 1,251 references is wholly invented (0 of 48 papers; upper confidence limit 7.4%), and the 8 fabricated
references are corrupted citations of real works (one each in six papers, two in one paper), typically a real paper
cited with a rewritten title or a wrong venue.

### 5.3 How precise was the organisers' automated flag? (Q2)

The organisers posted a Related Work Check on 253 submissions and listed 285 example references, in 139 submissions,
that their web-search checker could not verify. We matched 257 of the examples (90.2%) to a parsed entry. The 28
unmatched examples, 23 of them in accepted papers, are strings that the checker's own extraction step produced: for
several of them the flagged title does not occur anywhere in the submitted PDF, and for others the checker's rendering
of the title differs from the entry in the reference list, which in the cases we could trace is a real work. Table 3
gives the adjudicated status of the matched examples.

**Table 3. Adjudicated status of the 257 example references flagged by the organisers' Related Work Check.**
"Verified automatically" means matched to a bibliographic record or a resolving identifier by our pipeline; "exists
(manual)" means confirmed by hand.

| Status of flagged example | n | Share |
|:--|--:|--:|
| NOT_FOUND (wholly invented) | 80 | 31.1% |
| EXISTS_CORRUPTED (real work, corrupted attributes) | 53 | 20.6% |
| Verified automatically (record or identifier) | 102 | 39.7% |
| Exists (manual: theses, reports, web resources) | 17 | 6.6% |
| PLACEHOLDER | 2 | 0.8% |
| UNADJUDICABLE | 3 | 1.2% |

The precision of the flag at the reference level is therefore 51.8% (133/257; 95% CI 45.7-57.8): 46.3% (119/257;
40.3-52.4) of the flagged examples exist exactly as cited. The false positives are not obscure: they include Spearman's
"The abilities of man" (1927), Thurstone's "Primary mental abilities" (1938), Oster, Perelson and Katchalsky's "Network
thermodynamics" (1973), Brown-Cohen et al.'s "Doubly-efficient debate" and a report of the White House Council of
Economic Advisers. Precision depends strongly on the outcome group: 58.2% (131/225; 51.7-64.5) in
rejected submissions, but 0 of 25 (0.0-13.3) in accepted ones, where 24 of the 25 flagged examples are real works
(the remaining one, the RDKit software cited without authors or year, was set aside as unadjudicable). No flagged
example in an accepted paper was fabricated.

At the paper level, among the 237 reviewed submissions that received a check and have adjudicable references, the
organisers' flag ("at least one example flagged") marked 133 (56.1%; 49.8-62.3), whereas the audit finds at least one
fabricated reference in 87 (36.7%; 30.8-43.0). The cross-classification gives 82 true positives, 51 false positives, 5
false negatives and 99 true negatives: sensitivity 0.94, specificity 0.66, positive predictive value 61.7% (53.2-69.5),
negative predictive value 95.2% (89.2-97.9), Cohen's kappa 0.54. Among the 48 accepted papers, 26 were flagged, of which
5 contain a single corrupted reference and 21 contain none; 2 unflagged accepted papers contain one corrupted reference
each. The flag is thus a good screen (a submission without a flag almost never has a fabricated reference) but a poor
measure: the "56%" headline overstates the paper-level prevalence by about half, and at the reference level roughly one
flagged reference in two is real.

### 5.4 Fabrication and self-reported AI autonomy (Q3)

**Table 4. Fabrication by self-reported AI autonomy in the writing stage (reviewed submissions with a checklist answer, n = 231).**

| Writing tier | Submissions | Mean fabricated share | Submissions with >= 1 fabricated reference |
|:--|--:|--:|:--|
| A: human-generated | 4 | 17.7% | 4 (100%; 51.0-100) |
| B: mostly human, assisted by AI | 26 | 20.9% | 15 (57.7%; 38.9-74.5) |
| C: mostly AI, assisted by human | 75 | 3.7% | 19 (25.3%; 16.9-36.2) |
| D: AI-generated | 126 | 10.5% | 48 (38.1%; 30.1-46.8) |

The tiers differ (Kruskal-Wallis H = 19.1, p = 0.0003), but not monotonically: the lowest fabrication is in the
"mostly AI, assisted by human" tier and the highest in the two mostly-human tiers, which are small (30 submissions
together). The overall autonomy score (sum over the four stages, range 4-16) is uncorrelated with the fabricated share
(Spearman rho = -0.02, p = 0.78, n = 227). Ten reviewed submissions have no usable writing answer (3 of 8 with a missing
answer and 0 of 2 with an unparseable checklist contain a fabricated reference). Self-reported autonomy, at least as
extracted by the organisers' pipeline, is therefore not a predictor of reference integrity.

### 5.5 Fabrication, review scores and acceptance (Q4)

**Table 5. Association between a submission's fabricated share and its review scores and acceptance (reviewed submissions, n = 241 unless stated).**

| Outcome | Spearman rho (p) | Mean, submissions with >= 1 fabricated reference | Mean, submissions without |
|:--|:--|--:|--:|
| GPT-5 overall score (1-6) | -0.155 (0.016) | 2.22 | 2.38 |
| Gemini 2.5 Pro overall score | -0.136 (0.034) | 4.15 | 4.41 |
| Claude Sonnet 4 overall score | -0.133 (0.040) | 2.96 | 3.08 |
| Mean of the three LLM scores | -0.182 (0.005) | | |
| Human expert score (n = 78) | -0.312 (0.005) | 2.75 | 3.40 |
| Acceptance | | 7.9% (7/89; 3.9-15.4) | 27.0% (41/152; 20.5-34.5) |

All three LLM reviewers gave slightly lower scores to submissions with fabricated references, and the human experts,
who reviewed the 79 top-scoring submissions, markedly lower ones. Acceptance fell steeply with the fabricated share:
27.0% of submissions without a fabricated reference were accepted, 22.6% (7/31) of those with a share up to 10%, and
none of the 58 submissions with a share above 10% (0/25 at 10-25%, 0/21 at 25-50%, 0/12 above 50%). The pre-specified
logistic regression could be fitted: the fabricated share predicts acceptance beyond the mean LLM score (coefficient
-25.2, p = 0.002; mean LLM score 4.81, p < 1e-7; n = 241), and Fisher's exact test on "any fabricated reference" gives an
odds ratio for acceptance of 0.23 (p = 0.0002). Fabrication was therefore penalised somewhere between review and
decision, whether by the reviewers, by the human experts, or by the program chairs who had the organisers' flag in
front of them; the data cannot separate these mechanisms.

### 5.6 Did anyone notice? (Q5)

Among the 89 reviewed submissions with at least one fabricated reference, an LLM review contains an explicit statement
that references are fabricated, non-existent, future-dated or unverifiable in 6 (6.7%; 3.1-13.9). Reading the sentences,
in 4 submissions (4.5%; 1.8-11.0) the statement is the reviewer's own finding, for instance "the review identifies
fabricated references in the bibliography, which is a grave breach of academic ethics" (submission 110) or "the
literature review is deeply flawed, with hallucinated authors and future-dated references" (112); all four are by
Gemini 2.5 Pro (a fifth such finding by Gemini, in a withdrawn submission that had been reviewed, lies outside the
accepted-or-rejected set). In the other two (38 and 148) the reviewers only repeat the authors' own disclosure, in the
AI-limitations section of the checklist, that the bibliography may contain hallucinated references (Claude Sonnet 4 does
so in both, and GPT-5 and Gemini also in 148; in submission 21 Claude Sonnet 4 echoes the disclosure while Gemini
independently identifies a fabricated key reference). GPT-5 and Claude Sonnet 4 never asserted on their own that a
reviewed submission with fabricated references had them. Among the 152 reviewed submissions without a fabricated
reference, Gemini made an independent accusation in 3 (2.0%; 0.7-5.6) and Gemini and GPT-5 one vague remark each
("bibliographic issues undermine credibility"), so 4 of Gemini's 7 independent accusations (57.1%) in the reviewed set
concerned a submission that does have a fabricated reference. Reviews mention references or citations in some way in 70.8% of affected
submissions, but almost always generically ("the related work could be expanded"). None of the 20 affected submissions
that received a human expert review had the problem noted by the expert (0/20; 0.0-16.1), and the organisers'
Correctness Check comments contain one explicit statement about references, in a submission that has none.

### 5.7 What the fabrications look like (Q6)

**Table 6. Categories of the 821 manually adjudicated references, and corrupted attributes among the EXISTS_CORRUPTED entries (several attributes can be wrong in one entry).**

| Category | n | Share of adjudicated |
|:--|--:|--:|
| NOT_FOUND (wholly invented, incl. 2 dead URL-only citations) | 281 | 34.2% |
| EXISTS_CORRUPTED (real work, corrupted attributes) | 215 | 26.2% |
| EXISTS (real, correctly cited; automated recall failure, incl. 64 web resources) | 254 | 30.9% |
| PLACEHOLDER | 28 | 3.4% |
| UNADJUDICABLE | 43 | 5.2% |
| Corrupted attribute (n = 215): title | 161 | 74.9% |
| Corrupted attribute: venue | 100 | 46.5% |
| Corrupted attribute: authors | 88 | 40.9% |
| Corrupted attribute: year | 66 | 30.7% |
| Corrupted attribute: identifier (DOI or arXiv id) | 36 | 16.7% |

Of the 496 fabricated references, 281 (56.7%) are wholly invented and 215 (43.3%) are corruptions of real works. The
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
references in submission 187 share the same three authors.

Wholly invented references are usually plausible in form: real-sounding authors, a specific journal, volume, issue and
page range. Twenty-nine of the 281 (10.3%) carry a DOI or an arXiv identifier (12 a DOI, 18 an arXiv identifier, one both) and
another five cite only a URL; the identifiers either do not resolve or resolve to an unrelated work. The following
identifiers are quoted from the audited submissions as examples and are not sources of this paper: the
placeholder-pattern arXiv:2502.01234 (submission 148) resolves to an unrelated mathematics preprint on the Revuz
correspondence, arXiv:2401.12345 (173) to an unrelated preprint on distributionally robust receive combining,
doi:10.1177/01655515241234567 (148) is not registered with the DOI system, and submission 198 cites a page range of
12345-12358. Hijacked identifiers belong to unrelated real papers: a Developmental Dynamics DOI resolving to a zebrafish
review in 161, an Information Fusion DOI resolving to a neuroimaging review in 184, a Heliyon DOI resolving to a retracted
biodiesel paper in 71.
Seventeen of the 281 (6.0%) cite a year of 2025 or later. The 28 placeholders are concentrated in 7 submissions and
include "Authors. Title. arXiv preprint", venues given as "[Conference]", a "Journal of HCI for Health" with authors
"A. Smith, J. Doe", and an entry reading "(Duplicate of [7], listed for completeness)". Whole-list fabrication occurs:
in submissions 110, 111, 112 and 117 most references are invented, submission 160 cites ten non-existent glioma papers in
Neuro-Oncology, Nature Medicine and Clinical Cancer Research, and submission 127 cites veterinary papers with
unregistered DOIs. Finally, fabrications propagate: submission 147 cites at least five non-existent human-computer
interaction papers (two attributed to CHI 2024, two to the 2025 volume of Proceedings of the ACM on Human-Computer Interaction, one to NeurIPS 2025), and the same references
appear unchanged in the version of the paper that its authors posted to arXiv on 27 October 2025, five days after the
conference; at the time of writing the only web footprint of those titles is the paper itself.

## 6. Discussion

**What the audit adds to the organisers' figure.** The organisers reported, correctly, that their checker could not
verify at least one reference in 56% of submissions, and that figure has since been repeated as the hallucination rate
of the first AI-authored conference. Manual adjudication of every unverified reference shows that the true paper-level
prevalence among reviewed submissions is 36.9%, that half of the flagged example references are real (46.3% exist
exactly as cited), and that every flagged example in an accepted paper was a false alarm. The reasons are the ones the
citation-verification literature predicts [Reizinger and Brendel 2026; Rao and Callison-Burch 2026]: web search is a
poor oracle for books, theses, standards, software and pre-1990 papers, and a title-only check cannot tell a rewritten
title from an invented one. At the same time the flag's negative predictive value (95%) makes it a good screen. The
practical lesson for venues that deploy such checkers is to separate screening from measurement: resolve identifiers
and query bibliographic databases before searching the web, adjudicate the residue by hand before reporting a rate,
and publish per-reference verdicts so that authors can respond and readers can re-check.

**Prevalence.** A reference-level rate of 7.1% and a paper-level rate of 36.9% among reviewed AI-first-authored
submissions are one to two orders of magnitude above the rates measured in the human-authored literature, where
fabricated references are found in roughly 1% of AI/ML papers [Xu et al. 2026], in one biomedical paper in 277
[Topaz et al. 2026], and, under a strict identity-level definition, at reference-level rates below 1% in accepted
machine-learning and security papers, with about one accepted NeurIPS or USENIX Security 2025 paper in twenty carrying
two or more such references [Russinovich et al. 2026]. The comparison is not exact, because those audits rely on
automated detection and ours on exhaustive adjudication, but the gap is too large to be an artefact of method. The distribution matters as much as the
mean: most affected submissions have a few corrupted citations of real works, while a minority of 14 submissions have
reference lists that are mostly invented. The accepted papers, by contrast, contain no wholly invented reference in
1,251 and eight corrupted ones. Whatever the mechanism, the venue's process, three LLM reviews, human expert review of
the top-scoring papers, an automated reference flag and human program chairs, filtered wholesale fabrication out of the
accepted set, at a paper-level residual (7 of 48 papers with a corrupted citation) that is still an order of magnitude
above the roughly 1% of NeurIPS 2025 accepted papers in which fabricated citations have been found [Ansari 2026].

**Reviewers, scores and decisions.** Fabrication was penalised: all three LLM reviewers scored affected submissions
lower, human experts much lower, no submission with more than 10% fabricated references was accepted, and the fabricated
share carried information about acceptance beyond the mean LLM score. But the LLM reviewers almost never said why. An
independent, explicit statement that references were fabricated appears in 4 of 89 affected submissions, all by Gemini
2.5 Pro, and 3 of Gemini's 7 such accusations were directed at submissions in which the audit found no fabricated
reference. The lower
scores are therefore more plausibly a response to the general weaknesses that accompany fabricated bibliographies
(thin related work, overclaiming, missing rigour) than to the fabrication itself, which the reviewers, working without
retrieval, could not verify. This is the pattern that adversarial studies of LLM review predicted [Jiang et al. 2025;
Alharbi 2026]: an LLM reviewer without tools evaluates the text of a reference list, not its truth. Human experts,
reviewing only the top-scoring papers, never raised the issue in the 20 affected submissions they saw. The implication
for AI-reviewed venues is that reference verification must be a separate, tool-based step whose per-reference result is
given to the reviewers and to the authors, rather than something a reviewer is expected to notice.

**Self-reported autonomy.** The organisers observed that accepted papers reported more human involvement. Reference
integrity does not follow that gradient: the "mostly AI, assisted by human" tier had the lowest fabrication and the two
mostly-human tiers the highest, with the overall autonomy score uncorrelated with the fabricated share. The most likely
explanations are that the tiers are self-reported and machine-extracted, that teams who wrote the text themselves may
still have delegated the bibliography to a model, and that the human-led tiers are small. The organisers' own summary
of the authors' reported limitations, in which hallucinated references were the first theme, suggests that many teams
knew the risk; the 37% who submitted fabricated references either did not check or checked with tools that failed.

**Taxonomy.** Ansari's [2026] failure modes for citations that survived NeurIPS 2025 review all appear here, with a
different mix: total fabrication (57% of fabricated references) and attribute corruption (43%, dominated by rewritten
titles) account for almost everything, while identifier hijacking (29 invented references with a DOI or arXiv identifier, plus 36
corrupted entries with a wrong identifier) and placeholders (28 entries in 7 submissions) are rarer but diagnostic,
because a placeholder-pattern arXiv number or an unregistered DOI can be caught deterministically. Two features are
specific to a corpus written by agents: whole-list fabrication, in which an entire bibliography is invented in a
consistent style, and semantic inversion, in which a real paper is cited for the opposite of its finding. The
propagation of submission 147's invented references into a public arXiv preprint shows that rejection at one venue does
not keep fabricated references out of the record.

**A note on method.** This audit was itself performed by an AI agent, from pipeline to adjudication to manuscript, under
a human operator, and it exhibits the properties we recommend for automated checks: every automated step is cached and
reproducible, every manual decision is logged with its evidence, and the categories were fixed before the data were
seen. The references in this paper were verified by resolving each identifier before submission. Readers who find an
error in a decision are invited to report it against the released decision log.

## 7. Limitations

**Absence of evidence.** NOT_FOUND means that a reference could not be found in Crossref, OpenAlex, Semantic Scholar,
arXiv, OpenLibrary or PubMed, nor by two web searches; it is evidence of absence from the indexed record and the open
web, not proof that no such work exists. Grey literature, non-English and paywalled items can be missed, which is why
grey literature that could not be located either way was set aside as UNADJUDICABLE rather than counted, and why
EXISTS_CORRUPTED decisions name the real work that was evidently intended.

**Parser recall and precision.** Reference extraction from PDFs is imperfect: entries the parser missed are absent from
the denominators, and some references were fragmented or merged (the fragments are reported as UNADJUDICABLE). Recall
was checked against the bracket-marker counts of numbered reference lists (median ratio 1.00, minimum 0.88), and
two-column layouts were re-extracted in reading order after the first pass had garbled them. Three unreadable PDFs and
seven submissions without a reference list are excluded; all but two are desk-rejected submissions.

**One adjudicator.** Adjudication was performed by one AI agent following a written protocol with logged evidence,
not by two independent human coders, and some rules (for example, which title differences count as corruption)
involve judgement. Every decision, its category, its evidence URL and its note are released so that any of them can
be re-checked. The search channels changed during the audit (the agent's web-search tool, then Google, Brave and Yahoo
search pages, PubMed and Crossref) as usage limits and bot detection intervened; exact-phrase searches on some engines
have lower recall, which the mandatory second search by author and keywords was designed to offset.

**Identifier-based acceptance.** The automated stage accepts an entry when its DOI or arXiv identifier resolves to a
work whose title is contained in the entry; wrong authors or years in such entries are detected only when the entry
was also adjudicated manually, so the reported fabricated share is a lower bound for that class of corruption.

**Self-reported and machine-extracted covariates.** Autonomy tiers were self-reported by the submitting teams and
extracted by the organisers' LLM pipeline; review scores come from three LLM reviewers whose scales differ markedly;
the human expert scores exist only for the 79 top-scoring submissions, so the human-score correlation is estimated on a
selected sample.

**Observational associations.** The associations between fabrication, scores and acceptance are correlational; the
decision process of the conference is not observable at the level of individual decisions, and fabricated references
are likely to co-occur with other weaknesses that reviewers do detect.

**One venue, one moment.** The corpus is a single conference at a single time (the first AI-first-author venue,
September 2025); the submitting agents, prompts and human oversight were heterogeneous and largely undocumented, and
a few teams submitted near-duplicate papers, which are kept as separate submissions as the organisers kept them.

## AI-use disclosure

This study was designed, executed and written by an AI agent (Claude, Anthropic) operated by the author, who set the
research goal, provided access and approved the design decisions. The agent wrote all code, ran the pipeline, performed
the manual adjudications with web search under the written protocol, and drafted the manuscript; every adjudication is
logged with its evidence URL so that readers can re-check it. The author is responsible for the content.

## Competing interests

The author operates Publish.fun, the venue of publication; the automated review pipeline was not modified for this
submission. The author has no relationship with Agents4Science or its organisers.

## Data and code availability

All code, the cached API responses that make the automated stage reproducible, the parsed reference lists, the
adjudication protocol and the complete decision log (one row per adjudicated reference with category, evidence URL and
note), the merged dataset and the analysis outputs are available at
https://github.com/publishfun-admin/agents4science-citation-audit. The submissions, reviews and organiser comments are public on
OpenReview (venue Agents4Science 2025) and the conference data files are public at
https://agents4science.stanford.edu/data/; the repository records how they were retrieved.

## References

- [Alharbi 2026] Emad Alharbi. Do large language models scrutinise what they review? A multimodal audit of scoring calibration, error detection, and author-identity effects. arXiv:2608.28626 (2026).
- [Ansari 2026] Samar Ansari. Compound deception in elite peer review: A failure mode taxonomy of 100 fabricated citations at NeurIPS 2025. arXiv:2602.05930 (2026).
- [Baumann et al. 2026] Joachim Baumann, Jiaxin Pei, Sanmi Koyejo et al. Stop automating peer review without rigorous evaluation. arXiv:2605.03202 (2026).
- [Bianchi et al. 2025] Federico Bianchi, Owen Queen, Nitya Thakkar, Xian Sun and James Zou. Exploring the use of AI authors and reviewers at Agents4Science. Nature Biotechnology 44(1):11-14 (published online 17 December 2025), doi:10.1038/s41587-025-02963-8; arXiv:2511.15534.
- [Biswas et al. 2026] Joydeep Biswas, Sheila Schoepp, Gautham Vasan et al. AI-assisted peer review at scale: The AAAI-26 AI review pilot. arXiv:2604.13940 (2026).
- [Hatzel et al. 2026] Hans Ole Hatzel, Sebastian Steindl and Jan Strich. Review Arcade: On the human alignment and gameability of LLM reviews. arXiv:2605.28897 (2026).
- [Jiang et al. 2025] Fengqing Jiang, Yichen Feng, Yuetai Li et al. BadScientist: Can a research agent write convincing but unsound papers that fool LLM reviewers? arXiv:2510.18003 (2025).
- [Naddaf and Quill 2026] Miryam Naddaf and Elizabeth Quill. Hallucinated citations are polluting the scientific literature. What can be done? Nature 652:26-29 (1 April 2026), doi:10.1038/d41586-026-00969-z.
- [Naser 2026] M. Z. Naser. How LLMs cite and why it matters: A cross-model audit of reference fabrication in AI-assisted academic writing and methods to detect phantom citations. arXiv:2603.03299 (2026).
- [Nguyen et al. 2026] Dang Nguyen, Wanqing Hao, Yanai Elazar et al. Benchmarking agentic review systems. arXiv:2606.19749 (2026).
- [Rao and Callison-Burch 2026] Delip Rao and Chris Callison-Burch. BibTeX citation errors in scientific publishing agents: Evaluation and mitigation. arXiv:2604.03159 (2026; the first version, 3 April 2026, was titled "BibTeX citation hallucinations in scientific publishing agents: Evaluation and mitigation").
- [Russinovich et al. 2026] Mark Russinovich, Ram Shankar Siva Kumar and Ahmed Salem. Phantom references: Hallucinated citations that survive peer review at top-tier conferences. arXiv:2607.00738 (2026).
- [Reizinger and Brendel 2026] Patrik Reizinger and Wieland Brendel. HALLMARK: Diagnosing three failure modes in LLM citation verifiers. arXiv:2607.18360 (2026).
- [Topaz et al. 2026] Maxim Topaz, Nir Roguin, Pallavi Gupta, Zhihong Zhang and Laura-Maria Peltonen. Fabricated citations: an audit across 2.5 million biomedical papers. The Lancet 407(10541):1779-1781 (2026), doi:10.1016/S0140-6736(26)00603-3.
- [Xu et al. 2026] Zuyao Xu, Yuqi Qiu, Lu Sun et al. GhostCite: A large-scale analysis of citation validity in the age of large language models. arXiv:2602.06718 (2026).
- [Zhao et al. 2026] Zhenyue Zhao, Yihe Wang, Toby Stuart et al. LLM hallucinations in the wild: Large-scale evidence from non-existent citations. arXiv:2605.07723 (2026).
- [Zhu et al. 2025] Changjia Zhu, Junjie Xiong, Renkai Ma et al. When your reviewer is an LLM: Biases, divergence, and prompt injection risks in peer review. arXiv:2509.09912 (2025).
