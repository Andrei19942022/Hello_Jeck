# def a_function():
#     print('You just created a function!')
#
# a_function()


# Пустая функция
# def empty_function():
#     pass

# задача1 Создайте функцию,которая будет считать сумму чисел в массиве
# def a():
#     sum = 0
#     for i in range(10):
#         sum += 1
#         print(sum)
#
# a()

# передача аргументов функции
# def add(a,b):
#     return a + b
#
# print(add(1,2))

# def add(a,b):
#     return  a + b
#
# print(add(a=2,b=3))
#
# total =add(b=4,a=5)
# print(total)

# def keyword_function(a=1,b=2):
#     return  a+b
#
# print(keyword_function(b=4,a=5))
# print(keyword_function())

# def mixed_function(a,b=2,c=3):
#     return a+b+c
#
# mixed_function(b=4,c=5)
#
# print(mixed_function(1, b=4,c=5))
# print(mixed_function(1))

# def many(*args,**kwargs):
#     print(args)
#     print(kwargs)
#
# many(1,2,3 ,name = 'Mike',job = 'programmer')

# def functoin_a():
#     global a
#     a=1
#     b=2
#     return a + b
#
# def function_b():
#     c=3
#     return a + c
# print(functoin_a())
# print(function_b())

# функции могут быть вложенными
# def func1(a,b):
#     def inner_func(x):
#         return x*x*x
#     return inner_func(a)+ inner_func(b)
#
# print(func1(4,5))


# функцию можно записать в одну строку

# def sum(a,b): return a+b
# print(sum(1,5))


# задача2 написать функцию is_year_leap принимающую 1 аргумент - год и возвращающую True,если год високосный ,и False
# иначе

# def is_year_leap(year):
#     return year %4 ==0 and year % 100 !=0  or year % 400 ==0
# print(is_year_leap(int(input('введите год: '))))

# задача3 написать функцию square,принимающую один аргумент - сторону квадрата и возвращающую
#  3 значения(с помощью кортежа) периметр квадрата,площадь квадрата и  диоганаль квадрата.
# сторону квадрата вводить с клавиатуры.
# import math
#
# def square(a):
#     p = 4*a
#     s = a**2
#     d = math.sqrt(2)*a
#     return p,s,d
# print(square(int(input('введите сторону квадрата: '))))

# задача4 написать функцию season принимающую один аргумент номер месяца(от 1 до 12)
# и возвращающую время года которому этот месяц принадлежит зима,весна,лето или осень.
# номер месяца вводить с клавиатуры

# def season(num):
#     if num==12 or 1 <=num<=2:
#         print('зима')
#     elif 3 <= num<=5:
#         print('весна')
#     elif 6 <= num<=8:
#         print('лето')
#     elif 9<=num<=12:
#         print('осень')
#     else:
#         print('неверно введен номер месяца!')
# n = int(input('введите номер месяца(1-12): '))
# season(n)

# задача5 написать функцию is_prime принимающую 1 аргумент - число от 0 до 1000
# и возвращающую True если оно простое и False - иначе

# def is_prime(n):
#     d =2
#     while n % d  !=0:
#         d +=1
#     return d ==n
#
# n = int(input('введите число: '))
# print(is_prime(n))

# задача6функция вычисляющая среднее арифметическое элементов массива . массив должен состоять
# из случайных чисел длинной 10 элементов

import random
N = 10
arr = [0] *N
for i in range(N):
    arr[1] = random.randint(1,100)

def average(arr):
    s = 0
    for i in range(N):
        s += arr[i]
    return s /N
print(arr)
print(average(arr))