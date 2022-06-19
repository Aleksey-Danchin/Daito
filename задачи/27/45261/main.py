file = open('27B.txt', 'r')
n = int(file.readline())
mas = [int(x) for x in file.read().splitlines()]

# n = 6
# mas = [8, 20, 5, 13, 7, 19]

mas = [*mas, *mas]

mask = [0]
i = 0
while len(mask) < n:
    print(len(mask))
    i += 1

    mask.append(i)

    if len(mask) < n:
        mask.insert(0, i)

min_counter = -1
while len(mask) <= len(mas):
    print(len(mask), n * 2)
    # print(*mas, sep='\t')
    # print(*mask, sep='\t')
    # print()

    counter = 0

    for i in range(len(mask)):
        counter += mas[i] * mask[i]

    if counter < min_counter or min_counter == -1:
        min_counter = counter

    mask.insert(0, 0)

print(min_counter)
