from collections import defaultdict

with open('input.txt') as f:
    data = [a.strip() for a in f.readlines()]
    registers = [a[:a.index(' ')] for a in data]
    data = [a.split(' ') for a in data]
    data = [[f'dict["{a[0]}"]'] + a[1:] for a in data]
    data = [a[0:4] + [f'dict["{a[4]}"]'] + a[5:] for a in data]
    data = [" ".join(a[3:])+": " + " ".join(a[0:3]) for a in data]
    data = [a.replace('dec',"-=") for a in data]
    data = [a.replace('inc',"+=") for a in data]

dict = defaultdict(int)

for reg in registers:
    dict[reg] = 0

with open('test.txt','w') as f:
    for part in data:
        f.write(part)
        f.write('\n')



max_value = 0
max_key = ''

for key,value in dict.items():
    if value > max_value:
        max_value = value
        max_key = key

print(max_value)

