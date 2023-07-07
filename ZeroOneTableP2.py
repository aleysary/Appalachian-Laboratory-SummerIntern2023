import sys

# Check if the input file is provided
if len(sys.argv) < 2:
    print("Please provide the input file as an argument.")
    sys.exit(1)

input_file = sys.argv[1]

# Check if the output file name is provided
if len(sys.argv) < 3:
    print("Please provide the output file name as an argument.")
    sys.exit(1)

output_file = sys.argv[2]

# Define the mapping for replacement
mapping = {
    'TPP': '0',
    'TPN': '1'
}

# Define the column headers
column_headers = "header\t  kingdom\tphylum\t  class\t  order\tfamily\t  genus\tspecies\tPI"

# Read the input file
with open(input_file, 'r') as file:
    lines = file.readlines()

# Modify the table
modified_lines = []
max_pi_length = 0  # To track the maximum length of the PI column
for line in lines:
    parts = line.strip().split('\t')

    # Skip the line if it doesn't have enough columns
    if len(parts) < 9:
        continue

    # Replace the second and middle columns
    modified_parts = [parts[0].ljust(12), mapping.get(parts[1], 'N/A').ljust(8)]
    for col in parts[2:8]:
        modified_parts.append(mapping.get(col, 'N/A').ljust(8))

    # Determine the correct position of the PI column
    if len(parts) >= 10:
        modified_parts.append(parts[9].strip())
    elif len(parts) >= 9:
        modified_parts.append(parts[8].strip())

    # Update the maximum length of the PI column
    max_pi_length = max(max_pi_length, len(modified_parts[-1]))

    # Join the modified parts and add to the modified lines
    modified_line = '\t'.join(modified_parts)
    modified_lines.append(modified_line)

# Adjust the alignment of the PI column in all lines
adjusted_lines = []
for line in modified_lines:
    parts = line.split('\t')
    pi_column = parts[-1]
    adjusted_pi = pi_column.ljust(max_pi_length)  # Adjust the PI column length
    adjusted_line = '\t'.join(parts[:-1] + [adjusted_pi])
    adjusted_lines.append(adjusted_line)

# Insert the column headers at the beginning
adjusted_lines.insert(0, column_headers)

# Save the modified table to the output file
with open(output_file, 'w') as file:
    file.write('\n'.join(adjusted_lines))

print(f"Modified table has been saved to '{output_file}'.")
