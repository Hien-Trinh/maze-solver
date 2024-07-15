from graphics import Point, Line


class Cell():
    def __init__(self, left_wall, right_wall, top_wall, bottom_wall,
                 x1, x2, y1, y2, win) -> None:
        self.left_wall = left_wall
        self.right_wall = right_wall
        self.top_wall = top_wall
        self.bottom_wall = bottom_wall
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.win = win

    def draw(self):
        if self.left_wall:
            self.win.draw_line(Line(Point(self.x1, self.y1), Point(
                self.x1, self.y2)), "black")
        if self.right_wall:
            self.win.draw_line(Line(Point(self.x2, self.y1), Point(
                self.x2, self.y2)), "black")
        if self.top_wall:
            self.win.draw_line(Line(Point(self.x1, self.y1), Point(
                self.x2, self.y1)), "black")
        if self.bottom_wall:
            self.win.draw_line(Line(Point(self.x1, self.y2), Point(
                self.x2, self.y2)), "black")
