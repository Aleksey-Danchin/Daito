file = open('17.txt', 'r')
line = [int(x) for x in file.read().splitlines()]
file.close()

n = 10000
counter = 0
maxsum = 0

for i in range(n - 1):
    a = line[i]

    for j in range(i + 1, n):
        b = line[j]

        if (a*b) % 62 == 0:
            counter += 1
            maxsum = max(maxsum, a + b)

print(counter, maxsum)
