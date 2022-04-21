file = open('file.txt', 'r')
numbers = [int(x) for x in file.read().splitlines()]
file.close()


def f(n):
    return n > 0 and n % 10 == 9


counter = 0
max_sum = -1_000_000

for i in range(len(numbers) - 2):
    a = numbers[i]
    b = numbers[i + 1]
    c = numbers[i + 2]

    if not f(a) and f(b) and not f(c):
        counter += 1
        max_sum = max(max_sum, a + b + c)


print(counter, max_sum)
