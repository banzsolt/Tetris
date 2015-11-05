import random

__author__ = 'Zsolti'

class Block:

    __config_shapes = {
        '1':[[1, 1, 0],
             [0, 1, 1]],
        '2':[[0, 0, 1],
             [1, 1, 1]],
        '3':[[0, 1, 1],
             [1, 1, 0]],
        '4':[[0, 1, 0],
             [1, 1, 1]],
        '5':[[1, 1],
             [1, 1]],
        '6':[[1, 1, 1, 1]]
    }

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.shape = self.__config_shapes[str(random.randint(1, 6))]

    def rotate_right(self):
        result = [[]]
        for x in range (0, len(self.shape)):
            for y in range(0, len(self.shape[0])):
                result[y][x] = self.shape[x][y]
        self.shape = result

    def width(self):
        return len(self.shape[0])

    def height(self):
        return len(self.shape)

    def rotate_left(self):
        self.rotate_right()
        self.rotate_right()
        self.rotate_right()

    def move_left(self):
        self.y -= 1

    def move_right(self):
        self.y += 1

    def move_down(self):
        self.x += 1

    def set_x(self, newx):
        self.x = newx

    def set_y(self, newy):
        self.y = newy