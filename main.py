from window import Window, Point, Line, Cell

def main():
    win = Window(800, 600)
    point_a, point_b = Point(2, 400), Point(100, 300)
    point_c, point_d = Point(150, 193), Point(484, 494)
    cell2 = Cell(point_c, point_d, win)
    cell = Cell(point_a, point_b, win)
    cell.draw()
    cell2.draw()
    cell.draw_move(cell2)
    win.wait_for_close()

main()
