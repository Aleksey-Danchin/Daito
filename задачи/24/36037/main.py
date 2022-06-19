file = open('24.txt', 'r')
line = file.read()
file.close()

arr = line.split('XZZY')
arr = [len(x) for x in arr]

for i in range(1, len(arr)):
    arr[i] += 3

for i in range(0, len(arr) - 1):
    arr[i] += 3

print(len(arr))

mas_length = max(arr)

print(mas_length)
