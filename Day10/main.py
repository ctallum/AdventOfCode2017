with open('input.txt') as f:
    data = [a.strip() for a in f.readlines()]
    data = [int(a) for a in data[0].split(',')]

knot = list(range(256))

position = 0
skip = 0

for idx,val in enumerate(data):
    new_knot = knot[position:] + knot[:position]
    new_knot = list(reversed(new_knot[:val])) + new_knot[val:]
    knot = new_knot[-position:] + new_knot[:-position]
    
    position += (val + skip)

    while position > len(knot):
        position -= len(knot)

    skip += 1

print(f'Solution to Part 1: {knot[0] * knot[1]}')

#########################################################################

with open('input.txt') as f:
    data = [a.strip() for a in f.readlines()]
    data = data[0]
    data = [ord(a) for a in data]
    data += [17, 31, 73, 47, 23]

knot = list(range(256))

position = 0
skip = 0

for _ in range(64):

    for idx,val in enumerate(data):
        new_knot = knot[position:] + knot[:position]
        new_knot = list(reversed(new_knot[:val])) + new_knot[val:]
        knot = new_knot[-position:] + new_knot[:-position]
        
        position += (val + skip)

        while position > len(knot):
            position -= len(knot)

        skip += 1

dense_hash = []

for idx in range(16):
    section = knot[idx*16:(idx+1)*16]
    res = section[0]
    for val in section[1:]:
        res = res ^ val 
    dense_hash.append(res)

answer = ''
for val in dense_hash:
    answer += (hex(val)[2:])
        
print(f'Solution to Part 2: {answer}')
