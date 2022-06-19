file = open('24.txt', 'r')
lines = file.read().splitlines()
file.close()

n = 0
length = -1

for i in range(len(lines)):
    line = lines[i]
    counter = 0

    for l in line:
        if l == 'N':
            counter += 1

    if counter < length or length == -1:
        n = i
        length = counter

ordA = ord('A')
ordZ = ord('Z')
counter = [0 for _ in range(ordZ - ordA + 1)]

for l in lines[n]:
    code = ord(l)
    counter[code - ordA] += 1

max_code = max(counter)

for i in range(len(counter) - 1, -1, -1):
    if counter[i] == max_code:
        print(chr(ordA + i))
        break
