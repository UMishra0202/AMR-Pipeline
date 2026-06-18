import argparse
import subprocess

parser = argparse.ArgumentParser()

parser.add_argument("input_file")

args = parser.parse_args()

print("Running FASTA Statistics...")
subprocess.run(
    ["python", "scripts/fasta_stats.py", args.input_file]
)

print("\nFiltering Sequences...")
subprocess.run(
    ["python", "scripts/filter_fasta.py"]
)

print("\nGenerating CSV Summary...")
subprocess.run(
    ["python", "scripts/fasta_to_csv.py"]
)

print("\nGenerating GC Plot...")
subprocess.run(
    ["python", "scripts/gc_plot.py"]
)

print("\nPipeline Complete!")
