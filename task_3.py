# 3.	Создать переменные a, b, c и присвоить им значения 9, 17 и 5 соответственно. Проверить выполнение следующих
# условий:
# a.	a больше b
# b.	a не равно разности b и c
# c.	b равно сумме a и c
# d.	c меньше или равно сумме a и b
# e.	a меньше b, но больше c
# f.	b больше a или b больше c

a = 9
b = 17
c = 5
print(a > b)
print(a != b + c)
print(b == a + c)
print(c <= a + b)
print(c < a < b)
print(b > a or b > c)
