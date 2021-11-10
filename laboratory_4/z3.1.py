import math
# Трикутник задається координатами своїх вершин на площині:A(x1,y1),B(x2,y2),C(x3,y3)
# Визначити, чи є цей трикутник прямокутним.
x1 = int(input('Перша координата А: '))
y1 = int(input('Друга координата А: '))
x2 = int(input('Перша координата B: '))
y2 = int(input('Друга координата B: '))
x3 = int(input('Перша координата С: '))
y3 = int(input('Друга координата С: '))

AB = (math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2)))
BC = (math.sqrt(((x3 - x2) ** 2) + ((y3 - y2) ** 2)))
AC = (math.sqrt(((x3 - x1) ** 2) + ((y3 - y1) ** 2)))

"""
a = b + c 
c = a + b
b = a + c
"""
if AB == math.sqrt((BC ** 2) + (AC ** 2)) or BC == math.sqrt((AB ** 2) + (AC ** 2)) or AC == math.sqrt((BC ** 2) + (AB ** 2)):
    print("Заданий трикутник є прямокутним")
else:
    print("Даний трикутник не є прямокутним")