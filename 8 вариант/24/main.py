file = open('file.txt', 'r')
string = file.read()
file.close()

strings = string.split('Z')
sizes = [len(x) for x in strings]

length = 0
for i in range(1, len(sizes)):
    length = max(length, sizes[i - 1] + 1 + sizes[i])

print(length)
