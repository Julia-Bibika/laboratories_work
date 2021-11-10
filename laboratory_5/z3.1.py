import math
"""
Перевірити справедливість рівності при заданій точності Е:
sinx/x = [1 - x^2/3! + x^4/5!  - x^6/7! +....]
"""
# 0.Позначення
"""
S - сума
z - знак
a - x^2
b - факторіал
identity(тотожність) - sinx/x
"""
x = int(input("Введіть число від -1 до 1 : "))
eps = float(input('Введіть задану точність: '))
S = 1
z = -1
a = x**2
b = 3
identity = math.sin(x) / x
while True:
    S += z * (a / math.factorial(b))
    z *= z
    a = a**2
    b += 2
    print("S = {0}".format(S))
    if math.fabs(S) > eps:
        print("Справедливість є правильною")
    else:
        break