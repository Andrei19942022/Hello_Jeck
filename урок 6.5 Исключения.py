# Исключения - тип данных ,необходимый для того,чтобы сообщить программисту об ошибках
#
# Пример исключения - деление на ноль

# a = 100 / 0
# print(a)

# Исключения

# BaseException - базовое исключение от которого берут начало все остальные
# SystemExit - исключение порождаемое функцией sys.exit при выходе из программы
# KeyboardInterrupt - порождается при прерывании программы пользователем
# Exception - то,на чем фактически строятся все остальные ошибки
# StopIteration - порождается встроеной функцией  next,если в итераторе больше нет элементов
# ArithmeticError - арифметические ошибки
# FloatingPointError -  порождается при неудачном выполнении операции с плавающей запятой
# OverflowError - возникает,когда результат арифметической операции слишком велик для предстовления
# ZeroDivisionError - деление на ноль


# Конструкция  try - except
# try:
#  k = 1 / 0
# except ZeroDivisionError:
#  k = 0
# print(k)

# в блоке try мы перехватываем инструкцию,которая может породить исключение, а в блоке except мы перехватываем их.
# try:
#  k = 1 / 0
# except ArithmeticError:
#  k = 0
#  print(k)

# my_dict = {'a':1,'b':2,'c':3}
# try:
#     value = my_dict['d']
# except KeyError:
#     print('ключа не существует')



# my_dict = {'a':1,'b':2,'c':3}
# try:
#     value = my_dict['d']
# except IndexError:
#     print('такого индекса не существует!')
# except KeyError:
#     print('этого ключа нет в словаре!')
# except:
#     print('произошла другая ошибка')

# второй способ выявление нескольких исключений
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# try:
#     value = my_dict['d']
# except (IndexError, KeyError):
#     print('произошла ошибка IndexError или KeyError!')

# Оператор finally
# my_dict = {'a':1,'b':2,'c':3}
# try:
#     value = my_dict['d']
# except KeyError:
#     print('Произошла ошибка KeyError!')
# finally:
#     print('Оператор finally выполнен!')

# except или else

# my_dict = {'a':1,'b':2,'c':3}
# try:
#     value = my_dict['a']
# except KeyError:
#     print('произошла ошибка KeyError!')
# else:
#     print('ошибок не произошло!')

# except или else и оператор finally

# my_dict = {'a':1,'b':2,'c':3}
# try:
#     value = my_dict['a']
# except KeyError:
#     print('произошла ошибка KeyError!')
# else:
#     print('ошибок не произошло!')
# finally:
#     print('оператор finally выполнен!')

# задача3 Введите 2 числа с клавиатуры. поделите одно на другое.
# Обработайте ошибку деление на нольесли ошибок нет,то результат деления возвести в квадрат.
# Также используйте оператор finally

# try:
#     a = int(input('Введите первое число:'))
#     b = int(input('Введите второе число:'))
#     result = int(a) / int(b)
# except ZeroDivisionError:
#     print('что-то пошло не так....')
# else:
#      print('результат в квадрате: ', result **2)
# finally:
#      print('Конец.')

# Задача4 Введите два числа с клавиатуры. Поделите одно на другое.
# Обработайте деление на ноль,преобразование и общее исключение.

# try:
#     a  = int(input('Введите первое число: '))
#     b = int(input('Введите второе число: '))
#     print('Результат деления: ' , int(a) / int(b))
# except ValueError:
#     print('Преобразование прошло неудачно')
# except ZeroDivisionError:
#     print('Попытка деление на ноль')
# except Exception:
#     print('Общее исключение')


