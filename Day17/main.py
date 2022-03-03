from numpy import linspace

buffer = [0]

spot = 0
for insert in linspace(1,2017,2017):
    spot += 304
    spot = spot%len(buffer) + 1
    buffer.insert(spot,int(insert))
    

print(f'Solution to part 1: {buffer[buffer.index(2017)+1]}')

buffer = [0, 0]
buffer_len = 1
spot = 0
for insert in linspace(1,50000000,50000000):
    spot += 304
    spot = spot%buffer_len + 1
    if spot == 1:
        buffer[1] = int(insert)
    buffer_len += 1
    

print(f'Solution to part 2: {buffer[1]}')