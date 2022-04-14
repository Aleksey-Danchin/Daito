for x in range(95632, 95701, 2):
    dividers = []

    for i in range(2, x + 1, 2):
        if x % i == 0:
            dividers.append(i)

            if len(dividers) > 6:
                break

    if len(dividers) == 6:
        print(*dividers)
