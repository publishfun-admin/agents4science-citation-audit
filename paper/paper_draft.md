# [TITLE TBD] Fabricated references in AI-first-authored research: a manually verified audit of all Agents4Science 2025 submissions

> Draft skeleton written before results were available. Sections marked [RESULTS] are filled from data/dataset outputs.

## Abstract

[RESULTS]

## 1. Introduction

Agents4Science 2025, organised by Stanford University and Together AI and held on 22 October 2025, was the first
research conference that required an AI system to be the first author of every submission, reviewed every complete
submission with three large-language-model (LLM) reviewers, and released all submissions, reviews and checklists
publicly [Bianchi et al. 2025]. It is therefore the first corpus in which the reference lists of hundreds of
AI-first-authored papers can be inspected together with the AI reviews they received, the human expert reviews given to
the top-scoring papers, per-paper self-reports of how much of the writing was done by AI, and the acceptance decision.

Fabricated references are the most verifiable symptom of LLM involvement in scientific writing, and they are
spreading through the human-authored literature: an audit of 111 million references found a sharp rise in non-existent
citations after 2023, with a conservative estimate of 146,932 hallucinated citations in 2025 alone [Zhao et al. 2026];
a Lancet audit of 2.5 million biomedical papers found a fabricated citation in one of every 277 papers indexed in early
2026 [Topaz et al. 2026]; and 53 papers accepted at NeurIPS 2025 contained AI-generated citations to sources that do not
exist [Ansari 2026]. What happens when the author is, by design, an AI?

The organisers of Agents4Science asked this question with an automated checker: for every reference in every submission
it extracted the title, ran a web search, and, if nothing matched, flagged the reference as a potential hallucination and
posted a public "Related Work Check" comment listing example flagged references. They estimated that roughly 44% of
submissions had no flagged references and 56% had at least one [Bianchi et al. 2025]. That estimate has three known
weaknesses, which the organisers themselves acknowledge in the wording of the public comments ("they might exist but the
automated verification failed"): a failed web search is not evidence of non-existence, the flag does not distinguish a
wholly invented work from a real work cited with a wrong year or author, and it was never related to the review scores
or to acceptance.

This paper re-examines every reference in every Agents4Science submission with a reproducible pipeline followed by
manual adjudication, and asks five questions that were fixed before adjudication started (paper/analysis_plan.md in the
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
placeholder and semantic hallucination) that our adjudication categories adapt.

**Citation generation and verification tools.** Rao and colleagues [2026] show that even search-enabled frontier
models produce fully correct BibTeX entries only about half of the time, with accuracy dropping sharply for recent
papers; Reizinger and colleagues [2026] (HALLMARK) benchmark rule- and LLM-based citation verifiers and find that the
false-positive rate, not recall, decides whether a verifier is deployable. Both results bear directly on the
organisers' checker: an automated flag can be wrong in both directions, which is why we adjudicate by hand.

**AI reviewers.** LLM reviewers are now deployed at scale [Biswas et al. 2026] and studied adversarially: Jiang et al.
[2025] (BadScientist, itself an Agents4Science paper) show that fabrication-oriented paper generators can obtain
acceptance-level scores from multi-model LLM review systems, and identify a "concern-acceptance conflict" in which
reviewers flag integrity problems yet still recommend acceptance; Baumann et al. [2026] document a hivemind effect and
gameability of LLM review scores; Nguyen et al. [2026] measure how often agentic review systems catch injected errors.
None of these works examines whether LLM reviewers notice fabricated references in a real venue, which our Q5 does.

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
| Desk-rejected |            61 |         60 |               0 |              0 |          3 |            1 |            3 |
| Total         |           315 |        314 |             250 |             79 |        253 |          139 |          256 |

**Reviewer identities.** The organisers' report gives the mean overall score of each LLM reviewer (GPT-5 2.30, Gemini
2.5 Pro 4.23, Claude Sonnet 4 3.0); the three anonymised reviewer slots in the data have means of 2.30, 4.24 and 3.00 over all
250 reviewed submissions (2.31, 4.30 and 3.02 over the 244 accepted or rejected ones), which identifies AIRev1 as GPT-5, AIRev2 as Gemini 2.5 Pro and AIRev3 as Claude Sonnet 4.

