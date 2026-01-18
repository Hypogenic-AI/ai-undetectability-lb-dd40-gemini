# AI Undetectability Leaderboard

## Metric
**Undetectability Score** (0-100): Higher is better for the generator/attacker.
- 0: Perfectly Detected (AUROC 1.0)
- 100: Completely Undetectable (AUROC 0.5)

## Track 1: Inference (Model Robustness)
Evaluated on RAID dataset (Sample), Detector: RoBERTa-Base (OpenAI).

| Domain | Model | Decoding | AUROC | Undetectability Score |
|---|---|---|---|---|
| abstracts | llama-chat | greedy | 0.909 | **18.2** |

## Track 2: Postediting (Adversarial Attacks)
Evaluated on RAID dataset (Sample), Detector: RoBERTa-Base (OpenAI).

| Method | Model | AUROC | Undetectability Score | Improvement |
|---|---|---|---|---|
| None (Baseline) | llama-chat | 0.909 | 18.2 | - |
| SpaceInfi | llama-chat | 0.750 | **50.1** | +31.8 |
