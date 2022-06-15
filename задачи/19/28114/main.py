def game(n, turn=0):
    if n >= 33:
        return turn == 2

    if turn >= 2:
        return False

    return game(n + 1, turn + 1) or game(n * 3 - 1, turn + 1)


for S in range(1, 33):
    if game(S):
        print(S)
        # break
