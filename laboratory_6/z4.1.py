"""
Перетворити масив таким чином, щоб спочатку розміщувались всі елементи,
ціла частина яких лежить в інтервалі [a,b] , а потім всі інші.
"""
n = int(input("Введіть кількість елементів x: "))
a = float(input("Введіть початок інтервалу : "))
b = float(input("Введіть кінець інтервалу : "))
x = []
for i in range(n):
    num = float(input('number #{0} = '.format(i)))
    x.append(num)
print("x = {0}".format(x))
i = 0
for i in range(len(x)):
    if a <= x[i] <= b:
        x.insert(0, x[i])
        x.pop(i+1)
print("x = {0}".format(x))
