file = open('a.txt', 'r')
numbers = [int(x) for x in file.read().splitlines()]
file.close()

counter = 0
max_number = 0

for x in numbers:
    if x % 16 == 9 and x % 256 != 169:
        print(x)
        counter += 1
        max_number = max(max_number, x)

print(counter)
print(max_number)
