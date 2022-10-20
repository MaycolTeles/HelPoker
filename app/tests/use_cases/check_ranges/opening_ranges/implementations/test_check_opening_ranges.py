"""
Module containing the 'TestCheckOpeningRangesUseCase' Class.
"""

import unittest

from src.entities import Hand, Card, Value, Suit, Position
from src.use_cases import CheckOpeningRangesUseCase
from src.use_cases.check_ranges.opening_ranges.data_structures import (
    CheckOpeningRangesRequestModel,
)


class TestCheckOpeningRangesUseCase(unittest.TestCase):
    """
    Class to test the 'CheckOpeningRangesUseCase' Class.
    """

    def test_execute_should_open_pocket_aces_hand(self) -> None:
        """
        Method to test the 'execute' method with a condition that expects it to
        return that the hand should be opened.
        """
        test_hand = Hand([Card(Value.ACE, Suit.CLUB), Card(Value.ACE, Suit.HEART)])
        test_current_position = Position.BUTTON

        test_request_model = CheckOpeningRangesRequestModel(
            hand=test_hand,
            current_position=test_current_position,
        )

        check_opening_range = CheckOpeningRangesUseCase(test_request_model)
        actual = check_opening_range.execute()

        self.assertTrue(actual)

    def test_execute_should_not_open_seven_deuce_hand(self):
        """
        Method to test the 'execute' method with a condition that expects it to
        return that the hand should NOT be opened.
        """
        test_hand = Hand([Card(Value.DEUCE, Suit.CLUB), Card(Value.SEVEN, Suit.HEART)])
        test_current_position = Position.BUTTON

        test_request_model = CheckOpeningRangesRequestModel(
            hand=test_hand,
            current_position=test_current_position,
        )

        check_opening_range = CheckOpeningRangesUseCase(test_request_model)
        actual = check_opening_range.execute()

        self.assertFalse(actual)

    def test_execute_should_not_open_weak_hand(self):
        """
        Method to test the 'execute' method with a condition that expects it to
        return that the hand should NOT be opened, because of the position.
        """
        test_hand = Hand([Card(Value.SEVEN, Suit.CLUB), Card(Value.SIX, Suit.HEART)])
        test_current_position = Position.UTG

        test_request_model = CheckOpeningRangesRequestModel(
            hand=test_hand,
            current_position=test_current_position,
        )

        check_opening_range = CheckOpeningRangesUseCase(test_request_model)
        actual = check_opening_range.execute()

        self.assertFalse(actual)

    def test_execute_should_open_weak_hand(self):
        """
        Method to test the 'execute' method with a condition that expects it to
        return that the hand should be opened, because of the position.
        """
        test_hand = Hand([Card(Value.SEVEN, Suit.CLUB), Card(Value.SIX, Suit.CLUB)])
        test_current_position = Position.BUTTON

        test_request_model = CheckOpeningRangesRequestModel(
            hand=test_hand,
            current_position=test_current_position,
        )

        check_opening_range = CheckOpeningRangesUseCase(test_request_model)
        actual = check_opening_range.execute()

        self.assertTrue(actual)
