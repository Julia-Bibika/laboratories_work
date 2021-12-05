"""
Телефонний довідник друзів. База даних телефонних номерів друзів: прізвище ім’я по-батькові, рік народження, номер стільникового телефону, номер мобільного телефону.
Організувати вибір за довільним запитом. Дані зберігаються в масиві записів, який створюється динамічно.
"""
a = [['Bazeluk_Lidia_Oleksandrivna', '06.09.2021', '+380950935318'],
     ['Brovdi_Vitaliy_Mihalovich', '04.04.2004', '+380957489716'],
     ['Dovganich_Igor_Olegovich', '01.02.2004', '+380958745543'],
     ['Yovbak_Nika_Igorivna', '07.02.2021', '+380631335294'],
     ['Mudrenyuk_Sofia_Evgenivna', '10.08.2004', '0664064124'],
     ['Telinger_Ergard-Mark_Zholtovich', '19.05.2004', '0994548474'],
     ['Bibika_Anastasiia_Ruslanivna', '04.04.2004', '+380992881612']]
with open('z3(txt).txt', 'w') as file:
    for i in range(len(a)):
        file.write(' '.join(a[i]) + '\n')
info = str(input('Введіть запит : '))

f = open('z3(txt).txt')
for line in f:
    line1 = line.split(sep=' ')
    if info in line1 or info + "\n" in line1:
        print(*line1[::])
f.close()
