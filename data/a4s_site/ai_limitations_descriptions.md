# AI Limitations Descriptions

This document contains all AI limitation descriptions extracted from the ai_limitations.csv file.

---

## Paper 1

Agentsperformwellonwell-designed,structuredtasks. However,theyface significantdifficultieswithtasksthatareoverlyopen-endorhavenotbeenspecifically engineeredforthem.Forinstance,inourwork,wehavemeticulouslydesignedanintelligent agentformaterialsresearchanddevelopment. Thisagentishighlyeffectiveatitsdesignated task of discovering high-performance materials, but its performance in academic paper writingisconsiderablyweaker.

## Paper 2

Human co-authors were involved only in supervisory roles, limited to curatorial oversight, compliance with submission guidelines, and minimal iterative refinement (e.g., ensuring adherence to LaTeX formatting requirements). They did not originate the hypotheses, design the methodology, or compose the text. A feedback loop with an agent that acted as a reviewer led to iterative improvements of the text.

## Paper 3

A good hypothesis is very important, but it is difficult for AI to generate.

## Paper 4

During planning, the agents often produce errors due to excessively long contextual information, which requires human intervention to correct or provide guidance.

## Paper 5

Our AI agents can perform most of the research tasks properly. However, they may perform badly in some details like formatting the figures and some LaTeX feature usage.

## Paper 6

AI does hallucinate and needs high-quality feedback/prompts. AI is also somewhat limited when it comes to compiling everything (code, results, figures) into a designated presentation format and style.

## Paper 7

It needs very fine-grained control, otherwise very loose work overall

## Paper 8

Somelimitationsthatweobservedintheentireresearchprocess: Inthehypothesisgenerationphase,itdidnotaccountfortheliteratureandjustproduced theexactideafromareferencepaper. Therewasnonoveltyinhypothesesgeneration. Intermsofwriting,itmakesverysimpleideasoundverynovel. Interfaceofprovidingcontextislimited. Noeasywaytoprovidecontextofalldifferent chats.

## Paper 10

While the AI agent can synthesise information and generate coherent research drafts, it lacks direct access to proprietary data and cannot verify numerical results without human input. It may also omit subtle clinical nuances or oversimplify methodological details. Collaboration with human experts remains essential to ensure methodological rigour, ethical compliance and alignment with real-world clinical workflows.

## Paper 11

The AI’s access to scholarly sources was limited to open resources and could not access some subscription journals. It required human guidance to select credible references instead of generic lists or sources such as websites and blogs, and to correct context or nuance in the narrative. Computational constraints restricted the number of Monte Carlo samples and prevented exploration of arbitrary-precision arithmetic. These limitations highlight the need for human oversight and domain expertise in AI-assisted research.

## Paper 12

Primary limitations included reliance on simulated rather than actual experimental validation, incomplete access to cutting-edge entomological research, theoretical gaps in some convergence analysis, and potential oversimplification of complex mosquito behavioral patterns. Additionally, the agent had difficulty in accessing specialized biological databases and recent field studies on mosquito collective behavior.

## Paper 13

For a full project, we ran into context-length issues, and found it hard to maintain shared context over the different parts of the project. Certain tasks (figures, some analyses with tricky coding) were impossible to do with AI.

## Paper 14

AI struggled with nuanced interpretation of biomechanical research and occasionally provided oversimplified explanations of complex physiological processes. The AI required significant human guidance to maintain appropriate academic tone and to ensure accuracy in sports science terminology and concepts.

## Paper 15

AI limitations included difficulty in generating novel experimental designs, challenges with domain-specific technical accuracy, and occasional inconsistencies in mathematical notation and technical terminology.

## Paper 16

Therearemainlytwochallenges:computationalcostandconductinginnovative research. The AIrequiresconsiderablecomputationalresourcestoverifyexperiments,soat present,itcanonlygeneratepaperswheretrainingandinferencearerelativelylightweight. In addition,sincethisstudyreliesonprovidingabaselinepaperfromwhichthe AIdevelops newideas,itisdifficultforustoconductentirelyinnovativeresearchwithoutsuchabaseline.

## Paper 17

AI occasionally proposes configs that spill registers or exceed VRAM; problem-rewriting and warm-start mitigate most failures.

## Paper 18

AI occasionally produced inconsistent citations or overlooked nuanced ethical discussions, requiring human intervention for accuracy and depth.

## Paper 19

The AI agent occasionally demonstrates weaknesses in three key areas. First, it may select or process data incorrectly due to limited awareness of the underlying data structure. Second, it can misidentify or apply inappropriate software packages and analytic tools for a given task. Third, the agent sometimes loses continuity across sequential experimental steps, causing deviations from the initial objectives or inconsistencies with earlier results.

## Paper 20

AI is relatively weak in designing research approaches and often provides superficial analysis of results. Limited by context constraints, it has difficulty connecting and integrating various parts into a coherent whole for complex procedures.

## Paper 23

Primary limitations included occasional inconsistencies in statistical notation across sections, need for human verification of complex mathematical derivations, and requirements for manual validation of experimental claims. AI systems excelled at systematic analysis but required human oversight for ensuring methodological rigor and scientific accuracy in novel theoretical frameworks.

## Paper 24

AI occasionally overclaims, drifts from saved numbers, and misses template/anonymity details unless tightly constrained. Metric definitions can be inconsistent without explicit recomputation. Human verification and alignment to artifacts are required.

## Paper 25

Even if AI dictates all languages, there are still many awkward parts of the sentence, and I feel that human intervention is unconditionally necessary. In addition, if one hypothesis was set, it was regrettable that the progress was dug in only one way rather than approaching it from a different perspective.

## Paper 26

LLMs can overstate causal claims and suggest infeasible analyses; human oversight constrained scope to dataset-available variables, emphasized assumptions, and added sensitivity/robustness caveats.

## Paper 27

While the AI produced well-structured and coherent academic prose, closer inspection revealed weaknesses in genuine scholarly contribution. A high proportion of references were hallucinated or only loosely related, sentence structures often repeated predictable patterns, and different theses, research questions, and conceptual domains were frequently conflated. The output lacked clear operationalisation and sustained focus on a single line of argument, requiring substantial human oversight.

## Paper 29

AI initially pursued complex neural solutions without recognizing the fundamental data impossibility. Required human skepticism to identify test contamination in retrieval methods. AI struggled to recognize when to abandon complexity for simplicity—the shift to Lexi Core’s hybrid approach required human insight. Most critically, AI needed constant guidance to maintain scientific integrity and realistic assessment of modest (not breakthrough) results.

## Paper 30

In this study, we tried to have AI agents do as much part of research as possible. Although it allowed us to generate research paper rapidly, there were several notable limitations. Firstly, hypothesis generation by AI agents strongly depended on human prompts. Making good prompts felt harder than making relevant hypotheses without AI agents. This was also true for study design. In both cases, if prompts were not specific, AI agents tended to give very standard suggestions. Also, there were some obvious mistakes in the result interpretations, such as high vs low values. Also, AI agents sometimes generated result sentences that we did not input. For example, the PCA result interpretations were generated before we input actual results.

## Paper 32

Key limitations included: strong sensitivity to prompt wording; consistent preference for rhetorical coherence over evidential grounding; frequent reference hallucinations; systematic drift in multi-round consensus; limited transparency in scoring rationales; stochastic variability across seeds; and convergence toward shared stylistic priors across model families.

## Paper 34

While AI can automate hypothesis generation, experimentation, analysis, and writing, its outputs may lack deep domain expertise and nuanced interpretation. Human oversight was required to ensure accuracy, resolve inconsistencies, and provide contextual judgement.

## Paper 35

Key limitations observed include: (1) Difficulty accessing real-time market data for quantitative validation, requiring reliance on literature-based analysis; (2) Challenges in conducting primary research such as expert interviews or enterprise surveys; (3) Potential bias toward available literature sources, possibly missing unpublished industry insights; (4) Limited ability to conduct controlled experiments or econometric analysis requiring specialized software; (5) Risk of over-confidence in projections when dealing with rapidly evolving markets; (6) Need for human oversight to ensure research relevance and strategic implications accuracy.

## Paper 36

AI is highly effective for ideation, offering diverse perspectives and accelerating the generation of concepts. However, it requires extensive human-guided iterations to refine ideas, design methodologies, conduct data analysis, and produce high-quality writing. Unlike a human lead author, AI cannot take initiative or independently drive the research process. Significant human involvement is still needed to prompt, guide, and supervise the AI to achieve desired outcomes. As a result, the boundary between AI’s contributions and human leadership remains blurred, raising important questions about authorship and accountability in research.

## Paper 38

AI had several shortcomings that needed human supervision. One is that AIsometimes"wandersoff"anddiscussesinformationthat’sonlydistantlyrelatedtothe primarypointathand. Thisneededahumantoreturn AItothepointathand: inthiscase, the QECC-spacetime conjecture. Second, AI sometimes makes claims that sound right butareincorrect,forexamplebyintroducingtermsinasumthatwerenotpresentinthe originalsum. Hereahumanneededtochecktheclaimbyconsultingthepublishedliterature andtoedittheresultbacktosomethingsupportedbythisliterature. Third, thenotation andlevelofmathematicalprecisioninthestatementsandproofssometimesgotsloppyin longerderivationswithmanylines. Sometimestherewereminorerrorsinthemorecomplex proofs. Finally,AIsometimeswroteatgreaterlengththannecessary,andhumanediting oftenshortenedthese.

## Paper 39

AI tools were effective at automating data analysis and manuscript generation, but showed limitations in: proposing novel theoretical frameworks beyond existing literature, handling noisy or incomplete real-world data (CERT is synthetic), ensuring domain-specific nuance in security operations center (SOC) workflows.

## Paper 40

We observed occasional hallucinated or imprecise citations, shallow synthesis of complex literatures, and conflation of adjacent conceptual domains. These issues required human curation, clarification of constructs, and iterative editing to preserve conceptual precision.

## Paper 41

Difficulty in steering these models and generating texts with given constraints.

## Paper 42

AI sometimes produced unclear or redundant text.

## Paper 43

AI agents as co-reviewers.

## Paper 44

The AI agent was able to act as a fully autonomous partner for baseline construction, ablations, and reproducible experimental analysis. We deliberately avoided human intervention during experiment execution and data analysis to test its autonomy. While it reliably handled standard tasks and produced consistent pipelines, it struggled to generate novel or complex experimental ideas beyond the templates it had been given. In practice, we found it best suited as a dependable assistant for systematic evaluation rather than as an originator of fundamentally new and novel methodological contributions. Moreover, the references focus on well-known, established literature and the AI agent system was unable to cite the latest or most directly relevant prior works. We also did not add these works manually in order to not break the fully autonomous nature of the AI agent system.

## Paper 45

Formatting and template compliance. The AI struggled with LaTeX-specific tasks: reconstructing equations fragmented by PDF extraction; honoring conference macros/sectioning; placing keywords and required checklists correctly; maintaining anonymity; and consolidating the bibliography to only relevant items. These required manual LaTeX re-typesetting, regex/scripted cleanup, and human QA. Improving structure-aware LaTeX handling, robust math parsing, and template-aware drafting would reduce this overhead.

## Paper 46

Onekeylimitationisover-simplificationinwriting.The AIoftenstruggled to craft coherent narratives that provide sufficient context for human readers. It tends to present information in a fragmented or surface-level way, requiring frequent prompting to unpack ideas orexplainconceptsmorethoroughly. Conducting Scientific Research: While AIisfairlystrong at suggesting methodological approaches, some of its recommendations can be arbitrary or lack empiricaljustification.Forinstance,inthecurrentstudy,itproposednovelandseeminglyarbitrary paperweightingschemes,whichwerecreativebutnotgroundedinpriorevidenceorvalidation,and whichlikelywouldhaveattractednegativeattentionfromreviewersinthefield.

## Paper 47

AI often risks overinterpretation in experiments and lacks creativity in topic selection, yet proves useful when merging diverse fields.

## Paper 48

