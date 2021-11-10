"""
Нехай x_0 = 2 , x_1 = x_2 = 3, x_i = 7x_i_1 - x_i_2 * x_i_3  . Визначити x_n.
"""
x_0 = 2
x_1 = 3
x_2 = 3
i = int(input("Введіть номер елемента : "))
if i == 1:
    print(x_0)
elif i <= 3:
    print(3)
else:
    for j in range(4, i + 1):
        x_n = (7 * x_2) - (x_1 * x_0)
        x_0 = x_1
        x_1 = x_2
        x_2 = x_n
        print("x_n = {0}".format(x_n))
