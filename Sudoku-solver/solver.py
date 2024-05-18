from board import SudokuBoard

def solve_sudoku(board):
    row, col = board.find_empty_cell()
    if row is None:
        return True  # No empty cells, puzzle is solved

    for num in range(1, 10):
        if board.is_valid_move(row, col, num):
            board.place_number(row, col, num)
            if solve_sudoku(board):
                return True
            board.remove_number(row, col)

    return False  # No valid number can be placed