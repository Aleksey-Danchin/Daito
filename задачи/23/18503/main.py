def game(a, b):
    if a == 13:
        return 0

    if a == b:
        return 1

    if a > b:
        return 0

    return game(a + 1, b) + game(a + 2, b) + game(a * 3, b)


print(game(1, 10) * game(10, 15))
