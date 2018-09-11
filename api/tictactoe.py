import re
import random


class TicTacToe(object):
    """
    board: a nine-character string of spaces, x's and o's (lowercase).
    player: the character 'x' or 'o'
    """

    def is_board_valid(self, board):
        """
        Check if both whether the board is a valid representation
        of a tictacoe board, and whether it could be o's turn.
        """
        valid = re.match(r'^[o x]{9}$', board)  and (board.count("x") - board.count("o") in [0, 1]) or (board.count("o") - board.count("x") in [0, 1]) # noqa E501
        if valid is True:
            return valid
        else:
            return False

    def opponent(self, player):
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

    def is_winner(self, board, player):
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
        Plays a move by player at that index,
        returning a new state of the board.
        """
        splitted_board = list(board)
        splitted_board[index] = player
        return "".join(splitted_board)

    def expected_boards(self, board, player):
        """
        Returns a list of  boards that are expected from player's next move.
        """
        
        return [self.move(board, i, player) for i, char in enumerate(board) if char == " "] # noqa E501

    def score(self, board, player):
        """
        Returns -1 if its a loss, 0 if its a  tie, and 1 if its a win.
        """
        opp = self.opponent(player)
        if self.is_winner(board, player):
            return 1
        if self.is_winner(board, opp):
            return -1
        if self.is_tie(board):
            return 0

        return max(-1 * self.score(candidate, opp) for candidate in self.expected_boards(board, player)) # noqa E501
    #####################################
    #### Make the computer smart  ###############

    def makeMove(self, board, letter, move):
        board[move] = letter
    def chooseRandomMoveFromList(self,board, movesList):

        possibleMoves = []

        for i in movesList:

            if self.isSpaceFree(board, i):

                possibleMoves.append(i)
        if len(possibleMoves) != 0:

            return random.choice(possibleMoves)

        else:

            return None
    def isSpaceFree(self,board, move):
        # Return true if the passed move is free on the passed board.
        return board[move] == ' '
    def getBoardCopy(self,board):
        # Make a duplicate of the board list and return it the duplicate.
        dupeBoard = []
        for i in board:
            dupeBoard.append(i)
        return dupeBoard
    def getmove_server(self,board, computerLetter):
        # Given a board and the computer's letter, determine where to move and return that move.
        computerLetter = 'o'
        playerLetter='x'
        # Here is our algorithm for our Tic Tac Toe AI:
        # First, check if we can win in the next move
        for i in range(0, 9):
            copy = self.getBoardCopy(board)
            if not self.is_tie(copy):
                
                self.makeMove(copy, computerLetter, i)
                if self.is_winner(copy, computerLetter):
                    return i   
        # Check if the player could win on their next move, and block them.

        for i in range(0, 9):
            copy = self.getBoardCopy(board)
            if not self.is_tie(copy):
                self.makeMove(copy, playerLetter, i)
                if self.is_winner(copy, playerLetter):
                    return i
        # Try to take one of the corners, if they are free.
        move = self.chooseRandomMoveFromList(board, [0, 3, 7, 8])
        if move != None:
            return move
        # Try to take the center, if it is free.

        if self.isSpaceFree(board, 5):
            return 5
        # Move on one of the sides.
        return self.chooseRandomMoveFromList(board, [2, 4, 6, 8])