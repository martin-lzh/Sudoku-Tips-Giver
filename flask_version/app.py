"""
Sudoku Tips Giver
Copyright (c) 2025 Sudoku Tips Giver

A web application that helps users solve Sudoku puzzles with intelligent hints.
"""

from flask import Flask, render_template, jsonify, request
from functions import Board, is_valid
from sudoku_solver import get_next_hint, solve_sudoku, has_unique_solution
import random
import copy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

board = Board()

@app.route('/')
def index():
    return render_template('index.html', title='数独提示器 | Sudoku Tips Giver')

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
        
        # 获取下一步提示
        result = get_next_hint(board.board)
        if result[0] is None:
            return jsonify({
                'success': False,
                'message': result[1]
            })
        
        row, col, num, message = result
        
        # 获取这个位置所有可能的数字
        possible_numbers = []
        for n in range(1, 10):
            if is_valid(board.board, row, col, n):
                possible_numbers.append(n)
        
        # 找到最少可能性的格子
        min_row, min_col, min_constraint = board.find_constraint()
        is_minimal = (row == min_row and col == min_col)
        
        return jsonify({
            'success': True,
            'row': row,
            'col': col,
            'number': num,  # 如果只有一个可能的数字，这里会有值
            'possible_numbers': possible_numbers,
            'is_minimal': is_minimal,  # 标记是否是最少可能性的格子
            'message': message
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'处理请求时发生错误: {str(e)}'
        })

@app.route('/add_draft', methods=['POST'])
def add_draft():
    data = request.get_json()
    row = data.get('row')
    col = data.get('col')
    number = data.get('number')
    
    if None in (row, col, number):
        return jsonify({'success': False, 'error': 'Missing data'}), 400
    
    try:
        board.add_draft_number(row, col, number)
        draft_numbers = board.get_draft_numbers(row, col)
        return jsonify({
            'success': True,
            'draft_numbers': sorted(list(draft_numbers))
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

@app.route('/remove_draft', methods=['POST'])
def remove_draft():
    data = request.get_json()
    row = data.get('row')
    col = data.get('col')
    number = data.get('number')
    
    if None in (row, col, number):
        return jsonify({'success': False, 'error': 'Missing data'}), 400
    
    try:
        board.remove_draft_number(row, col, number)
        draft_numbers = board.get_draft_numbers(row, col)
        return jsonify({
            'success': True,
            'draft_numbers': sorted(list(draft_numbers))
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

@app.route('/clear_draft', methods=['POST'])
def clear_draft():
    data = request.get_json()
    row = data.get('row')
    col = data.get('col')
    
    if None in (row, col):
        return jsonify({'success': False, 'error': 'Missing data'}), 400
    
    try:
        board.clear_draft_numbers(row, col)
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

@app.route('/clear_all_drafts', methods=['POST'])
def clear_all_drafts():
    try:
        board.clear_all_draft_numbers()
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True) 