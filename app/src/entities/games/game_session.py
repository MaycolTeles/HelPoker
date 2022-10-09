"""
Module containing the 'GameSession' Class.
"""

from datetime import timedelta

from dataclasses import dataclass


@dataclass
class GameSession:
    """
    Class to represent a Poker Game Session.

    Attributes
    ----------
    total_players : int
        The number of the total players that subscribed to the game.

    current_players : int
        The number of the current players that still are in the game.

    blinds_time : timedelta
        The amount of time that takes to blinds go up.

    breaks_time_duration : timedelta
        The amount of time that the breaks lasts.
    """

    total_players: int
    current_players: int
    blinds_time: timedelta
    breaks_time_duration: timedelta
