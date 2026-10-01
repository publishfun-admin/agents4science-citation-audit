# Agents4Science 2025 citation audit

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23072623.svg)](https://doi.org/10.5281/zenodo.23072623)

Published paper: https://publish.fun/papers/PF-260930.000001 (Publish.fun, PF-260930.000001, 2026-09-30). Archived release: v1.1 on Zenodo, DOI 10.5281/zenodo.23072623 (concept DOI 10.5281/zenodo.23072622 resolves to the latest version); v1.0 is the version exactly as published.

Data, code and manuscript for *Fabricated references in AI-first-authored research: a manually verified audit of all
Agents4Science 2025 submissions* (Admin PublishFun, 2026). Everything the manuscript reports can be regenerated from
this repository without network access: the automated verification stage runs against cached API responses, and the
manual adjudication is a logged table of decisions.

## Layout

| Path | Contents |
|:--|:--|
| `code/` | Extraction, parsing, verification, adjudication tooling and the analysis scripts |
| `data/dataset/papers.csv` | One row per OpenReview submission (315): group, scores, decision, organiser check fields, self-reported autonomy |
| `data/refs/<number>_<forum_id>.verified.json` | The parsed reference list of each submission with the automated verdict, verification source (`via`) and identifiers per entry; `data/refs_v3/`, `data/refs_v4a/`, `data/refs_v4b/` are the earlier parses kept for provenance |
| `data/cache/` | Cached responses from Crossref, OpenAlex, Semantic Scholar, arXiv, OpenLibrary, Google Books and DOI/URL resolution |
| `data/adjudication/PROTOCOL.md` | The adjudication protocol, committed before the first decision (commit `18f47a4`) with its one amendment (`924d9f5`) |
| `data/adjudication/decisions.csv` | The 857 manual decisions: submission, entry index, category, evidence URL, note, adjudicator, date |
| `data/adjudication/retired_decisions.csv` | Decisions retired when a later parse changed the entry they were made for |
| `data/adjudication/organizer_flags.csv` | The organisers' flagged example references matched to parsed entries |
| `data/adjudication/blind/` | Blind re-adjudication samples and decisions (`blind_sample*.json`, `blind_decisions*.json`), the author's coded sheet (`human_coding_sheet.csv`), and the reference-strings-only sheets for an independent coder (see below) |
| `data/dataset/*.md`, `*.json` | Analysis outputs and validation reports (see the table below) |
| `data/a4s_site/` | Conference data files and how they were retrieved (`PROVENANCE.md`) |
| `paper/` | Manuscript (`paper.md`), results tables, analysis plan, response letters |

## Reproducing the manuscript's tables

Run from the repository root with Python 3.11 or later and `pandas numpy scipy unidecode rapidfuzz tabulate` installed.

| Command | Writes | Used for |
|:--|:--|:--|
| `python code/analysis.py` | `paper/results_tables.md`, `data/dataset/papers_final.csv` | Table 1b (flow), Q1 prevalence (Section 5.1, 5.2), Q2 flag metrics (5.3), Q3, Q4 (5.5), Q5 (5.6), sensitivity to PLACEHOLDER/UNADJUDICABLE; blind-agent labels for the adjustment |
| `BLIND_ESTIMATE=data/dataset/blind_autoverified_estimate_coder.json RESULTS_OUT=data/dataset/results_tables_coder_override.md python code/analysis.py` | `data/dataset/results_tables_coder_override.md` | Table 2b: the adjusted estimates anchored to the independent coder's labels (Q1b, Q1c) and the accepted-paper projection with and without the `other` stratum |
| `BLIND_ESTIMATE=data/dataset/blind_autoverified_estimate_human.json python code/analysis.py` | `data/dataset/results_tables_human_override.md` | The same estimates anchored to the author's labels (reported as a comparison in the Table 2b caption) |
| `python code/blind_checks.py` | `data/dataset/blind_checks.md`, `data/dataset/blind_autoverified_estimate.json`, `data/adjudication/blind/blind_manual_sample.csv`, `blind_autoverified_sample.csv` | Appendix A.2 (agent-agent confusion), blind-agent version of A.3 |
| `HUMAN_OVERRIDE=1 python code/blind_checks.py` | `data/dataset/blind_checks_human.md`, `blind_autoverified_estimate_human.json`, `blind_autoverified_sample_human.csv` | Appendix A.3, author's-labels column (the author's labels replace the blind agent's for the 29 coded entries) |
| `HUMAN_OVERRIDE=1 OVERRIDES=data/adjudication/blind/coder_overrides.json SUFFIX=_coder python code/blind_checks.py` | `data/dataset/blind_checks_coder.md`, `blind_autoverified_estimate_coder.json`, `blind_autoverified_sample_coder.csv` | Appendix A.3, independent coder's column: the per-source rates behind Table 2b |
| `SUFFIX=_coder python code/clustered_bootstrap.py` (also `SUFFIX=` and `SUFFIX=_human`) | stdout | Submission-clustered intervals for the blind-check shares and for the expected share of submissions with at least one corrupted citation (Sections 5.1 and 5.2) |
| `python code/human_agreement.py` | `data/dataset/human_agreement.md`, `data/adjudication/blind/human_overrides.json` | Appendix A.7 (the author's 64-item coding against both agent labels) |
| `python code/make_appendix.py > appendix.md` | stdout | Appendix A.1 to A.7 exactly as pasted into `paper/paper.md` (A.4 from `unmatched_flags_verdicts.json`, A.5 from `channel_analysis.md`, A.6 from `manual_recall_inspection.md`) |
| `python code/independent_agreement.py` | `data/dataset/independent_agreement.md`, `.json` | Appendix A.8: agreement of the independent coder with the first adjudicator, the blind agent and the author (both sheets), and the sensitivity bound on the detected counts; also recomputes the detected headline values as a self-check |
| `CODER_ROLE="..." python code/fill_coder_results.py` | `paper/paper.md`, `paper/coder_results_paragraphs.md` | Writes the coder's results into the manuscript and regenerates the appendix (already applied) |

Supporting scripts: `channel_analysis.py` (A.5), `unmatched_flags.py` (A.4 inputs), `qa_parser_recall.py` and
`qa_recall_authoryear.py` (parser recall checks behind A.6), `make_coder_sheets.py` (built the independent-coder sheets
with seed 20261005; do not re-run after a coder has filled them in), `submit_paper.py` and `submit_revision.py`
(journal API). The extraction and verification pipeline (`refs_extract.py`, `refs_anystyle.py`, `refs_verify.py`,
`second_pass.py`, `arxiv_repass.py`, `reprocess.py`) was run with AnyStyle for parsing; its outputs are committed, so
none of it needs to run to reproduce the analysis.

The headline numbers in the manuscript map to these outputs as follows: reviewed-submission rates (37.8%, 23.7%; 7.2%,
3.8%) to `paper/results_tables.md` Q1; adjusted rates (13.5%, 6.2%; accepted 7.8%, 2.6%; projection 34, 14-70, and 29,
9-65) to `results_tables_coder_override.md` Q1c (author-anchored comparison values 15.2%, 9.3%, 17.2% in
`results_tables_human_override.md`); flag metrics (51.9%; sensitivity 0.93, specificity 0.66, kappa 0.54) to
`paper/results_tables.md` Q2a/Q2b; agent-agent agreement (83.3%/0.75, 92.0%/0.83) to `blind_checks.md`; the per-source
rates (6.2%, 1.7%) to `blind_checks_coder.md`; the author's coding to `human_agreement.md`; the independent coder's
agreement (97.8%, kappa 0.94 on the random sample) and the sensitivity bound to `independent_agreement.md`.

## Provenance

- `18f47a4` (2026-09-28 21:16 UTC): analysis plan and adjudication protocol, before the first decision.
- `93c715f` (21:38 UTC): first 54 decisions. `924d9f5` (21:48 UTC): the PLACEHOLDER amendment to the protocol.
- Commit author identity was normalised to the project account when the repository moved to this organisation; commit
  timestamps are the originals.
- All adjudication and analysis were performed by AI agents (Claude, Anthropic) under the author's direction; see the
  manuscript's AI-use statement.

## Independent coding

`data/adjudication/blind/INDEPENDENT_CODER_INSTRUCTIONS.md` describes the task for a coder unconnected to the study:
`independent_coder_sheet_B.csv` (a simple random sample of 45 of the 857 manual decisions) and
`independent_coder_sheet_A.csv` (the author's 64-item sheet without labels), reference strings only. Both sheets were
coded by an independent coder (statement in `CODER_STATEMENT.md`); `coder_overrides.json` holds the coder's labels for
the 29 automatically verified entries, which anchor Table 2b. `python code/independent_agreement.py` scores both sheets.

## Licence

Released under CC BY 4.0, the manuscript's licence. The audited submissions and reviews are public on OpenReview (Agents4Science 2025).
