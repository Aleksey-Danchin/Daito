for i in range(201455, 201471):
    dividers = []

    for j in range(1, i + 1):
        if i % j == 0:
            dividers.append(j)
        if len(dividers) > 4:
            break

    if len(dividers) == 4:
        print(i, *dividers)
