import unittest
from unittest.mock import patch

from main import (
    collect_item,
    move_player,
    move_backward,
    play_again,
    get_player_name
)


class TestMysteryIsland(unittest.TestCase):

    def test_collect_rope(self):
        inventory = []

        collect_item("Jungle", inventory)

        self.assertIn("Rope", inventory)

    def test_cannot_collect_rope_twice(self):
        inventory = ["Rope"]

        collect_item("Jungle", inventory)

        self.assertEqual(inventory.count("Rope"), 1)

    def test_collect_lantern(self):
        inventory = []

        collect_item("Cave", inventory)

        self.assertIn("Lantern", inventory)

    def test_cannot_collect_item_at_beach(self):
        inventory = []

        collect_item("Beach", inventory)

        self.assertEqual(inventory, [])

    def test_move_from_beach_to_jungle(self):
        location, won = move_player("Beach", [])

        self.assertEqual(location, "Jungle")
        self.assertFalse(won)

    def test_cannot_cross_bridge_without_rope(self):
        location, won = move_player("Cave", [])

        self.assertEqual(location, "Cave")
        self.assertFalse(won)

    def test_can_cross_bridge_with_rope(self):
        location, won = move_player("Cave", ["Rope"])

        self.assertEqual(location, "Old Bridge")
        self.assertFalse(won)

    def test_cannot_light_beacon_without_lantern(self):
        location, won = move_player("Lighthouse", [])

        self.assertEqual(location, "Lighthouse")
        self.assertFalse(won)

    def test_can_win_with_lantern(self):
        location, won = move_player("Lighthouse", ["Lantern"])

        self.assertEqual(location, "Lighthouse")
        self.assertTrue(won)

    def test_move_backward(self):
        location, moved = move_backward("Jungle")

        self.assertEqual(location, "Beach")
        self.assertTrue(moved)

    def test_play_again_with_invalid_answer(self):
        with patch("builtins.input", side_effect=["maybe", "YES"]):
            result = play_again()

        self.assertTrue(result)

    def test_play_again_with_no(self):
        with patch("builtins.input", return_value="no"):
            result = play_again()

        self.assertFalse(result)

    def test_empty_name_is_rejected(self):
        with patch("builtins.input", side_effect=["", "Nese"]):
            name = get_player_name()

        self.assertEqual(name, "Nese")


if __name__ == "__main__":
    unittest.main()