P = [130, 171]
Q = [150, 185]


def f(A):
    for x in range(1200, 1900):
        x = x / 10

        p = P[0] <= x <= P[1]
        q = Q[0] <= x <= Q[1]
        a = A[0] <= x <= A[1]

        if not(not(p) or not(q) or a):
            return False

    return True


def main():
    for length in range(1, 50):
        for left in range(100, 200):
            A = [left, left + length]
            if f(A):
                print(A, length)
                return


main()
