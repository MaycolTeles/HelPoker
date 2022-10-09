"""
Module containing the 'TestGameGameSession' Class.
"""

import unittest
from datetime import time

from src.entities.games import GameSession


class TestGameSession(unittest.TestCase):
    """
    Class to test the 'GameSession' Class.
    """

    def test_game_constructor(self) -> None:
        """
        Method to test the '__init__' (or constructor) method.
        """

        total_players = 100
        current_players = 50
        blinds_time = time(minute=6)
        breaks_time_duration = time(minute=5)

        actual = GameSession(
            total_players=total_players,
            current_players=current_players,
            blinds_time=blinds_time,
            breaks_time_duration=breaks_time_duration,
        )

        self.assertEqual(actual.total_players, total_players)
        self.assertEqual(actual.current_players, current_players)
        self.assertEqual(actual.blinds_time, blinds_time)
        self.assertEqual(actual.breaks_time_duration, breaks_time_duration)
