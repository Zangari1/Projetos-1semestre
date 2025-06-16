import math
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

#math.pow(b,2) === b**2
delta = math.sqrt ( math.fabs( math.pow(b,2)-4*a*c))

x1 = (-b + delta)/(2*a)
x2 = (-b - delta)/(2*a)
print("valor de delta = ", delta)
print("raizes: x1 = ", x1, " x2 = ", x2)