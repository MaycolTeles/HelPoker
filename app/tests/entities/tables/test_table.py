"""
Module containing the 'TestTable' Class.
"""

import unittest

from src.entities.tables import Table, Position
from src.entities.players import Player


class TestTable(unittest.TestCase):
    """
    Class to test the 'Table' Class.
    """

    def test_table_constructor(self) -> None:
        """
        Method to test the '__init__' (or constructor) method.
        """
        test_players = [
            Player(
                name="Player_1",
                current_stack_size=10_000,
                current_tournament_place=1,
                current_table_position=Position.BIG_BLIND,
            ),
            Player(
                name="Player_2",
                current_stack_size=9_000,
                current_tournament_place=2,
                current_table_position=Position.BUTTON,
            ),
        ]

        actual = Table(test_players)

        self.assertEqual(actual.players, test_players)
        self.assertEqual(actual.total_players, len(test_players))
