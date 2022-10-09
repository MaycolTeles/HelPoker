"""
Module containing the 'TestCard' Class.
"""

import unittest

from src.domain.entities.cards import Card, Suit, Value


class TestCard(unittest.TestCase):
    """
    Class to test the 'Card' Class.
    """

    def test_card_constructor(self) -> None:
        """
        Method to test the '__init__' (or constructor) method.
        """
        test_card_value = Value.ACE
        test_card_suit = Suit.CLUB

        actual = Card(
            value=test_card_value,
            suit=test_card_suit,
        )

        self.assertEqual(actual.value, test_card_value)
        self.assertEqual(actual.suit, test_card_suit)

    def test_card_string_representation(self) -> None:
        """
        Method to test the '__str__' method.
        """
        test_card_value = Value.ACE
        test_card_suit = Suit.CLUB

        actual = str(Card(value=test_card_value, suit=test_card_suit))

        expected = f"{test_card_value.value} of {test_card_suit.value}"

        self.assertEqual(actual, expected)
