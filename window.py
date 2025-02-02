from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Mazer 9000")
        self.__canvas = Canvas(self.__root, bg="black", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running == True:
            self.redraw()

    def draw_line(self, line, fill_colour="white", width=2):
        line.draw(self.__canvas, fill_colour, width)

    def close(self):
        self.__running = False

class Point:
    def __init__(self, x, y):
        self.x = abs(x)
        self.y = abs(y)

class Line:
    def __init__(self, point_a, point_b):
        self.a = point_a
        self.b = point_b

    def draw(self, canvas, fill_colour, width=2):
        canvas.create_line(
                self.a.x, self.a.y, self.b.x, self.b.y, fill=fill_colour, width=width
        )

class Cell:
    def __init__(self, top_left, bottom_right, win=None,
                 left=True, right=True, top=True, bottom=True):
        self._x1 = top_left.x
        self._y1 = top_left.y
        self._x2 = bottom_right.x
        self._y2 = bottom_right.y
        self.has_left_wall = left
        self.has_right_wall = right
        self.has_top_wall = top
        self.has_bottom_wall = bottom
        self.visited = False
        self.win = win

    def draw(self):
        if self.win is None:
            return
        if self.has_left_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self.win.draw_line(line)
        else:
            line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self.win.draw_line(line, fill_colour="black")
        if self.has_right_wall:
            line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self.win.draw_line(line)
        else:
            line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self.win.draw_line(line, fill_colour="black")
        if self.has_top_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self.win.draw_line(line)
        else:
            line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self.win.draw_line(line, fill_colour="black")
        if self.has_bottom_wall:
            line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self.win.draw_line(line)
        else:
            line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self.win.draw_line(line, fill_colour="black")

    def draw_move(self, other, undo=False):
        if self.win is None:
            return
        centre_self = Point(
                (self._x1 + self._x2)//2, (self._y1 + self._y2)//2
        )
        centre_other = Point(
                (other._x1 + other._x2)//2, (other._y1 + other._y2)//2
        )
        connecting_line = Line(centre_self, centre_other)
        colour = "red"
        if undo:
            colour = "grey"
        self.win.draw_line(connecting_line, fill_colour=colour)
