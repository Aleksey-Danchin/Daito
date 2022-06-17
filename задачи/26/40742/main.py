from itertools import count


WEEK_SECONDS = 7 * 24 * 60 * 60
WEEK_START = 1633305600
WEEK_FINISH = WEEK_START + WEEK_SECONDS

week = [0 for _ in range(WEEK_SECONDS)]

file = open('26.txt', 'r')

n = int(file.readline())

for i in range(n):
    [s, f] = [int(x) for x in file.readline().split()]

    if i % 1000 == 0:
        print(f'{i}/{n}')

    if s <= WEEK_FINISH:
        start = max(WEEK_START, s)
        finish = 0

        if f >= WEEK_START:
            finish = min(f, WEEK_FINISH)
        elif f == 0:
            finish = WEEK_FINISH

        if finish > start:
            for j in range(start, finish):
                week[j - WEEK_START] += 1

file.close()

a = max(week)
counter = 0

for x in week:
    counter += x == a

print(a, counter)
