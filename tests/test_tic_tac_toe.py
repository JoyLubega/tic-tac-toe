import unittest
from api .views import app, tic


class TicTacToeTestCase(unittest.TestCase):
    """
    Tests for the Tictactoe end points
    """

    def setUp(self):
        self.client = app.test_client()

    def test_make_request_with_no_board_provided(self):
        """Should return 400 for missing board parameter"""
        response = self.client.get('/game')
        self.assertEqual(response.status_code, 400)
        self.assertIn('enter the board please',response.data.decode())

    def test_make_request_when_it_is_a_tie(self):
        """Should return 400 when the board provided is a tie"""
        response = self.client.get('/game', query_string="board=xxxoooxox")
        self.assertEqual(response.status_code, 400)
        self.assertIn('The board is a tie', response.data.decode())

    def test_invalid_board(self):
        """Should return 400 for an invalid board"""
        response = self.client.get('/game', query_string="board=oooooooooo")
        self.assertEqual(response.status_code, 400)
        self.assertIn('The board is invalid',response.data.decode())
    
    def test_not_plausibly_os_turn(self):
        """Should return 400 for if it was os turn to play"""
        r = self.client.get('/game', query_string="board=xxx      ")
        self.assertEqual(r.status_code, 400)

    def test_winning_board(self):
        self.assertTrue(tic.is_winner('xxxoo    ', player='x'))

    def test_loosing_board(self):
        self.assertFalse(tic.is_winner('xx xooooo', player='x'))        


    def test_valid_board_with_valid_return(self):
        """Should return 200 for valid board string"""
        response = self.client.get('/game?board= xxo  o  ')
        print(response)
        self.assertEqual(response.status_code, 200)
        self.assertIn('oxxo  o  ', response.data.decode())

    #testing for optimization
    def test_score_winning_and_losing_base_cases(self):
        self.assertEqual(tic.score('xxx      ', player='x'), 1)
        self.assertEqual(tic.score('xxx      ', player='o'), -1)

        self.assertEqual(tic.score('o  o  o  ', player='o'), 1)
        self.assertEqual(tic.score('o  o  o  ', player='x'), -1)
        self.assertEqual(tic.score('x  x  x  ', player='x'), 1)
        self.assertEqual(tic.score('x  x  x  ', player='o'), -1)

    def test_score_tie_base_cases(self):
        self.assertEqual(tic.score('xoooxxoxo', player='x'), 0)
        self.assertEqual(tic.score('xoooxxoxo', player='o'), 0)

    def test_score_easy_board_can_win(self):
        self.assertEqual(tic.score('oo xx    ', player='o'), 1)
        self.assertEqual(tic.score('oo xx    ', player='x'), 1)

if __name__ == "__main__":
    unittest.main()