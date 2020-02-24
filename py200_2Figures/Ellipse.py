import math


from Figures.BaseFigure import Figure


class Ellipse(Figure):
    def __init__(self, x=0, y=0, w=0, h=0):
        self.__x = x
        self.__y = y
        self.w = w
        self.h = h

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def perimeter(self):
        return 2 * math.pi * math.sqrt(((self.w / 2) ** 2 + (self.h / 2) ** 2) / 2)

    def square(self):
        return math.pi * self.w * self.h

    @property
    def width(self):
        return self.w

    @property
    def height(self):
        return self.h
