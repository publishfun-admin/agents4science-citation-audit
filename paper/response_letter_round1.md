# Response to the editor and reviewers (round 1)

We thank the editor and the three reviewers. The revision adds the validation that all three reviewers asked for, corrects an error in our own reference list, fixes a parser failure that the reviewers' question about completeness led us to find, and reworks the results around a robust secondary outcome. The main changes are:

1. **Blind validation of the labels (Sections 4 and 5.1).** A second, independent agent instance, given only the reference strings and the protocol and barred from the audit's data, re-adjudicated 150 sampled decisions: a stratified sample of 90 (30 NOT_FOUND, 30 EXISTS_CORRUPTED, 30 EXISTS) and a boundary sample of 60 (35 EXISTS_CORRUPTED, 25 EXISTS). Category agreement is 83.3% (Cohen's kappa 0.75) and fabricated-versus-not agreement 92.0% (kappa 0.83); on the boundary sample alone 81.7% (kappa 0.66) and 90.0% (kappa 0.79). The disagreements are almost all between adjacent categories, and the NOT_FOUND versus EXISTS_CORRUPTED boundary is the least stable, which is why the two are pooled in the primary outcome. Samples, blind decisions and comparison tables are released (data/adjudication/blind/).

2. **Blind check of the automatically verified entries (Sections 4, 5.1, 5.2 and 7).** The same design applied to 180 automatically verified entries (stratified by verification source) found 17 (9.4%; 95% CI 6.0-14.6) real works cited with a wrong author list, venue or identifier and 2 (1.1%) invented works, concentrated in title-based Crossref matches. We now report the adjudicated fabricated share as a lower bound, an adjusted estimate (reviewed submissions 7.2% -> 15.9%, 95% CI 13.2-21.2), and the wholly invented share (3.8% of references, 23.7% of reviewed submissions), which the blind check shows to be robust, alongside the primary outcome in every analysis.

3. **Our own reference list.** Every reference was re-verified at the author, title, venue and year level against the arXiv and Crossref records. The author list of Bianchi et al. now reads "Eric Sun"; two author lists that had been abbreviated with "et al." for a fourth author are given in full; the Rao and Callison-Burch entry notes the version-1 title; Phantom References (Russinovich et al.) and CiteAudit (Shi et al.) are added and discussed. The sentence in Section 6 about how our references were verified now says what was done and what the first version had let through.

4. **Parser completeness (Sections 4, 5.1 and 7).** The reviewers were right to ask. Extending the recall check to author-year lists showed that the CRF finder had merged several references into one entry in 31 hanging-indent lists (14 references parsed as one in the worst case). Parser v4 segments such lists by indentation or blank lines and re-joins wrapped lines; 32 submissions were re-parsed and re-verified, 160 references were added, existing decisions were remapped by reference text (decisions whose entry no longer exists were retired to data/adjudication/retired_decisions.csv), and the newly unverified entries were adjudicated (53 new decisions; 857 in total). Section 5.1 reports recall for all three list styles and the residual, and Section 7 gives the sensitivity of the headline rates to it and to the PLACEHOLDER and UNADJUDICABLE classifications.

5. **The 27 unmatched flagged examples (Section 5.3).** After re-parsing, 258 of the 285 examples match a parsed entry. Each of the 27 unmatched examples was examined (data/dataset/unmatched_flags_verdicts.json): 17 correspond to a verified or adjudicated-real entry rendered in different words by the checker's extraction step, 7 have titles that do not occur in the submitted PDF, 3 are indeterminate; none is itself the title of a work known to Crossref. Precision is bounded between 47.0% and 56.5% over all 285 examples, and the statement about accepted papers is now restricted to what was adjudicated.

6. **Section 5.6 accounting.** Reconciled against the released per-sentence classification: 6 of the 91 affected reviewed submissions have an explicit statement, in 4 the reviewer's own finding and in 2 an echo of the authors' disclosure; every statement is attributed; the informal "as often wrong as right" is replaced by the precision it implied (4 of 7). One keyword hit that concerned the paper's subject matter and one reviewed-but-withdrawn submission are excluded, and the analysis script now computes these counts from the classification file so that text and tables agree.

7. **Corpus counts (Section 3).** The organisers' 62 incomplete and 253 complete submissions reconcile with OpenReview's 61 desk rejections and our 250 reviewed submissions if one withdrawn submission was incomplete and three complete submissions were withdrawn before review; Section 3 now says so.

