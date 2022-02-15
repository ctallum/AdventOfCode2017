import sys
from collections import defaultdict
sys.setrecursionlimit(100000)

with open('input.txt') as f:
    data = [a.strip() for a in f.readlines()]
    data = list(data[0])

clean_string = []
non_junk = 0

in_garbage = False
for idx,val in enumerate(data):
    if val == '!':
        data[idx+1] = '*'
        continue

    if val == '<' and not in_garbage:
        in_garbage = True
        continue

    if val == '>':
        in_garbage = False
        continue

    if val in ['{','}'] and not in_garbage:
        clean_string.append(val)
    
    if in_garbage and val != '*':
        non_junk += 1


layer = 0
count = 0

for val in clean_string:
    if val == "{":
        layer += 1
        count += layer
    if val == "}":
        layer -= 1

print(count)
print(non_junk)