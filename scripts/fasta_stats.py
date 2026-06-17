sequence_dict = {}

report_lines = []

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


report_lines.append("Sequence Summary\n")

print("\nSequence Summary\n")

for gene, sequence in sequence_dict.items():


	length = len(sequence)


	gc_count = sequence.count("G") + sequence.count("C")


	gc_percent = (gc_count / length) * 100

	report_lines.append(f"{gene}")
	report_lines.append(f"Length: {length} bp")
	report_lines.append(f"GC Content: {gc_percent:.2f}%")
	report_lines.append("")


	print(f"{gene}")
	print(f"Length: {length} bp")
	print(f"GC Content: {gc_percent:.2f}%\n")

lengths = []

for sequence in sequence_dict.values():
    lengths.append(len(sequence))


report_lines.append("Overall Statistics")
report_lines.append(f"Number of sequences: {len(lengths)}")
report_lines.append(f"Longest sequence: {max(lengths)}")
report_lines.append(f"Shortest sequence: {min(lengths)}")
report_lines.append(f"Average length: {round(sum(lengths)/len(lengths), 2)}")

print("Overall Statistics")
print("Number of sequences:", len(lengths))
print("Longest sequence:", max(lengths))
print("Shortest sequence:", min(lengths))
print("Average length:", round(sum(lengths)/len(lengths), 2))

with open("results/fasta_report.txt", "w") as report_file:

    for line in report_lines:
        report_file.write(line + "\n")

print("\nReport saved to results/fasta_report.txt")