8. **Cross-study comparison (Section 6).** The claim that the gap is "too large to be an artefact of method" is removed. We now report a strict identity-level definition comparable to Russinovich et al. (invented works or wrong author lists): 5.3% of references and 29.9% of reviewed submissions (20.3% with two or more), against roughly one accepted NeurIPS or USENIX Security 2025 paper in twenty; accepted Agents4Science papers have 3 such references in 3 of 48 papers.

9. **Pre-specification timing (Section 4).** Commit hashes and timestamps are given: plan and protocol at 21:16 UTC on 28 September 2026, first decision at 21:38 UTC, PLACEHOLDER amendment at 21:48 UTC after 85 decisions (the first 85 decisions contain no placeholder).

10. **Reviewer-slot mapping and associational framing (Sections 3, 5.5, 5.6 and 6).** The mapping of slots to GPT-5, Gemini 2.5 Pro and Claude Sonnet 4 is stated as an inference from published means, and model-specific claims are phrased as "the slot identified as". The acceptance and score results are framed as associations, with the selected human-review sample noted. Logistic diagnostics are reported (convergence, standard errors, 95% CI, the quasi-separation above a 10% share, a non-converging indicator model and a binary model with odds ratio 0.22).

11. **Identifier examples (Section 5.7).** The quoted placeholder-pattern identifiers are marked as examples from the audited submissions, with submission and entry numbers and what each resolves to.

12. **Competing interest.** The disclosure stands; the venue's review pipeline was not modified for this submission, and the editor and reviewers were the venue's standard automated panel.

## Point-by-point

### Desk editor

- Non-resolving DOI and unrelated arXiv identifiers quoted as examples: addressed (item 11).
- Title drift in Rao and Callison-Burch: reference entry gives both titles (item 3).
- Single adjudicator: addressed (items 1 and 2).
- Section 5.6 inconsistency and unattributed statement: addressed (item 6).
- Search channels changed mid-adjudication: Section 7 now notes that the blind adjudicators used registry APIs and web search throughout and agreed with 26 of the 30 sampled NOT_FOUND decisions, which bounds the effect.
- Phantom References not cited; magnitude claims: addressed (items 3 and 8).
- Competing interest: item 12.
- Human-expert correlation on a selected subsample: Sections 5.5 and 7 (item 10).
- Logistic-regression separation diagnostics: item 10.

### Reviewer 1 (score 5, major revision)

- W1/Q1 independent validation and a checked sample of automatically verified entries: items 1 and 2.
- W2/Q2 completeness for unnumbered lists and sensitivity: item 4.
- W3/Q3 the unmatched flagged examples: item 5.
- W4/Q4 Section 5.6 accounting and reviewer identity: items 6 and 10.
- W5 acceptance model supports an association: item 10.
- W6 cross-literature magnitude: item 8.
- W7/Q5 timing of the plan and amendment: item 9.
- W8 the DOI example: item 11.
- W9 the release cannot be verified from the evidence: the repository was private during review at the author's request and will be public at publication; the revised outputs (per-question numbers, blind-check tables, unmatched-flag verdicts) are included in the released files.

### Reviewer 2 (score 8, accept)

- Q1 agreement with independent adjudications: item 1 (against a blind agent instance, not human coders; stated as such).
- Q2 whether the LLM reviewers were told to verify bibliographies: the organisers' report says the three reviewers shared one prompt calibrated to track human scores and mentions no instruction to verify references, and the reviewers had no retrieval tools; Section 6 now says this.
- Q3 placeholders: none is a LaTeX-template remnant; Section 5.7 now describes the five kinds of stub the writing agents left.
- W1-W4: items 11, 1, 10; the single-venue limitation is kept in Section 7.

### Reviewer 3 (score 6, major revision)

- W1/Q1 single adjudicator: items 1 and 2.
- W2/Q3 the "Xian Sun" error and author-level checking of our references: item 3; Section 6 discusses it as an instance of the failure mode the paper studies.
- W3/Q2 the unmatched flagged examples: item 5, with per-example evidence released.
- W4/Q4 RefChecker and CiteAudit, and the identity-level comparison: items 3 and 8.
- W5 the non-resolving DOI: item 11.
- W6 conference-level facts not verifiable from the evidence: the 56% figure is the complement of the organisers' statement that "approximately 44% of submissions have no hallucinated references (111 papers)"; submission counts, reviewer means and the arXiv propagation of submission 147 are documented in the released data and notes.
- W7 cross-definition comparison: item 8.
- Q5 sensitivity to PLACEHOLDER and UNADJUDICABLE: Section 7 (item 4).
