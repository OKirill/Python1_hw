array = [2, 4, 12, 16, 7, 9]

result = [i ** 2 for i in array]

print(result)

firstl = ['apple', 'lemo', 'mango']
secondl = ['apple', 'pineapple', 'mango']

thirdl = [fruit for fruit in firstl if fruit in secondl]
print(thirdl)

final = [2, 23, 12, 9, 15, 24, -18, 36]
final_sorted = [number for number in final if number % 3 == 0 and number >= 0 and number % 4 != 0]
print(final_sorted)
