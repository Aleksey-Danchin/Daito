file = open('file.txt', 'r')
rows = file.read().splitlines()
file.close()

rows = [[int(x) for x in row.split()] for row in rows]

rows = [row for row in rows if row[0] + row[1] > row[2]
        and row[0] + row[2] > row[1] and row[1] + row[2] > row[0]]

counter = 0
for row in rows:
    [a, b, c] = row

    if (a**2 + b ** 2 > c**2) and (a**2 + c**2 > b**2) and (b**2 + c**2 > a**2):
        counter += 1

print(counter)
