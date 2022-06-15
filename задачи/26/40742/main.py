WEEK_SECONDS = 7 * 24 * 60 * 60
WEEK_START = 1633305600
WEEK_FINISH = WEEK_START + WEEK_SECONDS

mas = []
file = open('26.txt', 'r')

n = int(file.readline())

for i in range(n):
    [s, f] = [int(x) for x in file.readline().split()]

    if s <= WEEK_FINISH and (f >= WEEK_START or f == 0):
        mas.append([s, f])

file.close()
