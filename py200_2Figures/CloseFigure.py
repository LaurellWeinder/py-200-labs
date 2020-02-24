from Figures.BaseFigure import Figure

class CloseFigure(Figure):

    def __init__(self,  *points):
        if len(points) % 2 != 0:
            raise ValueError('Not enough arguments. The amount must be even.')
        self.points = points

    def perimeter(self):
        pass

    def square(self):
        pass

