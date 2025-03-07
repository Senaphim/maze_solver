from window import Window 
from maze import Maze

def main():
    win = Window(800, 600)
    num_rows = 24
    num_columns = 32
    margin = 50
    cell_size_x = (800 - 2 * margin) / num_columns
    cell_size_y = (600 - 2 * margin) / num_rows

    maze = Maze(margin, margin, num_rows, num_columns, cell_size_x, cell_size_y, win)
    maze.solve()

    win.wait_for_close()

main()
