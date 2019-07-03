first_name = input("Введите Имя:")
last_name = input("Введите Фамилию:")
age = input("Введите свой возраст:")
weight = input("Введите свой вес: ")
age = int(age)
weight = int(weight)
if age <= 30 and 50 <= weight < 120:
    print(first_name + " " + last_name + ", ", age, "год, ", "вес", weight, "- хорошее состояние")

elif age > 40 and (weight < 50 or weight > 120):
    print(first_name + " " + last_name + ", ", age, "год, ", "вес", weight, "- К Врачу")

elif age > 30 and (weight < 50 or weight > 120):
    print(first_name + " " + last_name + ", ", age, "год, ", "вес", weight, "- следует заняться собой!")

else:
    print("Извиние вы не попадаете ни под какую категорию")

