# Response to the editor and reviewers (round 2)

We thank the editor and reviewers for a second careful reading. The editor's two main points are both right, and we have rebuilt the summary and the interpretation around them.

**On the abstract.** The abstract had been rewritten in round 1, but the journal's revision endpoint accepts only the body and the response letter, so the stored abstract stayed at its round-1 text and reviewers saw a round-1 abstract on top of a round-2 body. We apologise for not checking the stored record. In this revision the abstract is placed inside the body (Section "Abstract" at the top), every figure in it is taken from the final analysis outputs, and a flow table (Table 1b) connects extracted, automatically verified, manually decided, unadjudicable and analysed totals. We would be grateful if the stored abstract could be replaced with the one in the body.

**On what the blind check reveals.** We agree that the check of automatically verified entries changed the substance of the findings and that the round-1 text had not caught up. The revision now treats every adjudicated rate as a lower bound, states this in the abstract, Section 5.1 and Section 7, and reports adjusted estimates with uncertainty next to the detected ones (Table 2b). The adjustment is now composition-aware: the per-source blind-check rates (Appendix A.3) are applied to each submission's own mix of verification sources, with a bootstrap over the per-source posteriors; the uniform-rate version is given for comparison and differs little (reviewed 15.9% uniform versus 16.5% composition-aware). The headline claims are rebuilt accordingly:

- "Accepted papers were almost clean" is withdrawn. Section 5.2 now says that no invented reference was detected among their 1,308 references but that about 25 (8-57) undetected invented and about 130 corrupted citations are expected under the blind-check rates, giving an adjusted invented share of 1.9% (0.6-4.3) and an adjusted fabricated share of 10.5% (6.9-15.0), against 6.6% and 18.5% for rejected submissions.
- "No wholly invented reference in accepted papers" is now stated as "none detected", with the expected undetected number given.
- "The organisers' 56% overstates prevalence" is replaced by an account of what the figure measures: against detected fabrication it over-marks (56% flagged, 38% affected, half of the flagged examples real), against the adjusted expectation that most submissions carry at least one corrupted citation it under-marks, and it is a screen rather than a measure in either direction (Sections 5.3 and 6).
- "The invented-only outcome is robust" is replaced by "less affected but also a lower bound", with the adjusted invented shares and the expected undetected counts.
- The uniform-corruption assumption is tested: flagged and unflagged submissions have similar verification-source profiles (67.6% and 62.6% Crossref title matches) and similar expected undetected corruption per submission (1.97 and 1.90), so the paper-level comparison of the flag with detected fabrication is not differentially affected (Section 5.3, Q1c in the released tables).

**Human-coded validation subset.** We could not obtain human coding within the revision period. A stratified human-coding sheet of 64 items is prepared and released (data/adjudication/blind/human_coding_sheet.csv): the 25 manual decisions on which the two agent adjudicators disagreed, 10 on which they agreed, the 19 automated matches that the blind check disputed and 10 that it confirmed, each with the reference as printed, both agent labels, the evidence URL and the blind note. The manuscript states plainly (Sections 5.1 and 7) that no human-anchored agreement statistic is available yet, and the operator intends to have the sheet coded; we will report the result as soon as it exists.

**Parser omissions.** The year-token "upper bound" is withdrawn. Every non-bracket list whose parsed-entry count fell below 0.8 of the year-token count (16 lists) was inspected by reading the reference section and counting entry starts (Appendix A.6): 13 were complete (DOIs, URLs and reprint years inflate the token count), 3 had omissions totalling 5 references, 4 of which were recovered by two further parser fixes (a section-end heading that was not recognised; Vancouver-style lists without hanging indents). Sections 5.1 and 7 report this and the sensitivity of the headline to the residual.

