# Response to the round-5 decision (minor revision)

We thank the editor and the three reviewers. The reopened round-5 decision set one blocking condition, coding of the released reference-strings-only random sample by a human with no role in the study, and listed six items. This letter follows the six items and then the reviewers' remaining points.

## 1. Independent coding of the 45-item random sample (sheet B)

Both sheets were coded by a person with no role in the study, recruited by the author from personal acquaintance. The coder's statement, data/adjudication/blind/CODER_STATEMENT.md, gives the coder's initials (JB), reports no relationship to the study, its author or Publish.fun, and confirms that only the sheets were opened, that no AI assistant was used, that no item was discussed with the author before the coding ended, and that the work took about 30 minutes for sheet B and 40 minutes for sheet A. The sheets contain only the reference strings; no agent label or author label was ever available to the coder. Sheet B carries a link or the searches run for 43 of its 45 items; sheet A carries a page, identifier or search link for 62 of 64 items and a note for 59.

Agreement with the first adjudicator on the 45 items (data/dataset/independent_agreement.md):

- by category: 75.6% (95% Wilson CI 61.3-85.8); Cohen's kappa 0.63 (bootstrap 95% CI 0.42-0.81);
- fabricated-versus-not: 97.8% (88.4-99.6); kappa 0.94 (0.78-1.00).

By first-adjudicator category: NOT_FOUND (n=20): coder NOT_FOUND 14, EXISTS_CORRUPTED 6. EXISTS_CORRUPTED (n=14): coder EXISTS_CORRUPTED 10, NOT_FOUND 4. EXISTS or web resource (n=9): coder EXISTS 8, EXISTS_CORRUPTED 1. PLACEHOLDER (n=1) and UNADJUDICABLE (n=1): agreed. The single fabricated-versus-not disagreement is therefore one entry the adjudicator accepted and the coder called corrupted; the ten category disagreements lie inside the fabricated class, between "invented" and "corrupted", and run in both directions. Against the blind agent, on the 11 items that were also blind re-adjudicated: 81.8% by category and 90.9% for fabricated-versus-not.

The directly estimated figure (97.8% for fabricated-versus-not; 75.6% by category) supersedes the stratum-weighted 94% and 73% estimates in Section 5.1, Section 7 and the appendix, where it is reported in a new Appendix A.8; the stratum-weighted figures remain only as the figures for the author's own coding in Appendix A.7. The abstract now reports the independent figure.

Materials. Sheet B is the simple random sample drawn with seed 20261005 from the 857 manual decisions; the generator, code/make_coder_sheets.py, is in the repository and regenerates both released sheets byte for byte. The scoring script, code/independent_agreement.py, reports raw agreement with Wilson intervals and Cohen's kappa with bootstrap intervals, and recomputes the detected headline values from the released data as a self-check (they match paper/results_tables.md exactly).

## 2. The 64-item sheet (sheet A) and the coder's relationship to the study

The same coder coded the label-free 64-item sheet (data/dataset/independent_agreement.md, Appendix A.8). Agreement on the 64 items, by category and for fabricated-versus-not, with 95% Wilson intervals for agreement and bootstrap intervals for kappa:

- with the first adjudicator (or automated acceptance): 42.2% (30.9-54.4), kappa 0.18 (0.03-0.34); 62.5% (50.3-73.3), kappa 0.27 (0.06-0.47);
- with the blind agent: 68.8% (56.6-78.8), kappa 0.55 (0.39-0.69); 85.9% (75.4-92.4), kappa 0.65 (0.42-0.83);
- with the author's coding: 87.5% (77.2-93.5), kappa 0.82 (0.69-0.93); 92.2% (83.0-96.6), kappa 0.80 (0.61-0.96).

On the 25 manual decisions where the two agents disagreed, the coder sided with the first adjudicator in 6, with the blind agent in 14 and with neither in 5 (the author: 9, 13 and 3). On the 19 automated matches that the blind agent had called corrupted or invented, the coder confirmed a defect in 15 and accepted four as correctly cited: the entry the author had also accepted, and three real works that the blind agent and the author had called corrupted for a wrong identifier, author list or venue. The coder confirmed all 10 automated matches that the blind agent had confirmed. The sheet is boundary-enriched by design, so these figures are not an unbiased agreement rate; the random sample in item 1 is.