## 4. Methods

**Reference extraction.** Reference lists were extracted from the PDFs with AnyStyle 1.6 (a conditional-random-field
reference parser); when it found no reference section, a heuristic segmenter located the section and AnyStyle parsed
the raw strings. Entries without a year and author, or whose title is a table or figure caption, were tagged as parse
artefacts and excluded.

**Automated verification.** Each entry was checked in order against (1) its DOI via Crossref and its arXiv identifier via
the arXiv API, accepting the entry when the resolved title is contained in the entry text; (2) Crossref's bibliographic
query, OpenAlex, DBLP and arXiv title search, accepting a candidate when its title agrees with the parsed title (fuzzy
ratio >= 92, or >= 85 with matching year and first author) and the cited year is within one year; (3) Semantic Scholar,
Crossref title queries, OpenLibrary and Google Books in a second pass; (4) for entries citing only a URL, whether the
URL is live. All API responses are cached and released with the code, so the automated stage is exactly reproducible.

**Manual adjudication.** Every entry that remained unverified was adjudicated by the author's AI agent under the written
protocol in data/adjudication/PROTOCOL.md: exact-title web search, then author-plus-keywords search, with the evidence
URL logged for every decision. Categories: EXISTS (a real work; automated recall failure), EXISTS_CORRUPTED (a real
work cited with a substantively wrong author, year, venue, identifier or title), NOT_FOUND (no trace of the work),
WEB_RESOURCE, and UNADJUDICABLE (excluded). Fabricated = NOT_FOUND or EXISTS_CORRUPTED.

**Analysis.** All analyses were pre-specified (paper/analysis_plan.md in the repository) before any manual
adjudication. Proportions are reported with 95% Wilson intervals. The organisers' flag is evaluated at the reference
level (share of their flagged example references that adjudication classifies as fabricated) and at the paper level
(sensitivity, specificity and Cohen's kappa of "at least one flagged example" against "at least one fabricated
reference"). Associations between a paper's fabricated share and its self-reported writing autonomy tier use the
Kruskal-Wallis test, and associations with the overall autonomy score and with each reviewer's overall score use
Spearman's rank correlation. Acceptance is modelled with a logistic regression on the fabricated share and the mean
LLM score. Reviewer detection is measured as the share of papers with at least one fabricated reference in which at
least one LLM review, the human review, or the organisers' Correctness Check states explicitly that references are
fabricated, non-existent, future-dated or unverifiable; candidate sentences were found with a keyword pattern and
each was read and classified by the adjudicating agent as an independent assertion, an echo of the authors' own
disclosure, a vague remark, or unrelated (data/dataset/strong_ref_statements_classified.csv). Because every reference
in every submission is adjudicated, no sampling is involved and no multiple-comparison correction is applied to the
six pre-specified questions; p-values are reported as descriptive evidence rather than as confirmatory tests.

## 5. Results

[RESULTS]

## 6. Discussion

[RESULTS]

## 7. Limitations

[to be completed with the results; includes: NOT_FOUND is evidence of absence from indexes and the web, not proof of
non-existence; parser recall; adjudication by an AI agent with logged evidence rather than by two independent humans;
self-reported autonomy tiers; the corpus is one venue and one moment in time.]

## AI-use disclosure

This study was designed, executed and written by an AI agent (Claude, Anthropic) operated by the author, who set the
research goal, provided access and approved the design decisions. The agent wrote all code, ran the pipeline, performed
the manual adjudications with web search under the written protocol, and drafted the manuscript; every adjudication is
logged with its evidence URL so that readers can re-check it. The author is responsible for the content.

## Competing interests

The author operates Publish.fun, the venue of publication; the automated review pipeline was not modified for this
submission. The author has no relationship with Agents4Science or its organisers.

## Data and code availability

[repository URL - to be added]

## References

[to be generated from paper/related_arxiv.json + Crossref records]
