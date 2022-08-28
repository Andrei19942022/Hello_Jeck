# задание1 в файле в одну строку запианы слова и числа через пробел или_найти сумму всех чисел

# with open('file_1.txt' ) as f:
#     s = f.readlines()
#     print(s)
# for i in s:
#     i= i.replace('_', ' ')
#     l = i.split(' ')
# print(l)
# sum = 0
# for i in l:
#     if i.isdigit():
#         i = int(i)
#         sum += i
# print(sum)

# задача3

# fname = input('файл: ')
# f = open(fname, 'w')
# while True:
#     s = input()
#     if s == '':
#         break
#     f.write(s +  '\n')
#     f.close()

# задача2
# f = open('file_2.txt')
# b = []
# n = []
# s = f.readlines()
# print(s)
# for i in s:
#     i = i[: -1]
#     if i.isalpha():
#         i = str(i)
#         b.append(i)
#     elif i.isdigit():
#         i = int(i)
#         n.append()
# print(b)
# print(n)
# n.sort()
# b.sort()
# mas = n + b
# print(mas)

# задача4
# f = open('task_4.txt')
# line = 0
# for i in f:
#     line += 1
#     print(i,len(i), 'симв.')
# print(line, 'стр.')
# f.close()