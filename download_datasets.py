from datasets import load_dataset
import os
import json

os.makedirs("datasets", exist_ok=True)

# 1. HC3
print("Downloading HC3...")
try:
    hc3 = load_dataset("Hello-SimpleAI/HC3", trust_remote_code=True)
    hc3.save_to_disk("datasets/hc3")
    print("HC3 downloaded.")
    # Save sample
    with open("datasets/hc3_sample.json", "w") as f:
        # Convert to dict for JSON serialization if needed, though dataset items are usually dicts
        item = hc3['train'][0]
        json.dump(item, f, indent=2)
except Exception as e:
    print(f"Error downloading HC3: {e}")

# 2. TuringBench
print("Downloading TuringBench...")
try:
    # Load AA task (Authorship Attribution)
    tb = load_dataset("turingbench/TuringBench", "AA", trust_remote_code=True)
    tb.save_to_disk("datasets/turingbench")
    print("TuringBench downloaded.")
    with open("datasets/turingbench_sample.json", "w") as f:
        item = tb['train'][0]
        json.dump(item, f, indent=2)
except Exception as e:
    print(f"Error downloading TuringBench: {e}")

# 3. RAID (Sample)
print("Downloading RAID sample...")
try:
    # Streaming to avoid full download
    raid = load_dataset("liamdugan/raid", streaming=True)
    # Get first 100 examples
    raid_sample = list(raid['train'].take(100))
    
    with open("datasets/raid_sample.json", "w") as f:
        json.dump(raid_sample, f, indent=2)
    print("RAID sample downloaded.")
except Exception as e:
    print(f"Error downloading RAID: {e}")

print("Done.")
