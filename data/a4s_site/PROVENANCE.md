# Agents4Science 2025 public data — provenance

Downloaded 2026-09-28 (UTC) from https://agents4science.stanford.edu/data/ (Apache directory index; files are loaded by
https://agents4science.stanford.edu/submissions.html via submissions.js). The organizers' report (Bianchi, Queen, Thakkar,
Sun, Zou; arXiv:2511.15534; Nature Biotechnology 2026) states that all submitted papers, reviews, checklists and
recordings were made public at that site.

Files:
- papers.csv / papers_with_ids.csv — 247 reviewed submissions: title, OpenReview forum link, AIRev1-3 scores (1-6),
  Human_score, status (accepted/rejected), autonomy A-D for hypothesis_development / experimental_design /
  data_analysis / writing, primary/secondary topic; papers_with_ids adds paper_id (OpenReview submission number).
- ai_involvement_checklist_responses.csv — 316 rows (all submissions incl. desk-rejected): checklist answers +
  explanations + ai_limitations_description, extracted by the organizers from PDFs.
- agent_use.csv — Paper ID -> agents/models/platforms used (organizer-extracted).
- gold_agent_desc.csv / gold_agent_descriptions_filtered.md — agent descriptions per paper.
- ai_limitations.csv / ai_limitations_descriptions*.md — free-text AI limitations per paper.
- clf_results.csv — LLM topic classification per PDF filename.
- codebase_audits_results.csv — 49 code audits (+ per-paper reports at data/code_audits/reproducibility_reports/).
