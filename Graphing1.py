import sys
import matplotlib.pyplot as plt
import numpy as np

# Check command-line args
if len(sys.argv) < 3:
    print("Error: please provide input and output file names")
    sys.exit(1)
    
input_file = sys.argv[1] 
output_file = sys.argv[2]

# Initialize arrays  
pi_range = []
fdr = [] 

# Extract data from input file
with open(input_file) as f:
    next(f) # skip header
    
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
        
# Convert to NumPy arrays
fdr = np.array(fdr)
pi_range = np.array(pi_range)

# Create plot 
fig, ax = plt.subplots(figsize=(12,6))
ax.plot(pi_range, fdr, '-o') 

# Set x-axis limits
ax.set_xlim(0, 40) 

# Label plot
ax.set_xlabel('PI range')
ax.set_ylabel('FDR')
ax.set_title('FDR vs PI range')
ax.grid(True)

# Save figure and show message
plt.savefig(output_file)
print(f"Graph saved to {output_file}")