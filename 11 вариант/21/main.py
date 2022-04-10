def game(a, b, turn=0):
    if a + b >= 144:
        flag = turn in (2, 4)
        # print(f"game({a}, {b}, {turn})={flag}")
        return flag
        # return turn == 2 or turn == 4

    if turn >= 4:
        flag = False
        # print(f"game({a}, {b}, {turn})={flag}")
        return flag

    if turn % 2 == 0:
        flag = game(a + 1, b, turn + 1) and game(a * 2, b, turn +
                                                 1) and game(a, b + 1, turn + 1) and game(a, b * 2, turn + 1)
        # print(f"game({a}, {b}, {turn})={flag}")
        return flag

    flag = game(a + 1, b, turn + 1) or game(a * 2, b, turn +
                                            1) or game(a, b + 1, turn + 1) or game(a, b * 2, turn + 1)
    # print(f"game({a}, {b}, {turn})={flag}")
    return flag


# game(71, 1)
for i in range(1, 100):
    for S in range(1, 143):
        if game(S, i) and S == 69:
            print(i)
