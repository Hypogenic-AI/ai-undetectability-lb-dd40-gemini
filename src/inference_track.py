import os
import pandas as pd
import json
import numpy as np
from tqdm import tqdm
from utils import setup_path

setup_path()

try:
    from detectors.detector import get_detector
except ImportError as e:
    print(f"Error importing detector: {e}")
    # Fallback/Debug info
    import sys
    print(f"sys.path: {sys.path}")
    raise

def run_inference_track(output_file="results/inference_leaderboard.json"):
    print("Loading dataset...")
    df = pd.read_csv("datasets/raid/sample.csv")
    
    # We only care about AI models for the leaderboard ranking, 
    # but we also evaluate Human to see False Positive Rate.
    
    print("Initializing detector (ChatGPT-RoBERTa)...")
    try:
        detector = get_detector("chatgpt-roberta")
    except Exception as e:
        print(f"Failed to load chatgpt-roberta: {e}")
        print("Falling back to gpt2-base (Zero-shot)...")
        detector = get_detector("gpt2-base")

    results = []
    
    # Group by model
    for model_name, group in df.groupby("model"):
        print(f"Evaluating model: {model_name} ({len(group)} samples)")
        
        texts = group['generation'].tolist()
        
        # Batch inference if necessary, but detector.inference usually handles list
        # We'll do chunks of 16 to be safe with memory
        scores = []
        batch_size = 16
        for i in tqdm(range(0, len(texts), batch_size)):
            batch = texts[i:i+batch_size]
            try:
                batch_scores = detector.inference(batch)
                scores.extend(batch_scores)
            except Exception as e:
                print(f"Error in batch inference: {e}")
                scores.extend([0.5] * len(batch)) # Default to uncertainty
        
        avg_score = np.mean(scores)
        undetectability = 1 - avg_score
        
        results.append({
            "track": "inference",
            "model": model_name,
            "samples": len(texts),
            "avg_detector_score_ai_prob": float(avg_score),
            "undetectability_score": float(undetectability)
        })
        
    os.makedirs("results", exist_ok=True)
    with open(output_file, "w") as f:
        json.dump(results, f, indent=2)
    
    print(f"Inference track results saved to {output_file}")
    return results

if __name__ == "__main__":
    run_inference_track()
