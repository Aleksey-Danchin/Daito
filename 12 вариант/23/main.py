def f(a, b):
    if a == b:
        return 1

    if a > b:
        return 0

    return f(a + 5, b) + f(a + 4, b) + f(a * 3, b)


print(f(2, 6)*f(6, 30))
