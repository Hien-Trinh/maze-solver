from graphics import Window, Point, Line
from cell import Cell


def main():
    win = Window(800, 600)
    win.draw_line(Line(Point(10, 10), Point(100, 100)), "red")
    cell1 = Cell(True, False, True, False, 10, 100, 10, 100, win)
    cell2 = Cell(True, False, True, False, 100, 200, 100, 200, win)
    cell3 = Cell(True, False, True, False, 200, 300, 200, 300, win)
    cell4 = Cell(True, False, True, False, 300, 400, 300, 400, win)
    cell1.draw()
    cell2.draw()
    cell3.draw()
    cell4.draw()
    cell1.draw_move(cell2)
    cell2.draw_move(cell3)
    cell3.draw_move(cell4)

    win.wait_for_close()


main()
