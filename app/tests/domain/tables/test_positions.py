"""
Module containing the 'TestPositions' Class.
"""

import unittest

from src.domain.tables import Positions


class TestPositions(unittest.TestCase):
    """
    Class to test the 'Positions' Class.
    """

    def test_positions_types(self) -> None:
        """
        Method to test all the positions options types.
        """
        actual = set(position.value for position in Positions)
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
