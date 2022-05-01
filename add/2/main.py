import random


def tour(players):
    next_players = []

    n = len(players)

    for i in range(0, n, 2):
        next_players.append(players[i])

    return next_players


def is_done(players):
    n = len(players)

    if n % 2 != 0:
        n -= 1

    for i in range(0, n, 2):
        if players[i] in (1, 2) and players[i + 1] in (1, 2):
            return True

    return False


def game():
    players = list(range(1, 21))
    random.shuffle(players)

    while (len(players) > 1):
        if is_done(players):
            return True

        players = tour(players)
        random.shuffle(players)

    return False


counter = 0
turns = 0

while True:
    turns += 1
    if game():
        counter += 1

    if turns % 100_000 == 0:
        print(counter / turns)
