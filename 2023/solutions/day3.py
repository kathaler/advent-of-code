from utils import *
import string

class Point:
    def __init__(self, number, x, y):
        self.number = number
        self.gear_coordinate = (x, y)

    def __str__(self):
        return f"Point {self.number}: Coordinate {self.gear_coordinate}"
    

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
    
    
def get_point_if_gear(num, index, list_index, lists):
    num_length = len(str(num))
    list_length = len(lists[0])
    
    start = (index - num_length) + 1
    end = index
    
    rng = list(range(start, end + 1))
        
    if start - 1 >= 0:
        if str(lists[list_index][start-1]) == "*":
            return Point(num, list_index, start-1)
        else:
            rng.insert(0, rng[0]-1)
    if end + 1 < list_length:
        if str(lists[list_index][end+1]) == "*":
            return Point(num, list_index, end+1)
        else:
            rng.append(rng[-1]+1)
    if list_index-1 >= 0:
        for i in rng:
            if str(lists[list_index-1][i]) == "*":
                return Point(num, list_index-1, i)
    if list_index+1 < len(lists):
        for i in rng:
            if str(lists[list_index+1][i]) == "*":
                return Point(num, list_index+1, i)
    
    
def part2(char_lists):
    sum = 0
    points = []
    for list_index, list in enumerate(char_list):
        temp = ''
        for i, char in enumerate(list):
            if char.isdigit():
                temp += char
            if (not char.isdigit() or i == len(list)-1) and temp != '':
                if not char.isdigit():
                    i -= 1;
                new_point = get_point_if_gear(int(temp), i, list_index, char_lists)
                if new_point is not None:
                    points.append(new_point)
                temp = ''

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            if points[i].gear_coordinate == points[j].gear_coordinate:
                sum += points[i].number * points[j].number
    return sum
                

char_list = read_lines_to_char_lists("2023/inputs/day3.txt")
print(part1(char_list))
print(part2(char_list))