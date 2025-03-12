"""
Sudoku Tips Giver
Copyright (c) 2025 Sudoku Tips Giver

A web application that helps users solve Sudoku puzzles with intelligent hints.
"""

from flask import Flask, render_template, jsonify, request
from functions import Board, is_valid
from sudoku_solver import get_next_hint, solve_sudoku
import random
import copy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

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

def generate_sudoku(difficulty='medium'):
    # 根据难度设置保留的数字数量范围
    difficulty_ranges = {
        'easy': (35, 40),
        'medium': (25, 30),
        'hard': (20, 25)
    }
    min_numbers, max_numbers = difficulty_ranges.get(difficulty, (25, 30))  # 默认中等难度
    
    board = [[0]*9 for _ in range(9)]
    solution = None
    
    # 首先生成一个完整的有效数独
    def fill_board(board):
        empty = find_empty(board)
        if not empty:
            return True
            
        row, col = empty
        nums = list(range(1, 10))
        random.shuffle(nums)  # 随机打乱数字顺序
        
        for num in nums:
            if is_valid(board, row, col, num):
                board[row][col] = num
                if fill_board(board):
                    return True
                board[row][col] = 0
        return False
    
    def find_empty(board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 0:
                    return (i, j)
        return None
    
    def is_valid(board, row, col, num):
        # 检查行
        for x in range(9):
            if board[row][x] == num:
                return False
        
        # 检查列
        for x in range(9):
            if board[x][col] == num:
                return False
        
        # 检查3x3方格
        start_row = row - row % 3
        start_col = col - col % 3
        for i in range(3):
            for j in range(3):
                if board[i + start_row][j + start_col] == num:
                    return False
        return True
    
    # 生成完整的数独解
    fill_board(board)
    solution = copy.deepcopy(board)
    
    # 获取所有填充的位置
    filled_positions = [(i, j) for i in range(9) for j in range(9)]
    random.shuffle(filled_positions)
    
    # 计算需要移除的数字数量
    total_numbers = 81
    target_numbers = random.randint(min_numbers, max_numbers)
    numbers_to_remove = total_numbers - target_numbers
    
    # 逐个移除数字，确保保持唯一解
    removed = 0
    for pos in filled_positions:
        if removed >= numbers_to_remove:
            break
            
        row, col = pos
        temp = board[row][col]
        board[row][col] = 0
        
        # 如果移除后不再具有唯一解，恢复该数字
        board_copy = copy.deepcopy(board)
        if not has_unique_solution(board_copy):
            board[row][col] = temp
        else:
            removed += 1
    
    return board, solution

@app.route('/generate', methods=['POST'])
def generate():
    try:
        data = request.get_json()
        difficulty = data.get('difficulty', 'medium')  # 如果未指定难度，默认为中等
        board, solution = generate_sudoku(difficulty)
        return jsonify({
            'success': True,
            'board': board,
            'solution': solution
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'message': '生成数独时发生错误'
        })

@app.route('/get_hint', methods=['POST'])
def hint():
    try:
        data = request.json
        if not data or 'board' not in data:
            return jsonify({
                'success': False,
                'message': '无效的请求数据'
            })

        board_str = ''.join([''.join(map(str, row)) for row in data['board']])
        board = Board()
        board.string_to_board(board_str)
        
        # 先获取完整解
        solved_board = [row[:] for row in board.board]  # 创建深拷贝
        if not solve_sudoku(solved_board):
            return jsonify({
                'success': False,
                'message': '这个数独没有解！'
            })
        
        # 获取下一步提示
        result = get_next_hint(board.board)
        if result[0] is None:
            return jsonify({
                'success': False,
                'message': result[1]
            })
        else:
            row, col, num, message = result
            return jsonify({
                'success': True,
                'row': row,
                'col': col,
                'number': num,
                'message': message,
                'possible_numbers': [n for n in range(1, 10) if is_valid(board.board, row, col, n)],
                'solved_board': solved_board  # 返回完整解
            })
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'处理请求时发生错误: {str(e)}'
        })

if __name__ == '__main__':
    app.run(debug=True) 