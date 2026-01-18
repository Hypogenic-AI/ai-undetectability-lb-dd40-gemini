# Resources Catalog

## Summary
This document catalogs all resources gathered for the research project "A Leaderboard for AI Undetectability".

## Papers
Total papers downloaded: 5

| Title | Authors | Year | File | Key Info |
|-------|---------|------|------|----------|
| Counter Turing Test CT^2 | Chakraborty et al. | 2023 | papers/2310.05030... | AI Detectability Index |
| TURINGBENCH | Uchendu et al. | 2021 | papers/2109.13296... | Benchmark for AA |
| Evade ChatGPT Detectors | Cai & Cui | 2023 | papers/2307.02599... | Adversarial Attack |
| Who Said That? | Cui et al. | 2023 | papers/2310.08240... | Social Media Benchmark |
| RAID | Dugan et al. | 2024 | papers/2405.07940... | SOTA Benchmark |

See `papers/README.md` for details.

## Datasets
Total datasets downloaded: 1 (Sample) + others attempted

| Name | Source | Size | Task | Location | Notes |
|------|--------|------|------|----------|-------|
| RAID | HuggingFace | 6M+ (Sample: 100) | Robust Detection | datasets/raid/ | Parquet format |
| HC3 | HuggingFace | - | Human vs AI | - | Download failed (legacy script) |
| TuringBench | HuggingFace | - | AA | - | Download failed (legacy script) |

See `datasets/README.md` for details.

## Code Repositories
Total repositories cloned: 3

| Name | URL | Purpose | Location |
|------|-----|---------|----------|
| RAID | github.com/liamdugan/raid | Benchmark | code/raid/ |
| DetectGPT | github.com/eric-mitchell/detect-gpt | Detection Method | code/detect-gpt/ |
| TuringBench | github.com/AdaUchendu/TuringBench | Benchmark | code/turingbench/ |

See `code/README.md` for details.

## Resource Gathering Notes

### Search Strategy
- Used `find_papers.py` to identify initial set of relevant papers.
- Manually searched Google/ArXiv for PDFs and code.
- Prioritized benchmarks (RAID, TuringBench) and adversarial attacks.

### Selection Criteria
- **RAID**: Chosen because it is the most comprehensive and recent (2024) benchmark.
- **SpaceInfi**: Chosen for its simplicity and effectiveness as an adversarial baseline.
- **CT^2**: Chosen for the "AI Detectability Index" concept relevant to the inference track.

### Challenges
- **Dataset Access**: Some older datasets (HC3, TuringBench) rely on legacy HuggingFace loading scripts which are no longer supported in the current `datasets` library. Workaround: Focus on RAID (Parquet-based) or manually download files if strictly needed later.
- **Environment**: `pip` was missing in venv, used miniconda python.

### Recommendations for Experiment Design
1.  **Primary Dataset**: **RAID**. It covers everything we need (diverse models, domains, attacks).
2.  **Baselines**: Use DetectGPT (code available) and supervised RoBERTa (often included in RAID repo or easily trainable).
3.  **Metrics**: ROC-AUC, F1-score, and **AI Detectability Index (ADI)**.
4.  **Tracks**:
    - **Inference**: Use RAID's diverse models.
    - **Postediting**: Use RAID's adversarial attacks + implement SpaceInfi.
