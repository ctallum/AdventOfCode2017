
a = 634
b = 301

def step(a_start,b_start):
    a, b = a_start, b_start
    while True:
        a = a * 16807
        a = a%2147483647
        if a%4 == 0:
            break
    a_match = bin(a)[-16:]

    while True:
        b = b * 48271
        b = b%2147483647
        if b%8 == 0:
            break
    b_match = bin(b)[-16:]

    return (a, b, a_match==b_match)

count = 0
for _ in range(5000000):
    a,b,check = step(a,b)
    if check:
        count += 1

print(count)
