import pandas as pd
import random
import re

input_file = "datasets/raid/sample.csv"
output_file = "datasets/raid/sample_attacked_space.csv"

def insert_space_before_comma(text):
    # Find all commas
    commas = [m.start() for m in re.finditer(r",", text)]
    if not commas:
        return text
    
    # Pick a random comma (or the first one for consistency/simplicity)
    # The paper mentions "random comma", but for deterministic testing, let's try first comma first
    # actually, paper says "random comma". Let's do random.
    idx = random.choice(commas)
    
    # Insert space
    return text[:idx] + " " + text[idx:]

df = pd.read_csv(input_file)

# Only attack AI text
# Check label format. RAID uses 'model' or 'label'. Let's inspect content.
# Assuming 'label' column exists and 'human' is the negative class.
# If 'label' is 'ai' or similar, we attack.

# In RAID sample, let's see what the labels are. 
# Usually 'human' vs 'gpt-4', etc.
# If it's NOT 'human', we treat it as AI.

def attack_row(row):
    if str(row.get("label", "")).lower() != "human":
        return insert_space_before_comma(row["generation"])
    return row["generation"]

df["generation"] = df.apply(attack_row, axis=1)

df.to_csv(output_file, index=False)
print(f"Attacked dataset saved to {output_file}")
