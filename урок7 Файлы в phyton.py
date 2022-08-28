# открытие файла

# метод open()

# fp = open('C:/xyz.txt' , 'r')

# f = open('example.txt' , 'r')
# print(*f)
# print(f)
# f.close()



# f = open('example.txt' , 'r')
# try:
#     print(*f)
# finally:
#     f.close()


# with open('example.txt' , 'r') as f:
#     print(*f)

# with open('example.txt' , 'w') as f:
#      print(*f)

# f = open('example.txt' , 'r')
# print(f.read(7))
# print(f.read(7))
# f.close()


# функция readline
# x = open('test.txt', 'r')
# print(x.readline())
# print(x.readline())
# x.close()
#
# x = open('test.txt', 'r')
# print(x.readlines())
# x.close()

# f = open('xyz.txt', 'w')
# f.write('Hello \nAndrei')
# f.close()

# Функция rename

# import os
# os.rename('xyz.txt' ,'abc.txt')

# import os
# print('Текущая директория:', os.getcwd(''))
# os.mkdir('folder') - создать папку (каталог)

# import os
# os.chdir('folder')
# print('Текущая директория изменилась на folder:', os.getcwd())


# import os
# os.chdir('folder')
# os.chdir( ' ..  ')
# os.makedirs('nested1/nested2/nested3')

# import os
# удаление файла
# os.remove('abc.txt')

# удаление папки
# import os
# os.chdir('nested1')
# os.chdir('nested2')
# os.rmdir('nested3')




