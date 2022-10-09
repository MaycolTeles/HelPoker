"""
Module containing the 'TestHand' Class.
"""

import unittest

from src.domain.entities.hands import Hand
from src.domain.entities.cards import Card, Suit, Value


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
        expected = "A of Clubs and A of Hearts"

        self.assertEqual(actual, expected)
