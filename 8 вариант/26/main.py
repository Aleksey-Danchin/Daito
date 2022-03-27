file = open('file.txt', 'r')
[S, n] = [int(x) for x in file.readline().split()]
sizes = sorted([int(x) for x in file.read().splitlines()])
file.close()

replaced = []

for i in range(n):
    if sum(replaced) + sizes[i] > S:
        break

    replaced.append(sizes[i])

print(len(replaced))

for i in range(len(replaced) + 1, n):
    if sum(replaced) - replaced[-1] + sizes[i] <= S:
        replaced.pop(-1)
        replaced.append(sizes[i])
    else:
        break

print(replaced[-1])
