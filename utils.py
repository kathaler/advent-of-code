def read_lines_from_file(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
    return lines

def read_lines_to_char_lists(file_name):
    lines = read_lines_from_file(file_name)
    char_lists = [list(line.strip()) for line in lines]
    return char_lists