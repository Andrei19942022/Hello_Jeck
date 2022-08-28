# задача5.
# m = int(input('Введите 1е число '))
# n = int(input('Введите 2е число '))
# if m <= n:
#     for i in range(m, n+1):
#         print(i,end=" ")
# elif m > n:
#     for i in range(m, n-1, -1):
#         print(i,end=" ")

# задача4

# m = int(input('введите первое число'))
# n = int(input('введите второе число'))
# if m <= n:
#     for i in range(m, n + 1):
#        print(i,end="")
# else:
#     print('первое число должно быть меньше второго,повторите')

# задача 8

# num = [1,5,2,9,2,9,1]
# for i in num:
#     if num.count(i) == 1:
#        print(i)

# задача10
# for i in range(0 ,51):
#     if i ==35:
#         continue
#     print(i,end=" ")

# задача11

# string = ['hello my friend' , 'my name is' ,'house','cat','dog']
# string1 = []
# for i in string:
#     if ' ' in i :
#         string1.append(i)
# print(string1)

# задача7

# import random
# a = int(input('введите нужное число: '))
# number = [random.randint(1, 50) for a in range(a)]
# print(number)

# задача9

# a = ['student1', 'student2','student3']
# b = []
# for i  in a:
#     print(i + ' _good')



# задача6
# name = input('введите имя и фамилию через пробел: ')
# name = name.split(' ')
# print(name)
# name = name[::-1]
# print(name)
# name =' ' .join(name)
# print('фамилия  и имя: ' , name)

# задача7

# задача1
# max = (4 **4) **4
# print(max)

# задача2a
# from math import  *
# x = float(input('введите число'))
# if (2 * x - pow(x,2)) != 0:
#     a = (1 + x + pow(x,2)) / (2 * x + pow(x,2))
#     b = (1 - x + pow(x,2)) / (2 * x - pow(x,2))
#     c = 5 -2 * pow(x,2)
#     y = (a + 2 - b) * c
#     print(y)
# else:
#     print('деление на ноль,введите другое число')

# 2b
# from math import *
# a = float(input('введите угол a в градусах'))
# b = float(input('введите угол b в градусах'))
# y = float(input('введите угол c  вградусах'))
# a = radians(a)
# b = radians(b)
# y = radians(y)
# f = pow(4,-1)*(sin(a+b-y)+sin(b+y-a)+sin(y+a-b)-sin(a+b+y))
# print(f)

# задача3
# a =0
# b = ""
# c = []
# print(bool(a))
# print(bool(b))
# print(bool(c))
