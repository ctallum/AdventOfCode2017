with open('input.txt') as f:
    data =  f.readlines()
    data = data[0].strip()


pairs = 0
for i in range(len(data)-1):
    if int(data[i]) == int(data[i + 1]):
        pairs += int(data[i])
if data[-1] == data[0]:
    pairs += int(data[0])

print(f'Solution to part 1: {pairs}')

pairs = 0
half = int(len(data)/2)
for i in range(len(data)-1):
    new_index = (i + half)%len(data)
    if int(data[i]) == int(data[new_index]):
        pairs += int(data[i])

print(f'Solution to part 2: {pairs}')