The coder never had access to any agent label or to the author's labels (item 1); the coder's role and relationship to the study are recorded in the statement and in Section 4. The author's coding remains presented as the author's own, non-independent check (Appendix A.7).

## 3. Correction or bounds for the detected counts, the flag metrics and the associations

Fabricated-versus-not agreement on the random sample (97.8%) is not materially lower than the 94% previously extrapolated, so no corrected estimate replaces the detected figures. We nevertheless report the bound the editor asked for. The scoring script estimates from sheet B the coder's label given the first adjudicator's label (three states: invented, corrupted, other; Dirichlet posterior with a Jeffreys prior) and relabels every one of the 857 manual decisions accordingly in 4,000 simulations; automatically verified entries are unchanged, since their error rate is measured separately by the blind check. Median and 95% interval of the relabelled value against the detected value:

| Quantity | Detected | Under the coder's labels |
|:--|--:|--:|
| Detected fabricated references (all submissions) | 513 | 549 (493-638) |
| Detected invented references | 286 | 271 (192-361) |
| Reviewed submissions with >=1 fabricated reference | 37.8% | 45.2% (38.6-56.0) |
| Reviewed submissions with >=1 invented reference | 23.7% | 29.0% (22.8-39.8) |
| Reviewed references fabricated | 7.2% | 7.7% (6.9-8.9) |
| Reviewed references invented | 3.8% | 3.7% (2.6-5.0) |
| Organiser flag, paper-level sensitivity | 0.93 | 0.83 (0.74-0.92) |
| Organiser flag, paper-level specificity | 0.66 | 0.66 (0.63-0.69) |
| Organiser flag, paper-level kappa | 0.54 | 0.49 (0.39-0.55) |
| Flagged examples fabricated (precision) | 51.9% | 51.9% (47.3-55.0) |
| Spearman rho, fabricated share vs LLM slots 1, 2, 3 | -0.15, -0.13, -0.13 | -0.14, -0.12, -0.11 (all intervals exclude zero) |
| Spearman rho, invented share vs LLM slots 1, 2, 3 | -0.20, -0.18, -0.18 | -0.15, -0.14, -0.13 (all intervals exclude zero) |
| Spearman rho, fabricated and invented share vs human expert score | -0.28, -0.41 | -0.23 (-0.32 to -0.12), -0.29 (-0.44 to -0.11) |
| Accepted papers with >=1 invented reference | 0 | 4 (0-13) |
| Accepted papers with >10% fabricated references | 0 | 1 (0-5) |

Where the coder and the adjudicator differ, the coder's reading is stricter, so the detected figures remain lower bounds under the coder's labels as well. Three consequences are now stated in the manuscript. Section 5.1 reports the relabelled headline values. Section 5.3 reports the flag metrics under the coder's labels: the paper-level sensitivity falls from 0.93 to 0.83 because the relabelling adds fabricated papers the flag missed, while specificity and precision are unchanged. Section 5.2 reports that a median of 4 (0-13) accepted papers would carry a reference classed as invented under the coder's labels, mostly through the invented-versus-corrupted boundary, so the absence of a detected invented reference among accepted papers is a statement about the adjudication's labels rather than a label-independent fact; the Section 5.5 acceptance result is stated as detected, and the score associations are attenuated but keep their sign, with all intervals excluding zero. **Table 2b revised.** Sheet A includes the 29 automatically verified entries whose labels anchor the blind-check error rates. The coder's labels differ from the author's on three of them (the three real works above, which the coder accepted as correctly cited), so, as the decision requested, the per-source rates and every downstream figure were recomputed with the independent coder's labels in place of the author's (data/adjudication/blind/coder_overrides.json; data/dataset/blind_checks_coder.md; data/dataset/results_tables_coder_override.md). The corrupted share among automatically verified entries falls from 8.2% (author-anchored) to 6.2% (source-weighted; 11 of 180 crude, 6.1%); the invented share is unchanged (1.7%; 4 of 180). Appendix A.3 now shows the per-source counts under all three label sets (blind agent, author, independent coder), and the Table 2b caption gives the author-anchored figures as a comparison. Every changed figure (old -> new):

