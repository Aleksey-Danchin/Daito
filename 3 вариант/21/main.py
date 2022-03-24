def game(state, counter=0):
    if state >= 201:
        return counter == 2 or counter == 4

    if counter < 5:
        if counter % 2 == 0:
            return game(state + 1, counter + 1) and game(state * 2, counter + 1)
        else:
            return game(state + 1, counter + 1) or game(state * 2, counter + 1)

    return False


for S in range(1, 201):
    if game(S):
        print(S)
