from flask import Flask, request, jsonify, abort
from flask_optimize import FlaskOptimize
from api.models import TicTacToe
 

app = Flask(__name__)
flask_optimize = FlaskOptimize()



tic= TicTacToe()

    
@app.route('/game')
# @flask_optimize.optimize()
def newgame():
    """
    Get request to return the next board
    """
    board = request.args.get('board')
              
    if board is None:
        return jsonify({'error':'enter the board please'}) ,400
    if (board == ''):
        return jsonify({'error':'Board can not be empty'}) ,400
    if tic.is_winner(board,'o') == True:
        return jsonify({'Message':'The board provide is a tie'}) ,400

    if tic.is_board_valid(board)== False:
        
        return jsonify({'error':'The board is invalid'}), 400

    if tic.is_tie(board) == True  :
        return jsonify({'Message':'The board is a tie'}), 400
    if tic.is_winner(board,'o'):
        return jsonify({'Message':'Player O is the winner'}), 400

    
    possible_boards = tic.expected_boards(board, 'o') # all boards of the given player (o)
    winning_board=max(possible_boards, key=lambda candidate: -1 * tic.score(candidate, 'o'))
    
    return jsonify({
                "next_board":winning_board
                                    })
