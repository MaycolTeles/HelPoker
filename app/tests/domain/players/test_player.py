"""
Module containing the 'TestPlayer' Class.
"""

import unittest

from src.domain.players import Player
from src.domain.tables import Positions


class TestPlayer(unittest.TestCase):
    """
    Class to test the 'Player' Class.
    """

    def test_player_constructor(self) -> None:
        """
        Method to test the '__init__' (or constructor) method.
        """

        name = "Maycol"
        total_chips = 5_000
        current_tournament_place = 300
        current_table_position = Positions.BUTTON

        actual = Player(
            name=name,
            total_chips=total_chips,
            current_tournament_place=current_tournament_place,
            current_table_position=current_table_position,
        )

        self.assertEqual(actual.name, name)
        self.assertEqual(actual.total_chips, total_chips)
        self.assertEqual(actual.current_tournament_place, current_tournament_place)
        self.assertEqual(actual.current_table_position, current_table_position)
