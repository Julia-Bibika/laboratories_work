"""
Дано типізований файл, який містить дійсні числа. Упорядкувати числа у файлі за зростанням.
"""
import random
n = int(input("Введіть кількість чисел: "))
a = [random.randint(-50, 50) for i in range(n)]
with open('z2text.txt', 'w') as file:
    file.write(' '.join(map(lambda el: str(el), a)))
with open('z2text.txt') as file:  # зчитування даних
    line = file.readline()
    numbers = list(map(lambda el: int(el), line.split(sep=' ')))
    print(numbers)
with open('z2text.txt', 'w') as file:
    numbers = sorted(numbers)
    print(numbers)
    file.write(' '.join(map(lambda el: str(el), numbers)))