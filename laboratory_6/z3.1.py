import math
"""
Ззнайти вектор
c=2(a +c)- b, де a,b,c є R^n
"""
# 0.Позначення
"""
num - номер елемента вектору а 
num_1 - номер елемента b
num_2 - номер елемента c
sum - сума всіх елментів вектору а
sum_1 - сума всіх елментів вектору b
sum_2 - сума всіх елментів вектору c
"""
n = int(input("Кількість елементів векторів: "))
a = []
b = []
c = []
sum = 0
sum_1 = 0
sum_2 = 0
for i in range(n):
    num = int(input('Вектору a number #{0} = '.format(i)))
    a.append(num)
for i in range(n):
    num_1 = int(input('Вектору b number #{0} = '.format(i)))
    b.append(num_1)
for i in range(n):
    num_2 = int(input('Вектору c number #{0} = '.format(i)))
    c.append(num_2)
for i in range(n):
    sum += (a[i]**2)
for i in range(n):
    sum_1 += (b[i]**2)

a_length = math.sqrt(sum)
b_length = math.sqrt(sum_1)
i = 0
for i in range(len(c)):
    num_3 = (2 * (a_length + c[i])) - b_length
    c.insert(i, num_3)
    c.pop(i-1)
print("Вектор c = {0}".format(c))
