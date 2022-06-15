def game(a, turn=0):
    if a > 64:
        return turn == 3

    if turn > 3:
        return False

    if turn % 2 == 0:
        return game(a + 1, turn + 1) or game(a * 2, turn + 1)

    return game(a + 1, turn + 1) and game(a * 2, turn + 1)


for S in range(1, 65):
    if game(S):
        print(S)
