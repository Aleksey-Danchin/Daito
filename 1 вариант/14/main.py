n = 5**2022 - 2 * 5**1010 + 25**850 + 2500
counter = 0

while n > 0:
    d = n % 5
    n = n // 5

    if d == 4:
        counter += 1


print(counter)
