"""
Ущільнити задану матрицю, вилучаючи із неї рядки і стовпці, заповнені нулями.
"""
B = []
b = int(input("Введіть кількість рядків матриці : "))
c = int(input("Введіть кількість стовбців матриці : "))
sum_1 = 0
sum_2 = 0
for i in range(b):
    B.append([int(input("Введіть number#{0}{1}: ".format(i, j))) for j in range(c)])
print(B)
i = 0
j = 0
for i in range(b):
    for j in range(c):
        sum_1 = sum_1 + B[i][j]
        if sum_1 == 0:
            B.pop(i)
    break
print(B)
