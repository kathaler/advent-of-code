from utils.utils import *

def is_valid_game(game):
    vals = [12,13,14]
    for i in range(len(game)):
        if 'red' in game[i] and int(game[i-1]) > vals[0]:
            return False
        if 'green' in game[i] and int(game[i-1]) > vals[1]:
            return False
        if 'blue' in game[i] and int(game[i-1]) > vals[2]:
            return False
    return True

def get_power(game):
    vals = [0,0,0]
    for i in range(len(game)):
        if 'red' in game[i] and int(game[i-1]) > vals[0]:
            vals[0] = int(game[i-1])
        if 'green' in game[i] and int(game[i-1]) > vals[1]:
            vals[1] = int(game[i-1])
        if 'blue' in game[i] and int(game[i-1]) > vals[2]:
            vals[2] = int(game[i-1])
    return vals[0]*vals[1]*vals[2]

def part1(word_lists):
    sum = 0;
    for word_list in word_lists:
        if is_valid_game(word_list):
            sum += int(word_list[1].replace(':', ''))
    return sum

def part2(word_lists):
    sum = 0
    for word_list in word_lists:
        sum += get_power(word_list)
    return sum
        
word_lists = read_lines_to_word_lists("2023/inputs/day2.txt")
print(part1(word_lists))
print(part2(word_lists))