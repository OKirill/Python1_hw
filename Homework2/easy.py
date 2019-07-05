# fruits = ['apple', 'lemon', 'pineapple', 'watermelon']

# Второе задание

a = {2, 7, 12, 15, 4}
b = {5, 15, 2, 8, 10}

c = a - b
print(c)

# Третье задание
first = [4, 12, 41, 22, 46, 5, 3, 24, 23]
second = []

for i in first:
    if i % 2 == 0:
        second.append(i / 4)

    else:
        second.append(i * 2)

print(second)
