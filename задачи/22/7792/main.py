def f(x):
    a = 10
    b = 0
    while x > 0:
        y = x % 10
        x = x // 10
        if y < a:
            a = y
        if y > b:
            b = y

    return a, b


for x in range(9999, 999, -1):
    if f(x) == (5, 7):
        print(x)
        break
