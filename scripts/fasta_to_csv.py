import csv

sequence_dict = {}

current_header = None
current_sequence = ""

with open("data/sample.fasta", "r") as fasta_file:

    for line in fasta_file:
        line = line.strip()

        if line.startswith(">"):

            if current_header:
                sequence_dict[current_header] = current_sequence

            current_header = line[1:]
            current_sequence = ""

        else:
            current_sequence += line

if current_header:
    sequence_dict[current_header] = current_sequence


with open("results/sequence_summary.csv", "w", newline="") as csv_file:

    writer = csv.writer(csv_file)

    writer.writerow(["Gene", "Length", "GC_Content"])

    for gene, sequence in sequence_dict.items():

        length = len(sequence)

        gc_count = sequence.count("G") + sequence.count("C")

        gc_percent = round((gc_count / length) * 100, 2)

        writer.writerow([gene, length, gc_percent])

print("CSV report generated")
print("Output: results/sequence_summary.csv")
