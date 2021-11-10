import math
"""
Якщо x < n , то y = ln(x) - n
Якщо x = n , то y = ln(x) - n
Якщо x > n , то y = cos (n*x)
"""
x = int(input("Введіть перше значення : "))
n = int(input("Введіть друге значення : "))

if x < n or x == n:
    y = math.log1p(x) - n
    print("y = {0:.1f}".format(y))
else:
    y = math.cos(n * x)
    print("y = {0:.1f}".format(y))