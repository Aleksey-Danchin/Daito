B = [10, 15]
C = [20, 27]


def F(A):
    for x in range(50, 300):
        x = x // 10

        b = B[0] <= x and x <= B[1]
        c = C[0] <= x and x <= C[1]
        a = A[0] <= x and x <= A[1]

        q1 = bool(b + c)
        q2 = q1 <= a
        q3 = not q2

        if q3:
            return False

    return True


for length in range(1, 20):
    for left in range(7, 30):
        A = [left, left + length]
        if F(A):
            print(length, A)
