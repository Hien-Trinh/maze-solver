from graphics import Window
from maze import Maze
import sys


def main():
    # Create the GUI window
    win = Window(800, 800)

    # Create the maze object with parameters
    maze = Maze(10, 10, 5, 5, 20, 20, win)

    # Solve the maze
    maze.solve()

    # Wait for the window to close
    win.wait_for_close()


if __name__ == "__main__":
    main()
