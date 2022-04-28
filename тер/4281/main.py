file = open('b.txt', 'r')
n = int(file.readline())
numbers = [int(x) for x in file.read().splitlines()]
file.close()

terner = [0]
for i in range(n):
    terner.append(terner[i] + numbers[i])

m = 0
l = n + 1

c = 0
for i in range(1, n):
    for j in range(0, i):
        c += 1

        if c > 100_000_000:
            c = 0
            print(m, l, j, i)

        s = terner[i + 1] - terner[j]

        if s % 43 == 0:
            if s > m:
                m = s
                l = i - j + 1
            elif s == m and (i - j + 1) < l:
                l = i - j + 1

            break

print(m, l)
