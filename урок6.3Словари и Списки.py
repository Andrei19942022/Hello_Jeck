# d = {}
# d = {'dict': 1, 'dictionary': 2}
# print(d)

# d = dict(short='dict',long='dictionary')
# d_2 = dict([(1,1),(2,4)])
# print(d,'\n', d_2)

# d = dict.fromkeys(['a','b'])
# d2 = dict.fromkeys(['a','b'],100)
# print(d, '\n' , d2)

# генератор словарей
# d = {a:a**2 for a in range(7)}
# print(d)

# d = {1: 2, 2: 4, 3: 9}
# d[4] = 4 ** 2
# print(d[1])
# print(d)

# методы словарей
# dict.clear() -очищает словарь
# dict.copy() - возвращает копию словаря
# dict.items() - возвращает пары
# dict.keys() -возвращает ключи в словаре
# dict.pop() - удаляет ключ и возвращает значение
# dict.values() - возвращает значения в словаре
# len(dict) - определяет количество элементов в списке

# months = { 1: 'jan',2:'feb',3:'mar',4:'apr',
#            5:'may', 6:'jun',7:'jul',8:'aug',
#            9:'sep', 10:'oct',11:'nov', 12:'dec'}
# count = len(months)
# print(count)

# удаление элемента по ключу.Операция Del

# del salary['secretary']
# print(salary)

# salary = {'director':200.0,
#           'secretary':100.0,
#           'menegery': 120.0,}
# print(salary)
# key = 'secretary'
# if key in salary:
#     del salary['secretary']
#     print(salary)

# использование вложенных словарей
# position = {'manager': {'director' ,
#                         'deputy director'},
#             'teacher':{'specialist',
#                        'methjdist',
#                        'senior lecturer'},
#             'staff':{'cleaner',
#                      'porter',
#                     ' watchman'}}
# count1 = len(position)
# count2 = len(position['manager'])
# count3 = len(position['staff'])
#
# print(position, 'len:', count1, '\n' ,
#       position['manager'] , 'len:', count2, '\n',
#       position['staff'], 'len:' , count3, '\n')
# операция in. определение наличия ключа в словаре
# salary = {'director': 12000.0,
#           'secretary':10000.0,
#           'locksmith':18000.0}
# print(salary)
#
# key = 'scretary'
# if key in salary:
#     del salary['secretary']
#     print(salary)
#
# key2 = 5
# if key2 in salary:
#     del salary[key2]

# операция not in . определение отсутствия ключа в словаре
# words = dict()
# count = int(input('количество слов в словаре: '))
# i = 0
# while i<count:
#     print('ввод слов')
#     wrd = str(input('слово: '))
#     value = int(input('значение: '))
#
#     if wrd not in words:
#         words[wrd] = value
#     i = i + 1
#     print(words)

# встроенная функция zip
# numbers = dict(zip([1,2,3],['one', 'two', 'three']))
# print(numbers)

# mn - ключ , months[mn] -значение ключа

Months = {1:'jan', 2:'feb', 3:'mar'}
for mn in Months:
    print(mn, ':' ,Months[mn])

# сортировка словаря
# A = { 'f':10, 'a':2, 'c':17}
# ak = A.keys()
# print(ak)
# list_ak = list(ak)
# print(list_ak)
# list_ak.sort()
# print(list_ak)
# B = {}
# for k in list_ak:
#     print('(',k, ':' , A[k], ')')
#     B[k] = A[k]
#     print(B)

# обход словаря с помощью цикла for

# months = { 1: 'jan',2:'feb',3:'mar',4:'apr',
#            5:'may', 6:'jun',7:'jul',8:'aug',
#            9:'sep', 10:'oct',11:'nov', 12:'dec'}
#
# for mn in months:
#     print(mn, ':' , months[mn])



# задача1создайте словарь
# person = {'name':'Nikolay', 'age':50, 'city':'Minsk'}
# print(person['age'])


# ЗАДАЧА2значением словаря могут быть и списки. создайте словарь с ключами bmv,tesla
# и списками из 3х моделей в качестве значений.
# выведите первое и последнее значение каждого из ключей
# models =  {'bmv': ['x5' , 'x6' , 'x8'],
#            'tesla': ['g2' , 'g3' , 'g4']}
# print(models['tesla'][0],models['tesla'][2])
# print(models['bmv'][0], models['bmv'][2])



# задача3Исправьте ошибке в коде чтобы получить требуемый вывод.Вывод True

# d1 = {'a':100, 'b':200, 'c':300}
# d2 = {'a':300 ,'b':200,'d':400}
#
# print(d1['b']) == (d2['b'])

# задание4 дан словарь с числовыми значениями. необходимо их все
# перемножить и вывести на экран

# number = {'data1':375 , 'data2':567, 'data3':37, 'data4':21}
# result = 1
# for key in number:
#     result = result * number[key]
# print(result)

# задача5 даны 2 списка одинаковой длины .необходимо создать из них словарь таким образом,
# чтобы элементы первого списка ключами ,а элементы второго -соответственно значениями нашего словаря
# keys = ['red', 'green' , 'blue']
# values = ['065095060e', 'df265256' , 'b520560']
# color = dict(zip(keys,values))
# print(color)

# задача6 создать словарь из строки 'pythonist' следующим образом:
# в качестве ключей возьмите буквы строки,а значениями пусть будут числа,
# соответствующие количеству вхождений данной буквы в строку
# str = 'pythonist'
# my_dict = {i: str.count(i) for i in str}
# print(my_dict)


# дом.задание  у вас есть словарь,где ключ-название продукта. значение- список,который содержит
# цену кол-во товара. выведите через '-' название -цену-кол-во.
# с клавиатуры вводите название товара и его кол-во.  n - выход из программы.
# посчитать цену выбранных товаров и сколько товаров осталось в изначальном списке