"""
Module containing the 'TestValue' Class.
"""

import unittest

from src.entities.cards import Value


class TestValue(unittest.TestCase):
    """
    Class to test the 'Value' Class.
    """

    def test_value_types(self) -> None:
        """
        Method to test all the values options types.
        """
        actual = set(value.value for value in Value)
        expected = {"2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"}

        self.assertEqual(actual, expected)
