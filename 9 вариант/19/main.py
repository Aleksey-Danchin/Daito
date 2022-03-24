def game(a, b, turn=0):
    if a + b >= 101:
        return turn == 2

    if turn >= 2:
        return False

    if turn % 2 == 0:
        return game(a + 1, b, turn + 1) or game(a * 2, b, turn + 1) or game(a, b + 1, turn+1) or game(a, b * 2, turn+1)

    return game(a + 1, b, turn + 1) or game(a * 2, b, turn + 1) or game(a, b + 1, turn+1) or game(a, b * 2, turn+1)


for S in range(1, 94):
    if game(S, 7):
        print(S)
