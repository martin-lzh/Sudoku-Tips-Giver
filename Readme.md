# Sudoku Tips Giver

This project provides tools to assist with solving Sudoku puzzles. It includes functions to check the validity of a number in a Sudoku board, find the most constrained cell, convert a string representation of a Sudoku board to a 2D list, and check if the board is solved. Additionally, it includes a `Board` class to represent and manipulate a Sudoku board.

## Usage

### main.ipynb

The `main.ipynb` notebook demonstrates how to use the `Board` class and its methods. Below is a brief overview of the steps:

1. **Import the Board class:**

    ```python
    from functions import Board
    ```

2. **Create a Board object:**

    ```python
    board = Board()
    ```

3. **Load a board from a string:**

    ```python
    s = "001030000/002000040/006501029/230607080/000803000/010004367/420108500/080000000/000070408"
    board.string_to_board(s)
    ```

4. **Print the board:**

    ```python
    for row in board.board:
        print(row, end="\n")
    ```

5. **Check if the board is solved and find the most constrained cell:**

    ```python
    if board.is_solved():
        print("The board is solved!")
    else:
        i, j, const = board.find_constraint()
        print("On row ", i+1, "and column ", j+1, "the block has ", const, "possibilities!")
    ```

6. **Add a number to the board:**

    ```python
    board.add(row=9, col=8, num=1)
    ```

7. **Remove a number from the board:**

    ```python
    board.remove(row=9, col=8)
    ```

### functions.py

The `functions.py` file contains the implementation of the `Board` class and several helper functions:

- **is_valid(board, row, col, num):** Checks if a number is valid in a given cell of the Sudoku board.
- **find_constraint(board):** Finds the most constrained empty cell in the Sudoku board.
- **string_to_board(s):** Converts a string representation of a Sudoku board to a 2D list.
- **is_solved(board):** Checks if the Sudoku board is solved.
- **board_to_string(board):** Converts a 2D list representation of a Sudoku board into a string.

### Board Class

The `Board` class provides methods to manipulate the Sudoku board:

- **add(row, col, num):** Add a number to the board at the specified position.
- **remove(row, col):** Remove a number from the board at the specified position.
- **is_valid(row, col, num):** Check if a number can be placed in a given position on the Sudoku board.
- **is_solved():** Check if the Sudoku board is solved.
- **find_constraint():** Finds the cell with the minimum number of possible values (constraints) in the Sudoku board.
- **string_to_board(s):** Converts a string representation of a Sudoku board into a 2D list.
- **board_to_string():** Converts a 2D list representation of a Sudoku board into a string.