import math
"""
Побудувати прямокутну матрицю А, елементи якої задаються формулою:
a_y = cos(i**2 / i! + n)
Обчислити суму елементів матриці А, сума індексів яких непарна.
"""
B = []
b = int(input("Введіть кількість рядків матриці : "))
c = int(input("Введіть кількість стовбців матриці : "))
n = int(input("Введіть число n: "))
i = 1
j = 1
sum_dot = 0
for i in range(b):
    B.append([math.cos((i ** 2) / (math.factorial(i) + n)) for j in range(c)])
print(B)
i = 0
for i in range(b):
    for j in range(c):
        if (i + j) % 2 != 0:
            sum_dot = sum_dot + B[i][j]
print("Сума додатних елементів матриці з непарною сумою індексів : {0:.2f}".format(sum_dot))