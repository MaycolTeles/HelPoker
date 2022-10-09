"""
Module containing the 'TestPlayer' Class.
"""

import unittest

from src.domain.entities.players import Player
from src.domain.entities.tables import Position
from ...mocks import MockHand


class TestPlayer(unittest.TestCase):
    """
    Class to test the 'Player' Class.
    """

    @classmethod
    def setUpClass(cls) -> None:
        """
        Method to set up the variables to test.

        This method will execute only once and before all tests.
        """
        cls.test_name = "Maycol"
        cls.test_current_stack_size = 5_000
        cls.test_current_tournament_place = 300
        cls.test_current_table_position = Position.BUTTON

    def test_player_constructor(self) -> None:
        """
        Method to test the '__init__' (or constructor) method.
        """
        actual = Player(
            name=self.test_name,
            current_stack_size=self.test_current_stack_size,
            current_tournament_place=self.test_current_tournament_place,
            current_table_position=self.test_current_table_position,
        )

        self.assertEqual(actual.name, self.test_name)
        self.assertEqual(actual.current_stack_size, self.test_current_stack_size)
        self.assertEqual(
            actual.current_tournament_place, self.test_current_tournament_place
        )
        self.assertEqual(
            actual.current_table_position, self.test_current_table_position
        )

    def test_player_string_representation_without_hand(self):
        """
        Method to test the '__str__' (string representation) method without the player hand.
        """
        actual = str(
            Player(
                name=self.test_name,
                current_stack_size=self.test_current_stack_size,
                current_tournament_place=self.test_current_tournament_place,
                current_table_position=self.test_current_table_position,
            )
        )

        self.assertIn(self.test_name, actual)
        self.assertIn(f"{self.test_current_stack_size:,d}", actual)
        self.assertIn(f"{self.test_current_tournament_place:,d}", actual)
        self.assertIn(self.test_current_table_position.value, actual)

    def test_player_string_representation_with_hand(self):
        """
        Method to test the '__str__' (string representation) method with the player hand.
        """
        test_hand = MockHand()

        actual = str(
            Player(
                name=self.test_name,
                current_stack_size=self.test_current_stack_size,
                current_tournament_place=self.test_current_tournament_place,
                current_table_position=self.test_current_table_position,
                current_hand=test_hand,
            )
        )

        self.assertIn(self.test_name, actual)
        self.assertIn(f"{self.test_current_stack_size:,d}", actual)
        self.assertIn(f"{self.test_current_tournament_place:,d}", actual)
        self.assertIn(self.test_current_table_position.value, actual)
        self.assertIn(f"{test_hand}", actual)
