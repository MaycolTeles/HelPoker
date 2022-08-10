"""
Module containing the 'Player' Class.
"""

# TYPING IMPORTS
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.domain.tables import Positions

# MODULE IMPORTS
from dataclasses import dataclass


@dataclass
class Player:
    """
    Class to represent a Poker Player.

    Attributes
    -----------
    name : str
        The player name.

    total_chips : int
        The player's current amount of poker chips.

    current_tournament_place : int
        The player's current tournament place.

    current_table_position : Positions
        The player's current position in the table (i. e.: Button, UTG, etc.).
    """

    name: str
    total_chips: int
    current_tournament_place: int
    current_table_position: Positions
