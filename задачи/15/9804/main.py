def f(A):
    for x in range(0, 1_000_000):
        a = x & A == 0
        b = x & 17 == 0
        c = x & 29 == 0

        if not(c or (not b) or (not a)):
            return False

    return True


for A in range(0, 1025):
    if f(A):
        print(A)
        break