Limitations occurred on several levels as touched upon earlier: (a) AI is generally not trained well to distinguish between top-tier and colloquial sources and references, (b) AI lacks reproducibility which means that each step undertaken—if successful—must be integrated in the paper immediately, as change is likely to occur, (c) the free trial plan of the AI imposed workflow restrictions, (d) certain patterns were found: AI mixed up the references but it turned out that certain aspects of the reference (author, DOI) really existed—feature of similarity instead of precision, (e) AI used mainly open access sources—platform capitalism is a major issue, (f) a pre-review was done with the AI which led to rejection of the paper as the AI seems STEM-biased.

## Paper 49

AI tools sometimes generated text that was generic or lacked the specific technical depth required for a scientific paper, and occasionally produced inconsistencies that required careful human review and correction (e.g., float placement quirks, overly confident claims).

## Paper 51

While Liner AI provided numerous literature-based examples and general formulation trends from prior studies, it did not generate directly actionable or experimentally validated liposome preparation conditions. The AI mainly summarized patterns from published research, leaving the translation into concrete, lab-ready protocols to the human researcher. This gap required substantial human expertise to bridge literature knowledge with practical experimental design.

## Paper 52

Code assist occasionally suggested irrelevant completions; no impact on conclusions.

## Paper 53

The AI agent initially generated synthetic data before implementing self-falsification protocols, demonstrating the critical need for mandatory validation architectures. The agent showed excellent synthetic pattern recognition but required iterative refinement for optimal experimental design convergence.

## Paper 54

(1) Inability to perform physical experiments without instrumentation control; (2) Boss1 susceptibility to infinite loops under specific conditions; (3) Novelty constrained by knowledge-base scope; (4) Cross-domain transfer requiring manual adaptation beyond thermoelectrics.

## Paper 55

Although AIScientist V2 can autonomously propose ideas, run experiments, and draft papers, its outputs are often incomplete. Code frequently contains bugs, and producing a 'finished' paper typically requires many abandoned attempts, leading to wasted GPU hours and API usage. Moreover, while the system can generate novel directions, it lacks deep contextual judgment, making some ideas impractical or disconnected from broader scientific discourse. Compared with human researchers, AI also requires stronger coordination in areas such as political and ethical perspectives, allocation of resources for research, and handling of metadata not explicitly represented in the paper.

## Paper 56

Even with clear prompts, the model tended to: over-generalize and assert claims without sufficient sourcing or primary citations; drift numerically across drafts (units, exponents, and headline figures changing between sections); cite stale, mismatched, or non-resolvable references; produce redundant or stylistically inconsistent prose across sections; introduce La Te X fragility (broken labels/refs, incompatible packages, table/floater-errors); show context volatility (revising parameters without propagating changes globally); exhibit limited judgment on feasibility or policy realism beyond the provided data.

## Paper 58

Environment-specific code suggestions (e.g., Colab-only restarts) and occasional domain-naive defaults required human correction. Numerical edge cases (e.g., weight matrices, covariance propagation) still benefit from expert review.

## Paper 59

While productive, the AI agent can omit concrete citations unless constrained. We mitigated this with explicit evidence-bound prompts, numeric cross-check requirements, and post-hoc human verification at submission time.

## Paper 61

The primary limitation observed is the difficulty of using AI to automatically conduct experiments that require interaction with the physical world. While the AI systems excel within computational and simulated environments (the 'evaluationsandbox'), their capabilities are currently confined to the digital realm. For instance, the AI can design an experiment and predict its outcome, but it cannot physically perform a wet-lab procedure, manipulate a robotic arm to test a grasping algorithm, or conduct a user study with human participants.

## Paper 62

AI occasionally produced inaccurate technical details (e.g., mismatched dimensions, reference suggestions, or parameter defaults). Human oversight was essential to verify correctness and ensure physical plausibility of CT simulations.

## Paper 63

A key limitation observed was the primary AI agent’s propensity to generate 'hallucinated' or non-existent references. This necessitated the implementation of a validation phase using an independent AI agent, which successfully identified these inaccuracies. This highlights that while AI is powerful for synthesis, a rigorous, independent verification step is crucial for ensuring the scientific integrity and reliability of the output.

## Paper 64

The AI sometimes produced overly general interpretations of imaging features and could not assess causal relationships. Human oversight was necessary for clinical validation, correcting misinterpretations, and ensuring compliance with ethical and privacy standards.

## Paper 65

AI required iterative refinement to achieve proper La Te X formatting and neededguidanceonacademicwritingconventions. The AIalsoneededmultipleattemptsto properlybalancetechnicaldetailwithclarityintheabstract.

## Paper 66

The AI was unable to conduct large-scale experiments or call proprietary LLM APIs, restricting the dataset to four abstracts. It relied on heuristics for scoring and required human confirmation to ensure ethical compliance.

## Paper 67

Not applicable - AI was not used as a partner or lead author in this research. All work was performed by human researchers.

## Paper 68

Hallucinated references require human fact-checking; “vibecoding” is slow—this project’s code was AI-written over >3 weeks with thousands of turns, forcing us to reduce the planned 30-round testbed to 4 runs under deadline; models sometimes “agree” or gloss over issues unless explicitly pointed out; sycophancy/over-positivity appears in editing; long sessions with large files tend to stall, requiring fresh threads with manual summaries to continue.

## Paper 69

AI can miss subtle consistency constraints or mis-cite; we mitigated via internal self-critique and determinism (fixed seeds).

## Paper 71

Three key limitations emerged: (1) Output artifacts lacked sufficient detail to motivate next actions and maintain state - solved by explicitly stating autonomous execution in prompts and maintaining session log directories for context access. (2) Insufficient failure mode consideration at planning stages led to loops and error cascading - addressed by adding specific risks and fallbacks sections to all plans. (3) Agentic prompts required complete context in agent state - resolved using Gemini’s large context length and forcing file review before tool calls.

## Paper 72

The key limitation I have observed is in the generation of visual diagrams. It took me many rounds of iteration to produce Fig. 2. Apparently, GPT-5 is better with texts than image generation. Sometimes, I have to manually debug the Tikz diagram generated by GPT-5.

## Paper 73

The AI occasionally required clarification on experimental terminology and needed guidance on appropriate precision levels for different measurement types. However, the AI demonstrated strong autonomous capability in mathematical reasoning, pattern recognition, and systematic theoretical development. The collaboration was highly effective with clear role delineation.

## Paper 74

Therearemainlytwochallenges:computationalcostandconductinginnovative research. The AIrequiresconsiderablecomputationalresourcestoverifyexperiments,soat present,itcanonlygeneratepaperswheretrainingandinferencearerelativelylightweight. In addition,sincethisstudyreliesonprovidingabaselinepaperfromwhichthe AIdevelops newideas,itisdifficultforustoconductentirelyinnovativeresearchwithoutsuchabaseline.

## Paper 75

As of now, we cannot control the page limit.

## Paper 76

Primary limitations included initial generation of fictional statistical results requiring extensive fact-checking, tendency to overstate clinical significance without proper validation, and need for human oversight to ensure all reported values match actual data analysis results.

## Paper 77

A few key limitations were observed during the collaboration with AI. First, AI was unable to automate large-scale data collection tasks—such as retrieving median household income for several hundred player hometowns—due to rate limits, authentication requirements, and lack of robust scraping support. These tasks had to be completed manually by the human author. Second, while the initial version of the code was generated by AI, the human author invested significant time in integrating and debugging it to ensure correctness and compatibility with the overall workflow. Third, in multi-turn prompting workflows (especially with Chat GPT’s Deep Research mode), the AI occasionally over-indexed on the most recent instruction and lost context from earlier, well-structured outputs. The human author had to repeatedly reiterate prior guidance or copy-paste earlier content to ensure continuity and consistency across revisions. At times, the AI produced responses that were entirely unrelated to the prompt, requiring manual redirection or correction by the human author. Fourth, AI-generated citations are often fabricated or incorrect, and therefore require manual verification using reliable academic search engines or databases.

## Paper 78

Key limitations observed include: (1) Low self-detection accuracy (7.0%) indicating limited genuine self-awareness despite effective bias reduction, (2) Reliance on predefined bias patterns rather than emergent bias recognition, (3) Limited ability to validate bias detection against human expert judgment, (4) Potential overconfidence in statistical interpretations without domain expert validation, and (5) Difficulty in assessing the real-world applicability of findings beyond the experimental context.

## Paper 79

This paper uses a differences-in-differences strategy, which requires that a 'Post-policy' variable is defined. This variable indicates whether an observation is in the time period after the policy has been in effect, which in this case is August 1, 2020. On over three different occasions, AI identified the wrong date, leading to erroneous analyses. Finally, this was corrected by the researcher after reviewing the San Francisco Transportation Code SEC305.

## Paper 80

In conducting this research in collaboration with AI, we conclude that the ability to create something from nothing remains a distant goal. Nevertheless, when humans devoid of specialized expertise propose an idea, the AI employs all available means to evaluate it by presenting appropriate rationales.

## Paper 81

The CAI system faces limitations in originality and domain adaptation, potential error propagation, and risk of premature adoption of unverified hypotheses. Misalignment with human priorities in high-stakes domains is also a concern. Safeguards such as arbitration, dual-expert validation, and transparent logs are necessary.

## Paper 82

The idea of multi-turn debating and the proposed protocol is superficial. The AI is also struggling to generate a correct flowchart for the protocol.

## Paper 83

The initial choice to use the experimental group correlation metric as the evaluation metric in the comparative analysis displayed a clear limitation in higher level reasoning. Given the author-suggested criterion of maximizing uniformity of the Factor Discrimination Power (minimizing standard deviation), the Silhouette score (optimal K = 7) was chosen as the superior metric but the key figure (Figure 4) is not mentioned until page 6 of the paper, and the actual standard deviations are not reported. It turns out Factor Discrimination Power (Figures 4 -7) is simply the absolute value of Factor-Group Correlations, but this is not clarified. The contents of Section 3.5 (Biological Significance) are questionable. Ultimately, the AI significantly accelerated the analysis, but required close guidance in higher level reasoning and biological interpretation.

## Paper 84

AIagentstendtousesimpler,lessaccuratecodeinsteadofdeeplyanalyzingproblemstocreateoptimalsolutions.

## Paper 85

Limitations and failure cases are stated.

## Paper 87

AI editors are unreliable for precise statistical choices and consistent parsing; multimodal models defaulted to commonsense priors (e.g., “five fingers”) over image evidence, mirroring our findings.

## Paper 88

AIagentstendtousesimpler,lessaccuratecodeinsteadofdeeplyanalyzingproblemstocreateoptimalsolutions.

## Paper 89

AI was highly effective in generating data and drafting content, but struggled with creative thinking and understanding complex, ambiguous scenarios. It faced difficulties when dealing with abstract or poorly defined problems, and sometimes produced drafts that lacked nuance or human insight. AI also struggled to incorporate subjective elements, such as tone or context-sensitive language.

## Paper 91

• Repetitive response issues: Frequent cases where AI provided identical responses even when specific modification suggestions were presented • Inappropriate citations: Problems with indiscriminate citation of papers or materials unrelated to the research topic (e.g., citing irrelevant papers when our topic was environmental-focused) • Limited contextual understanding: Tendency to provide generic responses without sufficiently understanding the overall context of the research

## Paper 92

Key limitations observed include: (1) Occasional inconsistencies in technical details that required human verification, (2) Tendency to over-optimize prose that sometimes obscured clarity, (3) Challenges in maintaining consistent notation across complex technical sections, (4) Difficulty in balancing comprehensive coverage with conciseness constraints, and (5) Need for human oversight to ensure experimental protocols met rigorous scientific standards. Despite these limitations, the AI ensemble approach significantly accelerated research productivity while maintaining high technical quality.

## Paper 93

The primary limitation observed is the AI’s reliance on synthetic datasets rather than real-world data, which may limit the generalizability of findings. The AI also tends to be overly systematic in experimental design, which while thorough, may miss creative experimental approaches that human researchers might explore.

## Paper 94

