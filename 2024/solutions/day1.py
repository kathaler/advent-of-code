# python3 -m 2024.solutions.day1

from utils.utils import *

def part_1(l1, l2):
   sum = 0
   for i in range(len(l1)):
      sum += abs(int(l1[i]) - int(l2[i]))
      
   return sum

def part_2(l1, l2):   
   d1 = {}
   d2 = {}
   
   for l in l1:
      d1[l] = d1.get(l, 0) + 1
      
   for l in l2:
      d2[l] = d2.get(l, 0) + 1
      
   sum = 0
   for k in d1.keys():
      if k in d2.keys():
         sum += int(k) * d2[k] * d1[k]
   
   return sum 
      


lines = file_to_list_by_line('2024/inputs/day1.txt')

sum = 0
l1 = []
l2 = []
for line in lines:
   vals = line.split('   ')
   l1.append(vals[0])
   l2.append(vals[1])

l1 = sorted(l1)
l2 = sorted(l2)

print(part_1(l1, l2))
print(part_2(l1, l2))