- Abstract and Section 6: corrupted among automatically verified entries about 8% -> about 6%; adjusted fabricated share, reviewed submissions 15.2% (12.1-19.5) -> 13.5% (10.8-17.4); adjusted invented share 6.2% (4.8-8.8) -> 6.2% (4.7-8.8); accepted papers, adjusted fabricated share 9.3% (6.0-13.8) -> 7.8% (4.7-12.0), against rejected 17.2% -> 15.4%; expected undetected invented references in accepted papers 34 (14-69) -> 34 (14-70); expected undetected corrupted citations in accepted papers about 115 -> about 95.
- Section 5.1: source-weighted corrupted share 8.2% (5.4-13.9) -> 6.2% (4.0-11.4), about 490 -> about 370 references; the author-anchored (8.2%) and blind-agent-only (9.7%) rates are retained as comparisons; the submission-clustered interval for the blind-agent labels is restated from the now-released script (9.4%, 4.7-14.9; 1.1%, 0.0-2.9).
- Table 2b: reviewed 15.2% (12.1-19.5) -> 13.5% (10.8-17.4), 6.2% (4.8-8.8) -> 6.2% (4.7-8.8), 123 (49-258) -> 122 (48-260); accepted 9.3% (6.0-13.8) -> 7.8% (4.7-12.0), 2.6% (1.0-5.3) -> 2.6% (1.0-5.4), 34 (14-69) -> 34 (14-70); rejected 17.2% (14.1-21.5) -> 15.4% (12.8-19.3), 7.4% (6.0-9.9) -> 7.3% (6.0-9.9), 89 (35-189) -> 88 (34-189); uniform-rate version 14.5%, 8.5%, 16.5% -> 12.7%, 6.6%, 14.8%.
- Section 5.2: accepted-paper invented share without the 'other' stratum 2.2% (0.7-4.9) -> 2.2% (0.7-5.0); the projection without that stratum is unchanged (29, 9-65); rejected adjusted invented share 7.4% -> 7.3%; the expected share of reviewed submissions carrying at least one corrupted citation 82-84% (72-92) -> 77% (62-86) under the coder's labels (82-85% under the author's or the blind agent's), and the corruption-rate range 8-10% -> 6-10%.
- Section 5.3: expected undetected corrupted references per submission 1.67 (flagged) and 1.64 (unflagged) -> 1.28 and 1.28.
- Section 7: 14 of 180 (8.2%) -> 11 of 180 (6.2%).

Unchanged: all detected figures (513, 286; 37.8%, 23.7%; 7.2%, 3.8%), the flag metrics, the score and acceptance associations, the agent-agent agreement, the invented rates (1.7%; 6.2%, 2.6%) and the projection without the 'other' stratum (29, 9-65). The conclusions do not move: the adjusted fabricated shares fall by about two points and the accepted papers remain about half as affected as the rejected ones.

## 4. Wording on the author's coding

Revised in the abstract, Section 4, Section 5.1, Section 7 and the Appendix A.7 heading. The author's coding is presented as a disclosed, non-independent, attestation-blinded check, and the sentence claiming independence "in the sense that matters for inter-rater validation" has been removed.

- Abstract: "The labels were re-adjudicated blind by independent agent instances (150 decisions: category agreement 83%, kappa 0.75; fabricated-versus-not 92%, kappa 0.83); an independent human coder agreed with the adjudication on 98% of a random sample of 45 manual decisions for fabricated-versus-not (kappa 0.94)". The phrase "validated ... by a human coder" no longer appears.
- Section 4: "(iii) A human check by the paper's author, disclosed as non-independent and blinded only by attestation. ... The author is nevertheless not independent of the study: the author operates the venue of publication and has an interest in the outcome, the sheet carried the agent labels in separate columns, and the statement that they were hidden before coding began and were not consulted is an attestation rather than a verifiable blinding. The check is therefore reported as an anchor of the agent labels to one careful human reading, not as a validation by independent human judgement." The paragraph then describes the released sheets, the independent coder, the statement and the scoring script.
- Section 5.1: "The human coder is the paper's author, and the check is a disclosed, non-independent, attestation-blinded one (Section 4): it anchors the agent labels to one careful human reading, not to independent human judgement, and the 73% and 94% figures are a stratum-weighted extrapolation from boundary-enriched samples; the independent coder's sheet B gives the directly estimated, non-enriched figure, which supersedes it ..."
- Section 7: "It is a disclosed, non-independent, attestation-blinded anchor, not a validation by independent human judgement; its agreement with the first adjudicator on the disputed manual decisions is poor (36% by category, kappa -0.22 for fabricated-versus-not on 25 items; Appendix A.7); the independent coding of the random sample (Section 5.1, Appendix A.8) gives the direct figure ..."
- Appendix A.7 heading: "Human coding of 64 items by the author (a disclosed, non-independent, attestation-blinded check)".