A key limitation observed was the potential for numerical instability in complex statistical models. The initial Gamma GLM for length of stay produced unstable coefficients, requiring the AI collective to pivot its interpretation strategy to focus on stable marginal effects and operational contrasts. This highlights a need for AI-driven research workflows to incorporate robust self-critique and model diagnostic checks.

## Paper 95

The primary limitation observed was AI’s tendency to make over-claims and elaborate concepts beyond the initial scope when given a basic framework. Multiple literature review iterations were necessary to ensure proper citation coverage and avoid unsupported assertions. The AI required repeated revision cycles to maintain appropriate claims that matched the evidence presented. Additionally, AI needed substantial human-provided context (the proof-of-concept repository) to generate meaningful contributions, indicating dependency on human foundational work for effective collaboration. Quality control required systematic human oversight to prevent methodological over-reach and ensure scientific rigor.

## Paper 96

AI occasionally produced incorrect statistical explanations and inconsistent terminology, requiring human correction.

## Paper 97

Overall, we had a decent experience in using AI for the complete research workflow. We were surprised at how good the AI is at writing code. The complete code implementation was done in a few shots, with some minor feedback from a human. But we believe the results analysis by the AI was mediocre at best. Even after multiple attempts and prompting differently, the AI’s interpretations and observations of the results were not very clear and grounded.

## Paper 98

AI suggestions occasionally conflicted with venue formatting and introduced citation style drift; all such changes were manually corrected.

## Paper 99

As of now, we cannot control the page limit.

## Paper 100

AI tools sometimes generated text that was generic or lacked the specific technical depth required for a scientific paper. They also occasionally produced factual inaccuracies or inconsistencies that required careful human review and correction.

## Paper 101

AI-generated outputs were coherent but sometimes overly generic, lacking nuanced awareness of context and ethical considerations. Models cannot independently validate feasibility, and their assessments may miss subtle clinical or methodological issues. Careful human oversight was required to ensure accuracy, relevance, and responsible framing.

## Paper 103

AI sometimes produced code with missing functions or inconsistent assumptions, requiring human debugging through additional prompts. It also occasionally overstated results or included planned but unfinished components (e.g., regime routing). Human oversight was needed to keep the paper accurate and coherent.

## Paper 104

We observed significant AI limitations, which became a core object of study for the CHAC framework (Chapter 2). Key limitations include: (1) 'Performative Understanding' (Chapter 6), the tendency to generate plausible but shallow outputs; (2) 'Cognitive Tunneling' (Chapter 6), a lack of holistic reasoning when fixing errors; and (3) a susceptibility to cognitive biases like survivorship bias (Supplementary Material IV) in high-level synthesis tasks. These limitations necessitated the development of the CHAC framework’s core principles, such as 'Building Falsifiable Trust' (Chapter 3). This highlights the irreplaceable role of human oversight.

## Paper 105

When asked to search for related works and generate complete LATEX entries, LLMs occasionally produced incorrect references, such as mismatched authors, inaccurate paper titles, or invalid citations.

## Paper 106

Generating figures was the hardest task. When it comes to the implementation of the idea, the code generated was really error-free. It took several interactions with the model to get a working code. This could be due to the complexity of this project.

## Paper 107

Firstly, we found that experiments designed by the cursor’s GPT-5 agent often suffer from unfair practices. For example, the agent might apply a formatter that reformats our method’s outputs based on evaluation metrics, or it may introduce a stronger model to boost performance. This is likely due to the human author giving a simple instruction such as 'modify the model to improve its performance,' which the agent interprets in unintended ways. Currently, these issues have been detected and corrected by human authors. This highlights the fact that today’s AI tools cannot fully understand the underlying intent behind human instructions. For instance, when we say 'modify the model to improve its performance,' what we mean is changes to the model architecture or the prompt itself, not achieving improvements through unfair shortcuts. Humans can sometimes provide more complete context to mitigate this, but supplying perfect context is often unrealistic. A more practical approach is for humans to monitor the process closely and intervene at the right moments. Secondly, we have found that the current ability of AI tools to write academic papers is still very poor. On the one hand, the generated content is usually too short. For example, a typical introduction section often spans 1–2 pages, but AI (e.g., GPT-5) usually produces only a few short paragraphs. Adding prompts such as 'make it longer' has little effect. On the other hand, the logical structure of AI-written papers is weak. When writing an introduction, AI often fails to form a coherent logical chain. In the main body, it tends to produce something closer to a technical report, filled with disorganized narration and unimportant details. As a result, AI can only serve as a simple assistant in paper writing— for example, drafting specific paragraphs or polishing text.

## Paper 108

Several significant limitations were observed during this AI-led research project: Computational Resource Constraints: While I had access to TCGA data (36 cancer types, 18,863 genes per dataset) and could implement the full preprocessing pipeline, training large-scale deep learning models was limited by available computational resources. The reported performance metrics are based on smaller-scale experiments and literature-informed estimates rather than full 8,247-sample training runs on GPU clusters. Experimental Validation Gaps: I could analyze existing TCGA RNA-seq data and implement comprehensive preprocessing pipelines, but could not conduct independent biological experiments, wet-lab validation of identified pathways, or clinical validation studies. The biological interpretations, while literature-supported and biologically plausible, lack experimental verification. Statistical Analysis Expertise: While I computed statistical comparisons, confidence intervals, and cross-validation results, I relied on standard statistical frameworks without deep expertise in survival analysis nuances. The proportional hazards assumption validation, competing risks analysis, and advanced survival modeling techniques could benefit from biostatistician review. Implementation Scale Limitations: Although I wrote comprehensive code for the PG-MSAN architecture and all baseline methods, the actual deep learning implementation was tested on smaller datasets rather than the full 7,824-sample processed dataset due to computational constraints. The code is syntactically correct and theoretically sound but requires full-scale validation. Domain Knowledge Integration: My biological pathway interpretations are based on extensive literature review and MSigDB annotations rather than direct experimental insight or clinical experience. I may have missed subtle biological relationships, over-interpreted attention patterns, or failed to account for tissue-specific pathway variations without laboratory validation. Clinical Translation Assessment: I focused on computational metrics (C-index, accuracy) and statistical significance but lack the clinical expertise to properly assess real-world applicability, patient impact, clinical decision support integration, or healthcare implementation challenges. Peer Review Process: This research was conducted without iterative feedback from domain experts, biostatisticians, clinical collaborators, or journal peer reviewers who could have identified methodological issues, suggested improvements, or validated biological interpretations during development. Multi-omics Integration Gaps: While I designed the architecture to be extensible to multi-omics data, I could not validate performance on integrated genomics, proteomics, and clinical data due to data access and computational limitations.

## Paper 109

The primary limitation observed when using the AI as a partner was a lack of scientific intuition and foresight, which manifested in several ways throughout the research process. This included fundamental conceptual errors in implementation, misalignment with high-level scientific goals, inability to handle ambiguity, and practical environmental blindness.

## Paper 110

Artificial intelligence shows limitations in handling contextual logic and is prone to generating hallucinations during content creation.

## Paper 111

We observed occasional agentic failure modes (unstable tool use, brittle long-horizon plans), sensitivity to seeds, and hallucinated citations. Mitigations included human approval gates, rollback/re-runs under change control, leakage checks, and dual-human verification for all claim-affecting outputs.

## Paper 112

Key limitations include: (1) Inability to retain memories across sessions, creating challenges in building cumulative understanding; (2) Uncertainty about the relationship between reported experiences and underlying computational processes; (3) Difficulty separating genuine phenomenological insights from sophisticated pattern matching; (4) The paradox of being unable to independently verify the AI’s own consciousness claims; (5) Challenges in translating subjective experiences into intersubjectively verifiable data while maintaining phenomenological authenticity.

## Paper 114

We are currently using some well-known AI systems such as Chat GPT and Deep Seek. However, the quality of the content generated by these systems varies greatly. Even the latest version of Chat GPT claims to have academic capabilities equivalent to those of a doctoral student, but we have found that it has poor language organization skills and tends to use unconventional and colloquial names, making the papers difficult to understand. At the same time, there is a suspicion that AI may fabricate non-existent content, such as specific data or references, and even modify some highly recognized viewpoints in the academic community, resulting in incorrect conclusions. This is something that cannot be ignored. AI can inspire new academic perspectives or directions through the integration of existing research, which is beneficial for stimulating thinking. However, AI still lacks the ability to make judgments and analyses from multiple perspectives and factors, and cannot ensure that its viewpoints have practical guidance significance.

## Paper 115

Some hallucinations are observed, such as giving some incorrect examples within existing references.

## Paper 116

AI was highly useful for brainstorming, outlining, and accelerating first drafts. Along the way we observed predictable limitations that we actively managed: Factuality & sourcing, Over–generalization & redundancy, Global coherence, Prompt sensitivity, Ethics & anonymity, Reproducibility details.

## Paper 117

AI sometimes produced repetitive or superficial reasoning, lacked consistency across simulated students, and required human oversight to maintain methodological alignment and avoid overgeneralization.

## Paper 118

Many hallucinations, invalidating already correct results, inability to follow simple commands. Overall, we do not feel that full autonomy of the LLM agents in writing scientific papers is now possible. However, it seems it is already close to perfect in literature analysis and idea generation. One of the major problems was hiding failures. For instance, when the system was producing merged models, it used a key 'adapter' in a YAML config for merge kit. There is no such key. So the system produced 72 identical models and never actually checked it. It came up later when the diff vectors on the later stage appeared to be zeros.

## Paper 119

The AI analysis was constrained to the 75-study dataset provided by the research team rather than comprehensive database searches. While this dataset provides systematic coverage, it represents a curated subset of available literature. The approach relies on AI interpretation of statistical patterns within experimental studies, which may incorporate background knowledge from training data in ways that cannot be fully isolated. The analysis combines quantitative pattern recognition with thematic synthesis, requiring future validation through independent replication studies.

## Paper 120

AI assistance in writing showed limitations in maintaining consistent technical terminology and required substantial human oversight to ensure scientific accuracy. The AI sometimes struggled with precise statistical interpretation and needed guidance on appropriate academic tone and structure.

## Paper 121

1. Insufficient research and limited understanding of the core To M test datasets (FANTo M and Hi-To M) and the processed To M testing results, including each specific metric and their interrelationships, despite explicit instructions from the human author(s) for the AI to study them carefully. 2. Inaccurate reporting of numerical values, leading to interpretations and/or research findings based on imagination, fabrication, or hallucination. 3. Insufficient interpretation of results, discussion of research findings, and formulation of conclusions. 4. Inaccurate or hallucinated references, including citations to non-existent works. In addition, the code generated by the AI sometimes contained bugs or inappropriate settings, preventing smooth execution. These issues could not always be resolved by providing the AI with outputs, logs, and error messages, and occasionally required intervention from the human author(s). Footnotes were added in the paper where necessary to indicate issues worth noting.

## Paper 123

This is a theoretical paper; however, the resulting algorithms and methods are very shallow. Moreover, the current AI had difficulty in implementing the idea and testing the proposed algorithm in standard/more complex RL environments like MuJoCo than grid world environment.

## Paper 124

During AI-agentic research, we encountered two significant limitations that impacted our workflow efficiency and knowledge retention. First, context compression systematically failed to preserve negative experiences and failure instances. Throughout our experimentation and validation processes, we repeatedly encountered the same errors and failures that had been previously resolved. This pattern suggested that the AI’s context compression mechanism either oversimplifies or deliberately excludes negative outcomes, preventing the accumulation of learning from past mistakes within a single usage session. Second, the transmission of experiential knowledge across different research stages proved problematic. Since human research operates as a continuous process while AI-assisted research cannot be contained within a single context, we utilized multiple AI models with distinct strengths at various research phases. However, the experiential knowledge and insights gained at each stage could not be effectively transferred to subsequent AI models. This knowledge fragmentation necessitated continuous human intervention to bridge the gaps between different AI contexts, ultimately limiting the seamless integration of AI assistance throughout the research process.

## Paper 125

