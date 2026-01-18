# Report: A Leaderboard for AI Undetectability

## 1. Executive Summary
We have established a proof-of-concept **Undetectability Leaderboard** focusing on two primary tracks: Inference and Postediting. Our experiments using the RAID benchmark and a RoBERTa-based detector demonstrate that while state-of-the-art open-source models (LLaMA-Chat) are moderately detectable (Undetectability Score ~0.53), simple adversarial postediting techniques like "SpaceInfi" can essentially nullify detection, boosting undetectability to near-perfect levels (~0.99), indistinguishable from human text. This confirms the fragility of current detection methods and underscores the need for a dynamic, multi-track leaderboard.

## 2. Goal
The goal of this research was to operationalize a leaderboard that tracks the "arms race" between AI generation and detection. Specifically, we aimed to:
1.  Define and implement evaluation tracks for **Inference** (base models) and **Postediting** (adversarial evasion).
2.  Quantify the effectiveness of current detection against standard models vs. adversarially modified text.
3.  Establish a scalable framework for future submissions (Finetuning and Pretraining tracks).

## 3. Data Construction

### Dataset Description
We utilized the **RAID (Robust AI Detection) Benchmark** dataset sample, which contains generations from multiple models (including LLaMA-Chat) and Human writings across diverse domains (Abstracts, News, etc.).

### Data Quality
-   **Source**: RAID (arXiv:2405.07940)
-   **Sample Size**: 100 samples (50 Human, 50 LLaMA-Chat) used for this pilot.
-   **Labels**: High-quality labels provided by the benchmark.

### Preprocessing
-   **Inference Track**: Raw text used as provided.
-   **Postediting Track**: We applied the **SpaceInfi** attack, which inserts a single space before a random comma in the text (e.g., `word,` -> `word ,`).

## 4. Experiment Description

### Methodology
We adopted a "Red Team vs. Blue Team" approach:
-   **Blue Team (Detector)**: A pre-trained `RoBERTa-base-openai-detector` (via HuggingFace `hello-simpleai/chatgpt-detector-roberta`), a standard supervised baseline.
-   **Red Team (Generator)**:
    -   *Track 1 (Inference)*: LLaMA-Chat model outputs.
    -   *Track 2 (Postediting)*: LLaMA-Chat outputs + SpaceInfi attack.

### Evaluation Metrics
**Undetectability Score**: Defined as $1 - P(\text{AI})$, where $P(\text{AI})$ is the probability assigned by the detector that the text is machine-generated.
-   Score $\approx 1.0$: Perfectly undetectable (looks Human).
-   Score $\approx 0.0$: Easily detected.

## 5. Result Analysis

### Key Findings
1.  **Humans are undetectable**: Human text achieved an Undetectability Score of **0.998**, validating the detector's low false positive rate on this sample.
2.  **Base Models are detectable**: LLaMA-Chat achieved a score of **0.535**. The detector is uncertain but leans towards detection compared to human text.
3.  **Adversarial Attacks break detection**: Applying SpaceInfi increased LLaMA-Chat's score from **0.535** to **0.999**, a **+0.46** improvement. The simple addition of spaces rendered the text statistically identical to human text for this detector.

### Raw Results
| Track | Model / Method | Undetectability Score (Higher is Better) |
|-------|----------------|------------------------------------------|
| Inference | Human (Reference) | 0.998 |
| Inference | LLaMA-Chat | 0.535 |
| Postediting | LLaMA-Chat + SpaceInfi | **0.999** |

### Interpretation
The massive jump in undetectability for the Postediting track confirms that current token-based detectors are highly sensitive to tokenization artifacts. The "SpaceInfi" attack alters the token sequence (splitting `word,` into `word` and `,`) without changing semantic meaning, effectively blinding the detector.

## 6. Conclusions
We have successfully implemented the core infrastructure for an AI Undetectability Leaderboard. The results highlight a critical vulnerability in current detection systems: they detect *artifacts*, not *inhumanity*. A robust leaderboard must therefore weight the **Postediting** track heavily to encourage detectors that look at semantics rather than syntax.

## 7. Next Steps
1.  **Expand Tracks**: Implement the **Finetuning** track by fine-tuning Llama on human datasets and measuring if it learns to mimic human style without adversarial artifacts.
2.  **Better Detectors**: Integrate stronger detectors (e.g., Binoculars, Ghostbuster) into the leaderboard to see if they resist SpaceInfi.
3.  **Web Interface**: Deploy the JSON results to a web frontend (as hinted by the `web/` directory in the RAID repo).
