def read_lines_from_file(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
    return lines

def read_lines_to_char_lists(file_name):
    lines = read_lines_from_file(file_name)
    char_lists = [list(line.strip()) for line in lines]
    return char_lists

def read_lines_to_word_lists(file_name):
    lines = read_lines_from_file(file_name)
    char_lists = [list(line.split()) for line in lines]
    return char_lists

def file_to_list_by_empty_line(file_name):
    with open(file_name, 'r') as f:
        return f.read().split("\n\n")
    return None
 
def file_to_list_by_line(file_name):
    with open(file_name, 'r') as f:
        return f.read().splitlines()
    return None
