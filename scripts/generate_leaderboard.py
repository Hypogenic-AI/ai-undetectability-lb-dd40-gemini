import json
import pandas as pd
import os

BASELINE_FILE = "results/eval_baseline.json"
ATTACKED_FILE = "results/eval_attacked.json"
OUTPUT_FILE = "results/LEADERBOARD.md"

def load_results(filepath):
    with open(filepath, "r") as f:
        data = json.load(f)
    return data["scores"]

def calculate_undetectability(auroc):
    """
    Calculate Undetectability Score (0-100).
    AUROC 1.0 (Perfect Detection) -> 0
    AUROC 0.5 (Random Guessing) -> 100
    """
    val = max(auroc, 0.5)
    return (1 - val) * 200

def generate_markdown(baseline_scores, attacked_scores):
    NL = chr(10)
    md = f"# AI Undetectability Leaderboard{NL}{NL}"
    md += f"## Metric{NL}"
    md += f"**Undetectability Score** (0-100): Higher is better for the generator/attacker.{NL}"
    md += f"- 0: Perfectly Detected (AUROC 1.0){NL}"
    md += f"- 100: Completely Undetectable (AUROC 0.5){NL}{NL}"
    
    md += f"## Track 1: Inference (Model Robustness){NL}"
    md += f"Evaluated on RAID dataset (Sample), Detector: RoBERTa-Base (OpenAI).{NL}{NL}"
    md += f"| Domain | Model | Decoding | AUROC | Undetectability Score |{NL}"
    md += f"|---|---|---|---|---|{NL}"
    
    models = set(s['model'] for s in baseline_scores if s['model'] != 'all')
    
    for model in sorted(models):
        entries = [s for s in baseline_scores if s['model'] == model and s['attack'] == 'none']
        if not entries: continue
        entry = next((s for s in entries if s['domain'] == 'abstracts'), entries[0])
        
        auroc = entry['auroc']
        score = calculate_undetectability(auroc)
        md += f"| {entry['domain']} | {model} | {entry['decoding']} | {auroc:.3f} | **{score:.1f}** |{NL}"

    md += f"{NL}## Track 2: Postediting (Adversarial Attacks){NL}"
    md += f"Evaluated on RAID dataset (Sample), Detector: RoBERTa-Base (OpenAI).{NL}{NL}"
    md += f"| Method | Model | AUROC | Undetectability Score | Improvement |{NL}"
    md += f"|---|---|---|---|---|{NL}"
    
    for model in sorted(models):
        baseline_entries = [s for s in baseline_scores if s['model'] == model and s['attack'] == 'none']
        attacked_entries = [s for s in attacked_scores if s['model'] == model and s['attack'] == 'none']
        
        if not baseline_entries or not attacked_entries: continue
        
        b_entry = next((s for s in baseline_entries if s['domain'] == 'abstracts'), baseline_entries[0])
        a_entry = next((s for s in attacked_entries if s['domain'] == 'abstracts'), attacked_entries[0])
        
        b_auroc = b_entry['auroc']
        a_auroc = a_entry['auroc']
        
        b_score = calculate_undetectability(b_auroc)
        a_score = calculate_undetectability(a_auroc)
        imp = a_score - b_score
        
        md += f"| None (Baseline) | {model} | {b_auroc:.3f} | {b_score:.1f} | - |{NL}"
        md += f"| SpaceInfi | {model} | {a_auroc:.3f} | **{a_score:.1f}** | +{imp:.1f} |{NL}"

    return md

if __name__ == "__main__":
    if os.path.exists(BASELINE_FILE) and os.path.exists(ATTACKED_FILE):
        b_scores = load_results(BASELINE_FILE)
        a_scores = load_results(ATTACKED_FILE)
        
        md_content = generate_markdown(b_scores, a_scores)
        
        with open(OUTPUT_FILE, "w") as f:
            f.write(md_content)
        
        print(f"Leaderboard generated at {OUTPUT_FILE}")
    else:
        print("Results files missing.")
