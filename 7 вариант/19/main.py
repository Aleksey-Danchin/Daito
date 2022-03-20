def game(a, b, turn=0):
    if a + b >= 122:
        return turn == 2

    if turn >= 2:
        return False

    return game(a + 2, b, turn + 1) or game(a * 2, b, turn + 1) or game(a, b + 2, turn + 1) or game(a, b * 2, turn + 1)


for S in range(1, 118):
    if game(S, 3):
        print(S)