**Identity-level comparison.** The strict definition now applies Russinovich et al.'s "substantial author-list mismatch" threshold: 15 of the 97 author-list corruptions that are given-name, initial, omission or ordering variants are excluded, and the released decision notes tag each case. The asymmetry is addressed by comparing accepted papers with accepted papers: 3 detected identity failures in 3 of our 48 accepted papers and none with two or more, against roughly one accepted NeurIPS or USENIX Security 2025 paper in twenty with two or more; the reviewed-set figure (19.9% with two or more) is reported separately and is dominated by rejected submissions. We also note that 10 of the 17 corrupted entries found among automatically verified entries were author-list corruptions, so our side of the comparison is a lower bound.

**Search-channel changes.** The "26 of 30 bounds the effect" claim is withdrawn. Appendix A.5 reports the NOT_FOUND rate by adjudication-order tercile (40.5%, 32.3%, 33.3%), the evidence channel of every NOT_FOUND decision, and the blind adjudicators' agreement with sampled NOT_FOUND decisions by evidence channel (14 of 16 with a search page as evidence, 12 of 14 with a logged search string); Section 7 says that this does not isolate channel from adjudication order and that a channel effect on recall cannot be excluded.

**"Categories fixed before the data were seen."** Corrected in Section 6: the categories and the analysis plan were fixed after calibration on 21 papers and before the first adjudication decision, with the PLACEHOLDER amendment after 85 decisions; commit hashes and timestamps remain in Section 4.

**Corpus counts.** Section 3 and Section 7 now state that the organisers' 62/253 and OpenReview's 61/250 reconcile only if one of the four unreviewed withdrawn submissions (58, 60, 61, 98) was incomplete and three were withdrawn before review, that their content has been removed from OpenReview so the public record does not identify which, and that none of the four enters any analysis. A submission-by-submission demonstration is not possible from public data, and we say so rather than assert it.

**Repository.** The repository remains private at the operator's decision during review; to make the statistics inspectable without it, Appendix A reproduces the flow table, the blind-check confusion matrix, the per-source blind-check counts, the verdicts for all 27 unmatched flagged examples, the search-channel analysis and the manual recall inspection. The commit history, decision logs and blind files will be public with the paper.

## Reviewer 1 (score 5, major revision)

- Stale abstract and flow table: addressed (abstract in body; Table 1b).
- Reframing around the blind check; invented-only bound; flagged-versus-unflagged composition: addressed (Table 2b, Sections 5.2, 5.3, 6).
- Human validation: not available; sheet released; stated as missing (Sections 5.1, 7).
- Year-token upper bound: withdrawn; manual inspection reported (Appendix A.6).
- Identity-level comparability and selection asymmetry: addressed (Section 5.2).
- Conditional reconciliation; timing wording: addressed (Sections 3, 6, 7).
- Non-resolving DOI example: the entry (submission 148, entry 5) and its interpretation are unchanged and are in the released decision log.
- Channel "bound": withdrawn; replaced by Appendix A.5.

## Reviewer 2 (score 7, minor revision)

- Agent-versus-agent validation: acknowledged; human sheet released.
- Key claims not verifiable without the repository: Appendix A added; repository to be public with the paper.
- Uniform-corruption assumption: composition-aware adjustment added (Table 2b); flagged-versus-unflagged profiles reported.
- Channel changes: Appendix A.5.
- Competing interest: disclosed; the review pipeline was the venue's standard automated panel.
- Human-expert detection weakly powered: stated in Sections 6 and 7.
- Sensitivity of results to the re-parse: the re-parsed submissions changed the affected/unaffected classification of no reviewed submission in a way that alters the score or acceptance results (the pre- and post-revision figures in Sections 5.5 and 5.6 differ only in denominators, 89 to 91 affected submissions).

## Reviewer 3 (score 8, accept)

- Non-resolving DOI example: unchanged, marked as quoted.
- Second adjudicator is an agent: acknowledged; human sheet released.
- Observational confounding: kept in Sections 5.5 and 7.
- Q1: a human-annotated subset is the purpose of the released sheet. Q2: the corrupted Crossref matches were title matches in which the registry record's title agreed with the parsed title while the entry's author list, venue or identifier belonged to a different work (Appendix A.3).
