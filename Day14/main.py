data = 'hfdlxzhv'

knots = []

for idx in range(128):
    knots.append(f'{data}-{idx}')

for idx,knot in enumerate(knots):
    knots[idx] = [ord(a) for a in knot]
    knots[idx] += [17, 31, 73, 47, 23]


def solve(data):

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
        answer += ("{0:#0{1}x}".format(val,6)[4:])

    new_answer = ''
    for val in answer:
        new_answer +=  (bin(int(val, 16))[2:] ).zfill(4*len(val))
        
    return new_answer

part1 = []
for part in knots:
    part1.append(solve(part))

locations = []

for idx1,row in enumerate(part1):
    for idx2,col in enumerate(row):
        if col == '1': 
            locations.append((idx1,idx2))

print(len(locations))


def region(locations, loc):
    
    locations.remove(loc)
    
    if (loc[0]+1,loc[1]) in locations:
        region(locations,(loc[0]+1,loc[1]))

    if (loc[0]-1,loc[1]) in locations:
        region(locations,(loc[0]-1,loc[1]))

    if (loc[0],loc[1]+1) in locations:
        region(locations,(loc[0],loc[1]+1))

    if (loc[0],loc[1]-1) in locations:
        region(locations,(loc[0],loc[1]-1))

    return


regions = 0

while len(locations) > 0:
    region(locations,locations[0])
    regions += 1


print(regions)