# кортежи
# a = (1,2,3,4,5,6)
# print(a)
# b = (1,)
# print(b)

# a = (1, 2, 3, 4, 5, 6)
# b = [1, 2, 3, 4, 5, 6]
# print(a.__sizeof__())
# print(b.__sizeof__())

# преобразование кортежа в список
# a =(10,2.13,'sguare',89,'c')
# b = [1,2,3]
# c = list(a)
# d = tuple(b)
# print(c)
# print(d)

# Список изменяем .кортеж нет
# nested = (1, 'do',['param',10,20])
# nested [2][1] = 15
# print(nested)

# объединение кортежей
# a = (1,2,3,4,5,6,7)
# b = (0,9,8,7,6,5,4)
# c = a +b
# print(c)

# умножение кортежей
# a = (1,2,3,4)
# c = a * 2
# print(c)

# функции кортежей len-длина кортежа, count -количество заданного элемента в кортеже

# a = (1, 2, 3, 4, 5, 6, 7)
# print(a.count(5), len(a))

# функции max и min
# a = (1, 2, 3, 4, 5, 6, 7)
# print('max',max(a), 'min', min(a))
# b = ('a', 'ab', 'e', ' world')
# print('max',max(b), 'min', min(b))

# задача1 создайте кортеж из случайных 10 чисел.найти максимальный и минимальный элемент

# import random
# a = [random.randint(0,50) for i in range(10)]
# b = tuple(a)
# print(b)
# print('max',max(a), 'min',min(b))

# задача2 заполните один кортеж 10-ю случайными числами от 0 до 5 .второй кортеж от -5 до 0.
# объединить 2 кортежа с помощью оператора +

# import random
# a = tuple([random.randint(0,5) for i in range(10)])
# b = tuple([random.randint(-5,0) for i in range(10)])
# c = a + b
# print(c, '\n количество нулей: ', c.count(0))

# задача3
# вывести данные кортежа без скобок,через запятую.
# обязательно:элементы кортежа - строки

# a = ('one', 'two', 'three')
# b = ',' .join(a)
# print(b)

# задача4 два кортежа.определить сумма какого из кортежей больше и вывести соответствующее сообщение
# на экран(сумма больше в кортеже-)
# вывести на экран порядковые номера минимальных элементов этих кортежей

# a = (13,5,43,49,67,32,12,98,6,10,34,20,55,68,14,60,14)
# b = (53,21,4,23,76,3,43,12,54,342,21)
# s_a = sum(a)
# s_b = sum(b)
# if s_a > s_b:
#     print('сумма больше в кортеже - a')
# else:
#     print('сумма больше в кортеже - b')
#
# print('min a' , min(a), 'номер - ' , a.index(min(a)))
# print('min b' , min(b), 'номер - ' , b.index(min(b)))


# a = (0,1,2,3,4,5,6,7,8,9)
# s_a = sum(a)
# print(a)


# Дом.задание1 найти самое длинное слово в строке

# string = 'python java c c++ javascript pascal php'
# print(string)
# words = string.split()
# id_longest = 0
# c = 0
# for i in words:
#     if len(words) < len(words[c]):
#         id_longest = c
#     c += 1
# print(words[id_longest])

# задание2преобразовать текст с список слов
# с удалением знаков препинания

# string = input('write down a text:\n')
# sings = ['.' , ',' , ':' , ';' , '!' , '?' , '(',')']
# words = string.split()
# i = 0
# for word in words:
#     if word[-1] in sings:
#        words[i] = word[:-1]
#        word = words[i]
#     if word[0] in sings:
#         words[i] = word[1:]
#     i += 1
#
# for i in words:
#     print(i,end= '')
# print()
