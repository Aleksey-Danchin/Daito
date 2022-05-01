def f(n):
    mas = []
    for i in range(0, len(n), 2):
        a = n[i]
        b = n[i+1]
        if a > b:
            mas.append(a-b)
        else:
            mas.append(b-a)

    return mas


n = [6, 5, 4, 1, 3, 100, 5, 1]
while (len(n) > 1):
    print(n)
    n = f(n)

print(n)
