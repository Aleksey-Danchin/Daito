def f(x):
    s = 0
    while x > 0:
        s = s + x % 9
        x = x // 3
    return s


for x in range(80, 1_000_000):
    if f(x) == 17:
        print(x)
        break
