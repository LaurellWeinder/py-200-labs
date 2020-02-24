from Figures.BaseFigure import Figure

class Triangle(Figure):
    def __init__(self,  *points):
        if len(points) != 6:
            raise ValueError('Insufficient amount of arguments')
        self.points = points

    def perimeter(self):
        pass

    def square(self):
        pass