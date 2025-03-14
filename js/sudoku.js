/**
 * Sudoku Tips Giver
 * Copyright (c) 2025 Sudoku Tips Giver
 * 
 * Core Sudoku logic implementation in JavaScript
 */

class SudokuBoard {
    constructor(savedState = null) {
        if (savedState) {
            // 从保存的状态恢复
            this.board = savedState.board;
            this.solution = savedState.solution;
            this.initialCells = new Set(savedState.initialCells);
            
            // 初始化草稿数组
            this.draftNumbers = Array(9).fill().map(() => 
                Array(9).fill().map(() => new Set())
            );
            
            // 从保存的状态恢复草稿数字
            if (savedState.draftNumbers) {
                for (let i = 0; i < 9; i++) {
                    for (let j = 0; j < 9; j++) {
                        if (savedState.draftNumbers[i] && savedState.draftNumbers[i][j]) {
                            const numbers = savedState.draftNumbers[i][j];
                            numbers.forEach(num => this.draftNumbers[i][j].add(num));
                        }
                    }
                }
            }
        } else {
            // 创建新的状态
            this.board = Array(9).fill().map(() => Array(9).fill(0));
            this.solution = null;
            this.initialCells = new Set();
            this.draftNumbers = Array(9).fill().map(() => 
                Array(9).fill().map(() => new Set())
            );
        }
    }

    // 用于序列化的方法
    toJSON() {
        return {
            board: this.board,
            solution: this.solution,
            initialCells: Array.from(this.initialCells),
            draftNumbers: this.draftNumbers.map(row =>
                row.map(cell => Array.from(cell))
            )
        };
    }

    // 检查数字在指定位置是否有效
    isValid(row, col, num) {
        // 检查行
        for (let x = 0; x < 9; x++) {
            if (this.board[row][x] === num) return false;
        }

        // 检查列
        for (let x = 0; x < 9; x++) {
            if (this.board[x][col] === num) return false;
        }

        // 检查3x3方格
        let startRow = row - row % 3;
        let startCol = col - col % 3;
        for (let i = 0; i < 3; i++) {
            for (let j = 0; j < 3; j++) {
                if (this.board[i + startRow][j + startCol] === num) return false;
            }
        }

        return true;
    }

    // 生成完整的数独解
    generateSolution() {
        let numbers = Array.from({length: 9}, (_, i) => i + 1);
        for (let i = 0; i < 9; i++) {
            for (let j = 0; j < 9; j++) {
                if (this.board[i][j] === 0) {
                    numbers = this.shuffleArray(numbers);
                    for (let num of numbers) {
                        if (this.isValid(i, j, num)) {
                            this.board[i][j] = num;
                            if (this.generateSolution()) {
                                return true;
                            }
                            this.board[i][j] = 0;
                        }
                    }
                    return false;
                }
            }
        }
        return true;
    }

    // 检查当前数独谜题是否有唯一解
    hasUniqueSolution() {
        // 创建棋盘副本
        const tmpBoard = JSON.parse(JSON.stringify(this.board));
        let solutionCount = 0;
        
        // 辅助函数：检查是否可以放置数字
        const isValidPlacement = (board, row, col, num) => {
            // 检查行
            for (let x = 0; x < 9; x++) {
                if (board[row][x] === num) return false;
            }
            
            // 检查列
            for (let x = 0; x < 9; x++) {
                if (board[x][col] === num) return false;
            }
            
            // 检查3x3方格
            const startRow = row - row % 3;
            const startCol = col - col % 3;
            for (let i = 0; i < 3; i++) {
                for (let j = 0; j < 3; j++) {
                    if (board[i + startRow][j + startCol] === num) return false;
                }
            }
            
            return true;
        };
        
        // 递归解数独
        const solve = (board) => {
            // 如果已经找到多个解，就停止搜索
            if (solutionCount > 1) return;
            
            // 寻找空格子
            let emptyCell = null;
            for (let i = 0; i < 9 && !emptyCell; i++) {
                for (let j = 0; j < 9 && !emptyCell; j++) {
                    if (board[i][j] === 0) {
                        emptyCell = { row: i, col: j };
                    }
                }
            }
            
            // 如果没有空格子，找到一个解
            if (!emptyCell) {
                solutionCount++;
                return;
            }
            
            const { row, col } = emptyCell;
            
            // 尝试每个数字
            for (let num = 1; num <= 9; num++) {
                if (isValidPlacement(board, row, col, num)) {
                    board[row][col] = num;
                    solve(board);
                    board[row][col] = 0; // 回溯
                }
            }
        };
        
        solve(tmpBoard);
        
        // 返回是否只有一个解
        return solutionCount === 1;
    }

    // 生成数独题目
    generatePuzzle(difficulty) {
        // 清空棋盘和初始格子集合
        this.board = Array(9).fill().map(() => Array(9).fill(0));
        this.initialCells.clear();
        
        // 生成完整解
        this.generateSolution();
        
        // 保存完整解
        this.solution = JSON.parse(JSON.stringify(this.board));
        
        // 根据难度确定要移除的数字数量
        let cellsToRemove;
        switch(difficulty) {
            case 'easy':
                cellsToRemove = 40; // 保留40-45个数字
                break;
            case 'medium':
                cellsToRemove = 50; // 保留30-35个数字
                break;
            case 'hard':
                cellsToRemove = 60; // 保留20-25个数字
                break;
            default:
                cellsToRemove = 50; // 默认中等难度
        }

        // 随机排序所有位置
        let positions = Array.from({length: 81}, (_, i) => i);
        positions = this.shuffleArray(positions);
        
        // 逐个尝试移除数字，并保证唯一解
        for (let i = 0; i < positions.length && cellsToRemove > 0; i++) {
            let pos = positions[i];
            let row = Math.floor(pos / 9);
            let col = pos % 9;
            
            // 暂存当前值
            let temp = this.board[row][col];
            
            // 尝试移除
            this.board[row][col] = 0;
            
            // 检查是否仍有唯一解
            if (this.hasUniqueSolution()) {
                cellsToRemove--; // 成功移除一个数字
            } else {
                // 如果没有唯一解，则恢复
                this.board[row][col] = temp;
            }
        }

        // 记录初始数字的位置
        for (let i = 0; i < 9; i++) {
            for (let j = 0; j < 9; j++) {
                if (this.board[i][j] !== 0) {
                    this.initialCells.add(`${i},${j}`);
                }
            }
        }

        this.clearAllDraftNumbers();  // 生成新题目时清除所有草稿
        return this.board;
    }

