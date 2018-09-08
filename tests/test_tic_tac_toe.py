import unittest
from api .views import app


class TicTacToeTestCase(unittest.TestCase):
    """
    Tests for the Tictactoe end points
    """

    def setUp(self):
        self.client = app.test_client()
        self.valid_board= '+xxo++o++'

    def test_make_request_with_no_board(self):
        """Should return 400 for missing board"""
        
        response = self.client.get('/game')
        self.assertEqual(response.status_code, 400)
        print(response.data.decode())
        self.assertIn('enter the board please',response.data.decode())
