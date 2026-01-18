# Downloaded Datasets

This directory contains datasets for the research project. Data files are NOT committed to git due to size.

## Dataset 1: RAID (Robust AI Detection)

### Overview
- **Source**: [HuggingFace: liamdugan/raid](https://huggingface.co/datasets/liamdugan/raid)
- **Size**: 6M+ samples (Full dataset). We have downloaded a small sample.
- **Format**: HuggingFace Dataset (Parquet).
- **Task**: Detection of AI-generated text across 11 models, 8 domains, and adversarial attacks.
- **License**: Check repository.

### Download Instructions

**Using HuggingFace:**
```python
from datasets import load_dataset
# Load full dataset (large!)
dataset = load_dataset("liamdugan/raid")
# Load streaming (recommended for exploration)
dataset = load_dataset("liamdugan/raid", streaming=True)
```

### Sample Data
See `datasets/raid/sample.json` for the first 100 examples.
Each example contains:
- `generation`: The text content.
- `label`: ai or human (check specific fields).
- `model`: The model used (e.g. gpt-4).
- `domain`: e.g. news, recipes.
- `attack`: method used (if any).

## Other Datasets (Attempted)
- **HC3**: `Hello-SimpleAI/HC3`. Failed to download due to legacy script support in `datasets` library.
- **TuringBench**: `turingbench/TuringBench`. Failed to download due to legacy script support.

To use these, you may need an older version of `datasets` or find a Parquet version.
