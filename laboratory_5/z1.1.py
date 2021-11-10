import math
"""
Обчислити значення виразу (1 + cos(0.1))(2 + cos(0.2))*....*(9 + cos(0.9)).
"""
dob = 1
a = 1
b = 0.1
for i in range(1, 10):
    num = (a + math.cos(b))
    a += 1
    b += 0.1
    dob *= num
print("dob = {0:.2f}".format(dob))