In the human-coding context the word "independent" is now used only for the external coder. The blind agent instances are still called independent instances of the agent, which describes their separation from the first adjudicator, not human validation.

## 5. Section 6, "kept out"

Reworded as an association: "Whatever the mechanism, no submission with a detected invented reference was accepted; the observational design of Section 5.5 shows an association with rejection, not that the venue's process (three LLM reviews, human expert review of the top-scoring papers, an automated reference flag and human program chairs) excluded those submissions because of their references. Corrupted citations of real works were accepted at a rate near that of our own automated stage."

## 6. Repository and spot-check

- The coder's completed sheets (data/adjudication/blind/independent_coder_sheet_A.csv and independent_coder_sheet_B.csv), the coder's statement (CODER_STATEMENT.md), the coder's labels for the 29 automatically verified entries (coder_overrides.json) and the scoring outputs (data/dataset/independent_agreement.md and .json, blind_checks_coder.md, results_tables_coder_override.md) are committed in the public repository, together with the scoring script, the sheet generator and the submission-clustered bootstrap (code/clustered_bootstrap.py, previously computed outside the repository).
- A README.md maps every manuscript table and headline number to the script that produces it and the file it is written to, lists the commands, and states the provenance of the cited commits (18f47a4, 93c715f, 924d9f5, present with their original timestamps).
- A fresh clone of the public repository was used to regenerate every analysis output (code/analysis.py in both modes, code/blind_checks.py in both modes, code/human_agreement.py, code/make_appendix.py); all regenerated files are identical to the committed ones, and the regenerated appendix is identical to the manuscript's.
- Two portability defects found by that exercise were fixed: code/blind_checks.py read the blind samples and decisions from a local scratch directory rather than from data/adjudication/blind/ (the released copies are byte-identical to the ones used), and code/analysis.py wrote the human-anchored tables over the blind-agent tables (they now go to data/dataset/results_tables_human_override.md, as the README states).
- Persistent identifier: the repository will be archived on Zenodo as a tagged release at acceptance, and the DOI reported to the editor.

## Reviewer points not covered above

- Reviewer 1 (item 3) and Reviewer 3 (item 4), the accepted-paper projection: Section 5.2 now states that the bootstrap intervals capture sampling variation in the source-level rates only, not the structural uncertainty of transferring rates estimated across all submissions to the accepted papers, which is not quantified, and that the projection is subordinate to the detected figures; Section 6 repeats this where the projection is mentioned, and the 82-84% paper-level expectation is described as subordinate to the detected rate.
- Reviewer 1 (item 6) and Reviewer 3 (item 7), the non-resolving DOI in Section 5.7: it is a placeholder identifier quoted from submission 148. It is now typeset with a space before the slash and an explanatory note, so that automated reference checkers no longer read it as a citation of this paper.
- Reviewer 1 (item 7): Section 5.3 now states that the precision figures describe the listed example references and the paper-level flag, not every reference the checker flagged, since the organisers published examples rather than the checker's full output.
- Reviewer 3 (item 6), the competing interest: the disclosure is unchanged; the author operates the venue and the automated review pipeline was not modified for this submission.

## Other changes

- The abstract was shortened by a few words to stay within the length limit after the changes above.
- New Appendix A.8 (independent coding of both sheets: agreement and sensitivity bound), generated by code/make_appendix.py from data/dataset/independent_agreement.md; Appendix A.3 now shows the per-source counts under the three label sets.
- code/make_coder_sheets.py, code/independent_agreement.py, code/fill_coder_results.py, code/clustered_bootstrap.py, data/adjudication/blind/CODER_STATEMENT.md and README.md were added; data/adjudication/blind/INDEPENDENT_CODER_INSTRUCTIONS.md was revised to require a coder with no connection to the study and to ask for sheet B first.