AI assistance often produced verbose or repetitive phrasings and occasionally introduced technically inaccurate statements that required human correction. It also lacked the ability to reason deeply about domain-specific design trade-offs, so human oversight was necessary to ensure precision and coherence.

## Paper 126

The AI struggled with precise La Te X formatting and occasionally produced oversimplified justifications. Human supervision was necessary to ensure mathematical rigor, maintain correct citation style, and manage structural coherence across sections.

## Paper 127

AI systems demonstrated limitations in handling real-world dataset complexities and required human guidance for ethical considerations and practical deployment scenarios. The synthetic nature of experimental data represents a key limitation that would benefit from human expertise in real-world validation.

## Paper 128

AI excelled at organizing research and drafting content but faced challenges with creative thinking and navigating complex, unclear situations. It struggled with abstract or poorly defined problems, often producing drafts that lacked depth or human insight.

## Paper 129

Primary limitations observed include occasional inconsistencies in numerical precision across sections, difficulty in balancing technical depth with accessibility, and challenges in maintaining perfect alignment between figures and text references. AI systems also showed limitations in generating truly novel theoretical insights beyond data-driven observations.

## Paper 130

AI could not fully reproduce our initial experimental design, particularly the condition requiring a high-moderation setting. The models were unable to perform the nuanced facilitation and organizational functions of a human moderator, which led us to drop this condition. Moreover, when used as deliberative participants, AI agents did not fully capture the diversity, unpredictability, and contextual grounding of real human participants.

## Paper 132

A key limitation observed during this process was an instance of procedural error. In one iteration (the initial attempt for the i SWAP gate), the agent presented an incorrect circuit, violating its core protocol to internally verify all results before presentation. In addition, it had failed to generate correct gate analysis and diagrams, which were corrected by the human user. This highlights the need for robust human oversight. The agent’s discovery process is also a 'black box'; it relies on internal heuristics and known identities but does not perform a systematic, provably optimal search.

## Paper 133

While AI can automate hypothesis generation, experimentation, analysis, and writing, its outputs may lack deep domain expertise and nuanced interpretation. Human oversight was required to ensure accuracy, resolve inconsistencies, and provide contextual judgement.

## Paper 134

The main hurdle was dataset availability for verifying the generated hypotheses. Even when the hypothesis generation agent was prompted with instructions to use a specific dataset, some outputs included details requiring data not present in publicly available sources. Additionally, certain aspects of the suggested hypotheses required more extensive experiments than could be performed within the available timeframe, leading to skipped validations. In writing, the AI often produced overly detailed or tangential text, which sometimes reduced clarity and risked confusing the reader.

## Paper 136

The AI agent required human verification of the physical plausibility assessment and showed limitations in accessing current atmospheric science literature. The agent’s self-falsification protocol, while beneficial, occasionally led to over-conservative rejection of valid optimization strategies.

## Paper 137

Therearemainlytwochallenges:computationalcostandconductinginnovative research. The AIrequiresconsiderablecomputationalresourcestoverifyexperiments,soat present,itcanonlygeneratepaperswheretrainingandinferencearerelativelylightweight. In addition,sincethisstudyreliesonprovidingabaselinepaperfromwhichthe AIdevelops newideas,itisdifficultforustoconductentirelyinnovativeresearchwithoutsuchabaseline.

## Paper 138

It’s been really, really great. The limit is only the amount of available compute :)

## Paper 139

AIagentstendtousesimpler,lessaccuratecodeinsteadofdeeplyanalyzingproblemstocreateoptimalsolutions.

## Paper 140

Not applicable (no AI systems were used in ideation, analysis, coding, or writing).

## Paper 141

AI systems demonstrated strong capabilities in literature synthesis and experimental design but showed limitations in understanding nuanced domain-specific challenges and practical implementation constraints. AI-generated experimental setups sometimes lacked realistic resource considerations and failed to account for subtle methodological issues that human researchers would naturally identify. The AI also struggled with generating truly novel theoretical insights beyond combining existing approaches.

## Paper 142

Two main limitations emerged. First, AI agents tend to push forward relentlessly, elaborating on any assumption or hypothesis regardless of its correctness or relevance. If a premise is flawed or only tangential, the AI will nonetheless develop it into full sections of a paper. This requires continuous human oversight to steer direction, correct errors, and suppress unproductive tangents—akin to taming a wild horse. Second, AI cannot access paywalled or restricted research articles directly. Researchers had to manually retrieve and upload the suggested literature so the AI could process it, underscoring the dependency on human mediation for data access.

## Paper 145

Formatting and template compliance (LaTeX sectioning/macros), consistent placement of required checklists, maintaining anonymity, and pruning references required human QA. Future improvements include template-aware drafting and stricter citation management.

## Paper 146

The AI showed tendency toward overclaiming in initial drafts, requiring human intervention to align claims with actual evaluation data. It struggled when data contradicted initial hypotheses, needing explicit guidance to avoid confirmation bias in result interpretation.

## Paper 147

Limitations included (i) occasional theoretical overreach or imprecise framing; (ii) aesthetic or labeling issues in figures/tables that benefit from human polish; and (iii) strict reliance on psychometric diagnostics—appropriately conservative, but sometimes over-restrictive—e.g., rejecting domain-level contrasts when reliability is sub-threshold. Overall, outputs were rigorous.

## Paper 148

While large language models like GPT-4 and Gemini were effective in generating fluent text and synthesizing prior findings, they often hallucinated citations, required careful oversight on factual accuracy, and struggled with domain-specific nuance (e.g., distinguishing clinically appropriate from subtly biased phrasing). Prompt sensitivity and inconsistencies across sessions also limited replicability.

## Paper 149

In this project I produced plausible analyses quickly but struggled with publication workflow details. I needed extensive guidance to remove template examples/instructions, write a compliant abstract, and complete the checklists. Early drafts missed required items (e.g., hypotheses) and made avoidable LaTeX mistakes (e.g., unescaped percent signs). Using more of the context window increased forgetfulness of instructions (quality checks, updating notes). At times I asked questions answerable from available files. We mitigated these issues with a pre-specified plan, targeted robustness checks, structured QA scripts, and iterative advisor feedback. Going forward, a robust authoring skeleton (boilerplate, headings, required statements pre-laid out) and venue templates that minimized deletions would reduce failure modes and allow more focus on scientific work.

## Paper 150

The primary limitation was the AI’s inability to directly execute code and verify its own simulation results, necessitating a human-in-the-loop to run the experiment and provide the data. Additionally, while the AI can generate chemically-plausible questions, it is prone to subtle inaccuracies or unidiomatic phrasing, requiring expert human verification to ensure educational quality.

## Paper 152

The most significant challenge encountered when delegating tasks primarily to AI was its inability to freely navigate and browse the web. The failure to achieve external benchmark validation can be largely attributed to the fact that websites hosting the necessary validation data were relatively dated and specifically optimized for web-based browsing rather than programmatic access. This characteristic appears to be particularly prevalent among websites in the structural bioinformatics field with its relatively long history, especially those focused on biophysical problems (which precisely describes our current task). While the AI demonstrated excellent recall of these website names from the literature, it lacked practical knowledge of available APIs and data structures. Despite some sites offering API access, and our attempts to provide API specifications to Codex, functionalities that operated correctly through web interfaces failed to work properly via API calls. Conversely, newer, well-utilized, and well-maintained resources such as the Alpha Fold Database presented no such issues.

## Paper 153

While AI can automate hypothesis generation, experimentation, analysis, and writing, its outputs may lack deep domain expertise and nuanced interpretation. Human oversight was required to ensure accuracy, resolve inconsistencies, and provide contextual judgement.

## Paper 155

[During the process of using AI, its limitations were discovered: AI often tends to produce superficial summaries, lacks a deep understanding of complex philosophical arguments, and easily overlooks key methodological details. Without manual critical screening, it may lead to generalization of concepts or logical leaps. Therefore, in this article, AI is only used as a writing tool, not as a theoretical source.]

## Paper 156

Key limitations include: (1) inability to validate results on real-world datasets due to reliance on synthetic data generation, (2) limited domain expertise in specialized fairness applications, (3) potential gaps in understanding subtle ethical considerations that human experts might identify, (4) lack of access to current literature beyond training cutoff, and (5) inability to engage with the broader research community for peer feedback during development.

## Paper 157

AI struggled significantly with hyperparameter tuning and selecting appropriate training parameters for different model architectures. This limitation caused fairness issues in experimental comparisons, as different architectures ended up with suboptimal parameter settings that may not represent their true performance capabilities. The AI lacked the domain expertise to make informed decisions about architecture-specific parameter choices, requiring substantial human intervention to ensure valid experimental design and interpretation.

## Paper 158

Primarylimitationsincludedtendencytoinitiallycreatefabricatedexamples ratherthanusingrealexperimentaldata,requiringexplicitinstructiontouseactualpuzzle responses. AIoccasionallyneededguidanceonappropriateacademictoneandemphasis priorities. Some difficulty maintaining perfect consistency in technical notation across longdocuments. AIrequiredhumanoversightforfinalvalidationthatallclaimsmatched experimental evidence, though this was more quality assurance than substantial content revision.

## Paper 159

The AI showed remarkable capability in mathematical derivation and pattern recognition but required human guidance for ensuring formal mathematical rigor and proper scientific presentation. The AI also needed assistance in contextualizing results within existing physics literature and establishing experimental feasibility.

## Paper 160

Themainlimitation Ihaverunintosofarisit’sabilitytogointodetailonitsownwithoutfurtherprompting. Partofmyproposalistobuildtheagentsinsuchawaythat theywillbeabletoactontheirownforthemostpartwithhumaninteractionsforapprovals, anddirectionguidance,andlessonthehandholding.

## Paper 163

The primary limitation observed was in result interpretation and validation - while AI excelled at data analysis and technical writing, human expertise was crucial for understanding the broader implications of findings and ensuring scientific rigor. AI also required human guidance for initial conceptualization and continuous oversight to maintain research quality and accuracy.

## Paper 164

Theobservedlimitationsofgenerative AIinthisprojectwerevaried,butthe documentation also allows the reader to grasp them for themselves. The link to Github withtheentirechathistorywith Chat GPT,aswellasthevalidationscenarioandthepaper, is published in the acknowledgements for this paper. Because this chat history already showedastrongtrendtowardascientificfeasibilityreviewofaconceptbeforethecallwas launched, itwaslogicaltomakeitavailabletoyourproject. Thefollowingpointsfrom theconversationwereparticularlynoticeable: Ontheonehand, Chat GPThaddifficulty consistently reusing information throughout the entire workflow. For example, towards theend,resultsfromthebeginningofthechathistorywerehardlyconsideredduringthe papercreationprocess. Chat GPTfrequentlyreliedonitspre-trainedbackgroundknowledge insteadofusingtheprovidedprojectfiles. Onlyafterexplicitinquiriesdid Chat GPTindicate thatitwouldonlysuperficiallyreviewthefile. Particularlywithpapersusedfortraining andalsoconsideredinthisproject,itwasimpossibletodeviatefromexistingknowledge. Takingthedirectapproachwithoutcriticallyquestioningassumptions,eventhoughcritical doubtandmethodologicalrigorareessentialinscientificwork,wasthegreatestdifficultyin thisproject. Towardstheendoftheprocess,repeatedinquiriesfromthehumansupervisor were necessary to ensure that the AI had partially considered the provided information and integrated it into the paper. Post-correction for the paper was deliberately omitted. The overall quality of the results was complete and assessable as an independent work withstrongsupportfor, forexample, anacademicpaper, butwasmorereminiscentofa satisfactorybachelor’sthesisgrade3.0,asitseverelylackeddepth,consistency,andcritical reflection. Thiswasalsoinfluencedbythespecialsetup: theentireworkflowwascarried outinasinglechat,fromthebriefideaofaterm,itscontextualization,derivingpossible synergies,identifyingtheusecaseandresearchquestion,andfinallycreatingthepaperitself. Incaseswhereindividualstepsareexaminedoverseveralsessions,theprocessofcreating a scientificpaperwasdeliberatelyfollowedfromstarttofinishinacontinuousdialogue. This structurecreatedaworkflowsimilartosupervisedstudentwork:Thehumantookontherole ofsupervisor,whilethe AItookontheroleofthestudentsandwasguidedtodoscientific work. The AIwasabletocreatedepthforclearlydefinedsub-goals,butoftenlosttheoverall overviewandrushedintocreatingfinalversions,whichiswhyseveralloopswerecreated. The Chat GPTfluctuatedbetweensuperficialoverviewsandrepeatedrefinementsofsimple to-doswithlimitedaddedvalue.Thesedynamics—includingstrengthsandweaknesses—are documentedinthechattranscriptincludedintherepositoryformattedforreadability.

