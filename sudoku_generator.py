import random

SUDOKU_SIZE = 9
EMPTY_CELL = -1

def is_valid(board, row, col, num):
    for i in range(SUDOKU_SIZE):
        if board[row][i] == num or board[i][col] == num:
            return False
    
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    
    return True


def generate_random_sudoku():
    board = [[EMPTY_CELL] * SUDOKU_SIZE for _ in range(SUDOKU_SIZE)]
    
    for row in range(SUDOKU_SIZE):
        for col in range(SUDOKU_SIZE):
            if board[row][col] == EMPTY_CELL:
                random_numbers = list(range(1, 10))
                random.shuffle(random_numbers)
                for num in random_numbers:
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        break
    
    return board