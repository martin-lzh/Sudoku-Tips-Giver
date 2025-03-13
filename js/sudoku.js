/**
 * Sudoku Tips Giver
 * Copyright (c) 2025 Sudoku Tips Giver
 * 
 * Core Sudoku logic implementation in JavaScript
 */

class SudokuBoard {
    constructor() {
        this.board = Array(9).fill().map(() => Array(9).fill(0));
        this.solution = null;
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

    // 生成数独题目
    generatePuzzle(difficulty) {
        // 清空棋盘
        this.board = Array(9).fill().map(() => Array(9).fill(0));
        
        // 生成完整解
        this.generateSolution();
        
        // 保存完整解
        this.solution = JSON.parse(JSON.stringify(this.board));
        
        // 根据难度移除数字
        let cellsToRemove;
        switch(difficulty) {
            case 'easy':
                cellsToRemove = 45; // 保留35-40个数字
                break;
            case 'medium':
                cellsToRemove = 55; // 保留25-30个数字
                break;
            case 'hard':
                cellsToRemove = 65; // 保留20-25个数字
                break;
        }

        // 随机移除数字
        let positions = Array.from({length: 81}, (_, i) => i);
        positions = this.shuffleArray(positions);
        
        for (let i = 0; i < cellsToRemove; i++) {
            let pos = positions[i];
            let row = Math.floor(pos / 9);
            let col = pos % 9;
            this.board[row][col] = 0;
        }

        return this.board;
    }

    // 获取提示
    getHint() {
        // 找到第一个空格子
        for (let i = 0; i < 9; i++) {
            for (let j = 0; j < 9; j++) {
                if (this.board[i][j] === 0) {
                    return {
                        row: i,
                        col: j,
                        value: this.solution[i][j]
                    };
                }
            }
        }
        return null;
    }

    // 检查是否有唯一解
    hasUniqueSolution() {
        let solutions = 0;
        let tempBoard = JSON.parse(JSON.stringify(this.board));
        
        const countSolutions = (board, row, col) => {
            if (solutions > 1) return;
            
            if (row === 9) {
                solutions++;
                return;
            }
            
            if (col === 9) {
                countSolutions(board, row + 1, 0);
                return;
            }
            
            if (board[row][col] !== 0) {
                countSolutions(board, row, col + 1);
                return;
            }
            
            for (let num = 1; num <= 9; num++) {
                if (this.isValid(row, col, num)) {
                    board[row][col] = num;
                    countSolutions(board, row, col + 1);
                    board[row][col] = 0;
                }
            }
        };
        
        countSolutions(tempBoard, 0, 0);
        return solutions === 1;
    }

    // 工具函数：打乱数组
    shuffleArray(array) {
        for (let i = array.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [array[i], array[j]] = [array[j], array[i]];
        }
        return array;
    }
}

// 导出类供其他模块使用
if (typeof module !== 'undefined' && module.exports) {
    module.exports = SudokuBoard;
} 