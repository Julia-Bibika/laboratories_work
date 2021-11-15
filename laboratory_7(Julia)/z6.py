"""
Знайти номер першого із рядків, який містить хоча б один додатний елемент.
"""
import random
A = []
b = int(input("Введіть кількість рядків матриці : "))
c = int(input("Введіть кількість стовбців матриці : "))

for i in range(b):
    A.append([random.randint(-10, 2) for j in range(c)])
print(A)
i = 0
j = 0

for i in range(b):
    for j in range(c):
        if A[i][j] > 0:
            print(A[i])
    break
