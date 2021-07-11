import unittest

from rps.Player import Player


class PlayerTestCase(unittest.TestCase):
    def setUp(self):
        self.player = Player('Jules', True, False)

    def test_player_default_attributes(self):
        self.assertEqual(self.player.name, 'Jules')
        self.assertTrue(self.player.is_p1)
        self.assertFalse(self.player.is_cpu_player)
        self.assertEqual(self.player.score, 0)

    def test_player_score_increments_correctly(self):
        self.player.add_to_score()
        self.player.add_to_score()
        self.assertEqual(self.player.score, 2)
