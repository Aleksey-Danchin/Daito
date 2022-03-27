file = open('b.txt', 'r')
n = int(file.readline())

result = 0
minDiff = 1000000

for i in range(n):
    [a, b] = sorted([int(x) for x in file.readline().split()])

    result += b

    if (b - a) % 43 != 0:
        minDiff = min(minDiff, b - a)

file.close()

if result % 43 == 0:
    result -= minDiff

print(result)
