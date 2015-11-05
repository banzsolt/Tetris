__author__ = 'Zsolti'

class Bord:

    _last_block = None

    def __init__(self, width, height):
        self.x = height
        self.y = width
        self.matrix = [[0 for y in range(self.y + 2)] for x in range(self.x + 1)]

        #set the right and left borders to be 1
        for x in range(0, self.x + 1):
            self.matrix[x][0] = 1
            self.matrix[x][self.y + 1] = 1

        for y in range(0, self.y + 1):
            self.matrix[self.x][y] = 1

    def width(self):
        return len(self.matrix[0]) - 2


    def check_row_filled(self):
        full_rows = []

        for x in range(0, self.x):
            full_rows.append(x)
            for y in range(0, self.y + 1):
                if self.matrix[x][y] == 0:
                    full_rows.remove(x)
                    break

        print(full_rows)
        if len(full_rows) > 0:
            for row in full_rows:
                for y in range(1, self.y + 1):
                    self.matrix[row][y] = 0
                while row > 0:
                    for y in range(1, self.y + 1):
                        self.matrix[row][y] = self.matrix[row-1][y]
                    row -= 1
                        

    def new_block(self, block, xposition, yposition):
        if self._last_block == None:
            self._last_block = block
        else:
            # remove the old block place
            shape_x = 0
            for x in range(self._last_block.x, self._last_block.x + block.height()):
                shape_y = 0
                for y in range(self._last_block.y, self._last_block.y + block.width()):
                    if block.shape[shape_x][shape_y] == 1:
                        self.matrix[x][y] = 0
                    shape_y += 1
                shape_x += 1

        shape_x = 0
        for x in range(xposition, xposition + block.height()):
            shape_y = 0
            for y in range(yposition, yposition + block.width()):
                if block.shape[shape_x][shape_y] == 1:
                    self.matrix[x][y] = block.shape[shape_x][shape_y]
                shape_y += 1
            shape_x += 1
        self._last_block.set_x(xposition)
        self._last_block.set_y(yposition)
        
    def next_step(self):
        colide = False
        if self._last_block is None:
            return True
        block_y = 0
        for possition in range(self._last_block.y, self._last_block.y + self._last_block.width()):
            if self._last_block.shape[int(self._last_block.height())-1][block_y] == 1:
                if self.matrix[self._last_block.x + self._last_block.height()][possition] == 1:
                    self.save_matrix()
                    colide = True
                    return colide
            block_y += 1
        if not colide:
            self.new_block(self._last_block, self._last_block.x+1, self._last_block.y)
            return colide

    def save_matrix(self):
        self._last_block = None
