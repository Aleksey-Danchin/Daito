def game(a, b, turn=0):
    if a + b >= 62:
        return turn in (2, 4)

    if turn == 4:
        return False

    if turn % 2 == 0:
        return game(a+1, b, turn + 1) and game(a*2, b, turn + 1) and game(a, b+1, turn + 1) and game(a, b*2, turn + 1)

    return game(a+1, b, turn + 1) or game(a*2, b, turn + 1) or game(a, b+1, turn + 1) or game(a, b*2, turn + 1)


for s in range(1, 52):
    if game(10, s):
        print(s)
