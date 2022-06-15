def game(a, turn=0):
    if a > 64:
        return turn == 2

    if turn > 2:
        return False

    return game(a + 1, turn + 1) or game(a * 2, turn + 1)


for S in range(1, 65):
    if game(S):
        print(S)
