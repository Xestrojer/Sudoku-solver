from board import SudokuBoard
from solver import solve_sudoku

class SudokuSolver:
    def __init__(self, grid):
        self.board = SudokuBoard(grid)

    def solve(self):
        return solve_sudoku(self.board)

    def get_solution(self):
        if self.solve():
            return self.board.grid
        return None