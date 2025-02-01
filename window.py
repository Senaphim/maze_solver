from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Mazer 9000")
        self.__canvas = Canvas(self.__root, bg="blue", height=height, width=width)
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
