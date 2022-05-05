import random

n = 1_000_000
s = 0

for i in range(n):
    s += random.randint(1, 6)
    print(s / (i+1))
