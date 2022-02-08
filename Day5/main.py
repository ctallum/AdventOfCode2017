from typing import Tuple, List

with open('input.txt') as f:
    data = [a.strip() for a in f.readlines()]
    data = [int(a) for a in data]

def step(idx: int, list: List[int]) -> Tuple(int, List[int]):
    end = list[idx] + idx
    if list[idx] >= 3:
        list[idx] -= 1
    else:
        list[idx] += 1
    return end, list

count = 0
idx = 0

while True:
    try:
        idx, data = step(idx, data)
        count += 1
    except IndexError:
        print(count)
        break
