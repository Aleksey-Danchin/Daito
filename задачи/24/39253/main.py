file = open('24.txt', 'r')

line = [len(x) for x in file.read().split('D')]
maxsum = 0

for i in range(len(line)-1):
    maxsum = max(maxsum, line[i] + line[i+1] + 1)
print(maxsum)
