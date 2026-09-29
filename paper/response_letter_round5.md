# Response to the round-5 decision (minor revision)

We thank the editor and the three reviewers. The reopened round-5 decision sets one blocking condition, coding of the released reference-strings-only sheets by a human with no role in the study, and lists six items. This letter follows the six items and then the reviewers' remaining points. The markers PENDING-CODER and PENDING-USER show where figures will be inserted once the independent coding and the archive exist; the submission tool refuses to send a letter or manuscript that still contains such a marker.

## 1. Independent coding of the 45-item random sample (sheet B)

PENDING-CODER: sheet B, 45 items, coded by [role; relationship to the study: none]. Agreement with the first adjudicator: categories X% (95% Wilson CI), Cohen's kappa K (bootstrap 95% CI); fabricated-versus-not Y% (CI), kappa K2 (CI); by first-adjudicator category (NOT_FOUND n=20, EXISTS_CORRUPTED n=14, EXISTS or web n=9, PLACEHOLDER 1, UNADJUDICABLE 1). Against the blind agent on the 11 items that were also blind re-adjudicated: ... (data/dataset/independent_agreement.md).

Section 5.1, Section 7 and Appendix A.7 now report this directly estimated figure and it supersedes the stratum-weighted 73%/94% estimate, which is retained only as the figure for the author's own coding.

Materials. Sheet B is the simple random sample drawn with seed 20261005 from the 857 manual decisions; the generator, code/make_coder_sheets.py, is now in the repository and regenerates both released sheets byte for byte. The sheets contain only the reference strings (columns item, reference_as_printed, CODER_CATEGORY, CODER_EVIDENCE_URL, CODER_NOTE) and no label of any kind. The scoring script, code/independent_agreement.py, reports raw agreement with Wilson intervals and Cohen's kappa with bootstrap intervals against the first adjudicator (all items) and the blind agent (items also blind re-adjudicated), and recomputes the detected headline values from the released data as a self-check (they match paper/results_tables.md exactly).

## 2. The 64-item sheet (sheet A) and the coder's relationship to the study

PENDING-CODER: sheet A, 64 items. Agreement with the first adjudicator: ...; with the blind agent: ...; with the author's coding: ... (overall and by stratum; data/dataset/independent_agreement.md).

The coder never had access to any agent label or to the author's labels: the sheets carry none, the instructions (data/adjudication/blind/INDEPENDENT_CODER_INSTRUCTIONS.md) forbid opening any other file in the repository, the use of an AI assistant, and discussion with the author before both sheets are finished, and the coder confirms each point in data/adjudication/blind/CODER_STATEMENT.md, which also records the coder's role and relationship to the study. PENDING-CODER: summarise the statement (role, relationship: none, dates, time spent). Section 4 and Appendix A.7 state this.

## 3. Correction or bounds for the detected counts, the flag metrics and the associations

