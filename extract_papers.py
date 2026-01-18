import pdfplumber
import glob
import os

pdf_files = glob.glob("papers/*.pdf")
output_file = "papers_summary.txt"

with open(output_file, "w") as out:
    for pdf_path in sorted(pdf_files):
        print(f"Processing {pdf_path}...")
        out.write(f"\n\n=== FILE: {os.path.basename(pdf_path)} ===\n")
        try:
            with pdfplumber.open(pdf_path) as pdf:
                # Read first 3 pages
                for i, page in enumerate(pdf.pages[:3]):
                    text = page.extract_text()
                    if text:
                        out.write(f"--- Page {i+1} ---\n")
                        out.write(text)
                        out.write("\n")
        except Exception as e:
            out.write(f"Error reading {pdf_path}: {e}\n")

print("Extraction complete.")
