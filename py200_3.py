from py_200_3Patterns import *


class LinkedList(Observer):
    class Node(Subject):
        def __init__(self, data, prev_node=None, next_node=None):
            super().__init__()
            self.next_node = next_node
            self.prev_node = prev_node
            self.data = data

        def __str__(self):
            return f'{self.data}'

        def __repr__(self):
            return f'{self.data}'

    def __init__(self):
        self.__structure_driver = None
        self.size = 0
        self.head = None

    def insert_in_the_beginning(self, data: Subject):
        if not isinstance(data, Subject):
            raise TypeError('Data must me inherited from Subject class')
        data.add_observer(self)                          # Я решила отказаться от хвоста. Просто поняла,
        if self.head is None:                            # что от него нет никакого толка, кроме вставки в конец.
            self.head = self.Node(data)                  # Два вида вставки: перед головой и после определенной ноды.
        else:
            new_node = self.Node(data, next_node=self.head)
            new_node.next_node.prev_node = new_node
            self.head = new_node
        self.size += 1

    def append_to_the_end(self, data: Subject):
        if not isinstance(data, Subject):
            raise TypeError('Data must me inherited from Subject class')
        data.add_observer(self)
        # Добавляем ноду в конец, проходясь циклом по всем
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

    def insert_after_node(self, node, data: Subject):
        if not isinstance(data, Subject):
            raise TypeError('Data must me inherited from Subject class')
        if self.head is None:
            raise ValueError('List in empty')
        data.add_observer(self)
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
            print('\n')

    def clear_list(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def safe_to_dict(self):
        ll_dict = {}
        i = 0
        curr_node = self.head
        while i < self.size:
            ll_dict[i] = curr_node.__str__()
            curr_node = curr_node.next_node
            i += 1
        return ll_dict


    def load_from_dict(self, ll_dict):  # Если здесь выводить новый список, получается,
        self.clear_list()               # что драйвер пишет словарь в неизвестный список
        for i in ll_dict.values():
            self.append_to_the_end(i)
        return self

    def read(self):
        self.load_from_dict(self.__structure_driver.read())

    def write(self):
        self.__structure_driver.write(self.safe_to_dict())

    def set_structure_driver(self, structure_driver):
        self.__structure_driver = structure_driver


if __name__ == '__main__':
    driver_name = input('Please enter driver name >  '.strip())

    builder = SDFabric().get_sd_driver(driver_name)
    driver = builder.build()

    ll = LinkedList()
    ll.set_structure_driver(driver)
    l2 = ll.read()
    json_str = {"0": "A", "1": "B", "2": "C"}  # json_str работает вот с таким словарем просто отлично.
    ll.print_list()


