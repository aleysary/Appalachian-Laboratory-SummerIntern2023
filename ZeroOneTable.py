import sys

# Check if the input file is provided as a command-line argument
if len(sys.argv) < 2:
    print("Please provide the input file as a command-line argument.")
    print("Usage: python3 ZeroOneTable.py <input_file> <output_file>")
    sys.exit(1)

input_file = sys.argv[1]

# Check if the output file is provided as a command-line argument
if len(sys.argv) >= 3:
    output_file = sys.argv[2]
else:
    output_file = "tableP.txt"  # Set a default output file name

# Open the input file for reading
with open(input_file, 'r') as file:
    # Read the lines from the file
    lines = file.readlines()
# Process each line and perform the replacements
output_lines = []
for line in lines:
    line = line.strip()  # Remove leading/trailing whitespaces
    parts = line.split('\t')  # Split the line by tab ('\t')

    # Check if the line contains the classification and PI part
    if len(parts) >= 3:
        classification = parts[1]
        pi = parts[2]

        # Split the classification into seven columns using ';'
        classification_columns = classification.split(';')

        # Store modified values of each column after removing prefixes
        modified_columns = [col.replace('k__', '').replace('p__', '').replace('c__', '').replace('o__', '').replace('f__', '').replace('g__', '').replace('s__', '') for col in classification_columns]

        # Construct the modified line
        modified_line = '\t'.join([parts[0]] + modified_columns + [pi])

        # Append the modified line to the output lines
        output_lines.append(modified_line)
    else:
        # If the line does not contain the classification and PI part, append it as is
        output_lines.append(line)

# Save the modified table to the output file
with open(output_file, 'w') as file:
    file.write('\n'.join(output_lines))
