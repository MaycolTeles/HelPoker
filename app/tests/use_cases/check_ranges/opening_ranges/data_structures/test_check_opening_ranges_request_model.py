"""
Module containing the "TestCheckOpeningRangesRequestModel" Class.
"""

import unittest

from src.entities import Hand, Card, Value, Suit, Position
from src.use_cases.check_ranges.opening_ranges.data_structures import (
    CheckOpeningRangesRequestModel,
)


class TestCheckOpeningRangesRequestModel(unittest.TestCase):
    """
    Class to test the "CheckOpeningRangesRequestModel" Data Structure (DS).
    """

    def test_check_ranges_request_model_constructor(self) -> None:
        """
        Method to test the CheckOpeningRangesRequestModel's constructor.
        """
        test_hand = Hand([Card(Value.ACE, Suit.ANY), Card(Value.ACE, Suit.ANY)])
        test_current_position = Position.BUTTON

        actual = CheckOpeningRangesRequestModel(
            hand=test_hand,
            current_position=test_current_position,
        )

        self.assertIsInstance(actual, CheckOpeningRangesRequestModel)
        self.assertEqual(actual.hand, test_hand)
        self.assertEqual(actual.current_position, test_current_position)
