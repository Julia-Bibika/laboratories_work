# Побудувати масив Х=(xk), елементи якого задаються формулою:
# x1 = a , xk = (2-xk_1^2)/b (k = 2,3,...n)
# де a, b – вводяться з клавіатури. Знайти середнє арифметичне значення від’ємних елементів масиву Х.
"""
n - к-сть елементів - int
a - перше число - int
b - друге число - int
"""
n = int(input("Введіть кількість елементів : "))
a = int(input("Введіть число a: "))
b = int(input("Введіть число b: "))
x = []
x.append(a)
k = 1
d = 0
sum = 0
c = 0

for k in range(1, n):
    xk = (2 - (x[k - 1] ** 2)) / b
    x.append(xk)
print("x = {0}".format(x))
for d in range(n):
    if x[d] < 0:
        sum += x[d]
        c += 1
average = sum / c
print("Середнє арифметичне списку x = {0:.2f}".format(average))
