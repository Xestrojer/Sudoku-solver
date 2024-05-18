class SudokuBoard:
    def __init__(self, grid):
        self.grid = grid
        self.size = 9

    def is_valid_move(self, row, col, num):
        # Check if 'num' is a valid move in the current position
        return (
            self.is_valid_row(row, num)
            and self.is_valid_col(col, num)
            and self.is_valid_box(row, col, num)
        )

    def is_valid_row(self, row, num):
        return num not in self.grid[row]

    def is_valid_col(self, col, num):
        return num not in [self.grid[row][col] for row in range(self.size)]

    def is_valid_box(self, row, col, num):
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if self.grid[i][j] == num:
                    return False
        return True

    def is_solved(self):
        return all(all(cell != 0 for cell in row) for row in self.grid)

    def find_empty_cell(self):
        for row in range(self.size):
            for col in range(self.size):
                if self.grid[row][col] == 0:
                    return row, col
        return None, None

    def place_number(self, row, col, num):
        self.grid[row][col] = num

    def remove_number(self, row, col):
        self.grid[row][col] = 0

    def __str__(self):
        # Display the Sudoku board
        lines = []
        for row in self.grid:
            lines.append(" ".join(map(str, row)))
        return "\n".join(lines)