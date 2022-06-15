def game(n, turn=0):
    if n >= 33:
        return turn in (2, 4)

    if turn >= 4:
        return False

    if turn % 2 == 0:
        return game(n + 1, turn + 1) and game(n * 3 - 1, turn + 1)

    return game(n + 1, turn + 1) or game(n * 3 - 1, turn + 1)


for S in range(1, 33):
    if game(S):
        print(S)
        # break
