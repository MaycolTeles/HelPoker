"""
Module containing the 'TestPosition' Class.
"""

import unittest

from src.entities.tables import Position


class TestPosition(unittest.TestCase):
    """
    Class to test the 'Position' Class.
    """

    def test_Position_types(self) -> None:
        """
        Method to test all the Position options types.
        """
        actual = set(position.value for position in Position)
        expected = {
            "UTG",
            "UTG+1",
            "UTG+2",
            "LoJack",
            "HiJack",
            "CutOff",
            "Button",
            "Small-Blind",
            "Big-Blind",
        }

        self.assertEqual(actual, expected)
