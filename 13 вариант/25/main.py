num = 650_000
counter = 0

while counter < 100:
    num += 1

    for divider in range(num - 1, 0, -1):
        if num % divider == 0:
            break

    if divider > 1:
        flag = False

        for i in range(2, divider):
            if divider % i == 0:
                flag = True
                break

        if flag:
            print(num, divider)
            counter += 1
