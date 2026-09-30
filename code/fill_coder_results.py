"""Fill the independent coder's results into the manuscript.

Usage (from anywhere), after the coder's sheets are saved in data/adjudication/blind/:
    CODER_ROLE="a <role>, with no connection to the study or to Publish.fun" python code/fill_coder_results.py [--dry-run]

Runs code/independent_agreement.py, requires sheet B to be fully coded (all 45 items; set ALLOW_PARTIAL=1 to override),
then replaces the placeholder sentences in paper/paper.md (Section 4, Section 5.1, Section 7, the abstract), regenerates
Appendix A.1 to A.8 with code/make_appendix.py, and writes paper/coder_results_paragraphs.md with the paragraphs for the
response letter. Each placeholder must occur exactly once; once replaced the script reports that they are gone."""
import os, sys, json, subprocess, re
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'); os.chdir(ROOT)
DRY = '--dry-run' in sys.argv
role = os.environ.get('CODER_ROLE')
if not role: sys.exit('set CODER_ROLE, e.g. CODER_ROLE="a doctoral student in computer science, with no connection to the study or to Publish.fun"')
subprocess.run([sys.executable, 'code/independent_agreement.py'], check=True, stdout=subprocess.DEVNULL)
J = json.load(open('data/dataset/independent_agreement.json')); S = J.get('summary', {})
if 'B_first' not in S or (S['B_first']['n'] < 45 and not os.environ.get('ALLOW_PARTIAL')): sys.exit(f"sheet B is not fully coded ({S.get('B_first', {}).get('n', 0)} of 45)")
if 'sensitivity' not in J: sys.exit('no sensitivity bound in the output; check the sheet')
b, bb, sens = S['B_first'], S.get('B_blind'), J['sensitivity']
def pct(x): return f'{x:.0f}%'
def ci(v): return f'{v[0]:.0f}-{v[1]:.0f}'
def svp(k):
    x = sens[k]; return f"{x['median']:.1f}% ({x['lo']:.1f}-{x['hi']:.1f})"
def kk(st, k): return f"kappa {st[k]:.2f} ({st[k + '_ci'][0]:.2f}-{st[k + '_ci'][1]:.2f})"
def sv(k, f='{:.0f}'):
    x = sens[k]; return f"{f.format(x['median'])} ({f.format(x['lo'])}-{f.format(x['hi'])})"
robust = abs(sens['fabricated_refs']['median'] - 513) / 513 <= 0.10 and abs(sens['reviewed_papers_fab_pct']['median'] - 37.8) <= 4
stricter = sens['fabricated_refs']['median'] >= 513 and sens['reviewed_papers_fab_pct']['median'] >= 37.8   # the coder's labels raise the counts
verdict = ("The detected figures are therefore robust to the coder's disagreements." if robust else
           ("The coder's reading is stricter than the adjudication where they differ, so the detected figures remain lower bounds under the coder's labels as well; the relabelled values are reported alongside them in Sections 5.2 and 5.3." if stricter else
            "The detected figures should therefore be read with these bounds, which are used in Sections 5.2 and 6."))
A_coded = 'A_first' in S
# ---- sentences
s4 = (f"sheet B was coded by {role}, working from the reference strings alone; the coder's statement "
      f"(data/adjudication/blind/CODER_STATEMENT.md) records that no other file was opened, that no AI assistant was used and that no item was discussed with the author before coding ended. "
      + ("The coder also coded sheet A. " if A_coded else "Sheet A was not coded by the independent coder. ")
      + "Agreement is reported in Section 5.1 and Appendix A.8, together with the sensitivity of the detected figures to the coder's labels.")
s51 = (f"; the independent coder's sheet B gives the directly estimated, non-enriched figure, which supersedes it: on the {b['n']} randomly sampled manual decisions the coder agreed with the first adjudicator on "
       f"{pct(b['cat_pct'])} by category (95% CI {ci(b['cat_ci'])}; {kk(b, 'cat_kappa')}) and on {pct(b['fab_pct'])} for fabricated-versus-not ({ci(b['fab_ci'])}; {kk(b, 'fab_kappa')}) (Appendix A.8)")
