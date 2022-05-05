file = open('a.txt', 'r')
lines = file.read().splitlines()
file.close()

maxlen = 0

alphabet = ''.join([chr(i) for i in range(ord('A'), ord('Z') + 1)])

for line in lines:
    counter = sum([x == 'G' for x in line])
    if counter < 15:
        for b in alphabet:
            if b in line:
                l = line.index(b)
                r = line.rindex(b)

                maxlen = max(maxlen, r - l)

print(maxlen)
