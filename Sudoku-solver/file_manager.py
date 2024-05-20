# reads a file and turns it into a 9x9 grid
def file_to_grid(filename):
    try:
        with open(filename, 'r') as file:
            numbers = list(map(int, file.read().split()))
            
            # Check for numbers below 0 or above 9 in file
            for number in numbers:
                if number < 0 or number > 9:
                    raise ValueError(f"Invalid number {number} found in file. Numbers must be between 0 and 9 inclusive.")
            # Check if there are correct amount of numbers in file
            if len(numbers) != 81:
                raise ValueError("The input file does not contain exactly 81 numbers.")

            grid = [numbers[i:i + 9] for i in range(0, 81, 9)]
            return grid
    except FileNotFoundError:
        raise FileNotFoundError(f"File {filename} not found. Please check the file path and name.")

# writes grid inside a file
def grid_to_file(grid, filename):
    with open(filename, 'w') as file:
        for row in grid:
            file.write(' '.join(map(str, row)) + '\n')