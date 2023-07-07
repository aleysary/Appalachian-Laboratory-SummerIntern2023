import pandas as pd
import numpy as np
import sys

if len(sys.argv) < 4:
    print("Usage: python your_script.py taxonomy_file.fasta fasta_file.fasta k_value")
    sys.exit(1)

taxonomy_file = sys.argv[1]
fasta_file = sys.argv[2]
k = int(sys.argv[3])

'''
Taxonomy 
'''
# Read the file
with open(taxonomy_file, 'r') as file:
    lines = file.readlines()

# I store the lines into a pandas DataFrame
df_tax = pd.DataFrame([line.strip().split('\t') for line in lines])

# I split the DataFrame into k parts
splits_tax = np.array_split(df_tax, k)

# I save each split as a separate file
for i, split in enumerate(splits_tax):
    split.to_csv(f'split_{i+1}.tax', sep='\t', index=False, header=False)


'''
The k-fold start for Taxonomy data
'''

# list to store the dataframes read from the files
taxonomy_splits = []

# load the dataframes
for i in range(1, k+1):
    split = pd.read_csv(f'split_{i}.tax')
    taxonomy_splits.append(split)

# Create the train/test folds for Taxonomy data
for i in range(k):
    # For training, use all the splits except the current one
    train_tax = pd.concat([taxonomy_splits[j] for j in range(k) if j != i])

    # For testing, use the current split
    test_tax = taxonomy_splits[i]

    # Save them to files
    train_tax.to_csv(f'train_fold_{i+1}.tax', index=False)
    test_tax.to_csv(f'test_fold_{i+1}.tax', index=False)


'''
FASTA 
'''

# Read the file
with open(fasta_file, 'r') as file:
    lines = file.readlines()


# I store the lines into a pandas DataFrame
sequences = []
sequence_id = None
current_sequence = []
for line in lines:
    line = line.strip()
    if line.startswith(">"):
        if sequence_id is not None:
            sequences.append([sequence_id, "".join(current_sequence)])
            current_sequence = []
        sequence_id = line
    else:
        current_sequence.append(line)

# I add the current sequence to the list if it exists
if sequence_id is not None and current_sequence:
    sequences.append([sequence_id, "".join(current_sequence)])

# This converts the list to a DataFrame
df_fasta = pd.DataFrame(sequences, columns=["Sequence_ID", "Sequence"])

# I split the DataFrame into k parts
splits_fasta = np.array_split(df_fasta, k)

# This saves each split as a separate file
for i, split in enumerate(splits_fasta):
    split.to_csv(f'split_{i+1}.fa', sep='\n', index=False, header=False)


'''
The k-fold start for FASTA data
'''

# list to store the dataframes read from the files
fasta_splits = []

# load the dataframes
for i in range(1, k+1):
    split_lines = []
    with open(f'split_{i}.fa', 'r') as file:
        lines = file.readlines()
        for j in range(0, len(lines), 2):
            sequence_id = lines[j].strip()
            sequence = lines[j+1].strip()
            split_lines.append([sequence_id, sequence])
    
    split_df = pd.DataFrame(split_lines, columns=["Sequence_ID", "Sequence"])
    fasta_splits.append(split_df)

# Create the train/test folds for FASTA data
for i in range(k):
    # For training, use all the splits except the current one
    train_fasta = pd.concat([fasta_splits[j] for j in range(k) if j != i])

    # For testing, use the current split
    test_fasta = fasta_splits[i]

    # Save them to files
    train_fasta.to_csv(f'train_fold_{i+1}.fa', sep='\n', index=False, header=False)
    test_fasta.to_csv(f'test_fold_{i+1}.fa', sep='\n', index=False, header=False)