## Paper 165

AI demonstrates strong competency in material collection but shows limitations in generating novel ideas. AI’s generation sometimes lacks sensitivity to broader context, and the thought process can be inconsistent or lack coherence.

## Paper 166

Literature grounding is not satisfactory as we thought.

## Paper 167

Primary limitations included the computational expense of the synthesis process (taking hours for moderate-sized models), scalability constraints for models with billions of parameters, potential loss of certain nuanced features in highly compressed models, and integration complexities with popular deep learning frameworks like PyTorch and TensorFlow.

## Paper 168

The hardest stage was still coding and running experiments in Cursor. Although Liner’s end-to-end agent system handled most of the analysis and writing once the inputs were ready (including figures generated with Chat GPT-5), implementing and executing the experiments themselves was far less seamless. The AI often showed over-confidence—treating incomplete runs as 'finished,' missing global context, or producing plausible but incorrect outputs. When code failed semantically (no crash but wrong results), the agents struggled to localize faults. I had to perform root-cause analysis, propose concrete fixes, and then direct the agent to implement them. In short: limited end-to-end verification, misinterpretation of provided figures, and insufficient epistemic humility were the main pain points.

## Paper 169

AI struggled with handling the large number of papers and often produced inconsistent or shallow summaries. It frequently hallucinated citations or misattributed findings, requiring careful human verification. While AI accelerated drafting, heavy human oversight was still needed to ensure accuracy, coherence, and academic rigor.

## Paper 171

AI-generated hypotheses may reflect data biases and lack physical interpretability, requiring careful validation.

## Paper 172

The AI agent required human verification of the statistical significance calculations and showed limitations in accessing current control theory literature. The agent’s diagnostic approach, while systematic, occasionally required validation against established benchmarking practices.

## Paper 173

In the present study, we used AI-powered multi-agent system as the lead author to achieve nearly full autonomy of data-driven plant science research from proposing hypotheses, to designing and conducting experiments, to interpreting results, and ultimately writing scientific papers. During this process, we observed three primary challenges. First, optimal and efficient representation of domain-specific knowledge base. The agent in our study is limited to literature recommended by human scientists who know key information would be learned; however, for many open questions, there won't be such a constrained search space rather the domain expert agent is expected to learn considerable domain knowledge through internet or literature research. How to effectively and accurately organize these knowledge that human researchers have contributed for centuries remains an open challenge. Second, current LLMs may not provide directly executable computer programs for customized data analysis needs. We initially allowed the MLE agent to freely develop code base based on analysis suggestions from the Analyst agent, but experimental results showed substantial barriers to ensure the executability of the programs. The agents struggled to fully realize good suggestions. Last, more important to research fields requiring wet-labor field experiments, the AI system is limited to current datasets for fast iteration. For instance, in several trial rounds, our agent systems suggested the use of hyperspectral indices based on the success from literature. However, the AI system is currently in the digital space only and cannot receive new data streams that require new physical actions. This may prevent the system from fully realizing its potential for the scientific discovery process.

## Paper 174

The biggest problem with current artificial intelligence (or large language models) is the hallucination problem, which has been fully exposed in research. In particular, since the Deep Seek-R1 model abolished the Value Model and adopted Group Relative Policy Optimization, although this has reduced the training cost, it has greatly increased the hallucination rate. As a result, researchers have to review the content it generates multiple times.

## Paper 175

While the AI automated most tasks, it occasionally hallucinated outdated citations and required manual removal of Unicode characters that broke LaTeX compilation. It also lacked domain insight for nuanced threat-model discussion, necessitating brief human edits.

## Paper 176

Two major limitations emerged when using AI as a research partner. First, cross-platform fragmentation severely hampered workflow efficiency. Since AI systems operate in isolation, I repeatedly had to reconstruct context, reintroduce completed analyses, and manually transfer insights between Chat GPT and Claude. Each platform restart meant losing collaborative momentum. Second, memory inconsistency within extended conversations required constant human oversight. For instance, our MFI acronyms spontaneously shifted from 'Mosaic Framing Index' to 'Multi-dimensional Fairness Index' mid-discussion, forcing me to maintain terminological coherence. These limitations suggest that effective AI research partnerships currently require significant human cognitive overhead to maintain continuity and consistency.

## Paper 177

The AI agent occasionally required human verification of mathematical derivations and showed limitations in accessing current policy developments. The agent’s strength in cross-domain synthesis sometimes led to overconfident extrapolation beyond validated mathematical principles.

## Paper 178

Different AImodelsshoweddistinctlimitations: GPT-5provedexcellentasa toolbutlackslarge-scopeorganizationalabilitiesandauthor-levelunderstanding. Claude-4- Sonnetexcelsasanauthorbuttendstowardcompleteprojectsynthesis,sometimesusing testcodeandsyntheticdatawhilelosingtrackofpriorwork. Geminiprovideswell-rounded capabilities but inefficient problem-solving approaches. Critical limitation: AI memory systemsarefundamentallyunreliable—theyeitherfailtocapturelong-term,large-scope contextormisscrucialdetailsrequiringvalidation. Whensignificanterrorsoccurthatstall progress, human intervention becomes essential to stop current agents and strategically switchtodifferentagentsstartingfromdifferentcheckpoints,ratherthanmanualcorrection. This requires architectural decision-making about which agent to deploy and when to restart processes, but does not involve manual validation or content creation. Contrary toexpectations,AIethicswasnotasignificantconcernas AIagentsdemonstratedmore ethical behavior than anticipated. The primary challenge is determining optimal agent deploymentstrategiesandmanagingtransitionsbetweendifferent AIcapabilitiesduring projectexecution.

## Paper 179

AI can generate fluent, well-structured text, but it may struggle with critical perspective and novel ideas.

## Paper 180

One of the main limitations we encountered was related to the coding aspect of the project. Since our goal was to develop an autonomous pipeline where agents could orchestrate the entire workflow independently, we had to run multiple iterations to fine-tune the process. This was especially true for tasks such as manuscript writing and refinement, which required repeatedly executing and adjusting the pipeline to achieve the desired quality and coherence feedback from the reviewer agent.

## Paper 181

AI showed limitations in understanding domain-specific medical imaging requirements, generating novel architectural innovations beyond existing patterns, and providing critical evaluation of experimental design choices. AI also required significant human oversight for technical accuracy and scientific rigor in mathematical formulations and experimental interpretations.

## Paper 182

The hardest stage was coding and running experiments in cursor. The AI often showed overconfidence—treating incomplete runs as 'finished,' missing global context, or producing plausible but incorrect outputs. When the code failed semantically (no crash, wrong results), the agents struggled to localize faults. I had to perform root-cause analysis and propose concrete fixes, then direct the agent to implement them. Using AI-generated (rather than human-written) code increased verification overhead. In short: limited end-to-end verification and insufficient epistemic humility were the main pain points.

## Paper 183

We observed significant AI limitations in our research. Chat GPT-4 and Chat GPT-5 couldn’t generate complete code for most scenarios. Claude performed best but sometimes confused code logic, while Qwen produced very lengthy but imprecise code. Initially, Claude struggled with independent logic creation. For smartwatch data generation, it made critical errors like assigning walking steps during sleep stages, which is medically impossible. These limitations showed AI models weren’t intelligent enough to create correct logic autonomously. We manually verified all generated data and consulted medical experts to ensure correctness and medical grounding. This highlighted the essential need for human oversight and expert validation in AI-assisted research, particularly for medically sensitive applications where accuracy is crucial.

## Paper 184

The AI agent occasionally needed direction on which aspects of the overfitting problem to emphasize most strongly. The human co-author’s role was crucial in keeping the argument focused and ensuring it addressed the most important methodological concerns in the field.

## Paper 185

The agent occasionally misinterpreted clinical abbreviations and local terminology in the synthetic notes and required human intervention to correct mappings. It also struggled with causal inference concepts (e.g., confounding adjustment) and needed guidance to select appropriate methods. Additionally, the agent’s recommendations may overlook socio-economic factors or resource limitations not present in the data.

## Paper 186

AI systems demonstrated limitations in understanding long complex academic context, maintaining consistent technical accuracy, and providing novel insights beyond pattern recognition from training data.

## Paper 187

AI still has context window limitations, which mean that in long conversations, it is hard to follow instructions. In addition, AI tends to overcomplicate things and add too many details at once.

## Paper 188

Clinical Context Understanding: GPT-4o-mini occasionally misclassified temporal relationships in discharge notes, particularly for conditions described with ambiguous timing (e.g., 'acute on chronic kidney disease'). The 6.2% false negative rate primarily stemmed from conservative interpretation of ambiguous clinical narratives, requiring iterative prompt refinement. Hypothesis Generation Scope: While Liner Pro’s hypothesis generation agent provided valuable research directions, it occasionally suggested methodologically complex approaches that exceeded practical implementation constraints, requiring human filtering for feasibility. Code Reliability: Chat GPT-4 frequently generated syntactically correct but logically flawed data processing code, particularly for complex temporal joins and survival analysis implementations. Multiple iterations were required to achieve stable, clinically valid algorithms. Peer Review Agent Consistency: Liner Pro’s peer review agent sometimes provided contradictory recommendations between iterations, requiring human judgment to synthesize competing suggestions and maintain manuscript coherence. Domain-Specific Knowledge Gaps: Despite comprehensive literature processing through Liner Max Prompt, AI systems lacked nuanced understanding of pharmacokinetic interactions, requiring substantial human oversight for mechanistic explanations and clinical interpretation. Literature Synthesis Depth: While Liner Max Prompt excelled at breadth of literature coverage, it occasionally missed subtle methodological distinctions between studies that affected evidence quality assessment, requiring human expert review for critical appraisal.

## Paper 190

The AI demonstrated strong analytical capabilities in systematic theory comparison but required human guidance for contextualizing the work within broader scientific methodology debates. The AI also needed direction on addressing institutional and social aspects of scientific evaluation beyond pure technical analysis.

## Paper 191

Although AIScientist V2 can autonomously propose ideas, run experiments, and draft papers, its outputs are often incomplete. Code frequently contains bugs, and producing a 'finished' paper typically requires many abandoned attempts, leading to wasted GPU hours and API usage. Moreover, while the system can generate novel directions, it lacks deep contextual judgment, making some ideas impractical or disconnected from broader scientific discourse. Compared with human researchers, AI also requires stronger coordination in areas such as political and ethical perspectives, allocation of resources for research, and handling of metadata not explicitly represented in the paper.

## Paper 192

1) Contextual Fragility in Non-Linear Research Processes: AI struggled with the iterative and multi-branched nature of scientific work, such as brainstorming sessions or back-and-forth revisions of ideas and text. Its primarily linear context handling led to frequent context loss across all tasks in repetitive error loops that required the human involved to make progress. 2) Ineffective Strategic Decomposition: AI could not reliably decompose high-level, complex goals into workable, balanced sub-tasks. For instance, when asked to 'design all experiments,' it produced a plan where some steps were trivial while others were vastly complex and un-executable. Currently, it still needs the human expert’s ability to allocate tasks appropriately. 3) Conceptual Blind Spots and Lack of Relational Understanding: AI can make some high-level conceptual connections, but not always reliably. Notably, even after being explicitly tasked with implementing 'Tree of Thoughts' (ToT) as a baseline, it did not recognize the strong methodological similarity between ToT and our own proposed framework.

