from utils.utils import *

def get_int_from_word(chars):
    num_words = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
    char_str = ''.join(str(char) for char in chars)
    for i in range(len(num_words)):
        if char_str == num_words[i]:
            return i+1;
    return -1

def part1(char_lists):
    num = 0
    for line in char_lists:
        i = 0;
        j = len(line) - 1
        f = ''
        l = ''
        while f == '' or l == '':
            if line[i].isdigit():
                f = line[i]
            else:
                i += 1
            if line[j].isdigit():
                l = line[j]
            else:
                j -= 1
            if i > j:
                break
        if f != '' and l != '':  
            num += int(f + l)
    return num

def part2(char_lists):
    for line in char_lists:
        l = [3,4,5]
        i = 0
        while i < len(line):
            for j in range(3, 6):  
                if i + j <= len(line):
                    res = get_int_from_word(line[i:i+j])
                    if res > 0:
                        line.insert(i, str(res))
                        i += 1
            i += 1
    return part1(char_lists)
                
            

char_lists = read_lines_to_char_lists('2023/inputs/day1.txt')
lines = read_lines_from_file("2023/inputs/day1.txt")
print(part1(char_lists))
print(part2(char_lists))