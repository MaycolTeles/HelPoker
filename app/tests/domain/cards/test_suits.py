"""
Module containing the 'TestSuits' Class.
"""

import unittest

from src.domain.cards.suits import Suits


class TestSuits(unittest.TestCase):
    """
    Class to test the 'Suits' Class.
    """

    def test_suits_types(self) -> None:
        """
        Method to test all the suits options types.
        """
        actual = set(suit.value for suit in Suits)
        expected = {"Clubs", "Hearts", "Diamonds", "Spades"}

        self.assertEqual(actual, expected)
