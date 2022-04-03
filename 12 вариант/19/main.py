def game(a, b, turn=0):
    if a + b >= 144:
        return turn == 2

    if turn >= 2:
        return False

    return game(a + 1, b, turn + 1) or game(a * 2, b, turn + 1) or game(a, b + 1, turn + 1) or game(a, b * 2, turn + 1)


for a in range(1, 142):
    if game(a, 2):
        print(a)
        break
