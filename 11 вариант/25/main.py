x = 450000
n = 6

while n > 0:
    x += 1

    for divider in range(x - 1, 0, -1):
        if x % divider == 0:
            break

    flag = False

    for i in range(2, divider):
        if divider % i == 0:
            flag = True
            break

    if flag:
        print(x, divider)
        n -= 1
