file = open('file.txt', 'r')
numbers = [int(x) for x in list(file.read())]
file.close()

counter = 1
max_counter = 1

for i in range(1, len(numbers)):
    if numbers[i] > numbers[i - 1]:
        counter += 1
        max_counter = max(max_counter, counter)
    else:
        counter = 1

print(max_counter)
