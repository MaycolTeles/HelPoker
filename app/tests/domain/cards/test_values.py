"""
Module containing the 'TestValues' Class.
"""

import unittest

from src.domain.cards.values import Values


class TestValues(unittest.TestCase):
    """
    Class to test the 'Values' Class.
    """

    def test_values_types(self) -> None:
        """
        Method to test all the values options types.
        """

        actual = set(value.value for value in Values)
        expected = {"2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"}

        self.assertEqual(actual, expected)
