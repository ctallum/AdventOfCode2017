from collections import defaultdict

with open('input.txt') as f:
    data = [a.strip() for a in f.readlines()]
    data = [a.split('\t') for a in data][0]
    data = [int(a) for a in data]

states = defaultdict(int)
count = 0
count2 = 0


first_iter = 0

# part 1

while True:

    max_index = data.index(max(data))
    max_value = data[max_index]
    data[max_index] = 0
    idx = max_index
    for i in range(max_value):
        idx += 1
        if idx == len(data):
            idx = 0
        data[idx] += 1
    
    states[tuple(data)] += 1

    count += 1
    
    if states[tuple(data)] > 1:
        first_iter = tuple(data)
        break

print(count)

# part 2

while True:
    max_index = data.index(max(data))
    max_value = data[max_index]
    data[max_index] = 0
    idx = max_index
    for i in range(max_value):
        idx += 1
        if idx == len(data):
            idx = 0
        data[idx] += 1

    count2 += 1

    if tuple(data) == first_iter:
        break
    

print(count2)
