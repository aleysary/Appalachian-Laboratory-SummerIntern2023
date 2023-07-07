import sys

# Read the input file and output file from command line arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# Define the column headers for the new columns
new_columns = ['PI range', 'Number of 1s', 'Number of 0s', 'Number of N/A']

# Create a dictionary to store the counts for each range
counts = {}

# Read the input file and process each line
with open(input_file, 'r') as file:
    for line in file:
        # Split the line 
        values = line.strip().split()

        # I Extract the PI range and values for each range
        pi_range = values[0] + ' to ' + values[2]
        range_values = values[3:]

        # I Count the number of 1s, 0s, and N/As in the range
        count_1s = range_values.count('1')
        count_0s = range_values.count('0')
        count_na = range_values.count('N/A')

        # Stores the counts in the dictionary
        counts[pi_range] = [count_1s, count_0s, count_na]

# Save the output in the output file
with open(output_file, 'w') as file:
    # Writes the header
    header = '\t'.join(new_columns)
    file.write(header + '\n')

    # Write the counts for each range
    for pi_range, count_values in counts.items():
        counts_str = '\t'.join(str(count) for count in count_values)
        row = f'{pi_range}\t{counts_str}'
        file.write(row + '\n')