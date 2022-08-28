# num_set = {1,2,3,4,5,6}
# print(num_set)

# string_set = {'Nicholas','Michelle','John','Mercy'}
# print(string_set)

# mixed_set = {2.0,'Nicholas',(1,2,3)}
# print(mixed_set)

# num_set = set([1,2,3,4,5,6])
# print(num_set)

# num_set = set([1, 2, 3, 4, 5,2,4, 6])
# print(num_set)

# x = {}
# print(type(x))

# x = set()
# print(type(x))

# months = set(['Jan','Feb','March','Apr', 'May','June','July',])
# for m in months:
#     print(m)

# months = set(['Jan','Feb','March','Apr', 'May','June','July',])
# print('May' in months)

# months = set(['Jan','Feb','March','Apr', 'May','June','July',])
# months.add('Oct')
# print(months)

# удаление множеств
# num_set = {1,2,3,4,5,6}
# num_set.discard(5)
# print(num_set)

# num_set = {1,2,3,4,5,6}
# num_set.remove(7)
# print(num_set)

# num_set = {'May','Aug', 'Oct'}
# num_set.pop()
# print(num_set)

# num_set = {1,2,3,4,5,6}
# num_set.clear()
# print(num_set)

# обьединение множеств

# x = set(['a','b','c'])
# y = set(['f', 'g','s'])
# r = x.union(y)
# print(r)

# x = {1,2,3}
# y = {4,5,6}
# z = {7,8,9}
# c = x.union(y,z)
# print(c)

# months = set(['Jan','Feb','March','Apr', 'May','June','July',])
# months2 = set(['Oct','Aug','Dec'])
# print(months|months2)

# x = {1,2,3}
# y = {4,5,6}
# z = {7,8,9}
# print(x|y|z)

# Пересечение множеств
# x = {1,2,3}
# y = {4,3,6}
# print(x & y )

# разница между между множествами
# a = {1,2,3}
# b = {4,3,6}
# print(a - b)
# print(b - a)

# методы множеств copy
# string = {'Nicholas', 'Michelle','John','Mercy'}
# x = string.copy()
# print(x)

# Метод isdisjoint
# string = {'Nicholas', 'Michelle','John','Mercy'}
# string2 = {'Jeff','Teddy'}
# x =string.isdisjoint(string2)
# print(x)

# метод len
# string = {'Nicholas', 'Michelle','John','Mercy'}
# print(len(string))

# метод frozenset

# my_set = frozenset([1,2,3,-10,40])
# print(type(my_set))


# задача1 Проверить ,есть ли в последовательности чисел дубликаты

# num_set = {1,2,3,4,5,6,3,1,}
# st = set(num_set)
# print(len(st) == len(num_set))

# задача3 создать множество.создать неизменяемое множество.
# выполнить операцию объединения созданных множеств.
# выполнить операцию пересечения созданных множеств

# st ={'it','is','set',1}
# frozen_st = frozenset({'it','is','frozen','set', 2})
# union = st | frozen_st
# intersection = st & frozen_st
# print(st)
# print(frozen_st)
# print(union)
# print(intersection)