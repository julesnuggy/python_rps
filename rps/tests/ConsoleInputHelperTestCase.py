import unittest

from Player import Player
from tests.helpers.ContextManager import captured_output
from utils.ConsoleInputHelper import print_scoreboard, print_game_end_results


class ConsoleInputHelperTestCase(unittest.TestCase):
    def setUp(self):
        with captured_output() as (out, err):
            self.output = out.getvalue().strip()
        self.p1 = Player('p1', True, False)
        self.p2 = Player('p2', False, False)
        self.p1.score = 5
        self.p2.score = 2

    def test_print_scoreboard_displays_correct_scores(self):
        # When
        print_scoreboard(self.p1, self.p2)
        # Then
        self.assertIn(self.output, 'p1\'s Score: 5')
        self.assertIn(self.output, 'p2\'s Score: 2')

    def test_print_game_end_results_displays_correct_results_if_p1_wins(self):
        # When
        print_game_end_results(self.p1, self.p2)
        # Then
        self.assertIn(self.output, 'p1\'s Score: 5')
        self.assertIn(self.output, 'p2\'s Score: 2')
        self.assertIn(self.output, 'p1 wins!')

    def test_print_game_end_results_displays_correct_results_if_p2_wins(self):
        # Given
        self.p1.score = 11
        # When
        print_game_end_results(self.p1, self.p2)
        # Then
        self.assertIn(self.output, 'p1\'s Score: 5')
        self.assertIn(self.output, 'p2\'s Score: 11')
        self.assertIn(self.output, 'p2 wins!')

    def test_print_game_end_results_displays_correct_results_if_is_draw(self):
        # Given
        self.p2.score = 11
        # When
        print_game_end_results(self.p1, self.p2)
        # Then
        self.assertIn(self.output, 'p1\'s Score: 11')
        self.assertIn(self.output, 'p2\'s Score: 11')
        self.assertIn(self.output, 'It\'s a draw!')
