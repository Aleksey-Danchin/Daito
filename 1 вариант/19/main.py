def game(turns, variants=[]):
    if turns[-1] >= 181:
        if len(turns) == 3 or len(turns) == 5:
            variants.append(turns)
        return variants

    if len(turns) > 5:
        return

    game(turns + [turns[-1] + 1], variants)
    game(turns + [turns[-1] * 2], variants)
    return variants


for i in range(1, 181):
    variants = game([i])

    if len(variants) >= 6:
        print(i)
        # print(variants)
