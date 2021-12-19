"""
Об’єкт “Черга” (реалізація стеку за допомогою одновимірного масиву цілих чисел)
поля:
для зберігання номерів першого та останнього елементів черги;
масив елементів;
методи:
виведення на екран;
додавання нового елементу;
видалення елементу;
знаходження суми елементів.
"""


class Turn:
    def __init__(self,  elements, first_and_last=0):
        self.first_and_last = first_and_last
        self.__elements = elements

    @property
    def get_elements(self):  # getter for elements
        return self.__elements

    def set_elements(self, val):  # setter for element
        for i in range(len(self.__elements)):
            if type(val) != int:
                raise Exception('Element should be integer type')
            self.__elements.append(val)

    def pop(self, key):     # видалення елементу
        self.__elements.pop(key)
        return self

    def append(self, value):        # додавання елементу в список
        if type(value) != int:
            raise Exception('Element should be integer type')
        self.__elements.append(value)
        return self

    def sum_elements(self):       # сума всіх елементів масиву
        return sum(self.__elements)

    def first_last(self):       # знаходження першого і останнього елементу
        return self.__elements[0], self.__elements[-1]

    def __str__(self):
        return str(self.__elements)


s1 = Turn([5, 4, 7, 6])
print(s1)
print(s1.sum_elements())
print(s1.first_last())
print(s1.append(2))
print(s1.pop(0))
