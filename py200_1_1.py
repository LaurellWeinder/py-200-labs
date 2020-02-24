# -*- coding: utf-8

# 
# Курс DEV-PY200. Объектно-ориентированное программирование на языке Python
# Тема 1.1 Основы ООП. Понятие класса, объекта. Создание экземпляра класса

# Лабораторная работа № 1.1 (4 ак.ч.)

# Слушатель (ФИО): Данилова А.Ю.

# ---------------------------------------------------------------------------------------------
# Понятие класса, объекта (стр. 1-22)

# 1. Создайте класс Glass с атрибутами capacity_volume и occupied_volume
#    Обязательно проверяйте типы (TypeError) и значения переменных (ValueError)

class Glass:
    def __init__(self, capacity_volume, occupied_volume):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError
        if capacity_volume < 0:
            raise ValueError
        self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError
        if occupied_volume < 0 or occupied_volume > capacity_volume:
            raise ValueError
        self.occupied_volume = occupied_volume


# 2. Создайте два и более объектов типа Glass
#    Измените и добавьте в любой стакан любое кол-во воды (через атрибуты)
#    Убедитесь, что у других объектов Glass атрибуты экземпляра класса не изменились.

g1 = Glass(400, 0)
g2 = Glass(200, 0)


# print(g1.__dict__)
# print(g2.__dict__)
# g1.occupied_volume = 200
# g2.capacity_volume = 300
# print(g1.__dict__)
# print(g2.__dict__)


# 3. Создайте класс GlassDefaultArg (нужен только __init__) c аргументом occupied_volume
#    По умолчанию occupied_volume равен нулю. Создайте два объекта с 0 и 200
#    Обязательно проверяйте типы (TypeError) и значения переменных (ValueError)

class GlassDefaultArg:
    def __init__(self, capacity_volume, occupied_volume=0):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError
        if capacity_volume < 0:
            raise ValueError
        self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError
        if occupied_volume < 0 or occupied_volume > capacity_volume:
            raise ValueError
        self.occupied_volume = occupied_volume


g3 = GlassDefaultArg(200)
g4 = GlassDefaultArg(400, 200)


# print(g3.__dict__, g4.__dict__)


# 4. Создайте класс GlassDefaultListArg (нужен только __init__) 
#    c аргументами capacity_volume, occupied_volume.
#    Пусть аргументом по умолчанию для __init__ occupied_volume = []. Будет список.
#    Попробуйте создать 3 объекта, которые изменяют occupied_volume.append(2) внутри __init__.
#    Создавайте объект GlassDefaultListArg только с одним аргументом capacity_volume.
#    Опишите результат.
#    Подсказка: можно ли использовать для аргументов по умолчанию изменяемые типы?


class GlassDefaultListArg:
    def __init__(self, capacity_volume, occupied_volume=[]):
        self.occupied_volume = occupied_volume
        self.occupied_volume.append(2)


# print(self.occupied_volume)


# В один и тот же лист добавляются двойки. Не надо так делать.
g5 = GlassDefaultListArg(200)
g6 = GlassDefaultListArg(500)
g7 = GlassDefaultListArg(300)


# print(g7.occupied_volume)


# 5. Создайте класс GlassAddRemove, добавьте методы add_water, remove_water
#    Обязательно проверяйте типы (TypeError) и значения переменных (ValueError)
#    Вызовите методы add_water и remove.
#    Убедитесь, что методы правильно изменяют атрибут occupied_volume.

class GlassAddRemove:
    def __init__(self, capacity_volume, occupied_volume):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError
        if capacity_volume < 0:
            raise ValueError
        self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError
        if occupied_volume < 0 or occupied_volume > capacity_volume:
            raise ValueError
        self.occupied_volume = occupied_volume

    def add_water(self, water):
        if water <= (self.capacity_volume - self.occupied_volume):
            self.occupied_volume += water
        else:
            self.occupied_volume = self.capacity_volume
            remaining_water = water - (self.capacity_volume - self.occupied_volume)
            return f'Вода, которая не влезла в стакан - {remaining_water}'

    def remove_water(self, water):
        if water <= self.occupied_volume:
            self.occupied_volume -= water
        else:
            raise ValueError('Не хватает воды!')


g8 = GlassAddRemove(400, 400)
# print(g8.add_water(100))
# print(g8.occupied_volume)

# 6. Создайте три объекта типа GlassAddRemove, 
#    вызовите функцию dir для трёх объектов и для класса GlassAddRemove.
#    а. Получите типы объектов и класса
#    б. Проверьте тип созданного объекта.

g9 = GlassAddRemove(200, 0)
g10 = GlassAddRemove(300, 300)
g11 = GlassAddRemove(100, 100)


# print(dir(g9))
# print(type(g9), isinstance(g9, GlassAddRemove))
# print(dir(g10))
# print(dir(g11))
# print(dir(GlassAddRemove))
# print(type(GlassAddRemove), isinstance(GlassAddRemove, GlassAddRemove)) # Интересненько.

# ---------------------------------------------------------------------------------------------
# Внутренние объекты класса (стр. 25-33)

# 7. Получите список атрибутов экземпляра класса в начале метода __init__, 
#    в середине __init__ и в конце __init__, (стр. 28-30)
#    а также после создания объекта.
#    Опишите результат.

