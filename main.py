from graphics import Window, Point, Line
from cell import Cell


def main():
    win = Window(800, 600)
    win.draw_line(Line(Point(10, 10), Point(100, 100)), "red")
    cell = Cell(True, False, True, False, 10, 100, 10, 100, win)
    cell.draw()
    win.wait_for_close()


main()
