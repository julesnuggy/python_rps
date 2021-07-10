import unittest

from rps.Player import Player


class PlayerTestCase(unittest.TestCase):
    def setUp(self):
        self.player = Player('Jules')

    def test_player_default_attributes(self):
        self.assertEqual(self.player.name, 'Jules')
        self.assertEqual(self.player.score, 0)

    def test_player_score_increments_correctly(self):
        self.player.add_to_score()
        self.player.add_to_score()
        self.assertEqual(self.player.score, 2)
