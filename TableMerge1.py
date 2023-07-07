import sys

def process_table(lines):
    table_data = []
    for line in lines:
        line = line.strip()
        if line.startswith("PI range") or line.startswith("-"):
            continue
        if line:
            values = line.split("\t")
            pi_range = values[0]
            row_data = [pi_range, int(values[1]), int(values[2]), int(values[3])]
            table_data.append(row_data)
    return table_data

def consolidate_tables(table_data_list):
    consolidated_table = []
    for table_data in table_data_list:
        for i, row_data in enumerate(table_data):
            if len(consolidated_table) <= i:
                consolidated_table.append(row_data)
            else:
                consolidated_table[i] = [consolidated_table[i][0]] + [a + b for a, b in zip(consolidated_table[i][1:], row_data[1:])]
    return consolidated_table

def print_table(table_data, output_file):
    headers = ["PI range", "Number of 1s", "Number of 0s", "Number of N/A"]
    output_file.write("\t".join(headers) + "\n")
    output_file.write("-" * 50 + "\n")
    for row_data in table_data:
        row_values = [str(value) for value in row_data]
        output_file.write("\t".join(row_values) + "\n")

def main():
    if len(sys.argv) < 2:
        print("Please provide a file name as an argument.")
        return

    file_name = sys.argv[1]

    with open(file_name, "r") as file:
        file_lines = file.readlines()

    table_data_list = []
    current_table_lines = []
    for line in file_lines:
        if line.startswith("-"):
            if current_table_lines:
                table_data = process_table(current_table_lines)
                table_data_list.append(table_data)
                current_table_lines = []
        else:
            current_table_lines.append(line)

    if current_table_lines:
        table_data = process_table(current_table_lines)
        table_data_list.append(table_data)

    consolidated_table = consolidate_tables(table_data_list)

    num_tables = len(table_data_list)
    output_file_name = f"K{num_tables}table2.txt"

    with open(output_file_name, "w") as output_file:
        print_table(consolidated_table, output_file)

    print(f"The consolidated table has been saved to '{output_file_name}'.")

if __name__ == "__main__":
    main()
