import csv
import matplotlib.pyplot as plt

genes = []
gc_values = []

with open("results/sequence_summary.csv", "r") as csv_file:
    reader = csv.DictReader(csv_file)

    for row in reader:
        genes.append(row["Gene"])
        gc_values.append(float(row["GC_Content"]))

plt.figure(figsize=(8,5))

plt.bar(genes, gc_values)

plt.title("GC Content of AMR Genes")
plt.xlabel("Gene")
plt.ylabel("GC Content (%)")

plt.tight_layout()

plt.savefig("results/gc_content_plot.png")

print("Plot saved: results/gc_content_plot.png")
