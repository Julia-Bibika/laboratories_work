"""
Ззнайти вектор
c=2(a +c)- b, де a,b,c є R^n
"""
# 0.Позначення
"""
num - номер елемента вектору а 
num_1 - номер елемента b
num_2 - номер елемента c
"""
n = int(input("Кількість елементів векторів: "))
a = []
b = []
c = []
for i in range(n):
    num = int(input('Вектору a number #{0} = '.format(i)))
    a.append(num)
for i in range(n):
    num_1 = int(input('Вектору b number #{0} = '.format(i)))
    b.append(num_1)
for i in range(n):
    num_2 = int(input('Вектору c number #{0} = '.format(i)))
    c.append(num_2)
i = 0
for i in range(len(c)):
    num_3 = (2 * (a[i] + c[i])) - b[i]
    c.insert(i, num_3)
    c.pop(i-2)
print("Вектор c = {0}".format(c))
