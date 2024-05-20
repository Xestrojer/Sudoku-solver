from board import SudokuBoard

def solve_sudoku(board, boardlen):
    row, col = board.find_empty_cell()
    if row is None:
        return True  # No empty cells, puzzle is solved

    for num in range(1, boardlen+1):
        if board.valid_move(row, col, num):
            board.place_number(row, col, num)
            if solve_sudoku(board, boardlen): # Calls itself until solved
                return True
            board.remove_number(row, col)

    return False  # No valid number can be placed