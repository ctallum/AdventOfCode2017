with open('input.txt') as f:
    data = [a.strip().split('\t') for a in f.readlines()]
    data = [[int(a) for a in row] for row in data]


count = 0
for row in data:
    count += (max(row) - min(row))

print(count)

count = 0
for row in data:
    for idx1,val in enumerate(row):
        for idx2,other_val in enumerate(row):
            if idx1 != idx2:
                if max([val,other_val])%min([val,other_val]) == 0:
                    count += max([val,other_val])/min([val,other_val])

print(int(count/2))