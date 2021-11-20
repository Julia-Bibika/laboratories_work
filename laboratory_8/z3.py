import math
"""
Нехай x_0 = x_1 = 1 x_i = sinx_i-1 + (x_i-2/ cos(x_i-1)). Визначити x_n.
"""
def create_x(i):
    if i == 0 or i == 1:
        return 1
    else:
        x_i = math.sin(create_x(i-1)) + (create_x(i-2)/math.cos(create_x(i-1)))
        return float(x_i)
i = int(input("Введіть номер елемента: "))
res = create_x(i)
print("{0}".format(res))

