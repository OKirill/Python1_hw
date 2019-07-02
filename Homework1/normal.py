# __author__ == Кирилл Олейник

def raise_to_power():
    i = input("Введите число:")
    i = int(i)
    if 0 < i < 10:
        print(i ** 2)
    else:
        print("Введите число в правильном диапазоне!")



a = input("Введите первую переменную:")

b = input("Введите вторую переменную:")
a = int(a)
b = int(b)

a = a + b
b = a - b
a = a - b

print(a)
print(b)

raise_to_power()