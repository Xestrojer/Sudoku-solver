from abc import ABC, abstractmethod
import math

class Board(ABC):
    @abstractmethod
    def __init__(self, grid):
        pass

    def place_number(self, row, col, num):
        self.grid[row][col] = num

    def remove_number(self, row, col):
        self.grid[row][col] = 0

    def is_solved(self):
        return all(all(cell != 0 for cell in row) for row in self.grid)
    
    def __str__(self):
        # Display the Sudoku board for debugging
        lines = []
        for row in self.grid:
            lines.append(" ".join(map(str, row)))
        return "\n".join(lines)

class SudokuBoard(Board):
    def __init__(self, grid):
        if len(grid) % int(math.sqrt(len(grid))) != 0:
            raise  ValueError('Sudoku grid is wrong size')
        else:
            self.grid = grid
            self.size = len(grid)
            self.boxsize= int(math.sqrt(len(grid)))

    def valid_move(self, row, col, num):
        # Check if 'num' is a valid move in the current position
        return (
            self.__valid_row(row, num)
            and self.__valid_col(col, num)
            and self.__valid_box(row, col, num)
        )

    def __valid_row(self, row, num):
        return num not in self.grid[row]

    def __valid_col(self, col, num):
        return num not in [self.grid[row][col] for row in range(self.size)]

    def __valid_box(self, row, col, num):
        start_row = self.boxsize * (row // self.boxsize)
        start_col = self.boxsize * (col // self.boxsize)
        for i in range(start_row, start_row + self.boxsize):
            for j in range(start_col, start_col + self.boxsize):
                if self.grid[i][j] == num:
                    return False
        return True

    def find_empty_cell(self):
        for row in range(self.size):
            for col in range(self.size):
                if self.grid[row][col] == 0:
                    return row, col
        return None, None
