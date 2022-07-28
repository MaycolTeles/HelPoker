"""
Module containing the 'TestCard' Class.
"""

import unittest

from src.domain.cards import Card, Suits, Values


class TestCard(unittest.TestCase):
    """
    Class to test the 'Card' Class.
    """

    def test_card_constructor(self) -> None:
        """
        Method to test the '__init__' (or constructor) method.
        """
        test_card_value = Values.ACE
        test_card_suit = Suits.CLUB

        actual = Card(
            card_value=test_card_value,
            card_suit=test_card_suit,
        )

        self.assertEqual(actual.card_value, test_card_value)
        self.assertEqual(actual.card_suit, test_card_suit)

    def test_card_string_representation(self) -> None:
        """
        Method to test the '__str__' method.
        """
        test_card_value = Values.ACE
        test_card_suit = Suits.CLUB

        actual = str(Card(card_value=test_card_value, card_suit=test_card_suit))

        expected = f"{test_card_value.value} of {test_card_suit.value}"

        self.assertEqual(actual, expected)
