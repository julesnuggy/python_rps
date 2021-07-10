import unittest

from rps.Enums import ResultEnum, MoveEnum
from rps.Game import Game
from tests.helpers.ContextManager import captured_output


class GameTestCase(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_game_default_attributes(self):
        self.assertEqual(self.game.is_game_running, True)
        self.assertEqual(self.game.p1_move, '')
        self.assertEqual(self.game.p2_move, '')
        self.assertEqual(self.game.result, ResultEnum.NONE)

    def test_can_end_game(self):
        # When
        self.game.end_game()
        # Then
        self.assertEqual(self.game.is_game_running, False)

    def test_can_set_player_moves_to_rock(self):
        # When
        self.game.set_p1_move('1')
        self.game.set_p2_move('1')
        # Then
        self.assertEqual(self.game.p1_move, MoveEnum.ROCK)
        self.assertEqual(self.game.p2_move, MoveEnum.ROCK)

    def test_can_set_player_moves_to_paper(self):
        # When
        self.game.set_p1_move('2')
        self.game.set_p2_move('2')
        # Then
        self.assertEqual(self.game.p1_move, MoveEnum.PAPER)
        self.assertEqual(self.game.p2_move, MoveEnum.PAPER)

    def test_can_set_player_moves_to_scissors(self):
        # When
        self.game.set_p1_move('3')
        self.game.set_p2_move('3')
        # Then
        self.assertEqual(self.game.p1_move, MoveEnum.SCISSORS)
        self.assertEqual(self.game.p2_move, MoveEnum.SCISSORS)

    def test_user_is_warned_when_invalid_move_is_input(self):
        with captured_output() as (out, err):
            output = out.getvalue().strip()

        # When
        self.game.set_p1_move('4')
        # Then
        self.assertIn(output, 'Not a valid move!')

    def test_can_set_game_result(self):
        # When
        self.game.set_result(ResultEnum.P1)
        # Then
        self.assertEqual(self.game.result, ResultEnum.P1)

    def test_get_game_result_correctly_calculates_result(self):
        # Given
        self.game.set_p1_move('1')
        self.game.set_p2_move('2')
        # When
        self.game.get_game_result()
        # Then
        self.assertEqual(self.game.result, ResultEnum.P2)

    def test_can_reset_result_state(self):
        # When
        self.game.reset_result_state()
        # Then
        self.test_game_default_attributes()

    def test_correctly_checks_is_valid_input(self):
        self.assertTrue(self.game.is_valid_input('1'))
        self.assertTrue(self.game.is_valid_input('2'))
        self.assertTrue(self.game.is_valid_input('3'))
        self.assertFalse(self.game.is_valid_input('4'))
        self.assertFalse(self.game.is_valid_input('abc'))
        self.assertFalse(self.game.is_valid_input(''))

    def test_correctly_checks_is_valid_move(self):
        self.assertTrue(self.game.is_valid_move(MoveEnum.ROCK))
        self.assertTrue(self.game.is_valid_move(MoveEnum.PAPER))
        self.assertTrue(self.game.is_valid_move(MoveEnum.SCISSORS))
        self.assertFalse(self.game.is_valid_move(None))
        self.assertFalse(self.game.is_valid_move('1'))
        self.assertFalse(self.game.is_valid_move(''))
