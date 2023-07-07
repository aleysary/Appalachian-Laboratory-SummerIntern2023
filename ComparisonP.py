import sys

def create_table(file1, file2):
    table = {}
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        for line1, line2 in zip(f1, f2):
            header, classification = line1.strip().split('\t')
            pi = line2.strip().split('\t')[2]
            table[header] = (classification, pi)

    return table

def write_table(table, output_file):
    with open(output_file, 'w') as f:
        for header, values in table.items():
            classification, pi = values
            f.write(f"{header}\t{classification}\t{pi}\n")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python3 script.py <file1> <file2> <output_file>")
        sys.exit(1)

    file1 = sys.argv[1]
    file2 = sys.argv[2]
    output_file = sys.argv[3]

    table = create_table(file1, file2)
    write_table(table, output_file)
