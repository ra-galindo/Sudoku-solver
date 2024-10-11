from flask import Flask, render_template, request
from flask_frozen import Freezer
from sudoku_solver import solve_sudoku

app = Flask(__name__)
freezer = Freezer(app)

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

# Command to freeze the app and generate static files
if __name__ == '__main__':
    app.run(debug=True)
    
@freezer.register_generator
def url_generator():
    yield '/'
