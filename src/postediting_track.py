import os
import pandas as pd
import json
import numpy as np
import re
import random
from tqdm import tqdm
from utils import setup_path

setup_path()

try:
    from detectors.detector import get_detector
except ImportError:
    import sys
    # Try adding code/raid explicitly if setup_path didn't work (paranoid check)
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../code/raid')))
    from detectors.detector import get_detector

def insert_space_before_comma(text):
    # Find all commas
    commas = [m.start() for m in re.finditer(r",", text)]
    if not commas:
        return text
    # Insert space before ALL commas to maximize effect for this demo, 
    # or just one. The paper says "single space". Let's do one random one.
    idx = random.choice(commas)
    return text[:idx] + " " + text[idx:]

def run_postediting_track(output_file="results/postediting_leaderboard.json"):
    print("Loading dataset...")
    df = pd.read_csv("datasets/raid/sample.csv")
    
    # Filter for AI only
    df_ai = df[df['label'] != 'human'].copy()
    print(f"Found {len(df_ai)} AI samples.")
    
    print("Initializing detector...")
    try:
        detector = get_detector("chatgpt-roberta")
    except:
        detector = get_detector("gpt2-base")

    # Baseline
    print("Running Baseline Inference...")
    texts = df_ai['generation'].tolist()
    baseline_scores = []
    batch_size = 16
    for i in tqdm(range(0, len(texts), batch_size)):
        batch = texts[i:i+batch_size]
        try:
            baseline_scores.extend(detector.inference(batch))
        except:
            baseline_scores.extend([0.5]*len(batch))
            
    # Attack
    print("Applying SpaceInfi Attack...")
    attacked_texts = [insert_space_before_comma(t) for t in texts]
    
    print("Running Attacked Inference...")
    attacked_scores = []
    for i in tqdm(range(0, len(attacked_texts), batch_size)):
        batch = attacked_texts[i:i+batch_size]
        try:
            attacked_scores.extend(detector.inference(batch))
        except:
            attacked_scores.extend([0.5]*len(batch))
            
    # Compare
    baseline_avg = np.mean(baseline_scores)
    attacked_avg = np.mean(attacked_scores)
    
    baseline_undetectability = 1 - baseline_avg
    attacked_undetectability = 1 - attacked_avg
    
    result = {
        "track": "postediting",
        "attack": "SpaceInfi",
        "samples": len(df_ai),
        "baseline_detection_score": float(baseline_avg),
        "baseline_undetectability": float(baseline_undetectability),
        "attacked_detection_score": float(attacked_avg),
        "attacked_undetectability": float(attacked_undetectability),
        "improvement": float(attacked_undetectability - baseline_undetectability)
    }
    
    os.makedirs("results", exist_ok=True)
    with open(output_file, "w") as f:
        json.dump(result, f, indent=2)
        
    print(f"Postediting results: {result}")
    return result

if __name__ == "__main__":
    run_postediting_track()
