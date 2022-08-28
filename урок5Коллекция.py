# import random
#
# c = [random.randint(0 ,100) for i in range(10)]
# print(c)
#
# print(c[0])
# print(c[-1])
# print(c[5])
# print(c[-4])

# Добавление элемента в конец список
# elements = []
#
# elements.append('a')
# elements.append('i')
# elements.append('b')
# elements.append('k')
#
# print(elements)

# добавление в список на указанную позицию

# elements = [1, 3, 'a' ,6, 'b']
# elements.insert(1, 2)
# print(elements)

# изменение элемента списка
# elements = [1,  3, 'a' , 6, 'b']
# elements[1] = 2
# print(elements)



# удаление элемента из списка
# 1 метод по индексу

# elements = [1, 3, 'a' , 6, 7 , 'b']
# del elements[1]
# print(elements)

# 2метод remove по имени, удаляет 1й найденный элемент в списке,элементы ищет с лева на право

# elements = [1, 3, 'a' , 6, 7 , 'b']
# elements.remove('a')
# print(elements)

# удаление элемента из вложенного списка

# my_list = ['hello' , 'world']
# elements = [1, 2, my_list, 6, 7, 'a']
#
# del elements[2][1]
# print(my_list)
# print(elements)

# Можно удалять целыми диапозонами
# elements = [ 1, 3, 6, 'a' , 'b' , 'abc', 123 , 444]
# del elements[4:]
# print(elements)
# del elements[:2]
# print(elements)
# del elements[1:3]
# print(elements)


# проверка наличие элемента в списке

# elements = [ 1, 3, 6, 'a' , 'b' , 'abc', 123 , 444]
#
# if  'a' in elements:
#     print('yes')

# # обьединение списка дополняет в текущий
# a = [1, 3, 5]
# b = [1, 5, 8,9]
# print(a + b)
#
# d = ['n', 'b', 'h']
# c = ['z', 'f', 'l']
# d.extend(c)
# print(d)


# копирование списка редко используется
# a = [1, 2, 3 , 4]
# b = a
#
# a.append
# b.append
# print('a', a)
# print('b' ,a)

# метод coppy
# a = ['кот', 'слон', 'змея']
# b = a.copy()
# a.append('собака')
# b.append('кошка')
# print(a)
# print(b)

# Для перебора списков в pyhton есть 2 цикла for и while:
# цикл for выглядит компактней

# цикл for
# elements = [1, 2, 3, 'neow']
# for i in elements:
#     print(i)

# # цикл while
# elements = [1, 2, 3, 'neow']
# elements_len = len(elements)
# i = 0
# while i < elements_len:
#     print(elements[i])
#     i +=1

# методы списка, дом.задание переписать

# list.append(x) -позволяет добавлять элемент в конец списка
# list1.extend(list2) - для сложения списков
# list.insert(i,x) - для добавления элемента на указанную позицию(i -позиция, x - элемент)
# list.remove(x) - удаляет элемент из списка(только первое вхождение)
# list.clear() - для удаление всех элементов (список становится пустым)
# list.copy() - для копирования списков
# list.count(x) - посчитает количество элементов х в списке
# list.index(x) - вернет позицию 1-го найденного элемента х в списке
# list.pop(i) - удалит элемент из позиции (i)
# list.reverse() - меняет порядок элементов в списке на противоположный
# list.sort() - сортирует список

# clear
# a = [1, 2, 3]
# a.clear()
# print(a)

# copy
# a = [1, 2, 3]
# b = a.copy()
# print( id(a), id(b), a, b)

# count
# elements = ['one', 'two', 'three', 'one', 'two', 'one']
# print(elements.count('one'))

# index
# elements = ['one', 'two', 'three', 'one', 'two', 'one']
# print(elements.index('three'))

# pop
# elements = [1, 'meow', 3, 'meow']
# elements.pop(1) - удаление с индексом 1
# print(elements)
#
# elements.pop() - удаляем 1-й элемент списка
# print(elements)
#
# elements.pop(-1)- удаляем последний элемент списка
# print(elements)

# reverse
# a = [1, 2,3,4]
# a.reverse()
# print(a)

# sort - по возрастанию
# elements = [3,19, 0, 3, 102, 3,1]
# elements.sort()
# print(elements)
#
# # sort - по убыванию
# elements = [3,19, 0, 3, 102, 3,1]
# elements.sort(reverse=True)
# print(elements)

# Вложенные списки;
# elements = [['яблоки', 50], ['апельсины', 190], ['груши', 100]]
# print(elements[0])
#
# print(elements[0][0])

# срезы- подмножества элементов из списка
# elements = [0.1, 0.2, 1,2,3,4,0.3,0.4]
# in_elements =elements[2:6]
# print(elements)
# print(in_elements)

# Задача.представить список в обратном порядке
# 1вариант
# elements = [1, 2, 5, 7, 8, 9, ]
# print(elements[::-1])
# #
# # 2вариант
# elements = [1, 2, 5, 7, 8, 9, ]
# elements.reverse()
# print(elements)

# Задача2 дан список некоторых целых чисел,найдите значение 20 в нем
# если оно присутствует ,замените его на 200.
# обновите список только при первом вхождении

# 1-ый мой вариант
# list1 = [1, 3, 9, 6 ,20, 7, 10, 20]
# if 20 in list1:
#     print('yes')
# list1[4] = 200
# print(list1)

# 2-ой вариант правильный вариант
# list1 = [5 ,10,15,20,25,50,20]
#
# print('список:\n' , list1)
# ind = list1.index(20)
# list1[ind] = 200
# #
# print('измененный список: \n ' , list1)


# задача3 Список из 7 цифр.если четных цифр в нем больше
# чем нечетных,то найти сумму всех его цифр,если
# нечетных больше,то найти произведение 1 3 и 6 элемента

# numbers = [1, 3, 4, 5, 6, 7, 8, ]
# count = 0
# count_2 = 0
# for i in numbers:
#     if i % 2 == 0:
#         count += 1
#     else:
#         count_2 += 1
# print('четных:' , count, 'нечетных:', count_2)
# sum = 0
# pr = 1
# if count > count_2:
#     for i in numbers:
#         sum +=1
#     print('сумма:' , numbers)
# else:
#     pr = numbers[0] * numbers[2] * numbers[5]
#     print('произведение:', pr)

# задача4найти совпадающие элементы двух списков

# a = [5,[1,2],2,'r',4,'ee']
# b = [4, 'we', 'ee' ,3,[1,2]]
# c = []
#
# for i in a:
#     if i in b:
#         c.append(i)
# print(c)


# задача5 даны 2 списка:сложить их,удалить все текстове переменные,
# посчитать количество элементов списка

# a = [4,6,'py','tell',78]
# b = [44,'hello',56,'exept',3]
#
# a.extend(b)
# a.insert(3,6)
# print(a)
# for i in a:
#     if type(i) is str:
#         a.remove(i)
# a.sort()
# print(a)

# дом.задание.дан список. все числа проверить на четность. все слова посчитать на
# гласных и согласных

list = [15,48,'hello',6,9,'world']
l = 0
h = 0
d = 0

for i in list:
    if type(i) is int:
        if i % 2 ==0:
            i = str(i)
            for k in i:
                k = int(k)
                l += k
            print(i,'сумма цифр:', l, '\n')
        else:
            index = list.index(i)
            list[index] = 1
    elif type(i) is str:
        for r in i:
            if r in  'aeoiu':
                h += 1
            else:
                d += 1
        print(i,'количество гласных:',h)
        print('количество согласных:', d,'\n')
        h = 0
        d = 0
print(list)
