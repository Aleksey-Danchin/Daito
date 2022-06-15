mas1 = []
mas2 = []
counter = 0
file = open('b.txt', 'r')

n = int(file.readline())

for i in range(n):
    x = int(file.readline())

    if x > 50:
        mas2.append(x)
    else:
        mas1.append(x)

file.close()

for i in range(len(mas2)):
    a = mas2[i]
    for j in range(len(mas1)):
        b = mas1[j]
        if (a+b) % 80 == 0:
            counter += 1

for i in range(len(mas2)-1):
    a = mas2[i]
    for j in range(i + 1, len(mas2)):
        b = mas2[j]
        if (a+b) % 80 == 0:
            counter += 1

print(counter)
