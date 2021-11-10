import random
# Дано: n є N, x , y є R^n .
# Побудувати вектор z , який містить спочатку додатні координати вектора x , а потім додатні координати вектора y.

"""
n - кількість координат
x - перший вектор (список с декількох координат)
y - другий вектор (список с декількох координат)
"""
n = int(input("Введіть кількість координат : "))
x = []
y = []
z = []

q = 0                                  # індекс елементу вектора  x
d = 0                                  # індекс елементу вектора  y
for i in range(n):
    num_x = random.randint(-10, 10)
    num_y = random.randint(-10, 10)
    x.append(num_x)
    y.append(num_y)
print("x = {0}".format(x))
print("y = {0}".format(y))
while q < len(x):
    if x[q] > 0:
        z.append(x[q])
    q += 1
while d < len(y):
    if y[d] > 0:
        z.append(y[d])
    d += 1
print("z = {0}".format(z))
