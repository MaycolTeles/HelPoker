"""
Module containing the 'TestHand' Class.
"""

import unittest

from src.domain.hands import Hand
from src.domain.cards import Card, Suits, Values


class TestHand(unittest.TestCase):
    """
    Class to test the 'Hand' Class.
    """

    def test_hand_constructor(self) -> None:
        """
        Method to test the '__init__' (or constructor) method.
        """
        test_card_1 = Card(Values.ACE, Suits.CLUB)
        test_card_2 = Card(Values.ACE, Suits.HEART)

        actual = str(Hand([test_card_1, test_card_2]))
        expected = "A of Clubs and A of Hearts"

        self.assertEqual(actual, expected)
