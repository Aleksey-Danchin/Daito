memory = {}


def f(a, b):
    if a in memory:
        return memory[a]

    if a == b:
        memory[a] = 1
        return 1

    if a > b:
        memory[a] = 0
        return 0

    if a in (5, 10, 22, 69):
        memory[a] = 0
        return 0

    c = f(a + 1, b) + f(a + 2, b) + f(a + 4, b)
    memory[a] = c
    return c


# print(f(1, 8) * f(8, 15) * f(15, 47) * f(47, 100))
print(f(1, 100))
print(memory)