if bb: s51 += f"; on the {bb['n']} of these items that were also blind re-adjudicated, agreement with the blind agent was {pct(bb['cat_pct'])} by category and {pct(bb['fab_pct'])} for fabricated-versus-not"
if A_coded:
    a, ab, aa = S['A_first'], S['A_blind'], S['A_author']
    s51 += (f". On the boundary-enriched sheet A the coder agreed with the first adjudicator on {pct(a['cat_pct'])} by category and {pct(a['fab_pct'])} for fabricated-versus-not, "
            f"with the blind agent on {pct(ab['cat_pct'])} and {pct(ab['fab_pct'])}, and with the author on {pct(aa['cat_pct'])} and {pct(aa['fab_pct'])} (Appendix A.8)")
s51 += (f". Relabelling every manual decision with the coder's label distribution given the first adjudicator's label ({J['n_sim']} simulations; Appendix A.8) gives "
        f"{sv('fabricated_refs')} fabricated references against the 513 detected and {sv('invented_refs')} invented against 286; {svp('reviewed_papers_fab_pct')} of reviewed submissions with at least one fabricated reference against 37.8% detected and "
        f"{svp('reviewed_papers_inv_pct')} with an invented one against 23.7%; flag sensitivity {sv('flag_sensitivity', '{:.2f}')} and specificity {sv('flag_specificity', '{:.2f}')} against 0.93 and 0.66; "
        f"Spearman correlations of the fabricated share with the three LLM scores of {sens['rho_fab_llm1']['median']:.2f}, {sens['rho_fab_llm2']['median']:.2f} and {sens['rho_fab_llm3']['median']:.2f} against -0.15, -0.13 and -0.13; "
        f"and {sv('accepted_with_invented')} accepted papers with an invented reference against none detected. "
        + verdict)
s7 = (f"; the independent coding of the random sample (Section 5.1, Appendix A.8) gives the direct figure, {pct(b['fab_pct'])} agreement for fabricated-versus-not ({kk(b, 'fab_kappa')}), and the sensitivity bound "
      + ("shows that the detected figures are robust to the coder's disagreements" if robust else ("shows that the detected figures remain lower bounds under the coder's stricter reading" if stricter else "is carried into Sections 5.2 and 6")) + "; the check's main result,")
sabs = f"an independent human coder agreed with the adjudication on {pct(b['fab_pct'])} of a random sample of 45 manual decisions for fabricated-versus-not (kappa {b['fab_kappa']:.2f});"
s52 = (f" Under the independent coder's labels (Section 5.1), a median of {sv('accepted_with_invented')} accepted papers would carry a reference classed as invented, mostly through the invented-versus-corrupted boundary, the least stable one, so the absence of a detected invented reference among accepted papers is a statement about the adjudication's labels rather than a label-independent fact.")
s53 = (f" Under the independent coder's labels (Section 5.1) the paper-level sensitivity is {sv('flag_sensitivity', '{:.2f}')}, the specificity {sv('flag_specificity', '{:.2f}')} and the example-level precision {svp('flag_example_precision_pct')}.")
R = [("no such coding was\navailable for this version.", s4),
     ("invention. At the paper level, a corruption rate near 8-10% of automatically verified entries would imply,", "invention." + s52 + " At the paper level, a corruption rate near 8-10% of automatically verified entries would imply,"),
     ("bounds the precision over all 285 examples between 47.0% and 56.5%.", "bounds the precision over all 285 examples between 47.0% and 56.5%." + s53),
     (" that the\nreleased 45-item simple random sample of manual decisions has not yet tested.", s51),
     (", and the released 45-item simple random sample of manual\ndecisions, which would test the stratum-weighted 73% and 94% figures directly, is uncoded in this version; the check's main result,", s7),
     ("a 64-item check by the author, disclosed as non-independent, anchors them to one human reading;", sabs),
     ("Of the 513 detected fabricated references, 56% were invented and 44% were corrupted real works; 32 invented references carried a DOI or arXiv identifier.",
      "Of the 513 detected fabricated references, 56% were invented; 32 invented references carried a DOI or arXiv identifier."),
     ("using a reproducible verification pipeline (DOI, arXiv and URL resolution;", "using a reproducible pipeline (DOI, arXiv and URL resolution;"),
     ("(an estimated 34, 14-69, would be expected undetected)", "(an estimated 34, 14-69, expected undetected)")]
