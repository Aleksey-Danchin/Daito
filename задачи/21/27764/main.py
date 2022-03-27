def game(a, b, turn=0):
    if a + b >= 47:
        return turn == 2 or turn == 4

    if turn >= 4:
        return False

    if turn % 2 == 0:
        return game(a + 1, b + 2, turn + 1) and game(a + 2, b + 1, turn + 1) and game(a * 2, b, turn + 1) and game(a, b * 2, turn + 1)

    return game(a + 1, b + 2, turn + 1) or game(a + 2, b + 1, turn + 1) or game(a * 2, b, turn + 1) or game(a, b * 2, turn + 1)


for S in range(1, 37):
    if game(S, 10):
        print(S)
