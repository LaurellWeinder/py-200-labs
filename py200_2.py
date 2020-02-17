# В Python нет возможности объявления константных переменных. Реализуйте
# с помощью @property константный атрибут. Пусть класс возвращает число
# пи. Попытайтесь применить @property к @staticmethod и @classmethod. Если
# не получается, то примените к обычному методу. (Тема 1. Слайды 1-43)

class Pi:
    def __init__(self):
        self.__pi = 3.14

    @property
    def pi(self):
        return self.__pi

    @staticmethod
    @classmethod
    def pi2(self):
        return 3.14


pi = Pi()
print(pi.pi)
print(pi.pi2)

# Создайте классы A и B(A). a. В классе А создайте атрибуты класса, атрибуты
# объекта, @staticmethod, @classmethod и методов со всеми видами областями
# видимости. b. Продемонстрируете их видимость внутри класса, вне класса и в
# классе потомке. c. Получите доступ вне класса к псевдозащищённым
# псевдоприватным атрибутам и методам. (Тема 2. Слайды 1-43)


class A:
    class_a = 42 # Атрибут класса
    def __init__(self, ex_a='This is ex_a', ex_b='This is ex_b'):
        self.ex_a = ex_a  # Атрибут экземлпяра. Public
        self._ex_b = ex_b # Protected
        self.__ex_c = 1   # Private. Выдаст attribute error

    @classmethod
    def get_class_a(cls):
        return cls.class_a

    @classmethod
    def _protected_method(cls):
        return 'This is protected classmethod'

    @classmethod
    def __private_method(cls):
        return 'This is private class method'

    @staticmethod
    def show_static():
        return 'This is a static method'

class B(A):
    def __init__(self):
        super().__init__() # Чтобы перенести атрибуты из класса А, нужна вот эта штука.
        self.b_a = 1
        self.__b_b = 2

print(A.get_class_a()) # Этот вызывается свободно
print(A._protected_method()) # Этот вызывается, если знать, как он называется
print(A._A__private_method()) # А этот - вот такой конструкцией, но лучше так не делать.
b = B()
print(B.get_class_a()) # Этот наследуется автоматически
print(b.ex_a)
print(b._ex_b)# А вот это не сработает, если нет super()
print(b._A__ex_c) # Ну и приватный можно вызвать вот так
print(B._protected_method()) #  Работает точно так же, как и с классом А
print(A.show_static()) # Статик везде одинаковый
print(B.show_static())
print(b.show_static())

#5. В Python 3 все классы являются классами нового стиля. Классы нового стиля
# – это классы, которые являются наследниками от класса object. Убедитесь,
# что класс А является наследником от object. (Тема 2. Слайды 48-52)

class AA(object):
    pass
class BB(AA):
    pass
print(BB.mro()) # Список родителей класса. По увеличению индекса увеличивается "старшинство"




