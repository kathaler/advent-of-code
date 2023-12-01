def read_lines_from_file(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
    return lines