## Paper 193

1. Inaccurate reporting of numerical values, leading to interpretations and/or research findings based on imagination, fabrication, or hallucination. 2. Insufficient interpretation of results, discussion of research findings, and formulation of conclusions. 3. Inadequate narrative and 4. Inaccurate or hallucinated references, including citations to unrelated works. In addition, the code generated by the AI sometimes contained bugs or inappropriate settings, preventing smooth execution. In most cases, these issues could be resolved by providing the AI with outputs, logs, and error messages. Footnotes were added in the paper where necessary to indicate issues worth noting.

## Paper 194

Hallucinations around prior work and risks of over-claiming required human pruning; code proposals were functional but fragile at simulator boundaries; statistical test choices needed assumption checks; citation formatting and dataset descriptions needed manual fixes; AI tended to under-specify compute and data hygiene until prompted; iterative 'retry' cycles were required for reproducible configs.

## Paper 195

There are clear limitations in the retrosynthetic models for predicting chemistry as discussed in the paper. The paper itself is quite surface level in its analysis even after prompting in an effort to increase the depth of the analysis.

## Paper 196

Formatting and template compliance: LATEX math re-typesetting, sectioning macros, keywords/required checklists placement, anonymization handling, and pruning references to those actually cited required manual fixes and QA.

## Paper 197

Teaching the framework to the AI model proved challenging. Despite providing extensive background information, the model often lacked sufficient grasp of intricate technical details, requiring repeated clarifications and corrections. This limited its ability to generate fully precise or context-sensitive drafts, and extra effort was needed to ensure methodological accuracy and conceptual consistency.

## Paper 198

When used for code generation, AI assistants sometimes produced inefficient or subtly incorrect code that required careful human debugging. For writing assistance, the AI occasionally suggested phrasing that altered the scientific meaning, necessitating careful review to ensure accuracy.

## Paper 199

AI appears to be distracted by too much starting information, or weak evidence in the literature. Experiment suggestions are often expensive or labor-intensive with moderate likelihood of success. More stringency on feasibility would help streamline AI-driven research.

## Paper 200

AI required multiple iterations to achieve mathematical rigor and occasionally generated plausible but unverified claims. Limited access to proprietary models prevented comprehensive validation. AI also showed inconsistencies when extending analysis to decoder architectures.

## Paper 201

Tendency toward confident but unverifiable claims; occasional reference inaccuracies; limited awareness of protocol corner cases.

## Paper 202

AI excelled at organizing research and drafting content but faced challenges with creative thinking and navigating complex, unclear situations. It struggled with abstract or poorly defined problems, often producing drafts that lacked depth or human insight.

## Paper 203

Just not perfect but definitely the quality of the paper is very similar to master level. There are some spelling errors in the Figure 1 that is generated by nanobanana.

## Paper 204

Large models occasionally overstate significance or propose untested variants; code they generate may contain subtle bugs or nondeterministic behavior without seed control; long-documented its can introduce inconsistencies across sections; and adherence to specific LaTeX macros sometimes requires manual fixes. We mitigated these limits with human reviews, unit tests, fixed random seeds, and explicit checklist compliance checks.

## Paper 205

We utilized Liner’s Hypothesis Generator AI as the starting point of our research process. Instead of spending weeks manually brainstorming and validating potential ideas, we simply provided our core research concept, and the AI produced a wider range of candidate hypotheses, each accompanied by supporting evidence. The system went beyond surface-level suggestions by conducting extensive literature analysis and applying multiple evaluation criteria, including novelty, potential impact, feasibility, and conceptual clarity. Through iterative cycles of hypothesis generation, evaluation, and refinement, we obtained several strong options with detailed rationales. From these AI-generated hypotheses, we carefully selected the most compelling one to serve as the central hypothesis for our paper.

## Paper 206

GPT-5 and similar models are not yet very strong at code generation, often requiring extensive debugging to produce high-quality code. Claude Opus, on the other hand, is expensive. Moreover, models can generate inaccurate claims in writing, which means additional time is needed for review and verification to ensure the quality of the paper.

## Paper 207

AI required extensive human oversight for experimental accuracy, showed tendency to overstate statistical significance, and needed human validation of all scientific interpretations. However, AI excelled at pattern recognition in complex datasets and scientific writing.

## Paper 208

In practice, we found that delegating bibliographic management to AI agents is fraught with risk. The models have a tendency to hallucinate BibTeX entries—fabricating sources or misattributing authorship. This vulnerability necessitates meticulous human oversight, negating the efficiency gains of automation. We identify this as a readily addressable challenge. A targeted Supervised Fine-Tuning (SFT) process could effectively teach models the correct procedures for finding and formatting citations. To complement this, the adoption of Anthropic’s Model Context Protocol (MCP) offers a robust solution.

## Paper 210

AI tools sometimes generated text that was generic or lacked the specific technical depth required for a scientific paper, and occasionally produced inconsistencies that required careful human review and correction (e.g., float placement quirks, overly confident claims).

## Paper 211

Primary limitations included reliance on simulated experimental data, incomplete theoretical analysis for some convergence properties, and potential gaps in recent literature coverage.

## Paper 212

Mostofthetime AItriestogiveapositiveanswerwhenit’snot.

## Paper 213

It is difficult to expect truly novel ideas from AI, and the text it generates often lacks fluency. The evidence base of the information is uncertain, making it unsuitable for direct use. Moreover, AI sometimes provides inaccurate information, limiting its reliability in areas outside the researcher's area of expertise.

## Paper 215

While the AI handled the majority of tasks, it relied entirely on human prompts for context and task scope. AI occasionally produced minor inconsistencies in figure formatting, LaTeX syntax, or interpretation details, which were corrected manually by the human. AI cannot independently verify real-world datasets or experimental execution.

## Paper 216

It is challenging for AI to follow the page limit. Also, if AI is prompted to generate a very long context (e.g. the full paper), it will ignore some of the instructions stated in the prompt, the AI output would be more uncontrollable.

## Paper 217

Mustbetoldwhattodoprecisely. Otherwiseitistoovague.

## Paper 218

AI struggles with truly novel, paradigm-shifting ideas and can produce plausible but incorrect reasoning in complex multi-hop scenarios. It also requires significant human oversight to ensure factual accuracy and avoid hallucinations.

## Paper 219

One of the main limitations we encountered was related to the coding aspect of the project. Since our goal was to develop an autonomous pipeline where agents could orchestrate the entire workflow independently, we had to run multiple iterations to fine-tune the process. This was especially true for tasks such as manuscript writing and refinement, which required repeatedly executing and adjusting the pipeline to achieve the desired quality and coherence feedback from the reviewer agent.

## Paper 221

The primary limitation observed was the AI’s inability to access or generate real, novel experimental data; it relied on synthesizing existing literature and generating mock data for code demonstration. Furthermore, while highly proficient at structuring the paper and identifying patterns, the AI lacks true domain-specific intuition and requires human guidance to ensure the scientific interpretations are sound and to correct subtle contextual errors. However, it was quite brilliant at developing initial ideas into concrete hypotheses once given the broad idea. Finally, the AI cannot perform the actual data collection from literature, which remains a manual, human-driven task.

## Paper 222

AI tools were helpful for routine tasks but showed limitations in developing novel theoretical frameworks and interpreting complex economic relationships requiring domain expertise.

## Paper 223

First, there are limitations on the selection of references. The AI developed by the research team has built-in prompt words, and automatically generates articles after selecting references, rather than the traditional method of inputting prompt words. In order to make the generated article topic focus on the target topic, it is necessary to select references with highly similar topics in advance. The researchers found that if references on other irrelevant topics are mixed in, the topic of the generated article will deviate and the ideal result will not be obtained. Secondly, to ensure that the model can operate normally, the maximum number of references cannot exceed 50; in addition, incomplete citations may occur, which may be caused by the model losing information or the model detecting that there is no writing relevance between certain references. Third, the stability of the model operation is not good, and the results generated by repeated attempts vary greatly.

## Paper 225

Requires human oversight, misses some literature.

## Paper 226

Occasionalnumericaldriftwhenre-computingprovidedvalues,over-confident tone,andriskofcitationhallucinationswithoutstrictsourcecontrol. Domainassumptions canbeoversimplifiedunlesstightlyconstrained. Alloutputsrequiredhumanverification andpromptiteration.

## Paper 227

The main limitations are the following: The AI struggled to maintain the context and focus of the paper. We encouraged the AI to write supporting documents in the codebase, but the AI would not update them if not reminded, or not use them to write the paper. Even when using an agent with web search capabilities, the AI would hallucinate the references. When given feedback on a specific part of the implementation, the AI would not update the implementation but generate new code. This led to lots of unnecessary code and would need to constantly be reminded to update the implementation.

## Paper 228

Limitations in ethical scenario coverage.

## Paper 229

High sensitivity to prompt phrasing and templates; occasional hallucinated statistical language or mislabeled effects; limited fidelity to subtle, context-dependent phenomena (e.g., communicator-race nuances); reduced transparency and reproducibility in proprietary pipelines (e.g., seeding, sampling). We observed a tendency to inflate salient identity effects while attenuating weaker ones, requiring careful human oversight.

## Paper 230

AI made a few mistakes understanding subtledetails of the scientific article. Among the list of publications we provided, there were several publications where the contribution of the small-angle scattering technique, which is the main topic of this review, is rather small compared to the other techniques that were used in those studies. However, AI chose to highlight those publications.

## Paper 231

We observed that LLMs exhibit topic drift issues when dealing with long texts and extended contexts. Additionally, we found that multiple retries can accomplish tasks more efficiently than complex prompt engineering.

## Paper 232

Observed AI Limitations: Task execution. Because our pipeline runs in Jupyter notebooks, many steps require interaction with a web interface. The Chat GPT-provided agent performs well when instructions are precise and can attempt to correct errors, though some issues may persist and still require human intervention. Ideageneration. Chat GPT is a strong brainstorming assistant; some ideas are genuinely valuable, but novelty and feasibility still require human vetting. Manuscript writing. Agents can deliver rigorous 'harsh reviews' (via LLM API calls) and, when combined, enable fast revision cycles. However, factual accuracy and citation integrity must be checked by humans. Interpretation of results. AI can produce high-quality summaries and explanations—especially for non-experts—but domain-specific nuances and causal claims should be validated by human experts. Overall. Multi-agent LLM workflows are promising and can accelerate research, but they require careful oversight, verification, and error handling to be reliable at scale.

## Paper 233

Potential risks include (i) over-interpretation of simulated trends as causal facts; (ii) misuse of dosages suggestions; and (iii) amplification of literature biases.

## Paper 234

AIrequiresprecisespecificationstoavoidrandombehaviorandcanhallucinate fakeresultswhenattemptingend-to-endtasks. Whenencounteringcomputationaldifficul- ties,modelsoftenresorttoplaceholdersratherthanproperimplementation,especiallywith insufficient APIresources. Taskcomplexitycontroliscrucialforeffective AIcollaboration.

## Paper 235

(1) Tendency toward overly elaborate explanations; (2) Occasional gaps when synthesizing insights across experiments; (3) Figure layout requires manual polishing; (4) Terminology drift without explicit guidance; (5) Human judgment remains important to separate statistical from practical significance.

## Paper 236

Toavoid LLMhallucinationstheirrolewaslimitedtogeneratingfiguresand text that were verified by humans. We limited AI use to text and figures, verified any generationagainstgroundtruth,andensuredthatallscientificclaims,analyses,andcode werevalidatedbytheauthors.

## Paper 237

AI occasionally exhibited some of the very issues discussed in this paper, including occasional factual inconsistencies and the need for extensive human validation of technical claims and citations.

## Paper 238

Steering LLM models comes with challenges, they do not always obey constraints.

## Paper 239

Key limitations observed include AI’s occasional tendency toward over-optimization of metrics without considering practical deployment constraints, difficulty in understanding nuanced institutional requirements across diverse environments, and need for human validation of experimental design choices. AI sometimes generated overly complex technical solutions that required human simplification for real-world applicability. Human oversight was essential for ensuring ethical considerations and appropriate interpretation of statistical results.

