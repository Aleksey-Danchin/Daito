def game(a, b):
    if a[-1] + b[-1] >= 101:
        yield len(a)
        return

    if len(a) < 5:
        yield from game(a + [a[-1] + 1], b + [b[-1]])
        yield from game(a + [a[-1] * 2], b + [b[-1]])
        yield from game(a + [a[-1]], b + [b[-1] + 1])
        yield from game(a + [a[-1]], b + [b[-1] * 2])


for S in range(1, 94):
    counter3 = 0
    counter5 = 0

    for size in game([7], [S]):
        if size == 3:
            counter3 += 1
        elif size == 5:
            counter5 += 1

    if counter3 > 1 and counter5 > 1 and counter5 % 4 == 0:
        print(S)
