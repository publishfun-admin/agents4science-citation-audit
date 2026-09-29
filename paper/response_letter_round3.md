# Response to the editor and reviewers (round 3) — DRAFT, pending the human-coded sheet

We thank the editor and reviewers. Of the three conditions, two require action by the operator of the venue and are noted below; the targeted qualifications are all made in the manuscript.

**1. Stored abstract.** The revision endpoint does not update the stored abstract; the body carries the current abstract (2,974 characters, every figure from the final outputs). [OPERATOR: replace the stored abstract with the body abstract before publication and confirm.]

**2. Human-coded validation sheet.** [PENDING: the 64-item sheet (data/adjudication/blind/human_coding_sheet.csv) is being coded by an independent human coder; the raw agreement and kappa with each agent label, overall and for the 19 disputed automated matches and the NOT_FOUND vs EXISTS_CORRUPTED boundary, will be added to Section 5.1 and Appendix A.2, and Table 2b will be recomputed if the per-source rates change.]

**3. Repository access.** [OPERATOR: make the repository public or grant the editor access; the commit history, decision logs, blind files and unmatched-flag verdicts are at https://github.com/publishfun-admin/agents4science-citation-audit.]

**Targeted qualifications (all made):**
- Section 5.3 now states that sensitivity, specificity, PPV and NPV are computed against detected labels, and qualifies the flagged-versus-unflagged comparison: similar source mixes make a large differential effect unlikely but do not establish equal within-source error rates.
- Section 5.1 reports that 37 of the 180 blind-checked automatically verified entries came from accepted papers (35 correctly cited, 1 corrupted, 1 unadjudicable, none invented), and Section 5.2 presents the accepted-paper invented estimate explicitly as a model-based projection from source-level rates resting on two events (1 of 101 Crossref title matches, 1 of 5 other-source entries).
- The "expected 86%" figure is removed from Section 6 and replaced in Section 5.2 by a submission-clustered bootstrap of the blind sample (84%, 95% interval 72-92), labelled a model expectation under spread-out errors; the clustered bootstrap for the corruption and invention rates (9.5%, 4.8-14.9; 1.1%, 0.0-2.8) is added to Section 5.1 and data/dataset/blind_checks_addendum.md.
- The parser-omission extrapolation is replaced: a random sample of 15 lists that pass the diagnostics was inspected (Appendix A.6); 13 of 14 assessable lists were complete and one had a single missing placeholder stub, giving an estimated omission rate of about one reference per fourteen non-bracket lists (roughly six across the corpus) with wide uncertainty. Appendix A.6 now describes the inspected set as 15 author-year or numbered lists plus one three-entry bracket list (submission 274).
- The tercile figures in Section 7 now match Appendix A.5 (40.9%, 31.9%, 33.3%; the earlier figures predated the last three adjudications).
- Section 2 now describes the blind re-adjudication as an agent-level analogue of CiteAudit's human validation, not a substitute for it.
