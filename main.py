from functions import Board
from sudoku_solver import get_next_hint

def main():
    print("欢迎使用数独提示器！")
    print("请输入数独题目（使用0表示空格，可以用空格或/分隔）")
    print("例如：001030000/002000040/006501029/230607080/000803000/010004367/420108500/080000000/000070408")
    
    while True:
        # 获取用户输入
        s = input("\n请输入数独（输入q退出）：")
        if s.lower() == 'q':
            break
        
        try:
            # 创建数独板
            board = Board()
            board.string_to_board(s)
            
            # 打印当前数独
            print("\n当前数独：")
            for row in board.board:
                print(row)
            
            # 获取提示
            result = get_next_hint(board.board)
            if result[0] is None:
                print("\n提示：", result[1])
            else:
                row, col, num, message = result
                print("\n提示：", message)
                
                if num is not None:
                    answer = input("是否要填入这个数字？(y/n)：")
                    if answer.lower() == 'y':
                        board.add(row+1, col+1, num)
                        print("\n更新后的数独：")
                        for row in board.board:
                            print(row)
        
        except Exception as e:
            print("错误：", str(e))
            print("请确保输入格式正确！")

if __name__ == "__main__":
    main() 