"""
Дано текстовий файл, який містить парну кількість цілих чисел. Визначити суму елементів з парними номерами.
"""
import random
sum = 0
n = int(input("Введіть парну кількість чисел: "))
a = [random.randint(1, 100) for i in range(n)]
with open('z1text.txt', 'w') as file:
    file.write(' '.join(map(lambda el: str(el), a))) # запис даних
with open('z1text.txt') as file:  # зчитування даних
    line = file.readline()
    numbers = list(map(lambda el: int(el), line.split(sep=' ')))
    for i in range(len(numbers)):
        if i % 2 == 0:
            sum += numbers[i]
    print(sum)
    print(numbers)