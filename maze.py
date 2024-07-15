from cell import Cell
import random
import time


class Maze:
    def __init__(self, x, y, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self.x = x
        self.y = y
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.cells = []

        self.create_cells()
        self.break_entrance_and_exit()

    def create_cells(self):
        for i in range(self.num_cols):
            cell_col = []
            for j in range(self.num_rows):
                cell_col.append(Cell(self.win))

            self.cells.append(cell_col)

        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self.draw_cell(i, j)

    def draw_cell(self, i, j):
        if self.win is None:
            return

        self.cells[i][j].draw(
            self.x + self.cell_size_x * j,
            self.x + self.cell_size_x * (j + 1),
            self.y + self.cell_size_y * i,
            self.y + self.cell_size_y * (i + 1),
        )

        self.animate()

    def animate(self):
        if self.win is None:
            return

        self.win.redraw()
        time.sleep(0.05)

    def break_entrance_and_exit(self):
        self.cells[0][0].top_wall = False
        self.cells[self.num_cols - 1][self.num_rows - 1].bottom_wall = False
        self.draw_cell(0, 0)
        self.draw_cell(self.num_cols - 1, self.num_rows - 1)
