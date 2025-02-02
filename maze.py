from window import Cell

class Maze:
    __init__(self, x1, y1, num_rows, num_colums, cell_size_x, cell_size_y, win):
        self._x1 = x1
        self._y1 = y1
        self.num_rows = num_rows
        self.num_columns = num_colums
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win 
        self._cells = []
        self._ceate_cells()

    def _ceate_cells(self):
        pass

