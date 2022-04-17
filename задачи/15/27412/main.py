def f(A):
    for x in range(1, 1000):
        a = x % A == 0
        b = x % 6 == 0
        c = x % 9 == 0

        q = a or (not b) or (not c)

        if not q:
            return False

    return True


for A in range(1000, 0, -1):
    if f(A):
        print(A)
        break
