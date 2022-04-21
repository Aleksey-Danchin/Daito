def game(a, turn=0):
    if a == 1:
        return turn in (2, 4)

    if turn >= 4:
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
        return not (False in variants)

    return True in variants


for S in range(1, 38):
    if game(S):
        print(S)
