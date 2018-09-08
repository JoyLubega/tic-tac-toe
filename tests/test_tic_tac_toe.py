import unittest
from api .views import app, tic




class TicTacToeTestCase(unittest.TestCase):
    """
    Tests for the Tictactoe end points
    """

    def setUp(self):
        self.client = app.test_client()

    def test_make_request_with_no_board_provided(self):
        """Should return 400 for missing board"""
        response = self.client.get('/game', query_string="noboard=uuuuuu")
        self.assertEqual(response.status_code, 400)
        self.assertIn('enter the board please',response.data.decode())

    def test_make_request_when_it_is_a_tie(self):
        """Should return 400 when the board provided is a tie"""
        response = self.client.get('/game', query_string="board=xxxoooxox")
        self.assertEqual(response.status_code, 400)
        self.assertIn('The board provide is a tie', response.data.decode())

    def test_invalid_board(self):
        """Should return 400 for an invalid board"""
        response = self.client.get('/game', query_string="board= 45xxoooxox")
        self.assertEqual(response.status_code, 400)
        self.assertIn('The board is invalid',response.data.decode())

    def test_empty_board(self):
        """Should return 400 for empty board string"""
        response = self.client.get('/game', query_string="board=")
        self.assertEqual(response.status_code, 400)
        self.assertIn('Board can not be empty',response.data.decode())
    
    def test_not_plausibly_os_turn(self):
        """Should return 400 for if it was os turn to play"""
        r = self.client.get('/game', query_string="board=xxx      ")
        print(r.data.decode())
        self.assertEqual(r.status_code, 400)

    def test_winning_board(self):
        self.assertTrue(tic.is_winner('xxxoo    ', player='x'))

    def test_loosing_board(self):
        self.assertFalse(tic.is_winner('xx xooooo', player='x'))        


    def test_valid_board_with_valid_return(self):
        """Should return 200 for valid board string"""
        response = self.client.get('/game', query_string="board= xxo  o  ")
        self.assertEqual(response.status_code, 200)
        self.assertIn('oxxo  o  ', response.data.decode())