# class Car:
#     pass
# car_object = Car()
# print(dir(Car))

# список атрибутов можно получить с помощью команды dir
# class Car:
#     color = 'grey'
#     def turn_on(self):
#         pass
#     def ride(self):
#         pass
# car_object = Car()
# print(dir(Car))

# class Car:
#     default_color = 'Grey'
#     default_weight = 5000
#
#     def __init__(self,color,model):
#         self.color = color
#         self.model = model
#
#     def turn_on(self):
#         pass

# задача1
# class TheExample:
#     a = 2
#     b = 3
#     def __init__(self,t,r):
#         self.t = t
#         self.r = r
#
#     def func(self):
#         self.c = 5
#         print(self.c)
#
#     def func1(self):
#         return self.a + self.b
#
#     def func2(self):
#         return self.t ** self.r
#
# example = TheExample(4,2)
# print(example.a)
# print(example.func1())
# print(example.func2())
# example.func()

# задача2
# калькулятор. создайте класс где реализованы функции(методы)математических операцийй.
# а также функция для ввод данных.

# class TheExample:
#     def __init__(self):
#         self.func4()
#
#     def func(self):
#         return self.a + self.b
#     def func1(self):
#          return self.a - self.b
#     def func2(self):
#         return self.a * self.b
#     def func3(self):
#         if self.b == 0:
#             return 'error'
#         else:
#             return self.a / self.b
#     def func4(self):
#         self.a = int(input())
#         self.b = int(input())
#
# while True:
#     print('+,-,/,*')
#     x = input()
#     print('numbers: ')
#     example = TheExample()
#     if x =='6':
#         break
#     if x == '+':
#         print(example.func())
#     if x == '-':
#          print(example.func1())
#     if x == '*':
#         print(example.func2())
#     if x == '/':
#         print(example.func3())



