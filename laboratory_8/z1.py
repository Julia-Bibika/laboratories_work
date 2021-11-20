"""
Дано три дійсних числа: a, b ,c. Використовуючи підпрограми для знаходження максимальнго та мінімального
серед двох дійсних чисел знайти max(a,b) + ((max(a,b) + min(b,c))**2.
"""
def my_max(a, b):
    if a > b:
        return a
    else:
        return b


def my_min(b, c):
    if c < b:
        return c
    else:
        return b

a = int(input("Введіть перше число : "))
b = int(input("Введіть друге число : "))
c = int(input("Введіть третє число : "))

res = my_max(a, b) + ((my_max(a, b) + my_min(b, c)) ** 2)
print(res)
