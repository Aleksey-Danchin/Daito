n = 550_000
c = 0

while c < 5:
    n += 1
    s = 0
    for i in range(2, n):
        if n % i == 0:

            flag = True
            for j in range(2, i):
                if i % j == 0:
                    flag = False
                    break

            if flag:
                s += i

    if s % 10 == 1:
        print(n, s)
        c += 1
