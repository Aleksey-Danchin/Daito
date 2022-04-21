from audioop import reverse


n = 520_000
x = 5

while x > 0:
    n += 1

    dividers = []
    for j in range(2, n):
        if n % j == 0:
            dividers.append(j)

    if len(dividers) > 0:
        s = str(sum(dividers))

        if s == s[::-1]:
            print(n, dividers, s)
            x -= 1