class OneMoreGlass:
    def __init__(self, capacity_volume, occupied_volume):
        print(self.__dict__)  # Пользовательских атрибутов нет
        self.capacity_volume = capacity_volume
        print(self.__dict__)  # Появился capacity volume
        self.occupied_volume = occupied_volume
        print(self.__dict__)  # Оба атрибута созданы


glass = OneMoreGlass(200, 0)

# 8. Создайте три объекта Glass. (стр. 27)
#    Получите id для каждого объекта с соответсвующим id переменной self.

glass1 = Glass(200, 0)
glass2 = Glass(400, 400)
glass3 = Glass(200, 100)
print(hex(id(glass1)))


# 9. Корректно ли следующее объявление класса с точки зрения:
#     - интерпретатора Python;
#     - соглашения о стиле кодирования
#    Запустите код.

class d:  # Не PEP8. С точки зрения интерпретатора, все ОК
    def __init__(f, a=2):  # первый параметр метода должен быть self.
        f.a = a

    def print_me(p):  # как и тут
        print(p.a)


d.print_me(d())


# 10. Исправьте
class A:
    def __init__(self, a):
        if 10 < a < 50:  # return не должен быть в init
            self.a = a;  # А это нехорошо с точки зрения PEP8, но почему нет.


# Объясните так реализовывать __init__ нельзя?


# 11. Циклическая зависимость (стр. 39-44)
#
from weakref import ref


# Я поначалу пыталась сделать так, как было в образце и так, как мы разбирали на лекции, но
# если честно, это только больше запутало меня. Поэтому я написала по-своему. Надеюсь, ничего страшного.

class LinkedList:
    class Node:
        def __init__(self, data, prev_node=None, next_node=None):
            self.next_node = next_node
            self.prev_node = prev_node
            self.data = data

        def __str__(self):
            return f'{self.data}'

        def __repr__(self):
            return f'{self.data}'

    def __init__(self):
        self.size = 0
        self.head = None

    def insert_in_the_beginning(self, data):  # Я решила отказаться от хвоста. Просто поняла,
        if self.head is None:                 # что от него нет никакого толка, кроме вставки в конец.
            self.head = self.Node(data)       # Два вида вставки: перед головой и после определенной ноды.
        else:
            new_node = self.Node(data)
            new_node.next_node = self.head
            new_node.prev_node = None
            new_node.next_node.prev_node = new_node
            self.head = new_node
        self.size += 1

    def append_to_the_end(self, data):  # Добавляем ноду в конец, проходясь циклом по всем
        new_node = self.Node(data)
        last = self.head
        if self.size == 0:
            self.head = new_node
        else:
            while last.next_node is not None:
                last = last.next_node
            last.next_node = new_node
            new_node.prev_node = last
            new_node.prev_node.next_node = new_node
        self.size += 1

    def insert_after_node(self, node, data):
        if self.head is None:
            raise ValueError('List in empty')
        current_node = self.head
        while current_node is not None:
            if current_node.data == node:
                break
            current_node = current_node.next_node
        if current_node is None:
            raise ValueError('Item not in the list')
        else:
            new_node = self.Node(data)
            new_node.prev_node = current_node
            current_node.next_node = new_node
            new_node.next_node = current_node.next_node.next_node
            if current_node.next_node is not None:
                current_node.next_node.prev_node = new_node
            current_node.next_node = new_node
        self.size += 1

    def find_node(self, node):  # Находит индекс ноды по значению.
        if self.head is None:
            raise ValueError('List in empty')
        current_node = self.head
        index = 0
        while current_node is not None:
            if current_node.data == node:
                break
            current_node = current_node.next_node
            index += 1
        if current_node is None:
            raise ValueError('Item not in the list')
        return index

    def find_by_index(self, index):  # Находит ноду по индексу.
        if 0 > index > self.size - 1:
            raise IndexError('Index out of range')
        current_node = self.head
        for i in range(index):
            current_node = current_node.next_node
        return current_node

    def remove_node(self, node):  # Удаляет ноду по индексу.
        index = self.find_node(node)
        remo_node = self.find_by_index(index)
        # remo_node = self.head
        # while remo_node.data != node:           # Можно сделать и так, тогда по циклу можно пройтись всего 1 раз.
        # 	remo_node = remo_node.next_node
        p = remo_node.prev
        n = remo_node.next
        d = remo_node.data
        if p is not None:
            p.next = n
        else:
            self.head = n
        if n is not None:
            n.prev = p
        else:
            self.head = n
        self.size -= 1
        return d

    def print_list(self):
        if self.size == 0:
            print('The list is empty')
        else:
            cur_node = self.head
            while cur_node is not None:
                print(cur_node.data, end=', ')
                cur_node = cur_node.next_node

    def clear_list(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    # def __iadd__(self, other):
    #     if not isinstance(other, LinkedList):
    #         raise TypeError
    #     current_node = self.head
    #     for i in range(self.size):
    #         current_node = current_node.next_node
    #     current_node.next_node = other.head
    #     other.head.prev_node = current_node
    #     current_node.next_node.prev_node = current_node
    #     self.tail = other.tail
    #     self.size += other.size
    #     other.clear_list()


if __name__ == '__main__':
    l1 = LinkedList()
    print(l1.size)
    l1.append_to_the_end('Q')
    l1.append_to_the_end('W')
    l1.append_to_the_end('E')
    l2 = LinkedList()
    l2.append_to_the_end('R')
    l2.append_to_the_end('T')
    l2.append_to_the_end('U')
    l1 += l2
    l1.print_list()