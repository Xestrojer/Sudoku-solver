from board import SudokuBoard
from solver import solve_sudoku

class SudokuSolver:
    def __init__(self, grid):
        self.board = SudokuBoard(grid)
        self.boardlen = len(grid)

    # method which returns True and solves the sudoku (if possible) or False (if impossible)
    def solve(self):
        return solve_sudoku(self.board, self.boardlen)
    
    # method which returns solved sudoku board object after solving it. 
    def get_solution(self):
        if solve_sudoku(self.board, self.boardlen):
            return self.board.grid
        return None