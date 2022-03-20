def game(state, turn='Петя', counter=1):
    if state >= 201:
        return turn == 'Петя' and (counter == 3 or counter == 5)

    if turn == 'Петя':
        if game(state + 1, 'Ваня', counter + 1) and game(state * 2, 'Ваня', counter + 1):
            return True
    else:
        if game(state + 1, 'Петя', counter + 1) or game(state * 2, 'Петя', counter + 1):
            return True

    return False


for S in range(1, 201):
    if game(S):
        print(S)
