import json
import pandas as pd
import os

input_file = "datasets/raid/sample.json"
output_file = "datasets/raid/sample.csv"

# Load JSON
with open(input_file, "r") as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data)

# Add ID if missing
if "id" not in df.columns:
    df["id"] = range(len(df))

# Map label
df["label"] = df["model"].apply(lambda x: "human" if x == "human" else "ai")

# Ensure required columns exist
required_columns = ["id", "generation", "label"]
for col in required_columns:
    if col not in df.columns:
        print(f"Warning: {col} missing from data")

# Save to CSV
df.to_csv(output_file, index=False)
print(f"Converted {len(df)} records to {output_file}")
