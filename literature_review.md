# Literature Review

## Research Area Overview
The research area focuses on **AI Undetectability** and **AI-Generated Text Detection**. With the proliferation of Large Language Models (LLMs) like ChatGPT, distinguishing between human-written and machine-generated text has become a critical challenge. The field has evolved from simple binary classification (Human vs. Machine) to more complex tasks involving authorship attribution (identifying specific models), robustness against adversarial attacks (postediting), and benchmarking across diverse domains and sampling strategies. Recent work emphasizes that current detectors are brittle and often fail when faced with simple obfuscation techniques or out-of-distribution data.

## Key Papers

### Paper 1: Counter Turing Test CT^2: AI-Generated Text Detection is Not as Easy as You May Think
- **Authors**: Megha Chakraborty et al.
- **Year**: 2023
- **Source**: arXiv:2310.05030
- **Key Contribution**: Introduces the **AI Detectability Index (ADI)** to rank LLMs based on their detectability. Proposed the Counter Turing Test (CT^2) benchmark.
- **Methodology**: Evaluated 15 LLMs using various detection methods (watermarking, perplexity, burstiness, etc.).
- **Key Findings**: Larger LLMs (like GPT-4) have a higher ADI (harder to detect). Current detection methods are fragile and easily circumvented.
- **Relevance**: Provides a metric (ADI) and a framework for evaluating the "inference" track of our leaderboard.

### Paper 2: TURINGBENCH: A Benchmark Environment for Turing Test in the Age of Neural Text Generation
- **Authors**: Adaku Uchendu et al.
- **Year**: 2021
- **Source**: arXiv:2109.13296
- **Key Contribution**: Created a benchmark with 200K articles covering 20 labels (19 models + Human). Defined two tasks: Turing Test (binary) and Authorship Attribution (multi-class).
- **Datasets Used**: 10K news articles prompted to 19 models (GPT-1 to GPT-3, GROVER, etc.).
- **Key Findings**: FAIR_wmt20 and GPT-3 were the hardest to detect at the time.
- **Relevance**: Establishes the standard for "Authorship Attribution" and provides a large-scale dataset structure we can emulate.

### Paper 3: Evade ChatGPT Detectors via A Single Space
- **Authors**: Shuyang Cai, Wanyun Cui
- **Year**: 2023
- **Source**: arXiv:2307.02599
- **Key Contribution**: Demonstrated a simple adversarial attack (**SpaceInfi**) where adding a single space before a comma breaks detection.
- **Methodology**: Tested against white-box and black-box detectors.
- **Key Findings**: Detectors rely on subtle tokenization cues rather than semantic understanding. "Token mutation" caused by the extra space disrupts the detection signal.
- **Relevance**: Directly relevant to the "postediting" track of our leaderboard. Shows that minimal changes can maximize undetectability.

### Paper 4: Who Said That? Benchmarking Social Media AI Detection
- **Authors**: Wanyun Cui et al.
- **Year**: 2023
- **Source**: arXiv:2310.08240
- **Key Contribution**: Introduced **SAID** (Social media AI Detection) benchmark using real-world data from Zhihu and Quora.
- **Key Findings**: Humans familiar with LLMs *can* distinguish AI text (96.5% accuracy on Zhihu subset), contradicting earlier assumptions. User-oriented detection (using user history) is more effective than text-only detection.
- **Relevance**: Highlights the importance of "in-the-wild" data and user context, relevant for a robust leaderboard.

### Paper 5: RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors
- **Authors**: Liam Dugan et al.
- **Year**: 2024
- **Source**: arXiv:2405.07940
- **Key Contribution**: The largest and most diverse benchmark (**RAID**) with 6M+ generations, 11 models, 8 domains, 11 attacks, and 4 decoding strategies.
- **Key Findings**: Detectors fail significantly on adversarial attacks, unseen domains, and different sampling strategies (e.g., repetition penalties).
- **Relevance**: This is the state-of-the-art benchmark to beat or build upon. Our leaderboard should likely include or reference RAID's diverse tracks.

## Common Methodologies
- **Detection Methods**:
    - **Zero-shot/Statistical**: Perplexity, Burstiness, Negative Log-Curvature (DetectGPT).
    - **Supervised Classifiers**: Fine-tuned RoBERTa/BERT (standard baseline).
    - **Watermarking**: Injecting signals during generation (though often removed by attacks).
- **Adversarial Attacks**:
    - **Character-level**: Inserting spaces, homoglyphs (SpaceInfi).
    - **Paraphrasing**: Using another LLM to rewrite.
    - **Sampling**: Changing temperature or repetition penalties.

## Datasets in the Literature
- **RAID**: 6M+ samples, 11 models, diverse domains. (The "Gold Standard" currently).
- **TURINGBENCH**: 200K samples, news domain, older models.
- **SAID**: Social media data (Zhihu/Quora).
- **HC3**: Human vs ChatGPT Comparison Corpus (often used as a baseline).
- **M4**: Multi-Generator, Multi-Domain, Multi-Lingual dataset.

## Recommendations for Our Experiment
Based on the review, our leaderboard should focus on **robustness** and ** undetectability** across different axes:
1.  **Inference Track**: Measuring ADI across different base models (referencing CT^2).
2.  **Postediting Track**: Evaluating resistance to detection after simple edits (like SpaceInfi or paraphrasing).
3.  **Finetuning Track**: How much does finetuning on human data improve undetectability?
4.  **Pretraining Track**: (More advanced) Does pretraining architecture affect detectability?

**Recommended Datasets**:
- **RAID**: For robust evaluation.
- **HC3**: For simple baseline comparisons.
- **TURINGBENCH**: For authorship attribution tasks.

**Recommended Baselines**:
- **Detectors**: GPTZero (commercial proxy), DetectGPT (zero-shot), RoBERTa-based classifier (supervised).
- **Generators**: GPT-4, LLaMA-2/3, Mistral.
