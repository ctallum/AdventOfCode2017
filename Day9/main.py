with open('input.txt') as f:
    data = [a.strip() for a in f.readlines()]
    data = list(data[0])

non_junk = 0
layer = 0
count = 0

in_garbage = False

for idx, val in enumerate(data):
    if val == '!':
        data[idx + 1] = '*'

    elif val == '<' and not in_garbage:
        in_garbage = True

    elif val == '>':
        in_garbage = False

    elif val == '{' and not in_garbage:
        layer += 1
        count += layer

    elif val == '}' and not in_garbage:
        layer -= 1

    elif in_garbage and val != '*':
        non_junk += 1

print(f'Solution to Part 1: {count}')
print(f'Solution to Part 2: {non_junk}')
