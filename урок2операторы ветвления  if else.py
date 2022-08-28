# модуль math - обширный функционал работы с числами
# import math
# import random
#
# math.acos(x) - арккосинус х. в радианах
# math.asin(x) - арксинус
# math.atan() - арктангенс

# Модуль random - функции для генерации свободных чисел

# random.randint(a,b) - случайное целое число n , a<n<b
# random.uniform(a,b) - случайное число с плавающей точкой
# random.random() - случайное число от 0 до 1
# random.choice(seq=) cлучайный элемент непустой последовательности

# задача1 вычислить сумму случайного 3-х значного числа

# import random
# n = random.randint(100,999)
# print(n)
# a = n //100
# b = (n // 10) %10
# c = n%10
# print(a + b+ c)

# оператор if
# a = 3
# if a > 1:
#      print('a > 1')
# if True:
#     print('hello')


# кострукция if - else .при истинном один набор команд, при ложном другой

# a =  2
# if a < 1:
#     print('a < 1')
# else:
#     print('a  > 1')

# задача1 узнать целое или нет число
# a = input()
# a = int(a)
# if a % 2 ==0:
#     print('число четное')
# else:
#     print('число нечетное')

# конструкция if - elif - else
a = int(input('введите число: '))
if a < 0:
    print('число меньше 0')
elif a == 0:
    print('число равно 0')
else:
    print('число больше 0')