from window import Window, Point, Line

def main():
    win = Window(800, 600)
    point_a, point_b = Point(2, 400), Point(100, 300)
    line = Line(point_a, point_b)
    win.draw_line(line, "white")
    win.wait_for_close()

main()
