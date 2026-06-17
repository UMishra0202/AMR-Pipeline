MIN_LENGTH = 50

sequence_dict = {}

current_header = None
current_sequence = ""

with open("data/sample.fasta", "r") as fasta_file:

    for line in fasta_file:
        line = line.strip()

        if line.startswith(">"):

            if current_header:
                sequence_dict[current_header] = current_sequence

            current_header = line
            current_sequence = ""

        else:
            current_sequence += line

if current_header:
    sequence_dict[current_header] = current_sequence

filtered_count = 0

with open("results/filtered_sequences.fasta", "w") as output_file:

    for header, sequence in sequence_dict.items():

        if len(sequence) >= MIN_LENGTH:

            output_file.write(header + "\n")
            output_file.write(sequence + "\n")

            filtered_count += 1

print("Filtering Complete")
print("Minimum Length:", MIN_LENGTH)
print("Sequences Retained:", filtered_count)
print("Output File: results/filtered_sequences.fasta")
