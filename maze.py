import time
import random
from window import Cell, Point

class Maze:
    def __init__(self, x1, y1, num_rows, num_columns, cell_size_x, cell_size_y,
                 win=None, seed=None):
        self._x1 = x1
        self._y1 = y1
        self.num_rows = num_rows
        self.num_columns = num_columns
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win 
        self._seed = seed
        self._cells = []
        if self._seed is not None:
            random.seed(self._seed)
        self._ceate_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

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
        for i in range(self.num_columns):
            for j in range(self.num_rows):
                self._draw_cell(i, j)

    # This is kind of redundant, but is included to structure as expected by bootdev.
    def _draw_cell(self, i, j): 
        if self._win is None:
            return
        self._cells[i][j].draw()
        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.01)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[0][0].draw()
        self._cells[self.num_columns - 1][self.num_rows - 1].has_bottom_wall = False
        self._cells[self.num_columns - 1][self.num_rows - 1].draw()

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            # List of possible neighbours
            neighbours_index = [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]
            neighbours_unvisited = []

            # Determine which neighbours have been visited. Skip if outiside maze bounds
            for pair in neighbours_index:
                if pair[0] < 0 or pair[1] < 0:
                    continue
                if pair[0] >= self.num_columns or pair[1] >= self.num_rows:
                    continue
                if not self._cells[pair[0]][pair[1]].visited:
                    neighbours_unvisited.append(pair)

            # If nowhere to go, draw cell
            if len(neighbours_unvisited) == 0:
                self._draw_cell(i, j)
                return

            # Select random directiion to go
            direction = random.randrange(0, len(neighbours_unvisited), 1)

            # Match case to knock out walls between cells and recursively visit the next cell
            match neighbours_unvisited[direction]:
                case [x, y] if x == i+1 and y == j:
                    self._cells[i][j].has_right_wall = False
                    self._cells[i+1][j].has_left_wall = False
                    self._break_walls_r(i+1, j)
                case [x, y] if x == i-1 and y == j:
                    self._cells[i][j].has_left_wall = False
                    self._cells[i-1][j].has_right_wall = False
                    self._break_walls_r(i-1, j)
                case [x, y] if x == i and y == j+1:
                    self._cells[i][j].has_bottom_wall = False
                    self._cells[i][j+1].has_top_wall = False
                    self._break_walls_r(i, j+1)
                case [x, y] if x == i and y == j-1:
                    self._cells[i][j].has_top_wall = False
                    self._cells[i][j-1].has_bottom_wall = False
                    self._break_walls_r(i, j-1)
                case _:
                    pass
   
    def _reset_cells_visited(self):
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._cells[i][j].visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if i == self.num_columns - 1 and j == self.num_rows - 1:
            return True
        # List of possible neighbours
        neighbours_index = [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]
        current_cell = self._cells[i][j]

        # Loop through neighbours to find cells to visit
        for pair in neighbours_index:
            if pair[0] < 0 or pair[1] < 0:
                continue
            if pair[0] >= self.num_columns or pair[1] >= self.num_rows:
                continue
            neighbour_cell = self._cells[pair[0]][pair[1]]

            # Match direction and draw move to that cell if valid
            match pair:
                case [x, y] if x == i+1:
                    if not current_cell.has_right_wall and not neighbour_cell.visited:
                        current_cell.draw_move(neighbour_cell)
                        if self._solve_r(x, y):
                            return True
                        else:
                            current_cell.draw_move(neighbour_cell, undo=True)
                case [x, y] if x == i-1:
                    if not current_cell.has_left_wall and not neighbour_cell.visited:
                        current_cell.draw_move(neighbour_cell)
                        if self._solve_r(x, y):
                            return True
                        else:
                            current_cell.draw_move(neighbour_cell, undo=True)
                case [x, y] if y == j+1:
                    if not current_cell.has_bottom_wall and not neighbour_cell.visited:
                        current_cell.draw_move(neighbour_cell)
                        if self._solve_r(x, y):
                            return True
                        else:
                            current_cell.draw_move(neighbour_cell, undo=True)
                case [x, y] if y == j-1:
                    if not current_cell.has_top_wall and not neighbour_cell.visited:
                        current_cell.draw_move(neighbour_cell)
                        if self._solve_r(x, y):
                            return True
                        else:
                            current_cell.draw_move(neighbour_cell, undo=True)

        # All directions exhausted and no route found
        return False
