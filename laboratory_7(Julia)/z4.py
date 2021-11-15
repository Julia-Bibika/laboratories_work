"""
Циклічно зсунути парні стовпці матриці зліва направо на k позицій. слідування.
"""
import random
# Циклічно зсунути парні стовпці матриці зліва направо на k позицій. слідування.
A = []
s = []
b = int(input("Введіть кількість рядків матриці : "))
c = int(input("Введіть кількість стовбців матриці : "))
k = int(input("Зсунути на скільки позицій: "))

for i in range(b):
    A.append([random.randint(-10, 10) for j in range(c)])
print(A)
j = 1
for j in range(b):
    for i in range(c - 1):
        s += A[i]
        s = s[-k:] + s[:-k]
        A.insert(i, s)
        A.pop(i + 1)
        s = []
print(A)
# for j in range(b):
#     for i in range(c - 1):
#         s += A[i]
#         s = s[-k:] + s[:-k]
#         A.insert(i, s)
#         A.pop(i + 1)
#         s = []