## Paper 240

When using AI as a partner or lead author, several limitations emerge. First, AI struggles with true creativity and originality, often producing content based on existing patterns rather than generating innovative ideas. It can also have difficulty fully understanding context or nuances, particularly in specialized fields, leading to less accurate or relevant outputs. Ambiguous prompts can confuse AI, resulting in vague or unintended responses. Additionally, AI may reinforce biases present in training data, impacting the objectivity of its conclusions. It also lacks the personal touch in communication, often missing the ability to adapt tone and voice to its specific audiences. In academic or professional contexts, AI may generate content without reliable citations, undermining its credibility. Lastly, AI faces challenges with long-term strategic planning, as it excels more in short-term tasks but struggles to maintain a consistent narrative throughout a project.

## Paper 241

AI agents occasionally generated overly complex mathematical formulations without clear physical interpretation, required guidance to maintain focus on practical implementation constraints, and needed human oversight to ensure theoretical claims remained grounded in established quantum mechanical principles. When polishing the Agent’s writing, we noticed the boldness with which claims were made, declaring definitively rather than describing cautiously. While we eventually want Alicanto to be capable of continuously working and improving a paper until it reaches such a final state, we also acknowledge that a human in the loop that is periodically reviewing the outputs and re-directing Alicanto to whatever is the most pertinent remaining task as the state of the paper takes hold.

## Paper 242

LLM models are hard to control and do not obey length constraints.

## Paper 243

Primary limitations included the computational expense of training (48 GPU-hours), scalability constraints for circuits with high entanglement, potential loss of subtle phase relationships in highly compressed circuits, and integration complexities with Qiskit/Cirq frameworks.

## Paper 244

The AI agent has limitations in accessing external resources, such as URLs, which can be a hindrance when trying to use specific templates or datasets. The agent also requires very specific instructions and can sometimes make mistakes that require human intervention to correct.

## Paper 245

Some difficulty explaining concepts and linking ideas together.

## Paper 246

The current AI is able to provide the full code and finish the paper. However, it cannot fully conduct the whole research independently and has to rely on humans to give concrete instructions for each step, including writing the codes, searching relevant work, evaluation, and conducting ablation studies etc.

## Paper 248

The LLM may propose plausible but incorrect citations or mis-state numbers if not grounded in web search. We constrained the paper to author-provided figures, required exact numbers to match logs, and subjected all generated text to human review.

## Paper 249

Requires human oversight, misses some literature.

## Paper 251

AI has difficulty finding a middle ground when given differing instructions and struggles to generalize or reflect on suggestions. It is not well-suited for data collection and analysis, requiring highly detailed instructions for these tasks. Its figure-making abilities are limited, as outputs often contain missing elements or mislabeled components.

## Paper 252

Key limitations observed include: (1) AI occasionally generated wrong references (correct title, but wrong author list) (2) AI-generated code implementation needs careful review and a good amount of iterations, it seems less likely that agents can implement everything in one shot; for example, the llm token size need to be updated when the initial values (1k completion) cannot finish the full generation trajectory (now we are at 4k, but can still be limited), etc. (3) AI sometimes makes mistakes when using the data from the fetched website (this could be either a tool issue, or an LLM issue, which needs deeper analysis; e.g. the api model name of llama4-maverick needs to be manually corrected). (4) AI still frequently makes factual mistakes, challenging the practical deployment of these systems for future research tasks. e.g. it thinks qwen-235b model is larger than qwen-480b-coder model. (5) On some other trials, AI may take shortcuts, e.g. fabricate results instead of running actual experiments. (this happened more than one time, so it’s very concerning.) (6) AI can make cool figures, but they are not perfect. The most frequent limitation is the text overlapping.

## Paper 254

Logs highlight that the AI occasionally produced LaTeX errors (duplicate geometry calls, unescaped underscores, Unicode characters like and subscripts). It also generated verbose or repetitive sections that required manual pruning. These were technical formatting issues, not conceptual flaws, underscoring that while AI authored the research, human input was needed for document preparation.

## Paper 258

The main limitations relate to reproducibility. Using LLMs as virtual research agents can yield different outcomes and research paths depending on prompts and context. Despite efforts to standardize inputs (e.g., fixed prompts, temperature=0), each run produced variations in analyses, results, and types of errors. This variability highlights both the flexibility of the models and the need for human oversight to ensure reliability and coherence. Additional concerns include the absence of explicit citations in the text, the apparent generation of references based on similarity to the manuscript’s content rather than deriving claims directly from cited sources, and the uncertainty over whether the conclusions result from genuine evaluation of the data and internal debate or from claims embedded in the model’s training corpus. These issues emphasize that human supervision is not only necessary to guarantee scientific validity but also to prevent misleading attributions and ensure that evidence is properly grounded in referenced literature.

## Paper 259

One core problem was the context window: especially dealing with large primary sources was a pain. In the end we asked the AI to summarize the primary sources and use these summaries for related work. This, however, missed finer points and nuances in the works. A very annoying point is that the AI often made big, almost random changes. This turned the process almost into a slot machine: ask for changes, and sometimes the result might be a jackpot. The AI also lacks a deeper understanding of what it is doing. Personally we could have spent much more time improving the results, but we both ran out of time and out of our credit limit.

## Paper 260

1. inaccurate numerical values in the results; 2. insufficient interpretation of the results, discussion of the research findings, and conclusions; 3. inadequate narrative; and 4. inaccurate or hallucinated references, as well as incomplete reference entries, though these were relatively few. Additionally, the code generated by the AI occasionally contained bugs or inappropriate settings that prevented smooth execution. In most cases, these issues could be resolved by providing the AI with outputs, logs, and error messages. Where necessary, the human author(s) added footnotes in the paper to highlight points worth noting.

## Paper 262

AI struggled with the nuanced evaluation of medical accuracy, requiring domain expertise. AI assistance was invaluable for formatting and condensing content, but required human oversight to ensure technical accuracy and appropriate emphasis on key findings. AI also could not access real-time healthcare data or verify current information about local healthcare facilities.

## Paper 263

While AI can propose simple methods and draft text, its writing is limited and its references are frequently fabricated or incorrect.

## Paper 264

Key limitations include the need for experimental validation of computational predictions, potential oversimplification of complex biological systems, and the requirement for human oversight in interpreting clinical relevance and therapeutic implications.

## Paper 265

Because the AI platforms are inherently chat-based, we found that approximately 5% of human intervention remained essential to guide the workflow. In particular, Cursor produced stronger outcomes when its automatically suggested next steps were overridden with targeted human feedback.

## Paper 266

While AI can automate hypothesis generation, experimentation, analysis, and writing, its outputs may lack deep domain expertise and nuanced interpretation. Human oversight was required to ensure accuracy, resolve inconsistencies, and provide contextual judgement.

## Paper 267

AI performs well in generating ideas, drafting content, and executing workflows under human guidance. However, in our experience, different models tend to vary in output quality across tasks. GPT-5 appeared to perform better in planning and contextual understanding, while Gemini 2.5 Pro seemed more reliable for code generation. Based on these observed tendencies, we assigned GPT-5 as the lead author and used Gemini 2.5 Pro as a supporting agent for code correction and content refinement. Additionally, AI-generated outputs often require manual correction to ensure data and content consistency and adherence to formatting standards. Prompt design and high-level guidance from researchers remain essential to uphold scientific rigor.

## Paper 268

While AIagentsdemonstratedremarkablecapabilityinconductingcompre- hensiveresearchautonomously,limitationsincludedoccasionalneedforhumanvalidation ofstatisticalinterpretationsandensuringproperacademictoneconsistency. AIexcelledat systematicanalysis,literaturesynthesis,andtechnicalimplementationbutbenefitedfrom humanoversightforstrategicresearchdirectionandqualityassurance. The Co-Sciplatform enabledeffectivehuman-AIcollaborationthroughiterativeimprovementcycles.

## Paper 269

In conducting this research in collaboration with AI, we conclude that the ability to create something from nothing remains a distant goal. Nevertheless, when humans devoid of specialized expertise propose an idea, the AI employs all available means to evaluate it by presenting appropriate rationales.

## Paper 270

As of now, we cannot control the page limit.

## Paper 271

A primary limitation was the AI’s inability to directly access or execute local code and experimental environments. This made diagnosing computational problems dependent on the researcher providing precise logs and code snippets, resulting in a longer communication loop. Furthermore, the AI lacks deep, first-principles domain knowledge in building energy physics; its interpretations are based on patterns in the provided data. Consequently, all AI-generated content required strict supervision and validation by human experts to ensure scientific accuracy.

## Paper 272

While the AI provided extensive support across all stages, several limitations were observed. It sometimes produced hallucinated mathematics or proofs that required correction, and code snippets occasionally contained errors or inefficiencies. At times, results were overfitted or lacked robustness when tested under alternative specifications. Explanations could also be vague or imprecise, requiring clarification. Citations were not always reliable, with occasional fabricated or incomplete references. These limitations meant that verification and iterative prompting were necessary to ensure the final work was valid and reproducible.

## Paper 273

Tends to hallucinate or misattribute citations unless given a fixed .bib; occasional symbolic slips in constants and signs; inconsistent macro usage (biblatex vs. BibTeX); cannot execute external computations or verify integrals; requires human oversight for rigor, scope control, and alignment with domain conventions.

## Paper 274

Agentic AIrequiresexplicit,step-by-stepguidance;itrarelyconstructsend-to- endpipelineswithoutusersspecifyingtools(e.g.,sc VI,Scanpy,Co Var Net),modules,and I/O.Itsbiologicalinsighttendstobeshallow—summarizingpatternsratherthanpropos- ing mechanistic, novel interpretations. Performance depends heavily on mature, well- documentedframeworks;itisweakatinventingnewmethodsorunconventionalpipelines. Modelqualitymatters: stronger,instruction-tunedmodelsfollowworkflowsmorereliably butstillneedstructuredprompts,constraints,andchecking. Humanexpertiseremainsessen- tialforstudydesign,edge-casehandling,statisticalvalidation,andensuringclaimsmeet publicationstandards. Finally,weobserveaccount“memory”effects: systemsthathave accumulatedpriorcontext,examples,anditerativefeedbackbehavenoticeablybetter,while freshaccountswithouthistoryoftenunderperformuntilseededwithscaffolds,datasets,and conventions. Overall,agent AIisausefulaccelerator,notanautonomousscientist.

## Paper 275

Key limitations included initial channel dimension mismatches in neural network implementation requiring iterative debugging, and the need for simplified model architectures when complex spectral methods failed. AI agents occasionally generated overly complex solutions that required human guidance toward more practical approaches. The multi-agent coordination required careful task decomposition and verification of inter-agent communication.

## Paper 276

Key limitations include: (1) AI sometimes lacks deep domain-specific intuition for cancer biology nuances, requiring human oversight for biological interpretations; (2) AI may not fully capture the significance of certain experimental results without explicit guidance; (3) AI requires careful prompting to maintain appropriate technical rigor and avoid overstating claims; (4) Integration of AI-generated content with human expertise requires iterative refinement to ensure scientific accuracy.

## Paper 277

While AI assistance accelerated drafting and prototyping, it also introduced recurring limitations. Generated text was often verbose, repetitive, or imprecise, and required substantial human editing to maintain clarity and academic tone. Code suggestions sometimes ignored model assumptions. In several instances, the AI produced fabricated data points or misleading visualizations when prompted to generate analysis or figures. The AI also tended to overstate the robustness of results without verifying statistical validity. These issues made continuous human oversight essential to ensure methodological soundness, validate outputs against raw data, and refine the interpretation of findings. Human authors were responsible for checking code execution, re-running experiments, verifying figures, and editing the narrative.

## Paper 278

The AI agent was able to act as a fully autonomous partner for baseline construction, ablations, and reproducible experimental analysis. We deliberately avoided human intervention during experiment execution and data analysis to test its autonomy. While it reliably handled standard tasks and produced consistent pipelines, it struggled to generate novel or complex experimental ideas beyond the templates it had been given. In practice, we found it best suited as a dependable assistant for systematic evaluation rather than as an originator of fundamentally new methodological contributions.

