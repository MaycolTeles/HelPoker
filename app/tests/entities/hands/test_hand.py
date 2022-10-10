"""
Module containing the 'TestHand' Class.
"""

import unittest

from src.entities.hands import Hand
from src.entities.cards import Card, Suit, Value


class TestHand(unittest.TestCase):
    """
    Class to test the 'Hand' Class.
    """

    def test_hand_constructor(self) -> None:
        """
        Method to test the '__init__' (or constructor) method.
        """
        test_card_1 = Card(Value.ACE, Suit.CLUB)
        test_card_2 = Card(Value.ACE, Suit.HEART)

        actual = str(Hand([test_card_1, test_card_2]))

        self.assertIn(str(test_card_1), actual)
        self.assertIn(str(test_card_2), actual)
        self.assertIn("OFF-SUITED", actual)
