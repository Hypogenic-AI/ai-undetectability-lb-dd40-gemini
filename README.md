# AI Undetectability Leaderboard

A dynamic leaderboard to track the state of AI text detection and evasion across four tracks: Inference, Postediting, Finetuning, and Pretraining.

## Key Findings (Pilot)
-   **Base Models are Detectable**: LLaMA-Chat has an undetectability score of ~0.53 against RoBERTa detectors.
-   **Adversarial Edits Win**: The **SpaceInfi** attack (inserting spaces before commas) boosts undetectability to **0.999**, making AI text indistinguishable from human text (0.998).
-   **Detector Fragility**: Current detectors rely heavily on tokenization artifacts that are easily obfuscated.

## Repository Structure
-   `src/`: Evaluation scripts.
    -   `inference_track.py`: Evaluates base model undetectability.
    -   `postediting_track.py`: Evaluates adversarial attack effectiveness.
-   `results/`: JSON outputs of the leaderboard.
    -   `inference_leaderboard.json`
    -   `postediting_leaderboard.json`
-   `datasets/`: RAID benchmark samples.
-   `code/raid/`: RAID benchmark evaluation harness.
-   `REPORT.md`: Full research report.

## How to Reproduce
1.  **Setup Environment**:
    ```bash
    uv venv
    source .venv/bin/activate
    uv pip install pandas numpy tqdm torch transformers scikit-learn openai datasets matplotlib lightgbm cohere sacrebleu nltk tiktoken wget lingua-language-detector
    ```
2.  **Run Inference Track**:
    ```bash
    python src/inference_track.py
    ```
3.  **Run Postediting Track**:
    ```bash
    python src/postediting_track.py
    ```
4.  **View Results**: Check `results/*.json` and `REPORT.md`.

## Credits
Based on the [RAID Benchmark](https://github.com/liamdugan/raid) and "Evade ChatGPT Detectors via A Single Space" (SpaceInfi).
