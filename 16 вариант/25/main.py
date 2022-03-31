counter = 0
number = 550_000

while counter < 5:
    number += 1
    s = 0

    for i in range(2, number):
        if number % i == 0:
            flag = True

            for j in range(2, i):
                if i % j == 0:
                    flag = False
                    break

            if flag:
                s += i

    if s % 10 == 7:
        print(number, s)
        counter += 1
