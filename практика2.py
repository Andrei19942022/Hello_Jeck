# задача1 создать папку на рабочем столе с помощью os
# import os
# os.mkdir(r'C:\Users\Lenovo\Desktop\folder')

# задача2 Удалить созданную папку c помощью os
# import os
# os.rmdir(r'C:\Users\Lenovo\Desktop\folder')

# задача3создать файл task_1.txt и переимеговать его на renamefile.txt

# import os
# os.rename('task_1.txt', 'renamefile.txt')

# задача4 Создайте словарь из строки 'helloamynameis' следующим образом: в качестве ключей возьмите буквы строки ,а значениями
# пусть будут числа,соответствующие количествув хождений данной буквы в строку
# string = 'helloamynameis'
# a = {key:string.count(key) for key in string}
# print(a)

# задача5 Даны 2 списка одинаковой длины.Необходимо создать из них словарь таким образом,чтобы элементы
# первого списка были ключами, а элементы второго - соответственнозначениями нашего словаря
# a = [ 1,2,3,4,5]
# b = ['a','b','c','d','e']
# c = dict(zip(a,b))
# print(c)

# задача6 Даны 2 списка чисел .Посчитайте сколько чисел содержится одновременно как в первом списке,так и во втором
# list = [1,2,3,4,5]
# list1 = [2,4,5,8,6]
# set1 =set(list)
# set2 = set(list1)
# intersection = set1.intersection(set2)
# print(len(intersection))

# задача7 создать кортеж с числами от 1 до 50используя генератор списков
# import random
# korteg = tuple(random.randint(1,50) for x in range(10))
# print(korteg)



