import sys

# Read input file
input_file = sys.argv[1]
output_file = sys.argv[2]
data = []
with open(input_file, 'r') as file:
    for line in file:
        data.append(line.strip().split('\t'))

# Modify PI Range column starting from row 3
for i in range(2, len(data)):
    data[i][0] = str(i - 2)

# Calculate FDR and add FDR column
data[0].append('FDR')
for row in data[1:]:
    if len(row) >= 3:
        num_1s = int(row[1])
        num_0s = int(row[2])
        if num_0s + num_1s != 0:
            fdr = num_1s / (num_0s + num_1s)
            row.append(f'{fdr:.11f}')
        else:
            row.append('N/A')
    else:
        row.append('N/A')

# Save the table with the FDR column to the output file
with open(output_file, 'w') as file:
    for row in data:
        file.write('\t'.join(row) + '\n')
