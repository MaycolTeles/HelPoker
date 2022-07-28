"""
Module containing the 'TestTable' Class.
"""

import unittest

from src.domain.tables import Table, Positions
from src.domain.players import Player


class TestTable(unittest.TestCase):
    """
    Class to test the 'Table' Class.
    """

    def test_poker_table_constructor(self) -> None:
        """
        Method to test the '__init__' (or constructor) method.
        """
        test_players = [
            Player(
                name="Player_1",
                total_chips=10_000,
                current_tournament_place=1,
                current_table_position=Positions.BIG_BLIND,
            ),
            Player(
                name="Player_2",
                total_chips=9_000,
                current_tournament_place=2,
                current_table_position=Positions.BUTTON,
            ),
        ]

        actual = Table(test_players)

        self.assertEqual(actual.players, test_players)
        self.assertEqual(actual.total_players, len(test_players))
