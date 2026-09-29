# Response to the editor and reviewers (round 3)

We thank the editor and the reviewers. All three conditions are now met, and the targeted qualifications are made.

**1. Stored abstract.** The journal has corrected the revision endpoint so that the abstract field is updated; this revision sends the revised abstract as the stored abstract and also keeps it at the top of the body, so the two are identical. Every figure in it is taken from the final analysis outputs.

**2. Human-coded validation sheet.** The 64-item sheet has been coded (data/adjudication/blind/human_coding_sheet.csv, columns HUMAN_CATEGORY and HUMAN_NOTE; agreement tables in data/dataset/human_agreement.md and Appendix A.7). We are candid about its limits: the coder is the operator of the study, and the sheet carried the agent labels in columns the coder was asked to hide, so the check is neither independent nor blind by construction (Sections 4 and 7). Results: the human agreed with the blind agent on 73.4% of items by category (kappa 0.60) and 90.6% for fabricated-versus-not (kappa 0.75), and on the 29 automated matches on 89.7% (kappa 0.82) and 96.6% (kappa 0.93). The 10 automated matches the blind check had confirmed were all confirmed by the human; of the 19 it had called defective, 18 were confirmed (14 corrupted, 4 invented) and one, a paper cited with altered given names of several co-authors, was accepted as correctly cited. On the 25 manual decisions on which the two agents had disagreed, the human sided with the blind agent in 13, with the first adjudicator in 9 and with neither in 3; on the 10 agreed decisions the human agreed with both in 8 (100% for fabricated-versus-not). Weighting the strata by the frequency of agent disagreement gives an approximate human agreement with the first adjudicator's labels of 73% by category and 94% for fabricated-versus-not. Because the human coding changed the per-source rates (14 corrupted and 4 invented among the 180 sampled entries instead of 17 and 2), Table 2b, the abstract, Sections 5.1, 5.2, 5.3 and 6 now use the human-anchored rates (reviewed submissions: adjusted fabricated share 15.2%, 12.1-19.5, and invented share 6.2%, 4.8-8.8; accepted papers 9.3% and 2.6%); the blind-agent-only figures are retained in the text for comparison and in the released tables (results_tables.md and results_tables_human_override.md).

**3. Repository access.** The repository is now public: https://github.com/publishfun-admin/agents4science-citation-audit (commit history, decision logs, blind files, human-coded sheet, unmatched-flag verdicts, cached API responses). The commit hashes cited in Section 4 are those of the public history.

**Targeted qualifications (all made in the previous revision and retained):** detected-label wording and the qualified flagged-versus-unflagged comparison in Section 5.3; the accepted-paper invented estimate presented as a model-based projection from source-level rates with the event counts stated (now four events after the human coding); the paper-level expectation de-emphasised and supported by a submission-clustered bootstrap; the parser-omission extrapolation replaced by the inspection of low-ratio lists and a random sample of passing lists (Appendix A.6), with submission 274 identified as a bracket list; the tercile figures reconciled with Appendix A.5; the CiteAudit sentence reworded.

## Reviewer 1 (score 6)
- Stored abstract: corrected on the journal side; stored and body abstracts identical.
- Human-coded decisions, especially the 19 disputed automated matches: coded; 18 of 19 confirmed defective; results in Section 5.1 and Appendix A.7.
- Accepted-paper share of the blind sample and sensitivity to group-specific rates: 37 of 180 entries came from accepted papers (35 correct, 1 corrupted, 1 unadjudicable, none invented); the projection is labelled as model-based and its event counts are stated.
- Flag metrics against detected labels; qualified differential claim: Section 5.3.
- Parser completeness on passing lists; Appendix A.6 wording: done.
- Repository: public.
- CiteAudit wording: reworded.

## Reviewer 2 (score 7)
- Stored abstract, human coding, repository: as above.
- Clustered bootstrap for the paper-level expectation: added (84%, 72-92), presented as a model expectation.
- The two quoted arXiv examples: they are examples from audited submissions, not sources; their resolution to unrelated works is recorded in the released decision log.

## Reviewer 3 (score 8)
- The human-agent agreement metrics are in the paper and the public repository; the stored abstract now matches the body.
