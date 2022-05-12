file = open('b.txt', 'r')

mas1 = []
mas2 = []
mas3 = []

n = int(file.readline())
numbers = sorted([int(x) for x in file.read().splitlines()])

for a in numbers:
    if a % 3 == 0:
        mas3.append(a)

    elif a % 3 == 1:
        mas1.append(a)

    else:
        mas2.append(a)

file.close()

maxsum = 1

if len(mas3) > 1:
    maxsum = max(mas3[-1] + mas3[-2], maxsum)

if len(mas1) > 0 and len(mas2) > 0:
    maxsum = max(maxsum, mas1[-1] + mas2[-1])

print(maxsum)
