from cell import Cell
import random
import time


class Maze:
    def __init__(
        self, x, y, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None
    ):
        self.cells = []
        self.x = x
        self.y = y
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.seed = seed

        if seed:
            random.seed(seed)

        self.create_cells()
        self.break_entrance_and_exit()
        self.break_walls_r(0, 0)
        self.reset_cells_visited()

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
        time.sleep(0.005)

    def break_entrance_and_exit(self):
        self.cells[0][0].top_wall = False
        self.cells[self.num_cols - 1][self.num_rows - 1].bottom_wall = False
        self.draw_cell(0, 0)
        self.draw_cell(self.num_cols - 1, self.num_rows - 1)

    def break_walls_r(self, i, j):
        self.cells[i][j].visited = True

        while True:
            neighbor = []

            if i > 0 and not self.cells[i - 1][j].visited:
                neighbor.append(0)
            if i < self.num_cols - 1 and not self.cells[i + 1][j].visited:
                neighbor.append(1)
            if j > 0 and not self.cells[i][j - 1].visited:
                neighbor.append(2)
            if j < self.num_rows - 1 and not self.cells[i][j + 1].visited:
                neighbor.append(3)

            if not neighbor:
                self.draw_cell(i, j)
                return

            direction_index = random.randrange(len(neighbor))
            direction = neighbor[direction_index]

            if direction == 0:
                self.cells[i][j].left_wall = False
                self.cells[i - 1][j].right_wall = False
                self.break_walls_r(i - 1, j)
            if direction == 1:
                self.cells[i][j].right_wall = False
                self.cells[i + 1][j].left_wall = False
                self.break_walls_r(i + 1, j)
            if direction == 2:
                self.cells[i][j].top_wall = False
                self.cells[i][j - 1].bottom_wall = False
                self.break_walls_r(i, j - 1)
            if direction == 3:
                self.cells[i][j].bottom_wall = False
                self.cells[i][j + 1].top_wall = False
                self.break_walls_r(i, j + 1)

    def reset_cells_visited(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self.cells[i][j].visited = False

    def solve(self):
        return self.solve_r(0, 0)

    def solve_r(self, i, j):
        self.animate()
        self.cells[i][j].visited = True
        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True

        if (
            i > 0
            and not self.cells[i - 1][j].visited
            and not self.cells[i - 1][j].right_wall
        ):
            self.cells[i][j].draw_move(self.cells[i - 1][j])
            if self.solve_r(i - 1, j):
                return True
            else:
                self.cells[i][j].draw_move(self.cells[i - 1][j], True)
        if (
            i < self.num_cols - 1
            and not self.cells[i + 1][j].visited
            and not self.cells[i + 1][j].left_wall
        ):
            self.cells[i][j].draw_move(self.cells[i + 1][j])
            if self.solve_r(i + 1, j):
                return True
            else:
                self.cells[i][j].draw_move(self.cells[i + 1][j], True)
        if (
            j > 0
            and not self.cells[i][j - 1].visited
            and not self.cells[i][j - 1].bottom_wall
        ):
            self.cells[i][j].draw_move(self.cells[i][j - 1])
            if self.solve_r(i, j - 1):
                return True
            else:
                self.cells[i][j].draw_move(self.cells[i][j - 1], True)
        if (
            j < self.num_rows - 1
            and not self.cells[i][j + 1].visited
            and not self.cells[i][j + 1].top_wall
        ):
            self.cells[i][j].draw_move(self.cells[i][j + 1])
            if self.solve_r(i, j + 1):
                return True
            else:
                self.cells[i][j].draw_move(self.cells[i][j + 1], True)

        return False