md = open('paper/paper.md', encoding='utf-8').read()
missing = [o for o, _ in R if md.count(o) != 1]
if missing: sys.exit('placeholders not found exactly once (already filled?): ' + ' | '.join(repr(m[:60]) for m in missing))
for o, n in R: md = md.replace(o, n)
app = subprocess.run([sys.executable, 'code/make_appendix.py'], check=True, capture_output=True, text=True).stdout
if '### A.8' not in app: sys.exit('make_appendix.py produced no A.8 section')
md = md[:md.index('### A.1')] + app[app.index('### A.1'):].rstrip() + '\n'
ab = md.split('## Abstract\n\n', 1)[1].split('\n\n', 1)[0]
print(f'abstract: {len(ab)} chars' + (' (OVER 3000: trim before submitting)' if len(ab) > 3000 else ''))
para = ['# Paragraphs for the response letter (auto-generated by code/fill_coder_results.py)\n',
        f"Item 1. Sheet B ({b['n']} items) was coded by {role}. Agreement with the first adjudicator: {pct(b['cat_pct'])} by category (95% Wilson CI {ci(b['cat_ci'])}; {kk(b, 'cat_kappa')}) and {pct(b['fab_pct'])} for fabricated-versus-not ({ci(b['fab_ci'])}; {kk(b, 'fab_kappa')})."
        + (f" Against the blind agent on the {bb['n']} items also blind re-adjudicated: {pct(bb['cat_pct'])} and {pct(bb['fab_pct'])}." if bb else '')
        + " By first-adjudicator category: " + '; '.join(f"{k}: coder " + ', '.join(f'{t} {v}' for t, v in c.items()) for k, c in J['sheet_B']['confusion_first_to_coder'].items()) + '.',
        '', ("Item 2. Sheet A (64 items): agreement with the first adjudicator " + f"{pct(S['A_first']['cat_pct'])}/{pct(S['A_first']['fab_pct'])}, with the blind agent {pct(S['A_blind']['cat_pct'])}/{pct(S['A_blind']['fab_pct'])}, with the author {pct(S['A_author']['cat_pct'])}/{pct(S['A_author']['fab_pct'])} (categories/fabricated-versus-not)." if A_coded else 'Item 2. Sheet A was not coded by the independent coder; the manuscript says so in Section 4.'),
        '', 'Item 3. Sensitivity table (data/dataset/independent_agreement.md):', '',
        open('data/dataset/independent_agreement.md').read().split('## Sensitivity', 1)[1].split('\n', 1)[1].strip(), '',
        ('Verdict: the detected figures are robust to the coder\'s disagreements (median relabelled counts within 10% of the detected ones).' if robust else 'Verdict: material disagreement; the bounds are carried into Sections 5.2 and 6 and the abstract.')]
open('paper/coder_results_paragraphs.md', 'w').write('\n'.join(para) + '\n')
if DRY: print('\n'.join(para)); print('\n--- Section 4 ---\n' + s4 + '\n--- Section 5.1 ---\n' + s51 + '\n--- Section 5.2 ---\n' + s52 + '\n--- Section 5.3 ---\n' + s53 + '\n--- Section 7 ---\n' + s7 + '\n--- Abstract ---\n' + sabs); sys.exit(0)
open('paper/paper.md', 'w', encoding='utf-8').write(md)
print('manuscript filled; letter paragraphs in paper/coder_results_paragraphs.md; robust =', robust)
