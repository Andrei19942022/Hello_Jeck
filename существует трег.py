print("СТОРОНЫ ТРЕУГОЛЬНИКА")
a  = float(input("a = "))
b  = float(input("b = "))
c  = float(input("c = "))
if a + b > c and b + c >  a and c + a > b:
    print("треугольник существует")
else:
    print("треугольник не существует")
