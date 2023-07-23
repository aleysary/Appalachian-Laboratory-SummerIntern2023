import sys
import matplotlib.pyplot as plt
import numpy as np

# Check if the filename and output name are provided as command-line arguments
if len(sys.argv) < 3:
    print("Please provide the input file name and output file name as command-line arguments.")
    sys.exit(1)

input_filename = sys.argv[1]
output_filename = sys.argv[2]

# Initialize empty lists to store the extracted data
pi_range = []
fdr = []

# Read the input file
with open(input_filename, 'r') as file:
    # Skip the header line
    next(file)

    # Extract data from each line in the file
  for line in file:
        # Split the line into individual columns
        columns = line.strip().split('\t')

        # Skip lines with insufficient columns
        if len(columns) < 5:
            continue

        # Skip lines with "N/A" values in the FDR column
        if columns[4] == "N/A":
            continue

        # Skip lines that do not have a valid integer in the first column
        try:
            pi = int(columns[0])
        except ValueError:
            continue

        # Extract the relevant columns
        pi_range.append(pi)
        fdr.append(float(columns[4]))


# Convert the fdr list to a NumPy array
fdr = np.array(fdr)

# Create the graph
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(pi_range, fdr, marker='o')
ax.set_xlabel('PI range')
ax.set_ylabel('FDR')
ax.set_title('FDR vs. PI range')
ax.grid(True)

# Save the graph to the specified output file
plt.savefig(output_filename)

# Display a success message
print(f"The graph has been saved to {output_filename}.")
