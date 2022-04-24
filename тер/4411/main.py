file = open('b.txt', 'r')
n = int(file.readline())
numbers = [int(x) for x in file.read().splitlines()]
file.close()

terner = numbers.copy()
for i in range(1, n):
    terner[i] += terner[i - 1]

counter = 0

for i in range(n - 2):
    if i % 1000 == 0:
        print(i, counter)
    a = numbers[i]

    for j in range(i + 2, n):
        b = numbers[j]

        if (a + b) % 3 != 0:
            continue

        s = terner[j - 1] - terner[i]

        if s % 2 != 0:
            continue

        counter += 1

print(counter)
