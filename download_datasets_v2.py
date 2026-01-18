from datasets import load_dataset
import os
import json
import random

os.makedirs("datasets/raid", exist_ok=True)

print("Downloading RAID sample (balanced)...")
try:
    # Streaming
    raid = load_dataset("liamdugan/raid", split='train', streaming=True)
    
    human_samples = []
    ai_samples = []
    
    for item in raid:
        if item['model'] == 'human':
            if len(human_samples) < 50:
                human_samples.append(item)
        else:
            if len(ai_samples) < 50:
                ai_samples.append(item)
        
        if len(human_samples) >= 50 and len(ai_samples) >= 50:
            break
            
    final_sample = human_samples + ai_samples
    
    with open("datasets/raid/sample.json", "w") as f:
        json.dump(final_sample, f, indent=2)
    print(f"RAID sample downloaded. {len(human_samples)} human, {len(ai_samples)} AI.")
except Exception as e:
    print(f"Error downloading RAID: {e}")
