import random
n = int(input("Введіть кількість чисел: "))
dob_number = 0
sum_number = 0

def my_sum(num):
    sum = 0
    for i in range(len(str(num))):
        sum += (num % 10)
        num = num // 10
    return int(sum)

def my_dob(num):
    dob = 1
    for i in range(len(str(num))):
        dob = dob * (num % 10)
        num = num // 10
    return int(dob)

for i in range(n):
    num = random.randint(10, 1000)
    dob_number = my_dob(num)
    sum_number = my_sum(num)
    print("Сума цифр числа {0} : {1}".format(num, sum_number))
    print("Добуток цифр числа {0} : {1}".format(num, dob_number))

