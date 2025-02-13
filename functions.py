"""
This module provides functions and a class to assist with solving Sudoku puzzles. 
It includes functions to check the validity of a number in a Sudoku board, 
find the most constrained cell, convert a string representation of a Sudoku board 
to a 2D list, and check if the board is solved. Additionally, it includes a `Board` 
class to represent and manipulate a Sudoku board.
Functions:
    is_valid(board, row, col, num): Checks if a number is valid in a given cell of the Sudoku board.
    find_constraint(board): Finds the most constrained empty cell in the Sudoku board.
    string_to_board(s): Converts a string representation of a Sudoku board to a 2D list.
    is_solved(board): Checks if the Sudoku board is solved.
Class:
    Board: A class representing a Sudoku board with methods to add, remove, and validate numbers, 
           check if the board is solved, find the most constrained cell, and convert between 
           string and 2D list representations.
"""

import random

# check if the number is valid on the board
def is_valid(board, row, col, num):
    """
    Check if a number can be placed in a given position on the Sudoku board without violating Sudoku rules.
    Args:
        board (list of list of int): The 9x9 Sudoku board.
        row (int): The row index where the number is to be placed.
        col (int): The column index where the number is to be placed.
        num (int): The number to be placed in the given position.
    Returns:
        bool: True if the number can be placed in the given position, False otherwise.
    """

    # check the row
    for i in range(9):
        if board[row][i] == num:
            return False
    # check the column
    for i in range(9):
        if board[i][col] == num:
            return False
    # check the 3x3 grid
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False
    return True

# find the most constrained cell
def find_constraint(board):
    """
    Finds the cell with the minimum number of possible values (constraints) in a Sudoku board.
    Args:
        board (list of list of int): A 9x9 list representing the Sudoku board, where 0 indicates an empty cell.
    Returns:
        tuple: A tuple (min_row, min_col, constraint) where min_row and min_col are the row and column indices of the cell 
               with the minimum number of possible values, and constraint is the number of possible values for that cell.
    """

    min_constraint = 10
    min_row = -1
    min_col = -1
    candidates = []
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                current_constraint = 0
                for num in range(1, 10):
                    if is_valid(board, i, j, num):
                        current_constraint += 1
                if current_constraint < min_constraint:
                    min_constraint = current_constraint
                    candidates = [(i, j)]
                elif current_constraint == min_constraint:
                    candidates.append((i, j))
    
    if candidates:
        min_row, min_col = random.choice(candidates)
    
    return min_row, min_col, min_constraint

# convert a string of numbers to a 2D list (board) (given '0' for empty cells)
def string_to_board(s):
    """
    Converts a string representation of a Sudoku board into a 2D list.
    Args:
        s (str): A string of length 81 representing the Sudoku board, where each character is a digit from 0-9.
    Returns:
        list: A 2D list (9x9) representing the Sudoku board, where each element is an integer.
    """

    board = []
    s = s.replace("\n", "")
    s = s.replace("/", "")
    s = s.replace(" ", "")

    if len(s) != 81:
        raise ValueError("Invalid input length. Must be 81 digits.")

    for i in range(9):
        row = []
        for j in range(9):
            row.append(int(s[i * 9 + j]))
        board.append(row)
    return board

def board_to_string(board):
    """
    Converts a 2D list representation of a Sudoku board into a string.
    Args:
        board (list of list of int): A 9x9 list representing the Sudoku board.
    Returns:
        str: A string of length 81 representing the Sudoku board, where each character is a digit from 0-9.
    """

    s = ""
    for i in range(9):
        for j in range(9):
            s += str(board[i][j])
        s += "/"
    return s

# check if the board is solved
def is_solved(board):
    """
    Check if a Sudoku board is solved.
    Args:
        board (list of list of int): The 9x9 Sudoku board.
    Returns:
        bool: True if the board is solved, False otherwise.
    """

    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return False
    return True


class Board:
    """
    A class representing a Sudoku board.
    Attributes:
        board (list of list of int): A 9x9 list representing the Sudoku board.
    """

    def __init__(self, board=None):
        """
        Initialize the Board class.
        Args:
            board (list of list of int, optional): A 9x9 list representing the Sudoku board. Defaults to None.
        """
        if board is None:
            self.board = [[0 for _ in range(9)] for _ in range(9)]
        else:
            self.board = board

    def __iter__(self):
        """
        Make the Board class iterable by rows.
        Returns:
            iterator: An iterator over the rows of the board.
        """
        return iter(self.board)

    def add(self, row, col, num):
        """
        Add a number to the board at the specified position.
        Args:
            row (int): The row index where the number is to be placed.
            col (int): The column index where the number is to be placed.
            num (int): The number to be placed in the given position.
        Returns:
            bool: True if the number was successfully added, False otherwise.
        """
        row = int(row - 1)
        col = int(col - 1)
        if is_valid(self.board, row, col, num):
            self.board[row][col] = num
            print("Number on row", row+1, "col", col+1, "added successfully!")
        elif self.board[row][col] == num:
            print("Number already exists in the cell!")
        elif self.board[row][col] != 0:
            print("Number already exists in the cell!")
        else:
            print("Invalid number! Try again.")
        pass

    def remove(self, row, col):
        """
        Remove a number from the board at the specified position.
        Args:
            row (int): The row index where the number is to be removed.
            col (int): The column index where the number is to be removed.
        """
        row = int(row - 1)
        col = int(col - 1)
        if self.board[row][col] == 0:
            print("Cell is already empty!")
            pass
        self.board[row][col] = 0
        print("Number on row", row+1, "col", col+1, "removed successfully!")
        pass


    def is_valid(self, row, col, num):
        """
        Check if a number can be placed in a given position on the Sudoku board without violating Sudoku rules.
        Args:
            row (int): The row index where the number is to be placed.
            col (int): The column index where the number is to be placed.
            num (int): The number to be placed in the given position.
        Returns:
            bool: True if the number can be placed in the given position, False otherwise.
        """
        return is_valid(self.board, row, col, num)

    def is_solved(self):
        """
        Check if the Sudoku board is solved.
        Returns:
            bool: True if the board is solved, False otherwise.
        """
        return is_solved(self.board)

    def find_constraint(self):
        """
        Finds the cell with the minimum number of possible values (constraints) in the Sudoku board.
        Returns:
            tuple: A tuple (min_row, min_col, constraint) where min_row and min_col are the row and column indices of the cell 
                   with the minimum number of possible values, and constraint is the number of possible values for that cell.
        """
        return find_constraint(self.board)

    def string_to_board(self, s):
        """
        Converts a string representation of a Sudoku board into a 2D list.
        Args:
            s (str): A string of length 81 representing the Sudoku board, where each character is a digit from 0-9.
        """
        self.board = string_to_board(s)
        return self.board
    
    def board_to_string(self):
        """
        Converts a 2D list representation of a Sudoku board into a string.
        Returns:
            str: A string of length 81 representing the Sudoku board, where each character is a digit from 0-9.
        """
        return board_to_string(self.board)

