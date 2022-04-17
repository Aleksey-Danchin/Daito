sum = 0


def F(n):
    global sum
    sum += n
    if n > 1:
        F(n - 1)
        F(n - 3)


F(6)
print(sum)
