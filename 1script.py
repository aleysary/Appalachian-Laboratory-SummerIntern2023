import subprocess
import sys

# Command 1: Clusterp.py
clusterp_command = ['python3', 'Clusterp.py', '12S_Combined.tax', '12S_Combined.fa', sys.argv[1]]
subprocess.run(clusterp_command)

k = int(sys.argv[1])

final_tables = []

for i in range(1, k+1):

  # Use zfill to pad index
  index_str = str(i).zfill(2)

  # Vsearch  
  vsearch_command = [
    'vsearch',
    '--usearch_global',
    f'test_fold_{i}.fa',  
    '--db', f'train_fold_{i}.fa',
    '--id', '0.70',
    '--maxaccepts', '100',
    '--maxrejects', '50',
    '--maxhits', '1',
    '--gapopen', '0TE',
    '--gapext', '0TE',
    '--userout', f'{index_str}TestAlignments.txt',
    '--userfields', 'query+target+id+alnlen+mism+opens+qlo+qhi+tlo+thi+evalue+bits+qcov',   
    '--query_cov', '0.8',
    '--threads', '28'
  ]
  
  subprocess.run(vsearch_command)

  # Vsearch to Metaxa
  vsearch_to_metaxa_command = [
    'python3',
    '3_VsearchToMetaxa.py',
    '-v', 
    f'{index_str}TestAlignments.txt',
    '-t',
    '12S_Combined.tax',
    '-o',
    f'{index_str}Test.tax'
  ]

  subprocess.run(vsearch_to_metaxa_command)

  # Trim Metaxa  
  trim_metaxa_ids_command = [
    'python3',
    '4_TrimMtxa2IDs.py',
    f'{index_str}Test.tax',
    f'Trmd_{index_str}.txt'
  ]

  subprocess.run(trim_metaxa_ids_command)

  # Data to Confusion
  data_to_confusion_command = [
    'java',
    'DataToConfusion_5-2.java',
    f'Trmd_{index_str}.txt',
    '12S_Combined.tax',
    f'NEWOUTPUTCONFUSION_{index_str}.txt'
  ]

  subprocess.run(data_to_confusion_command)

  # ComparisonP
  comparison_p_command = [
    'python3',
    'ComparisonP.py',
    f'NEWOUTPUTCONFUSION_{index_str}.txt',
    f'{index_str}TestAlignments.txt', 
    f't_{index_str}.txt'
  ]

  subprocess.run(comparison_p_command)

  # ZeroOneTable
  zero_one_table_command = [
    'python3',
    'ZeroOneTable.py',
    f't_{index_str}.txt',
    f't_{index_str}{index_str}.txt'
  ]

  subprocess.run(zero_one_table_command)

  # ZeroOneTableP2
  zero_one_table_p2_command = [
    'python3', 
    'ZeroOneTableP2.py',
    f't_{index_str}{index_str}.txt',
    f't_{index_str}{index_str}{index_str}.txt'
  ]

  subprocess.run(zero_one_table_p2_command)

  # BinX1s0s
  bin_x1s0s_command = [
    'python3',
    'BinX1s0s.py',
    f't_{index_str}{index_str}{index_str}.txt', 
    f't_{index_str}{index_str}{index_str}{index_str}.txt'
  ]

  subprocess.run(bin_x1s0s_command)

  # Binsize
  binsize_command = [
    'python3',
    'Binsize.py',
    f't_{index_str}{index_str}{index_str}{index_str}.txt',
    f't_{index_str}{index_str}{index_str}{index_str}{index_str}.txt'
  ]

  subprocess.run(binsize_command)

  # Binsize1
  binsize1_command = [
    'python3',
    'Binsize1.py',
    f't_{index_str}{index_str}{index_str}{index_str}{index_str}.txt',
    f't_{index_str}{index_str}{index_str}{index_str}{index_str}{index_str}.txt'
  ]

  subprocess.run(binsize1_command)

  # Append final table
  final_table = f't_{index_str}{index_str}{index_str}{index_str}{index_str}{index_str}.txt'

  final_tables.append(final_table)

# Automatically merge tables
print("Final merged table: merged_table.txt")

# Run TableMerge  
merge_tables_command = ['python3', 'TableMerge.py'] + final_tables
subprocess.run(merge_tables_command)

# Run TableMerge1
merged_table = f'K{k}table3.txt'
table_merge1_command = ['python3', 'TableMerge1.py', merged_table]
subprocess.run(table_merge1_command)

final_table_command = ['python3', 'FinalTable.py', f'K{k}table2.txt', f'K{k}table.txt']

result = subprocess.run(final_table_command, capture_output=True)

output_file = f'K{k}table.txt'
print(f"Final Table Output: {output_file}") 

print(result.stdout.decode())

