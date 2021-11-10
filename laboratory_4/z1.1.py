import math
# Обчислити площу трикутника, якщо трикутник задано довжинами сторін.
"""
Перша сторона - float - first_side
Друга сторона - float - second_side
Третя сторона - float - third_side
"""
# 1.Введення даних
first_side = float(input("Введіть першу сторону : "))
second_side = float(input("Введіть другу сторону : "))
third_side = float(input("Введіть третю сторону : "))
# 2. Обчислення даних
p = (first_side + second_side + third_side) / 2
square = (math.sqrt(p * (p - first_side)*(p - second_side)*(p - third_side)))
print("Площа заданого трикутника дорівнює {0:.1f}".format(square))