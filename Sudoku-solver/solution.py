from sudoku import SudokuSolver
from file_manager import grid_to_file

def solution(puzzle, output_filename):
    solver = SudokuSolver(puzzle)
    if solver.solve():
        solution = solver.get_solution()
        for row in solution:
            print(" ".join(map(str, row)))
        grid_to_file(solution, output_filename)
        print("\nSolution found!\n")
    else:
        print("No solution exists for this Sudoku.\n")