# FASTA statistics script

sequence_count = 0
sequence_lengths = []
current_sequence = ""

with open("data/sample.fasta", "r") as fasta_file:
    for line in fasta_file:
        line = line.strip()

        if line.startswith(">"):
            if current_sequence:
                sequence_lengths.append(len(current_sequence))

            sequence_count += 1
            current_sequence = ""

        else:
            current_sequence += line

# Save the final sequence
if current_sequence:
    sequence_lengths.append(len(current_sequence))

print("Number of sequences:", sequence_count)
print("Sequence lengths:", sequence_lengths)
print("Longest sequence:", max(sequence_lengths))
print("Shortest sequence:", min(sequence_lengths))
average_length = sum(sequence_lengths) / len(sequence_lengths)

print("Number of sequences:", sequence_count)
print("Sequence lengths:", sequence_lengths)
print("Longest sequence:", max(sequence_lengths))
print("Shortest sequence:", min(sequence_lengths))
print("Average length:", round(average_length, 2))
