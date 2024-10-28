from abc import ABC, abstractmethod


class Figure(ABC):

    def __init__(self, pos_x, pos_y, length, width):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.length = length
        self.width = width

    def move(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y


#######################################################
class ResizeMixin:
    def resize(self, length, width):
        self.length = length
        self.width = width
#######################################################


class Rectangle(Figure, ResizeMixin):
    pass


class Square(Figure, ResizeMixin):
    def __init__(self, pos_x, pos_y, size):
        super().__init__(pos_x, pos_y, size, size)


if __name__ == '__main__':
    rect_1 = Rectangle(1, 2, 3, 4)
    rect_2 = Rectangle(10, 15, 20, 25)

    square_1 = Square(5, 6, 9)


    for figure in (rect_1, rect_2, square_1):
        new_x = figure.length * 2
        new_y = figure.width * 2

        figure.resize(new_x, new_y)


