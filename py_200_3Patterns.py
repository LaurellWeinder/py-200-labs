# Шаблон проектирования "Стратегия"

import json
import pickle

class IStructureDriver:
    def read(self):
        pass

    def write(self, d):
        pass


class JSONFileDriver(IStructureDriver):
    def __init__(self, filename):
        self.__filename = filename

    def read(self):
        with open(self.__filename, encoding='UTF-8') as f:
            return json.load(f)

    def write(self, d):
        with open(self.__filename, 'w', encoding='UTF-8') as f:
            json.dump(d, f, ensure_ascii=False)


class JSONStringDriver(IStructureDriver):
    def __init__(self, s='{}'):
        self.__s = s

    def get_string(self):
        return self.__s

    def read(self):
        something = json.loads(self.__s)
        return something

    def write(self, d):
        self.__s = json.dumps(d, ensure_ascii=False)


class PickleDriver(IStructureDriver):
    def __init__(self, filename):
        self.__filename = filename

    def read(self):
        with open(self.__filename, 'rb') as f:
            return pickle.load(f)

    def write(self, d):
        with open(self.__filename, 'wb') as f:
            pickle.dump(d, f)


class SDWorker:
    def __init__(self, structure_driver: IStructureDriver):
        self.__structure_driver = structure_driver

    def read(self):
        self.__structure_driver.read()

    def write(self, d):
        self.__structure_driver.write(d)

    def set_structure_driver(self, structure_driver):
        self.__init__(structure_driver)


class SDBuilder:

    def build(self):
        return None

    def __str__(self):
        return self.__class__.__name__


class JSONFileBuilder(SDBuilder):
    def build(self):
        filename = input('Enter filename (.json)>')
        return JSONFileDriver(filename)


class JSONStrBuilder(SDBuilder):
    def build(self):
        s = input('Enter dictionary') #  ВОт это странно. Если мы пишем, то ок. А если читаем?
        return JSONStringDriver(f"{s}")


class PickleBuilder(SDBuilder):
    def build(self):
        filename = input('Enter filename (.bin)>')
        return PickleDriver(filename)


class SDFabric:
    def get_sd_driver(self, driver_name):
        builders = {'json': JSONFileBuilder,
                    'json_str': JSONStrBuilder,
                    'pickle': PickleBuilder}
        try:
            return builders[driver_name]()
        except:
            return SDBuilder()


class Observer:
    def update(self):
        pass


class Subject:

    def __init__(self):
        self.__o = set()

    def add_observer(self, o: Observer):
        self.__o.add(o)

    def remove_observer(self, o: Observer):
        self.__o.remove(o) # Вот тут что-то странное с синтаксисом творилось

    def notify(self):
        for o in self.__o:
            o.update(self)


class Data(Subject):
        def __init__(self, data):
            self.__data = data

        @property
        def read_data(self):
            return None

        @property
        def write_data(self):
            self.notify()
            return None