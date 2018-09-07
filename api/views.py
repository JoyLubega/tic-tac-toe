from flask import Flask, request, jsonify, abort
from models import TicTacToe

app = Flask(__name__)

tic= TicTacToe()
@app.route('/game')
def newgame():
    board = request.args.get('board')
    if board is None:
        return jsonify({'error':'enter the board please'})
    if tic.is_board_valid(board)== False:
        return jsonify({'error':'The board is invalid'})
    possible_boards = tic.expected_boards(board, 'o') # all plays
    winning_board=max(possible_boards, key=lambda candidate: -1 * tic.score(candidate, 'x'))
    return jsonify({"next_board":winning_board})
    
    # return tic.expected_boards(board, player='o')[0]
    
    
    # if tic.is_board_valid(board=board) == False:
    #     return jsonify({'error':'The board is invalid'})

    # or not tic.is_board_valid(board):
    #    abort(400)
    # return board
    
