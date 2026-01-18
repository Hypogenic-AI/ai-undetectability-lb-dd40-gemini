# Research Plan: A Leaderboard for AI Undetectability

## Motivation & Novelty Assessment

### Why This Research Matters
As AI-generated text becomes indistinguishable from human writing, the ability to detect it becomes critical for academic integrity, misinformation control, and platform safety. However, current detectors are often brittle. An "Undetectability Leaderboard" incentivizes the development of more human-like generation methods and, conversely, more robust detection systems. It shifts the focus from "how smart is this model?" to "how human is this model?".

### Gap in Existing Work
Existing benchmarks like RAID and TuringBench provide datasets and evaluations but are static snapshots. There is no live, competitive leaderboard that explicitly separates "inference" (base model), "postediting" (adversarial attacks), and "finetuning" tracks. Most current research treats detection as a binary classification problem rather than a continuous game of evasion and detection.

### Our Novel Contribution
We propose a dynamic leaderboard structure with four distinct tracks:
1.  **Inference**: Base model outputs.
2.  **Postediting**: Outputs modified by a program (e.g., adversarial attacks).
3.  **Finetuning**: Models fine-tuned for human-likeness.
4.  **Pretraining**: New architectures/models.

We will demonstrate the viability of this leaderboard by implementing the evaluation pipeline for the first two tracks (Inference and Postediting) using the RAID benchmark and the SpaceInfi adversarial attack.

### Experiment Justification
-   **Experiment 1 (Inference Track)**: Establish baseline detectability scores for standard LLMs (GPT-4, Llama, etc.) using state-of-the-art detectors. This validates the scoring metric.
-   **Experiment 2 (Postediting Track)**: Apply the "SpaceInfi" attack (inserting spaces) and measuring the drop in detection accuracy. This proves the need for a separate track for post-processing and highlights detector fragility.

## Research Question
Can we establish a robust, multi-track leaderboard framework that accurately quantifies the trade-off between AI text undetectability and content preservation?

## Proposed Methodology

### Approach
We will utilize the **RAID benchmark** codebase and dataset as the foundation. RAID provides a diverse set of generations and an evaluation harness. We will extend this to support our specific leaderboard tracks.

### Experimental Steps
1.  **Environment Setup**: Install `raid` dependencies and `detect-gpt` if needed.
2.  **Inference Track Baseline**:
    *   Load RAID dataset samples (Human vs. AI from various models).
    *   Run a battery of detectors (RoBERTa-base-detector, Log-Likelihood based).
    *   Compute "Undetectability Score" (1 - Detection Accuracy or similar).
3.  **Postediting Track Implementation**:
    *   Implement the **SpaceInfi** attack (inserting spaces before punctuation).
    *   Apply this to the RAID samples.
    *   Re-run detectors.
    *   Measure the delta in undetectability.
4.  **Leaderboard Generation**:
    *   Aggregating scores into a JSON/Markdown leaderboard format.

### Baselines
-   **Detectors**: RoBERTa-based detector (standard supervised baseline), Entropy-based / Perplexity-based (zero-shot).
-   **Generators**: Models available in RAID (e.g., GPT-3, GPT-4, Llama).

### Evaluation Metrics
-   **Detection Accuracy (ACC)**: Pr(Detector says AI | AI Text).
-   **Undetectability Score**: 1 - ROC-AUC (or simply 1 - ACC for balanced sets).
-   **Content Preservation** (for Postediting): Since we are using simple attacks like SpaceInfi, content is preserved by definition, but we will note this.

## Timeline and Milestones
-   **Phase 2 (10 min)**: Environment setup.
-   **Phase 3 (30 min)**: Implement SpaceInfi and integrate RAID evaluation harness.
-   **Phase 4 (40 min)**: Run detection on clean vs. attacked data.
-   **Phase 5 (20 min)**: Analyze results and compile leaderboard.
-   **Phase 6 (20 min)**: Documentation.

## Potential Challenges
-   **Compute**: Running large model detectors might be slow. *Mitigation*: Use smaller subsets of RAID (e.g., 100-500 samples) to demonstrate the pipeline.
-   **Dependencies**: RAID code might have complex dependencies. *Mitigation*: Use `uv` to manage them cleanly.

## Success Criteria
-   A functional script that takes a dataset (Track 1) or a postediting function (Track 2) and outputs a "Leaderboard Score".
-   Demonstration that SpaceInfi significantly increases undetectability scores.
