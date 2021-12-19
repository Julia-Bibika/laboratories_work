# import random
# """
# Об’єкт “Камери схову” (представити за допомогою одновимірного масиву комірок, як членів-класів, які містять на (зайнята чи вільна логічного типу та масиву відомостей про багаж) (використати члени-класи)
# поля:
# кількість комірок для зберігання багажу;
# одновимірний масив комірок, як членів-класів, які містять такі поля:
# для визначення того чи зайнята комірка;
# кількість одиниць багажу;
# одновимірний масив, який містить інформацію про багаж як член-клас (дата отримання багажу, вага, термін зберігання, ідентифікаційний номер власника);
# методи:
# виведення на екран кількості вільних та зайнятих комірок;
# визначення кількості вільних комірок через вказану кількість днів (за умови, що новий багаж надходити не буде);
# заповнення та звільнення комірок;
# визначення загальної ваги вантажу;
# визначення ваги вантажу, який належить власнику, ідентифікаційний номер якого надається.
# """
# class Chambers:
#     def __init__(self, k_cells, cells):
#         self.k_cells = k_cells
#         self.cells = cells
# class TakenPlace:
#     def __init__(self,check_cells, take=0, k_chambers=0,):
#         self.take = take
#         self.k_chambers = k_chambers
#         self.__check_cells = check_cells
#     def take_or_not(self,key):    # перевірка чи зайнято
#         if self.__check_cells[key] == 0:      #помилка
#             self.take = "Комірка {0} вільна".format(key)
#             return self.take
#         else:
#             self.take = "Комірка {0} зайнята".format(key)
#             return self.take
# class InfoChambers:
#     def __init__(self, date_get, weight, time_save, id_owner,size):
#         self.date_get = date_get
#         self.weight = weight
#         self.time_save = time_save
#         self.id_owner = id_owner
#         self.size = size
#         self.__check_cells = []
#     def append(self):   # створення списку
#         for i in range(self.size):
#             self.__check_cells.append(random.randint(0, 1))
#         return self.__check_cells
#     def check(self, size):   # кількість зайнятих і вільних
#         k = 0
#         g = 0
#         for i in range(size):
#             if self.__check_cells[i] == 0:
#                 k += 1
#             else:
#                 g += 1
#         return "Кількість вільних комірок {0},кількість зайнятих комірок {1}".format(k, g)
#
#
# from datetime import datetime as dt
# from datetime import timedelta
# import functools
#
#
# class Luggage:
#     _date = None
#     _owner = -1
#     _weight = 0.00
#     _duration = 0
#
#     def __init__(self, date, owner, weight, duration):
#         self._date = date
#         self._owner = owner
#         self._weight = weight
#         self._duration = duration
#
#     def getDate(self):
#         return self._date
#
#     def getOwner(self):
#         return self._owner
#
#     def getWeight(self):
#         return self._weight
#
#     def getDuration(self):
#         return self._duration
from datetime import timedelta
import functools
from datetime import date

class Luggage:
    _date = None
    _owner = -1
    _weight = 0.00
    _duration = 0

    def __init__(self, date, owner, weight, duration):
        self._date = date
        self._owner = owner
        self._weight = weight
        self._duration = duration

    def getDate(self):
        return self._date

    def getOwner(self):
        return self._owner

    def getWeight(self):
        return self._weight

    def getDuration(self):
        return self._duration


class Cell:
    _isfull = False
    _luggage = None

    def __init__(self):
        pass

    def appendLuggage(self, luggage):
        if not self._isfull:
            self._luggage = luggage
            self._isfull = True
            return True
        else:
            return False

    def isEmpty(self):
        return not self._isfull

    def getLuggage(self):
        return self._luggage

    def removeLuggage(self):
        self._luggage = None
        self._isfull = False


class Chamber:
    _cells = []

    def __init__(self, number_of_cells):
        for cell in range(0, number_of_cells - 1):
            self._cells.append(Cell())

    def _getFirstEmptyCell(self):
        for cell in self._cells:
            if cell.isEmpty():
                return cell
        return None

    def appendLuggage(self, luggage):
        cell = self._getFirstEmptyCell()
        if cell is not None:
            cell.appendLuggage(luggage)
        else:
            return False

    def removeLuggageFromCell(self, index):
        self._cells[index].removeLuggage()

    def getFreeCells(self):
        return list(filter(lambda cell: cell.isEmpty(), self._cells))

    def getFullCells(self):
        return list(filter(lambda cell: not cell.isEmpty(), self._cells))

    def getFreeCellsCount(self):
        return len(self.getFreeCells())

    def getFullCellsCount(self):
        return len(self.getFullCells())

    def getWeight(self, owner=None):
        if owner is None:
            cells = self.getFullCells()
        else:
            cells = list(filter(lambda cell: cell.getLuggage().getOwner() == owner, self.getFullCells()))
        return functools.reduce(lambda total, cell: total + cell.getLuggage().getWeight(), cells, 0)

    def forecastFreeCells(self, after_days):
        date_after = date.today() + timedelta(days=after_days)
        emptyAfter = list(filter(
            lambda cell: date_after > cell.getLuggage().getDate() + timedelta(days=cell.getLuggage().getDuration()),
            self.getFullCells()))
        return self.getFreeCells() + emptyAfter


ch = Chamber(10)

ch.appendLuggage(Luggage(date.today(), 1, 10, 2))
ch.appendLuggage(Luggage(date.today(), 2, 10, 2))
ch.appendLuggage(Luggage(date.today(), 3, 10, 3))
ch.appendLuggage(Luggage(date.today(), 1, 10, 4))
ch.appendLuggage(Luggage(date.today(), 2, 10, 5))

print(ch.getFullCellsCount())
print(ch.getFreeCellsCount())
print(ch.getWeight())
print(ch.getWeight(1))
print(len(ch.forecastFreeCells(2)))
print(len(ch.forecastFreeCells(3)))
print(len(ch.forecastFreeCells(4)))
