def adress_date(name, age, city):
    result = (f'{name}, {age}, год(а), проживает в городе {city}')
    return result


print(adress_date('Kirill', 28, 'Moscow'))



def max_number(num1, num2, num3):
    return max(num1, num2, num3)

print(max_number(2,8,4))

def endless_args(*args):
    return max(*args, key = len)

print(endless_args('priven','sssssssss','sss','dsada','afasgassssssssssssssssss','fa2'))






