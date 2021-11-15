from random import randint

i = int(input('Рядки: '))
j = int(input('Стовпці: '))
k = 0
m = [[randint(-10, 10) for x in range(j)] for y in range(i)]
print(m)

for x in range(i):
    for y in range(j):
        if x < y:
            if m[x][y] > 0:
                print(m[x][y])
                k += 1
print("Кількість додатних елементів матриці вище головної діагоналі : {0}".format(k))
# Визначити кількість додатних елементів матриці вище головної діагоналі.

