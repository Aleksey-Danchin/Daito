file = open('./17.txt', 'r')

mas = [int(x) for x in file.read().splitlines()]

file.close()

evenmas = []

for i in mas:
    if i % 2 == 0:
        evenmas.append(i)

msum = sum(evenmas) / len(evenmas)

maxsum = 0
counter = 0

for i in range(0, len(mas)-1):
    a = mas[i]
    b = mas[i+1]

    if (a % 3 == 0 or b % 3 == 0) and (a < msum or b < msum):
        counter += 1
        maxsum = max(maxsum, a + b)

print(counter, maxsum)
