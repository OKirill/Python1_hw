employees = ['Vasya', 'Stepan', 'Jhon', 'Jack']
salary = [55000, 720000, 120000, 63000]
taxes = 0.13
result = dict(zip(employees, salary))

print(result)
with open('salary.txt', 'w', encoding='utf-8') as file:
    for key, value in result.items():
        file.write(f'{key} - {value}\n')

with open('salary.txt', 'r', encoding='utf-8') as file:
    for line in file.readlines():
        employee, single_salary = line.strip().split(' - ')
        single_salary = int(single_salary)
        if single_salary < 500_000:
            print(f'{employee.upper()} - salary {single_salary - single_salary * taxes}')
