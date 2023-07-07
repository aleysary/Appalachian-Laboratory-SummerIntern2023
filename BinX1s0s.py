import sys

def generate_table(table_file):
    table_data = []
    with open(table_file, 'r') as file:
        for line in file:
            row = line.strip().split('\t')
            table_data.append(row)

    pi_range_genus = []
    for row in table_data[1:]:
        genus = row[7]
        pi = float(row[8])
        pi_range = int(pi) // 1
        pi_range_genus.append((pi_range, genus))

    result_table = []
    for i in range(100, -1, -1):
        pi_range = (i, i-1)
        genus_list = [genus for (range_val, genus) in pi_range_genus if range_val == i]
        genus_str = ''.join(genus_list)
        result_table.append((pi_range, genus_str))

    return result_table


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Please provide the table file and output file as command line arguments.")
        sys.exit(1)

    table_file = sys.argv[1]
    output_file = sys.argv[2]
    result_table = generate_table(table_file)

    with open(output_file, 'w') as file:
        file.write("PI Range\tgenus\n")
        for (pi_range, genus) in result_table:
            file.write(f"{pi_range[0]} to {pi_range[1]}\t{genus}\n")

    print(f"Table generated and saved to {output_file}.")


