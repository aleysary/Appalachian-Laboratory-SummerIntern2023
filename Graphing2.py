import sys
import matplotlib.pyplot as plt
import numpy as np

# Get input files from command line args
input_files = sys.argv[1:]

if len(input_files) < 4:
    print("Please provide 4 input file names")
    sys.exit(1)
    
# Create figure 
fig, ax = plt.subplots(figsize=(12,6))

# Loop through input files
for i, file in enumerate(input_files):

    # Get cleaner legend label  
    label = file.split('.')[0].replace("table", "")

    # Initialize arrays
    pi_range = []
    fdr = []
    
    # Extract data from input file
    with open(file) as f:
        next(f)
        for line in f:
            cols = line.strip().split('\t')
            if len(cols) < 5 or cols[4] == 'N/A':
                continue
            
            try:
                pi = int(cols[0])
            except ValueError:
                continue
                
            pi_range.append(pi)
            fdr.append(float(cols[4]))

    # Convert to numpy arrays
    fdr = np.array(fdr)
    pi_range = np.array(pi_range)

    # Plot line
    ax.plot(pi_range, fdr, label=label)

# Add labels, legend, etc  
ax.set_xlim(0, 40)
ax.set_xlabel('PI range')
ax.set_ylabel('FDR')
ax.set_title('FDR vs PI range') 
ax.legend()
ax.grid(True)

# Save figure
plt.savefig('combined.png')

print('Graph saved to combined.png')