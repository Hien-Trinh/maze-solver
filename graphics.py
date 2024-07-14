from tkinter import Tk, BOTH, Canvas


class Window():
    def __init__(self, width, height) -> None:
        self.root = Tk()
        self.root.title("Maze Solver")
        self.canvas = Canvas(self.root, bg="white", width=width, height=height)
        self.canvas.pack(fill=BOTH, expand=1)
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update()
        self.root.update_idletasks()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)

    def close(self):
        self.running = False


class Point():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


class Line():
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end

    def draw(self, canvas, fill_color):
        canvas.create_line(self.start.x, self.start.y,
                           self.end.x, self.end.y, fill=fill_color, width=2)


class Cell():
    def __init__(self, left_wall, right_wall, top_wall, bottom_wall, x1, x2, y1, y2) -> None:
        self.left_wall = left_wall
        self.right_wall = right_wall
        self.top_wall = top_wall
        self.bottom_wall = bottom_wall
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def draw(self, canvas):
        if self.left_wall:
            Line(Point(self.x1, self.y1), Point(
                self.x1, self.y2)).draw(canvas, "black")
        if self.right_wall:
            Line(Point(self.x2, self.y1), Point(
                self.x2, self.y2)).draw(canvas, "black")
        if self.top_wall:
            Line(Point(self.x1, self.y1), Point(
                self.x2, self.y1)).draw(canvas, "black")
        if self.bottom_wall:
            Line(Point(self.x1, self.y2), Point(
                self.x2, self.y2)).draw(canvas, "black")
