from graphics import Window, Point, Line, Cell


def main():
    win = Window(800, 600)
    win.draw_line(Line(Point(10, 10), Point(100, 100)), "red")
    cell = Cell(True, False, True, False, 10, 100, 10, 100)
    cell.draw(win.canvas)
    win.wait_for_close()


main()
