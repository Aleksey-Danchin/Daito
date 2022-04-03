def f(a, b):
    if a < b:
        return 0

    if a == b:
        return 1

    return f(a - 1, b) + f(a // 2, b)


print(f(30, 10) * f(10, 1))

# array = [0 for _ in range(0, 31)]

# array[30] = 1
# for i in range(30, 10, -1):
#     if array[i] > 0:
#         if i - 1 >= 10:
#             array[i-1] += array[i]
#         if i // 2 >= 10:
#             array[i//2] += array[i]

# for i in range(10, 0, -1):
#     if array[i] > 0:
#         if i - 1 >= 0:
#             array[i-1] += array[i]
#         if i // 2 >= 0:
#             array[i//2] += array[i]

# print(array)
# print(array[1])
