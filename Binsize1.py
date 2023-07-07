import sys

# Read the input file
filename = sys.argv[1]  # Assuming the input file is passed as a command-line argument
output_filename = sys.argv[2]  # Assuming the output file name is passed as a command-line argument
with open(filename, 'r') as file:
    lines = file.readlines()

# Process the input data
new_table = []
cumulative_counts = [0, 0, 0]  # Cumulative counts for 1s, 0s, and N/A

for i, line in enumerate(lines[1:], start=1):  # Skip the header line
    range_values = line.strip().split('\t')
    pi_range = f"100 to {101 - i}"

    counts = list(map(int, range_values[1:]))

    cumulative_counts = [sum(x) for x in zip(cumulative_counts, counts)]
    new_table.append([pi_range] + cumulative_counts)

# Save the new table to the output file
with open(output_filename, 'w') as output_file:
    output_file.write("PI range\tNumber of 1s\tNumber of 0s\tNumber of N/A\n")
    for row in new_table:
        output_file.write('\t'.join(map(str, row)) + '\n')
