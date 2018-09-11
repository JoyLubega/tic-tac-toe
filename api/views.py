from flask import Flask, request, jsonify
from api.tictactoe import TicTacToe
import random
import unicodedata




app = Flask(__name__)

tic = TicTacToe()


@app.route('/game')
def newgame():
    """
    Get request to return the next board
    """
    board = request.args.get('board')
    
    if board is None:
        return jsonify({'error': 'enter the board please'}), 400
        
    if len(board) < 9:
        response = jsonify({'Error': 'Board is short'})
        response.status_code = 400
        return response
    
    if tic.is_board_valid(board) is False:

        return jsonify({'error': 'The board is invalid'}), 400

    if tic.is_tie(board) is True:
        return jsonify({'Message': 'The board is a tie'}), 400
    if tic.is_winner(board, 'o'):
        return jsonify({'Message': 'Player O is the winner'}), 400
    # print(determine(board=board, player='o'))
    if board.count('o') - board.count('x') == 1 :
        next_player= 'x'
    if (board.count('x') - board.count('o') == 1) or (board.count('x') - board.count('o') == 0):
        next_player= 'o'

    if next_player == 'o':
        the_move = tic.getmove_server(board,'o')
        new = unicodedata.normalize('NFKD', board).encode('ascii','ignore')
        sep_list = list(new)
        sep_list[the_move]='o'
        next_board = "".join(sep_list)
        
        return jsonify({
                "next_board": next_board
                                    })

    if next_player == 'x': 
        possible_boards  = tic.expected_boards(board, next_player) # all boards of the given player # noqa E501
        return jsonify({
                "next_board": possible_boards[0]
                                    })

   
