def game(a, b, turn=0):
    if a + b >= 62:
        return turn == 3

    if turn == 3:
        return False

    if turn % 2 == 0:
        return game(a+1, b, turn + 1) or game(a*2, b, turn + 1) or game(a, b+1, turn + 1) or game(a, b*2, turn + 1)

    return game(a+1, b, turn + 1) and game(a*2, b, turn + 1) and game(a, b+1, turn + 1) and game(a, b*2, turn + 1)


for s in range(1, 52):
    if game(10, s):
        print(s)
