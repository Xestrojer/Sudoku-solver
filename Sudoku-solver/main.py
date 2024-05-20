from file_manager import file_to_grid
from solution import solution

if __name__ == "__main__":
  input_filename = 'Input.txt'
  output_filename = 'Output.txt'
  puzzle = file_to_grid(input_filename)
  print(f"Solving Sudoku:")
  solution(puzzle,output_filename)