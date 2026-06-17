sequence_dict = {}

current_header = None
current_sequence = ""

with open("data/sample.fasta", "r") as fasta_file:
    for line in fasta_file:
        line = line.strip()

        if line.startswith(">"):

            if current_header:
                sequence_dict[current_header] = len(current_sequence)

            current_header = line[1:]
            current_sequence = ""

        else:
            current_sequence += line

if current_header:
    sequence_dict[current_header] = len(current_sequence)

print("\nSequence Summary\n")

for gene, length in sequence_dict.items():
    print(f"{gene}: {length} bp")

lengths = list(sequence_dict.values())

print("\nOverall Statistics")
print("Number of sequences:", len(lengths))
print("Longest sequence:", max(lengths))
print("Shortest sequence:", min(lengths))
print("Average length:", round(sum(lengths)/len(lengths), 2))
