"""
Sudoku Tips Giver
Copyright (c) 2025 Sudoku Tips Giver

Sudoku solving algorithm implementation and hint generation.
"""

from functions import Board, is_valid
import copy

def solve_sudoku(board):
    """
    使用回溯法解数独
    Args:
        board: 数独棋盘（二维列表）
    Returns:
        bool: 是否找到解
    """
    # 找到一个空位置
    empty = find_empty(board)
    if not empty:
        return True
    
    row, col = empty
    
    # 尝试填入1-9
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            
            if solve_sudoku(board):
                return True
            
            board[row][col] = 0
    
    return False

def find_empty(board):
    """
    找到数独中的一个空位置
    Args:
        board: 数独棋盘
    Returns:
        tuple: (row, col) 或 None
    """
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def count_solutions(board, limit=2):
    """
    计算数独解的数量，最多计算到limit个
    Args:
        board: 数独棋盘
        limit: 解的数量上限
    Returns:
        int: 解的数量
    """
    solutions = []
    
    def solve_recursive(board):
        if len(solutions) >= limit:
            return
        
        empty = find_empty(board)
        if not empty:
            solutions.append(copy.deepcopy(board))
            return
        
        row, col = empty
        for num in range(1, 10):
            if is_valid(board, row, col, num):
                board[row][col] = num
                solve_recursive(board)
                board[row][col] = 0
    
    board_copy = copy.deepcopy(board)
    solve_recursive(board_copy)
    return len(solutions)

def has_unique_solution(board):
    """检查数独是否有唯一解"""
    def solve_with_limit(board, limit=2):
        solutions = []
        
        def solve_recursive(board):
            if len(solutions) >= limit:
                return
            
            # 找到一个空位置
            empty = None
            for i in range(9):
                for j in range(9):
                    if board[i][j] == 0:
                        empty = (i, j)
                        break
                if empty:
                    break
            
            # 如果没有空位置，说明找到了一个解
            if not empty:
                solutions.append([row[:] for row in board])
                return
            
            row, col = empty
            # 尝试1-9的数字
            for num in range(1, 10):
                if is_valid(board, row, col, num):
                    board[row][col] = num
                    solve_recursive(board)
                    board[row][col] = 0
                    
                    # 如果已经找到两个解，可以提前返回
                    if len(solutions) >= limit:
                        return
        
        board_copy = [row[:] for row in board]
        solve_recursive(board_copy)
        return solutions
    
    # 寻找最多两个解，如果找到两个就说明不是唯一解
    solutions = solve_with_limit(board)
    return len(solutions) == 1

def get_next_hint(board):
    """
    获取下一步最佳提示
    Args:
        board: 数独棋盘
    Returns:
        tuple: (row, col, num, message) 或 None
    """
    # 首先检查是否有唯一解
    if not has_unique_solution(board):
        return None, "这个数独没有唯一解！"
    
    # 找到约束最多的空格
    row, col, constraint = Board(board).find_constraint()
    if row == -1 or col == -1:
        return None, "数独已完成！"
    
    # 找到这个位置可以填的数字
    possible_nums = []
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            possible_nums.append(num)
    
    if len(possible_nums) == 1:
        message = f"在第{row+1}行第{col+1}列，只能填入数字{possible_nums[0]}"
    else:
        message = f"在第{row+1}行第{col+1}列，可以填入的数字有: {possible_nums}"
    
    return (row, col, possible_nums[0] if len(possible_nums) == 1 else None, message) 