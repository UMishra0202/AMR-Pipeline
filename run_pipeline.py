import subprocess

print("Running FASTA Statistics...")
subprocess.run(["python", "scripts/fasta_stats.py"])

print("\nFiltering Sequences...")
subprocess.run(["python", "scripts/filter_fasta.py"])

print("\nGenerating CSV Summary...")
subprocess.run(["python", "scripts/fasta_to_csv.py"])

print("\nGenerating GC Plot...")
subprocess.run(["python", "scripts/gc_plot.py"])

print("\nPipeline Complete!")
