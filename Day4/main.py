with open('input.txt') as f:
    data = [a.strip() for a in f.readlines()]
    data = [a.split(' ') for a in data]

count = 0

for row in data:
    if len(set(row)) == len(row):
        count += 1

print(f'Solution to part 1: {count}')

count = 0
for row in data:
    works = True
    for idx1,item in enumerate(row):
        for idx2,other_item in enumerate(row):
            if set(item) == set(other_item) and idx1 != idx2:
                works = False
    if works:
        count += 1

print(f'Solution to part 2: {count}')

    