The scoring script estimates from sheet B the coder's label given the first adjudicator's label (three states: invented, corrupted, other; Dirichlet posterior with a Jeffreys prior) and relabels every one of the 857 manual decisions accordingly in 4,000 simulations. It reports, against the detected value, the median and 95% interval of: the 513 detected fabricated references and the 286 invented ones; the paper-level rates among reviewed submissions (37.8%, 23.7%); the reference-level shares (7.2%, 3.8%); the Section 5.3 flag metrics (sensitivity 0.93, specificity 0.66, kappa 0.54, example-level precision 51.9%); and the Section 5.5 associations (Spearman correlations of the fabricated and invented shares with each LLM slot's score and with the human expert score; the number of accepted papers with an invented reference or with more than 10% fabricated references). Automatically verified entries are unchanged in this exercise, since their error rate is measured separately by the blind check.

PENDING-CODER: insert the sensitivity table and state the outcome: (a) if fabricated-versus-not agreement on sheet B is close to the 94% previously extrapolated, the detected figures stand and the bounds are reported in Section 5.2 and Section 7; (b) if it is materially lower, Section 5.2, Section 6 and the abstract report the corrected estimate or the bounds in place of the detected figures, and Sections 5.3 and 5.5 state whether the flag metrics and the associations are robust.

Sheet A includes the 29 automatically verified entries (19 called corrupted or invented by the blind agent, 10 confirmed) behind the human-anchored per-source rates. PENDING-CODER: if the coder's labels change any of those 29, Table 2b and every downstream figure are recomputed with the coder's labels in place of the author's (the HUMAN_OVERRIDE mechanism of code/blind_checks.py), and every changed figure is listed here; otherwise state that no per-source rate changed.

## 4. Wording on the author's coding

Revised in the abstract, Section 4, Section 5.1, Section 7 and the Appendix A.7 heading. The author's coding is now presented as a disclosed, non-independent, attestation-blinded check, and the sentence claiming independence "in the sense that matters for inter-rater validation" has been removed.

- Abstract: "The labels were re-adjudicated blind by independent agent instances (150 decisions: category agreement 83%, kappa 0.75; fabricated-versus-not 92%, kappa 0.83); a 64-item check by the author, disclosed as non-independent, anchors them to one human reading". The phrase "validated ... by a human coder" no longer appears. PENDING-CODER: add the independent coder's headline figure to the abstract.
- Section 4: "(iii) A human check by the paper's author, disclosed as non-independent and blinded only by attestation. ... The author is nevertheless not independent of the study: the author operates the venue of publication and has an interest in the outcome, the sheet carried the agent labels in separate columns, and the statement that they were hidden before coding began and were not consulted is an attestation rather than a verifiable blinding. The check is therefore reported as an anchor of the agent labels to one careful human reading, not as a validation by independent human judgement." The paragraph then describes the released reference-strings-only sheets, the coder statement and the scoring script. PENDING-CODER: replace "no such coding was available for this version" with the description of the coding.
- Section 5.1: "The human coder is the paper's author, and the check is a disclosed, non-independent, attestation-blinded one (Section 4): it anchors the agent labels to one careful human reading, not to independent human judgement, and the 73% and 94% figures are a stratum-weighted extrapolation from boundary-enriched samples ..." PENDING-CODER: continue with the directly estimated figure.
- Section 7: "It is a disclosed, non-independent, attestation-blinded anchor, not a validation by independent human judgement; its agreement with the first adjudicator on the disputed manual decisions is poor (36% by category, kappa -0.22 for fabricated-versus-not on 25 items; Appendix A.7) ..." PENDING-CODER: update the clause on the random sample.
- Appendix A.7 heading: "Human coding of 64 items by the author (a disclosed, non-independent, attestation-blinded check)".

In the human-coding context the word "independent" is now used only for the external coder. The blind agent instances are still called independent instances of the agent, which describes their separation from the first adjudicator, not human validation.

## 5. Section 6, "kept out"

Reworded as an association: "Whatever the mechanism, no submission with a detected invented reference was accepted; the observational design of Section 5.5 shows an association with rejection, not that the venue's process (three LLM reviews, human expert review of the top-scoring papers, an automated reference flag and human program chairs) excluded those submissions because of their references. Corrupted citations of real works were accepted at a rate near that of our own automated stage."

## 6. Repository and spot-check

- A README.md now maps every manuscript table and headline number to the script that produces it and the file it is written to, lists the commands, and states the provenance of the cited commits (18f47a4, 93c715f, 924d9f5, verified present with their timestamps).
- A fresh clone of the public repository was used to regenerate every analysis output (code/analysis.py in both modes, code/blind_checks.py in both modes, code/human_agreement.py, code/make_appendix.py); all regenerated files are identical to the committed ones, and the regenerated Appendix A.1 to A.7 is identical to the manuscript's.
- Two portability defects found by that exercise were fixed: code/blind_checks.py read the blind samples and decisions from a local scratch directory rather than from data/adjudication/blind/ (the released copies are byte-identical to the ones used, verified), and code/analysis.py wrote the human-anchored tables over the blind-agent tables (they now go to data/dataset/results_tables_human_override.md, as the README states).
- PENDING-CODER: the coder's completed sheets, CODER_STATEMENT.md, and the outputs of code/independent_agreement.py are committed.
- PENDING-USER: the release is archived on Zenodo under DOI 10.5281/zenodo.NNNNNNN, cited in the Data and code availability section.

## Reviewer points not covered above

- Reviewer 1 (item 3) and Reviewer 3 (item 4), the accepted-paper projection: Section 5.2 now states that the bootstrap intervals capture sampling variation in the source-level rates only, not the structural uncertainty of transferring rates estimated across all submissions to the accepted papers, which is not quantified, and that the projection is subordinate to the detected figures; Section 6 repeats this where the projection is mentioned, and the 82-84% paper-level expectation is described as subordinate to the detected rate.
- Reviewer 1 (item 6) and Reviewer 3 (item 7), the non-resolving DOI in Section 5.7: it is a placeholder identifier quoted from submission 148. It is now typeset with a space before the slash and an explanatory note, so that automated reference checkers no longer read it as a citation of this paper.
- Reviewer 1 (item 7): Section 5.3 now states that the precision figures describe the listed example references and the paper-level flag, not every reference the checker flagged, since the organisers published examples rather than the checker's full output.
- Reviewer 3 (item 6), the competing interest: the disclosure is unchanged; the author operates the venue and the automated review pipeline was not modified for this submission.

## Other changes

- The abstract was shortened by a few words to stay within the length limit after the wording change in item 4.
- code/make_coder_sheets.py, code/independent_agreement.py, data/adjudication/blind/CODER_STATEMENT.md and README.md were added; data/adjudication/blind/INDEPENDENT_CODER_INSTRUCTIONS.md was revised to require a coder with no connection to the study and to ask for sheet B first.
