# i = 0
# while i < 10:
#     print (i)
#     i = i + 1

# i = 0
# while i < 10:
#     print(i)
#
#     if i == 5:
#         break
#
#     i += 1

# i = 1
# result = 0
# while i <=  50:
#     result += i
#     i += 1
#     print(result)

# i = 1
#
# while i <= 10:
#     print(i ** 2)
#
#     i += 1

# i = 15
# while i != 0:
#     print(i)
#     i -= 1

# a = int(input('введите число :'))
# b = int(input ('введите второе число :'))
#
# while a < b:
#     a += 1
#     if a  == 0:
#
#         break
#
#     print(a)



# Условие  ELSE  в цикле  FOR
# for i in range(3):
#     print(i)
#
# else:
#     print('готово')

# Условие ELSE в цикле WHILE

# i = 0
# while i < 3:
#     print(i)
#     i += 1
# else:
#     print('готово')

# for i in range(6):
#     print(i)
#     if i == 4:
#         break
# else:
#     print('готово')

# a = 0
# mas = []
# while a < 98:
#     a += 7
#     mas.append(a)
# print(mas, 'Длина: ' , len(mas))


# a = 0
# mas1 = []
# while a < 125:
#     a += 5
#     mas1.append(a)
# print(mas1 , 'Длина массива:', len(mas1))

# Сделать колькулятор
# print('Ноль в качестве знака операции завершит работу программы')
# x = float(input('x='))
# y = float(input('y='))
# while True:
#     s = input('Знак (+ , - , * , /) :')
#     if s == '0':
#         break
#     elif s == '+':
#         print(x + y)
#     elif s == '-':
#         print(x - y)
#     elif s == '*':
#         print(x * y)
#     elif s =='/':
#         if y != 0:
#          print(x / y)
#         else:
#             print('Нельзя делть на ноль!')

# задача..Казино. Компьютер генерирует числа от 1 до 10 и от 1 до 2-х соответственно. Цифры от одного до 10 отвечают за номера, а от 1 до 2 за цвета(1-красный,2 черный).
# Пользователю дается 5 попыток угадать номер и цвет(Прим. введения с клавиатуры: 3 красный).В случае неудачи вывести на экран правильную
# import random
# num = random.randint(1,10)
# col = random.randint(1,2)
# print(num)
# print(col)
# i = 0
# while i <5:
#     i += 1
#     guess = int(input('ваше число:'))
#     color = (int(input('введите цвет: 1-красный или 2-черный:')))
#     if guess > num:
#         print('число меньше твоего.')
#         if color == col:
#             print('но! вы угадали цвет')
#         else:
#             print('вы не угадали цвет')
#     elif guess < num:
#         print('число больше твоего.')
#         if color == col:
#             print('но! вы угадали цвет.')
#         else:
#             print(' вы не угадали цвет.')
#     elif guess == num and col != color:
#         print('вы не угадали цвет,но угадали число!')
#     elif guess == num and col == color:
#         print(' поздравляю!' , num,col)
#         break
#
#     if i< 5:
#         print('попробуй снова')
#     else:
#         print('это было число', num, col, 'game over!')