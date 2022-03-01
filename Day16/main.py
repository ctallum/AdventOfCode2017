from string import ascii_lowercase

with open('input.txt') as f:
    data = [a.strip() for a in f.readlines()][0]
    data = data.split(',')
    data = [[a[0]]+a[1:].split('/') for a in data]

def s(line, args):
    idx = int(args[0])
    return line[-idx:] + line[:-idx]

def x(line,args):
    idx1 = int(args[0])
    idx2 = int(args[1])
    temp = line[:]
    temp[idx1] = line[idx2]
    temp[idx2] = line[idx1]
    return temp


def p(line, args):
    char1 = args[0]
    char2 = args[1]
    idx1 = line.index(char1)
    idx2 = line.index(char2)
    temp = line[:]
    temp[idx1] = line[idx2]
    temp[idx2] = line[idx1]
    return temp 


funcs = {'s': s, 'x': x, 'p':p}

line = list(ascii_lowercase)[:16]
for part in data:
    line = funcs[part[0]](line, part[1:])

print(f"Solution to part 1: {''.join(line)}")

line = list(ascii_lowercase)[:16]

init = line[:]

for loop_idx in range(1000000000):
    for part in data:
        line = funcs[part[0]](line, part[1:])
    if line == init:
        break
times = (1000000000%(loop_idx+1))

for loop_idx in range(times):
    for part in data:
        line = funcs[part[0]](line, part[1:])

print(f"Solution to part 2: {''.join(line)}")
