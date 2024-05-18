def is_valid_sudoku(board):
    for row in board:
        seen = set()
        for cell in row:
            if cell != 0:
                if cell in seen:
                    return False
                seen.add(cell)
    
    for col in range(9):
        seen = set()
        for row in board:
            if row[col] != 0:
                if row[col] in seen:
                    return False
                seen.add(row[col])
    
    for row_start in range(0, 9, 3):
        for col_start in range(0, 9, 3):
            seen = set()
            for i in range(row_start, row_start + 3):
                for j in range(col_start, col_start + 3):
                    if board[i][j] != 0:
                        if board[i][j] in seen:
                            return False
                        seen.add(board[i][j])
    
    return True

def is_complete_sudoku(board):
    return all(all(cell != 0 for cell in row) for row in board)