    // 找到最受约束的空格子
    findMostConstrainedCell() {
        let minPossibilities = 10;
        let candidates = [];
        
        for (let i = 0; i < 9; i++) {
            for (let j = 0; j < 9; j++) {
                if (this.board[i][j] === 0) {
                    let possibleCount = 0;
                    for (let num = 1; num <= 9; num++) {
                        if (this.isValid(i, j, num)) {
                            possibleCount++;
                        }
                    }
                    if (possibleCount < minPossibilities) {
                        minPossibilities = possibleCount;
                        candidates = [{row: i, col: j}];
                    } else if (possibleCount === minPossibilities) {
                        candidates.push({row: i, col: j});
                    }
                }
            }
        }
        
        if (candidates.length > 0) {
            // 随机选择一个候选位置，增加趣味性
            const randomIndex = Math.floor(Math.random() * candidates.length);
            return candidates[randomIndex];
        }
        return null;
    }

    // 获取提示
    getHint() {
        // 检查是否有空格子
        let hasEmpty = false;
        for (let i = 0; i < 9; i++) {
            for (let j = 0; j < 9; j++) {
                if (this.board[i][j] === 0) {
                    hasEmpty = true;
                    break;
                }
            }
            if (hasEmpty) break;
        }

        if (!hasEmpty) {
            return null;
        }

        // 找到最受约束的格子
        const bestCell = this.findMostConstrainedCell();
        if (!bestCell) {
            return null;
        }

        // 计算可能的数字
        let possibleNumbers = [];
        for (let num = 1; num <= 9; num++) {
            if (this.isValid(bestCell.row, bestCell.col, num)) {
                possibleNumbers.push(num);
            }
        }

        return {
            row: bestCell.row,
            col: bestCell.col,
            possibleNumbers: possibleNumbers,
            value: this.solution ? this.solution[bestCell.row][bestCell.col] : null
        };
    }

    // 检查是否完成
    isCompleted() {
        // 检查是否填满
        for (let i = 0; i < 9; i++) {
            for (let j = 0; j < 9; j++) {
                if (this.board[i][j] === 0) {
                    return false;
                }
            }
        }

        // 检查每一行
        for (let i = 0; i < 9; i++) {
            let row = new Set();
            for (let j = 0; j < 9; j++) {
                if (row.has(this.board[i][j])) {
                    return false;
                }
                row.add(this.board[i][j]);
            }
        }

        // 检查每一列
        for (let j = 0; j < 9; j++) {
            let col = new Set();
            for (let i = 0; i < 9; i++) {
                if (col.has(this.board[i][j])) {
                    return false;
                }
                col.add(this.board[i][j]);
            }
        }

        // 检查每个3x3方格
        for (let block = 0; block < 9; block++) {
            let square = new Set();
            let startRow = Math.floor(block / 3) * 3;
            let startCol = (block % 3) * 3;
            for (let i = 0; i < 3; i++) {
                for (let j = 0; j < 3; j++) {
                    let num = this.board[startRow + i][startCol + j];
                    if (square.has(num)) {
                        return false;
                    }
                    square.add(num);
                }
            }
        }

        return true;
    }

    // 检查格子是否为初始数字
    isInitialCell(row, col) {
        return this.initialCells.has(`${row},${col}`);
    }

    // 工具函数：打乱数组
    shuffleArray(array) {
        for (let i = array.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [array[i], array[j]] = [array[j], array[i]];
        }
        return array;
    }

    // 添加草稿数字
    addDraftNumber(row, col, num) {
        if (!this.isInitialCell(row, col) && this.board[row][col] === 0) {
            this.draftNumbers[row][col].add(num);
        }
    }

    // 移除草稿数字
    removeDraftNumber(row, col, num) {
        if (this.draftNumbers[row] && this.draftNumbers[row][col]) {
            this.draftNumbers[row][col].delete(num);
        }
    }

    // 获取格子的草稿数字
    getDraftNumbers(row, col) {
        return Array.from(this.draftNumbers[row][col]);
    }

    // 清除格子的所有草稿数字
    clearDraftNumbers(row, col) {
        if (this.draftNumbers[row] && this.draftNumbers[row][col]) {
            this.draftNumbers[row][col].clear();
        }
    }

    // 清除所有草稿数字
    clearAllDraftNumbers() {
        this.draftNumbers = Array(9).fill().map(() => 
            Array(9).fill().map(() => new Set())
        );
    }

    // 重写清空棋盘方法，添加清除草稿的功能
    clear() {
        this.board = Array(9).fill().map(() => Array(9).fill(0));
        this.solution = null;
        this.initialCells.clear();
        this.clearAllDraftNumbers();
    }
}

// 导出类供其他模块使用
if (typeof module !== 'undefined' && module.exports) {
    module.exports = SudokuBoard;
}