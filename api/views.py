from flask import Flask, request, jsonify
from api.models import TicTacToe


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
    if (board == ''):
        return jsonify({'error': 'Board can not be empty'}), 400
    if tic.is_winner(board, 'o') is True:
        return jsonify({'Message': 'The board provide is a tie'}), 400

    if tic.is_board_valid(board) is False:

        return jsonify({'error': 'The board is invalid'}), 400

    if tic.is_tie(board) is True:
        return jsonify({'Message': 'The board is a tie'}), 400
    if tic.is_winner(board, 'o'):
        return jsonify({'Message': 'Player O is the winner'}), 400

    possible_boards = tic.expected_boards(board, 'o') # all boards of the given player (o) # noqa E501
    winning_board=max(possible_boards, key = lambda candidate: -1 * tic.score(candidate, 'o')) # noqa E501

    return jsonify({
                "next_board": winning_board
                                    })
