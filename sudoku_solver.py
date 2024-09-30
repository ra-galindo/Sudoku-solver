# sudoku_solver.py

def is_valid(board, row, col, num):
    # Check if 'num' is not in the current row, column and 3x3 box
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    
    box_start_row = row - row % 3
    box_start_col = col - col % 3
    
    for i in range(3):
        for j in range(3):
            if board[box_start_row + i][box_start_col + j] == num:
                return False
                
    return True

def solve_sudoku(board):
    empty = find_empty_location(board)
    if not empty:
        return True  # No empty location, solved

    row, col = empty

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0  # Reset on failure

    return False

def find_empty_location(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None
