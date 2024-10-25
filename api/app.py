import os
from flask import Flask, render_template, request, jsonify
from sudoku_solver import solve_sudoku, is_valid

app = Flask(__name__, template_folder=os.path.abspath('templates'))

@app.route('/')
def index():
    """Render the main page with an input form."""
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve():
    """Receive and solve the Sudoku puzzle."""
    data = request.json.get('puzzle')
    if not data or len(data) != 9 or any(len(row) != 9 for row in data):
        return jsonify({"error": "Invalid input. The board must be 9x9."}), 400

    board = [[int(num) for num in row] for row in data]
    # Check if the initial board configuration is valid
    if not is_valid(board):
        return jsonify({"error": "This puzzle is unsolvable."}), 400

    if solve_sudoku(board):
        return jsonify({"solution": board})
    else:
        return jsonify({"error": "This puzzle is unsolvable."}), 400

if __name__ == '__main__':
    app.run(debug=True)
