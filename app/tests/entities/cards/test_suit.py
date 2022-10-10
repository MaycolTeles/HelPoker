"""
Module containing the 'TestSuit' Class.
"""

import unittest

from src.entities.cards import Suit


class TestSuit(unittest.TestCase):
    """
    Class to test the 'Suit' Class.
    """

    def test_suit_types(self) -> None:
        """
        Method to test all the suits options types.
        """
        actual = set(suit.value for suit in Suit)
        expected = {"Clubs", "Hearts", "Diamonds", "Spades", "Any"}

        self.assertEqual(actual, expected)
