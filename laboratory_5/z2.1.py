"""
Дано n є N. Побудувати алгоритм для визначення того, чи утворюють цифри зростаючу послідовність.
"""
"""
n - int - кількість елементів
"""
n = int(input("Введіть кількість елементів : "))
num_1 = 0
for i in range(n):
    num = float(input("number #{0} :".format(i)))
    if num > num_1:
        num_1 = num
        print("Послідовність зростає")
    else:
        break