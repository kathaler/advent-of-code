from utils import *

def get_conversion_table(m):
    maps = m[1:]
    ranges = []
    for m in maps:
        m = [int(char) for char in m.split(' ')]
        ranges.append(m)
    return(ranges)

def convert_num(num, table):
    for t in table:
        if num >= t[1] and num < t[1]+t[2]:
            return t[0] + (num - t[1])
    return num

def convert_nums(nums, maps, map_index):
    print(maps[map_index][0])
    if map_index == len(maps):
        return nums
    
    table = get_conversion_table(maps[map_index])
    for i in range(len(nums)):
        nums[i] = convert_num(nums[i], table)
    
    return convert_nums(nums, maps, map_index+1)

def part1(maps):
    nums = [int(char) for char in maps[0][1:]]
    return convert_nums(nums, maps[1:], 0)

def part2(maps):
    num_ranges = [int(char) for char in maps[0][1:]]
    nums = []
    i = 0
    while i < len(num_ranges):
        nums.extend([*range(num_ranges[i], num_ranges[i]+ num_ranges[i+1])])
        i += 2
    return convert_nums(nums, maps[1:], 0)

l = file_to_list_by_empty_line("2023/inputs/day5.txt")
l[0] = l[0].split(' ')
for i in range(len(l[1:])):
    l[i+1] = l[i+1].split("\n")
    
#print(min(part1(l)))
print(min(part2(l)))