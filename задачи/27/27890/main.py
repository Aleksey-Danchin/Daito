file = open('b.txt', 'r')

n = int(file.readline())

mindiff = 0
maxsum = 0

for i in range(n):
    [a, b] = sorted([int(x) for x in file.readline().split()])
    maxsum += b
    if (b-a) % 5 != 0:
        mindiff = min(mindiff, b-a)

file.close()

if maxsum % 5 == 0:
    maxsum -= mindiff

print(maxsum)
