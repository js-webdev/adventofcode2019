"""
Day 4
"""

input = "271973-785961"

min = int(input.split('-')[0])
max = int(input.split('-')[1])

numbers_p1 = []
numbers_p2 = []

def two_same(string):
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            return True
    return False

def always_increasing(string):
    res = True
    for index,num in enumerate(string):
      if index>0:
         if(int(num) < int(string[index-1])):
             res = False
    return res

def large_group(string):
    group_num = []
    for num in string:
        if(string.count(num)>2):
            group_num.append(num)
        elif(string.count(num)==2):
            return True
    return False

for num in range(min, max):
    if(two_same(str(num)) and always_increasing(str(num))):
        numbers_p1.append(num)

for p2 in numbers_p1:
    if(large_group(str(p2))):
        numbers_p2.append(p2)

print("Part 1: "+str(len(numbers_p1)))
print("Part 2: "+str(len(numbers_p2)))