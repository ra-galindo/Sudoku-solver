from flask import Flask, render_template, request
from sudoku_solver import solve_sudoku

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve():
    # Get the board input from the form
    board = request.form.getlist('board[]')
    
    # Convert the input strings to integers, and replace empty strings with 0
    board = [list(map(lambda x: int(x) if x else 0, board[i:i+9])) for i in range(0, 81, 9)]
    
    # Try to solve the Sudoku puzzle
    if solve_sudoku(board):
        return render_template('index.html', board=board)
    else:
        return render_template('index.html', board=None, error="No solution exists")


if __name__ == '__main__':
    app.run(debug=True)
