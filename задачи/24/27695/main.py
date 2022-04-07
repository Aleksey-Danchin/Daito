file = open('a.txt', 'r')
line = file.read()
file.close()

counter = 0
line = list(line)

maxcounter = 0
for i in range(len(line)-1):
    a = line[i]
    b = line[i+1]
    if a == b:
        counter = 1
    else:
        counter += 1
        maxcounter = max(maxcounter, counter)
print(maxcounter)
