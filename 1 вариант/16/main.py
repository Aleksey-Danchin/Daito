def F(n):
    if n <= 1:
        return 1

    if n % 2 == 1:
        return 5 * n + F(n-1) + F(2)

    return 3 * F(n - 1)


print(F(23))
