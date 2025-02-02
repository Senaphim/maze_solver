import time
from window import Cell, Point

class Maze:
    def __init__(self, x1, y1, num_rows, num_columns, cell_size_x, cell_size_y, win=None):
        self._x1 = x1
        self._y1 = y1
        self.num_rows = num_rows
        self.num_columns = num_columns
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win 
        self._cells = []
        self._ceate_cells()

    def _ceate_cells(self):
        for i in range(self.num_columns):
            column = []
            x_a = self._x1 + i * self.cell_size_x
            x_b = self._x1 + (i + 1) * self.cell_size_x
            for j in range(self.num_rows):
                y_a = self._y1 + j * self.cell_size_y
                y_b = self._y1 + (j + 1) * self.cell_size_y
                point_a = Point(x_a, y_a)
                point_b = Point(x_b, y_b)
                cell = Cell(point_a, point_b, self._win)
                column.append(cell)
            self._cells.append(column)
        self._draw_cells()

    # This is kind of redundant, but is included to structure as expected by bootdev.
    def _draw_cells(self): 
        if self._win is None:
            return
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._cells[i][j].draw()
                self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[0][0].draw()
        self._cells[self.num_columns - 1][self.num_rows - 1].has_bottom_wall = False
        self._cells[self.num_columns - 1][self.num_rows - 1].draw()