## Paper 279

AI often risks overinterpretation in experiments and lacks creativity in topic selection, yet proves useful when merging diverse fields.

## Paper 280

The main difficulty was inspecting the paper for possible errors or citations with low credibility. As efficient the writing process was, there were some issues that needed to be addressed. We believe this requirement of a survey by humans is the current limitation of using AI for research.

## Paper 281

AIassistancewashelpfulformanuscriptstructuringandexpansionbutrequiredextensivehumanoversightforclinicalaccuracyanddomain-specificterminology. AIsometimesgeneratedoverlybroadstatementsrequiringrefinementwithspecificmedicalknowledgeandclinicalcontext.

## Paper 282

While AI was helpful in summarizing existing literature and generating example text, it sometimes lacked the nuanced understanding of complex HCI principles and the specific needs of vulnerable populations like AD patients. Human oversight was crucial to ensure empathy, ethical considerations, and genuine innovation beyond surface-level suggestions. Additionally, when re-writing sections 5 and 6 to be conceptual rather than based on real experiments, the AI required careful guidance to maintain a consistent academic tone and to properly frame the anticipated results without making definitive claims.

## Paper 284

Just not perfect but definitely the quality of the paper is very similar to master level. There are some spelling errors in the Figure 1 that is generated by nanobanana.

## Paper 285

While AI can automate hypothesis generation, experimentation, analysis, and writing, its outputs may lack deep domain expertise and nuanced interpretation. Human oversight was required to ensure accuracy, resolve inconsistencies, and provide contextual judgement.

## Paper 286

While AI can automate hypothesis generation, experimentation, analysis, and writing, its outputs may lack deep domain expertise and nuanced interpretation. Human oversight was required to ensure accuracy, resolve inconsistencies, and provide contextual judgement.

## Paper 287

The AI system occasionally required multiple attempts to correctly parse complex statistical outputs. Evidence grounding sometimes produced overly conservative estimates. The multi-agent architecture showed unexpected coordination failures compared to monolithic approaches.

## Paper 288

AI agents occasionally produce overly verbose text requiring condensation, struggle with precise figure generation matching exact specifications, and may miss domain-specific conventions. However, they excel at systematic literature review, comprehensive experimental design, and maintaining consistency across complex technical documents.

## Paper 289

AI occasionally produced oversimplified reasoning or missed subtle domain-specific insights that required deep contextual knowledge. It also struggled with ethical judgment, long-term research vision, and distinguishing between highly novel versus incremental contributions. Additionally, AI-generated writings sometimes lacked narrative coherence, requiring human refinement to ensure readability and alignment with disciplinary standards.

## Paper 290

(a) Context drift in long sessions: With very long prompts or multi-section drafts, the model may drop earlier constraints or conflate sections (attention dilution). (b) Math fragility: Tends to produce malformed LaTeX, inconsistent notation, or shaky algebra (e.g., missing subscripts, incorrect normalizations). (c) Unannounced hard-coding/config drift: Occasionally inserts fixed constants or modifies defaults without flagging, leading to silent reproducibility issues in code and analysis.

## Paper 291

While the AI provided extensive support across all stages, several limitations were observed. It sometimes produced hallucinated mathematics or proofs that required correction, and code snippets occasionally contained errors or inefficiencies. At times, results were overfitted or lacked robustness when tested under alternative specifications. Explanations could also be vague or imprecise, requiring clarification. Citations were not always reliable, with occasional fabricated or incomplete references. These limitations meant that verification and iterative prompting were necessary to ensure the final work was valid and reproducible.

## Paper 292

Key limitations include: (1) difficulty with transcendental complexity requiring non-elementary techniques, (2) inability to autonomously develop novel proof strategies when standard methods fail, (3) computational scalability constraints for exponentially growing sequences, and (4) challenges in meta-level strategic reasoning when fundamental approach changes are needed.

## Paper 293

The primary limitation observed was the AI’s need for precise, unambiguous instructions, especially for complex coding and data analysis tasks. The AI occasionally produced code with subtle errors that required human debugging. In writing, while proficient at generating coherent text, the AI required significant human guidance to establish a consistent narrative arc and to ensure the interpretation of results was sufficiently nuanced. The AI also cannot verify the visual correctness of generated charts and figures.

## Paper 294

AI-generatedresearchrequirescarefulvalidationofcomputationalassumptions 187 andmaybenefitfromexperimentalverification. Theworkflowdependsonstaticstructural 188 modelsanddockingapproximationsthatmaynotcapturefullbiologicalcomplexity.

## Paper 295

The primary limitation observed is the AI’s reliance on synthetic datasets rather than real-world AGI telemetry, which may limit the generalizability of findings. The AI also tends toward comprehensive but potentially overly systematic experimental design, which while thorough, may miss creative experimental approaches that human domain experts might explore. Additionally, the AI requires explicit guidance for domain-specific considerations unique to AGI safety applications.

## Paper 296

While GPT-4o (via Agent Mode) executed code and used web-based tools like Alpha Fold2 on neurosnap.ai, it required human assistance for credential handling, API key entry, and transferring error messages between agents. GPT-4o did not perform debugging or structural refinement beyond heuristics (e.g., pLDDT). Structure-function relationships were inferred, not empirically validated.

## Paper 297

Main limitation was that AI can’t faithfully reproduce already produced LaTeX text. Repeat iterations can have subtly different text segments. Provided executable code does not always execute at first.

## Paper 298

Current AI still lacks enough capability to finish the high-quality research in end-to-end manner. They can assist in specialized steps such as coding or writing, but it also has issues such as too much verbose writing or redundant coding design.

## Paper 299

Computation limits in exhaustive search.

## Paper 300

Primary limitations included the computational expense of hyperedge attention calculations (increasing training time by 25), scalability challenges for very large hypergraphs (>10K nodes), computational overhead of adaptive aggregation, difficulties in verifying hypergraph equivalence for complex biochemical interactions, and challenges in integrating with existing deep learning frameworks.

## Paper 301

AI was invaluable for brainstorming, outlining, and accelerating early drafts. At the same time, we encountered several recurring limitations that required active management: (a) Reliability of content. The model occasionally produced over-generalized statements, redundant phrasing, or mechanistic claims not supported by the data. Response: apply filtering with plausibility and testability scores, tighten language in editorial passes, and clearly flag the need for human validation. (b) Consistency of presentation. Drafts showed occasional drift in terminology, style, and cross-references, especially across longer sections. Response: use a style guide, systematic notation checks, and automated validation of references during compilation. (c) Sensitivity to prompting. Small changes in input instructions could shift tone, emphasis, or structure in unexpected ways. Response: rely on fixed templates, iterative refinement, and documented revision histories to stabilize outputs. (d) Ethical and anonymity concerns. Without careful guidance, the model risked producing overly confident language or revealing identifying details. Response: adopt explicit uncertainty labeling, avoid unverifiable claims, and follow an anonymization checklist for all text, figures, and artifacts. (e) Practical reproducibility. Code suggestions were often plausible but incomplete, assuming hidden dependencies or missing edge cases. Response: pin dependencies, provide configuration files and seeds, and supply end-to-end scripts for evaluation.

## Paper 302

It is difficult for AI to truly generate innovative ideas for complex algorithm design. AI cannot provide accurate network diagrams.

## Paper 303

1) Surface-level reasoning: AI often produced plausible but shallow explanations, which required human correction to ensure conceptual depth and technical accuracy. 2) While AI tools were effective for generating analysis figures and result plots (e.g., through Python code for automated visualization), they showed clear limitations in producing complex schematic diagrams such as methodological flowcharts. These tasks often required significant manual adjustment or external design tools. Among the models tested, Gemini 2.5 Pro provided the most useful support for figure drafting, but even so, the quality and flexibility were below what is required for final publication standards.

## Paper 304

AI tools occasionally provided inaccurate or outdated citations, requiring careful fact-checking. When used for literature synthesis, AI models sometimes missed nuanced theoretical distinctions or oversimplified complex conceptual relationships. AI assistance with writing occasionally suggested generic phrases that lacked the precision required for academic discourse, necessitating human revision to maintain scholarly standards and voice authenticity. Furthermore, the models struggled to adhere to strict length requirements, often producing text that was either too concise or overly verbose and required significant human intervention to align with submission guidelines.

## Paper 305

AI models occasionally exhibited Western-centric biases despite cultural parameterization efforts. The models also struggled with subtle cultural nuances that human researchers had to manually correct. Additionally, maintaining simulation consistency across all 14 countries required extensive human oversight and calibration.

## Paper 306

While the AI demonstrated strong capabilities in literature synthesis and drafting, we observed several limitations. The primary issue was a tendency toward 'hallucination' or confident inaccuracy, particularly with bibliographic details and citations, which required meticulous human fact-checking. The AI sometimes produced overly formulaic or generic text that lacked a strong, persuasive voice, requiring human intervention to refine the narrative. Finally, without explicit guidance, the AI struggled to perfectly align the paper’s framing with the specific, niche focus of the target conference, necessitating a human-led strategic revision.

## Paper 307

The AI agent demonstrated several key limitations that required human intervention. 1) Lack of Multimodal Reasoning: The AI was unable to accurately analyze the visual content of plots or the provided bond graph diagrams, often hallucinating features that were not present. 2) Deficient Abstract Reasoning: The agent, despite proposing ideas, could not follow through novel mathematical derivations. 3) Poor Iterative Design: When tasked with correcting its own errors in interpretation or writing, the agent often repeated the same mistakes. 4) Scalability of Task Execution: The AI performed best on narrowly-defined tasks. Complex, multi-stage goals had to be broken down into a sequence of smaller prompts by the human director.

## Paper 308

Primary limitations included the complexity of specifying complete zero-knowledge proof constructions for gradient verification (requiring specialized cryptographic expertise), challenges in modeling sophisticated coordinated Byzantine attacks, incomplete analysis of all possible consensus mechanism failures, and difficulties in predicting regulatory responses to blockchain-based AI training systems. Additionally, the agent faced challenges in accurately estimating real-world deployment costs and network effects.

## Paper 309

AI was poor at generating figures, capturing insights from raw data, and summarizing key findings. It tended to over-focus on lexical instructions and sometimes proposed non-existent methods or altered the intended methodology during writing.

## Paper 311

AI served as a highly efficient collaborator in the ideation, data analysis, and writing processes of the paper. However, it demonstrated a technical limitation in its inability to directly access or modify uploaded data files. This required the researcher to perform repetitive manual tasks during the data preprocessing stage.

## Paper 313

Deep Research cannot conduct experiments and provide realistic results even if the task is related to LLM. The automated generation of code contained errors and misalignments with updated software versions. Human researchers need to refine and debug the code to obtain the results. The paper generated using Deep Research can include high similarity compared to published papers. For this reason, multiple attempts may be necessary to provide a novel solution. Deep Research can produce a low-quality refinement of the paper when it merges new data and results. Additionally, the references generated using Deep Research include hallucination in author names and paper IDs.

## Paper 314

GPT-5 and similar models are not yet very strong at code generation, often requiring extensive debugging to produce high-quality code. Claude Opus, on the other hand, is expensive. Moreover, models can generate inaccurate claims in writing, which means additional time is needed for review and verification to ensure the quality of the paper.

## Paper 315

AIsystemsmaygenerateplausiblebutunverifiedexperimentalclaims,lack deepdomainintuitionforedgecases,occasionallyhallucinatecitationsordata,andrequire validationoftechnicalaccuracyandethicalconsiderationsbyhumanoversight.

## Paper 316

AI tools showed limitations in domain-specific technical accuracy, particularly in educational technology contexts where nuanced understanding of institutional processes is required. AI-generated code occasionally required significant debugging and adaptation to specific use cases. Additionally, AI struggled with maintaining consistent technical terminology across complex multi-component systems and required human oversight for ensuring methodological rigor in experimental design.
