import unittest
from unittest.mock import patch
from main import main

class TestRockPaperScissorsLizardSpock(unittest.TestCase):

    @patch('builtins.input', side_effect=['rock'])
    @patch('random.choice', return_value='scissors')
    def test_user_wins(self, mock_random, mock_input):
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_any_call("You chose: rock")
            mock_print.assert_any_call("Computer chose: scissors")
            mock_print.assert_any_call("You win!")

    @patch('builtins.input', side_effect=['rock'])
    @patch('random.choice', return_value='rock')
    def test_tie(self, mock_random, mock_input):
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_any_call("You chose: rock")
            mock_print.assert_any_call("Computer chose: rock")
            mock_print.assert_any_call("It's a tie!")

    @patch('builtins.input', side_effect=['rock'])
    @patch('random.choice', return_value='paper')
    def test_user_loses(self, mock_random, mock_input):
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_any_call("You chose: rock")
            mock_print.assert_any_call("Computer chose: paper")
            mock_print.assert_any_call("You lose!")

    @patch('builtins.input', side_effect=['invalid'])
    def test_invalid_input(self, mock_input):
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_any_call("Invalid choice. Please try again.")

if __name__ == "__main__":
    unittest.main()