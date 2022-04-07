file = open('file.txt', 'r')
n = int(file.readline())

matrix = []
for i in range(100_000):
    matrix.append([])

for _ in range(n):
    [y, x] = [int(x) for x in file.readline().split()]
    matrix[y].append(x)

file.close()

for i in range(100_000):
    matrix[i] = sorted(matrix[i])

    for j in range(len(matrix[i]) - 1, 1, -1):
        if matrix[i][j] - matrix[i][j - 1] == 4:
            print(i, matrix[i][j] - 1)
            break
