def game(a, turn=0):
    if a == 1:
        return turn == 3

    if turn >= 3:
        return False

    variants = []

    if a % 2 == 0:
        variants.append(game(a / 2, turn + 1))
    else:
        variants.append(game(a - 2, turn + 1))

    if a % 3 == 0:
        variants.append(game(a / 3, turn + 1))
    else:
        variants.append(game(a - 3, turn + 1))

    if turn % 2 == 0:
        return True in variants

    return not (False in variants)


for S in range(1, 38):
    if game(S):
        print(S)
