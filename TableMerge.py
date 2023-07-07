import sys

class TableMerger:
    def __init__(self, output_file):
        self.output_file = output_file
        self.tables = []

    def add_table(self, table_file):
        self.tables.append(table_file)

    def merge_tables(self):
        merged_data = []
        for table_file in self.tables:
            with open(table_file, 'r') as f:
                table_data = f.readlines()
                merged_data.extend(table_data)
                merged_data.append('------\n')  # Add a separator between tables
        
        with open(self.output_file, 'w') as f:
            f.writelines(merged_data)

    @staticmethod
    def get_output_filename(num_tables):
        return f"K{num_tables}table3.txt"

if __name__ == "__main__":
    num_input_tables = len(sys.argv) - 1
    if num_input_tables < 2:
        print("Invalid number of input tables. Please provide at least 2 input tables.")
        sys.exit(1)

    output_file = TableMerger.get_output_filename(num_input_tables)
    table_merger = TableMerger(output_file)

    for i in range(1, num_input_tables + 1):
        table_file = sys.argv[i]
        table_merger.add_table(table_file)

    table_merger.merge_tables()
    print(f"Tables merged successfully. Output file: {output_file}")
