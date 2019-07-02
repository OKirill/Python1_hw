
# __author__ == Кирилл Олейник
# Задание 1
a = "some string"
b = 2
c = "string № " + str(b)
d = input("Введите своё имя: ")

print("Привет, " + d)
print(a)
print(b)
print(c)

# Задание 2

def number_plus():
    number = input("Введите любое число: ")
    number = int(number)
    print(number + 2)

number_plus()

def age_check():
    age = input("Введите свой возраст: ")
    age = int(age)
    if age >= 18:
        print("Доступ разрешен")
    else:
        print("Извините, пользование данным ресурсом только с 18 лет")

age_check()

