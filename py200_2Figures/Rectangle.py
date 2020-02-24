from Figures.BaseFigure import Figure


class Rectangle(Figure):
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
        return 2 * (self.w + self.h)

    def square(self):
        return self.w * self.h

    @property
    def width(self):
        return self.w

    @property
    def height(self):
        return self.h
