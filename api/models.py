import re
from flask import request, abort, jsonify

class TicTacToe(object):
    """
    board: a nine-character string of spaces, x's and o's (lowercase).
    player: the character 'x' or 'o'
    """
    
    def is_board_valid(self,board):
        """ 
        Check if both whether the board is a valid representation of a tictacoe board, and whether it could be o's turn. 
        """
        valid = re.match(r'^[o x]{9}$', board) and (board.count("x") - board.count("o") in [0, 1])
        if valid == True:
            return valid
        else:
            return False
    
    def opponent(self,player):
        """
        return the opponent
        """
        return {'o': 'x', 'x': 'o'}[player]
    
    def is_tie(self, board):
        """ 
        Checks if the result of the game is a tie
        """
        if ' ' in board:
            return False 
        else:
            return True
    
    def is_winner(self,board, player):
        """ 
        Checks if the result of the game is a win
        """
        win = [player, player, player]
        win_horizontal = [
            [board[0], board[1], board[2]] == win,
            [board[3], board[4], board[5]] == win,
            [board[6], board[7], board[8]] == win
        ]
        win_vertical = [
            [board[0], board[3], board[6]] == win,
            [board[1], board[4], board[7]] == win,
            [board[2], board[5], board[8]] == win
        ]
        win_diagonal = [
            [board[0], board[4], board[8]] == win,
            [board[2], board[4], board[6]] == win
        ]
        return any(win_horizontal) or any(win_vertical) or any(win_diagonal)
    
    def move(self, board, index, player):
        """ 
        Plays a move by player at that index, returning a new state of the board. 
        """
        splitted_board = list(board)
        splitted_board[index] = player
        return "".join(splitted_board)
    
    def expected_boards(self,board, player):
        """ 
        Returns a list of  boards that are expected from player's next move. 
        """
        return [self.move(board, i, player) for i, char in enumerate(board) if char == " "]
    
    def score(self,board, player):
        """ Returns -1 if player will lose on this board, 0 if player can tie, and 1 if player can win. """
        opp = self.opponent(player)
        if self.is_winner(board, player):
            return 1
        if self.is_winner(board, opp):
            return -1 
        if self.is_tie(board):
            return 0

        return max(-1 * self.score(candidate, opp) for candidate in self.expected_boards(board, player))