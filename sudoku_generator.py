import random
import math

SUDOKU_SIZE = 9
EMPTY_CELL = -1
SUB_SQUARE = int(math.sqrt(SUDOKU_SIZE))

def generate_random_sudoku(k):
    board = [[EMPTY_CELL for _ in range(SUDOKU_SIZE)] for _ in range(SUDOKU_SIZE)]


    def fill_diagonal():
        for i in range(0, SUDOKU_SIZE, SUB_SQUARE):
            fill_space(i, i)


    def fill_space(row, col):
        for i in range(SUB_SQUARE):
            for j in range(SUB_SQUARE):
                while True:
                    num = random_generator(SUDOKU_SIZE)
                    if digit_unused_in_subsquare(row, col, num):
                        board[row + i][col + j] = num
                        break


    def random_generator(nr):
        return math.floor(random.random() * nr + 1)
    

    def digit_unused_in_subsquare(row, col, num):
        for i in range(SUB_SQUARE):
            for j in range(SUB_SQUARE):
                if board[row + i][col + j] == num:
                    return False
        return True


    def is_safe_to_place(row, col, num):
        if any(board[row][x] == num for x in range(SUDOKU_SIZE)):
            return False
        if any(board[x][col] == num for x in range(SUDOKU_SIZE)):
            return False
        
        start_row, start_col = row - row % SUB_SQUARE, col - col % SUB_SQUARE
        return digit_unused_in_subsquare(start_row, start_col, num)

    def fill_remaining(i, j):
        if i == SUDOKU_SIZE - 1 and j == SUDOKU_SIZE:
            return True
        if j == SUDOKU_SIZE:
            i += 1
            j = 0
        if board[i][j] != EMPTY_CELL:
            return fill_remaining(i, j + 1)

        for num in range(1, SUDOKU_SIZE + 1):
            if is_safe_to_place(i, j, num):
                board[i][j] = num
                if fill_remaining(i, j + 1):
                    return True
                board[i][j] = EMPTY_CELL

        return False

    def remove_cells(count):
        while count > 0:
            row = random.randint(0, SUDOKU_SIZE - 1)
            col = random.randint(0, SUDOKU_SIZE - 1)
            if board[row][col] != EMPTY_CELL:
                board[row][col] = EMPTY_CELL
                count -= 1

    fill_diagonal()

    fill_remaining(0, SUB_SQUARE)

    remove_cells(k)

    return board

