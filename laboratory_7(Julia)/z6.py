"""
Знайти номер першого із рядків, який містить хоча б один додатний елемент.
"""
import random
A = []
b = int(input("Введіть кількість рядків матриці : "))
c = int(input("Введіть кількість стовбців матриці : "))
k = 0
for i in range(b):
    A.append([random.randint(-10, 2) for j in range(c)])
print(A)

for i in range(b):
    for j in range(c):
        if A[i][j] >= 0 and k == 0:
            print(A[i])
            k += 1
            if k > 0:
                break
