from utils import *
import string

def is_symbol(c):
    return c in string.punctuation and c != '.'

def is_part_num(num, index, list_index, lists):
    num_length = len(str(num))
    list_length = len(lists[0])
    
    start = (index - num_length) + 1
    end = index
    
    rng = list(range(start, end + 1))
        
    if start - 1 >= 0:
        if is_symbol(str(lists[list_index][start-1])):
            return True
        else:
            rng.insert(0, rng[0]-1)
    if end + 1 < list_length:
        if is_symbol(str(lists[list_index][end+1])):
            return True
        else:
            rng.append(rng[-1]+1)
    if list_index-1 >= 0:
        for i in rng:
            if is_symbol(str(lists[list_index-1][i])):
                return True
            
    if list_index+1 < len(lists):
        for i in rng:
            if is_symbol(str(lists[list_index+1][i])):
                return True
        
    return False;
    

def part1(char_lists):
    sum = 0
    for list_index, list in enumerate(char_list):
        temp = ''
        for i, char in enumerate(list):
            if char.isdigit():
                temp += char
            if (not char.isdigit() or i == len(list)-1) and temp != '':
                if not char.isdigit():
                    i -= 1;
                if is_part_num(int(temp), i, list_index, char_lists):
                    sum += int(temp)
                temp = ''
    return sum
                

char_list = read_lines_to_char_lists("2023/inputs/day3.txt")
print(part1(char_list))