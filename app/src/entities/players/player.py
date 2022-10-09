"""
Module containing the 'Player' Class.
"""

# TYPING IMPORTS
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..tables import Position
    from ..hands import Hand

# MODULE IMPORTS
from dataclasses import dataclass


@dataclass
class Player:
    """
    Class to represent a Poker Player.

    Attributes
    -----------
    name : str - Required.
        The player name.

    current_stack_size : int
        The player's current amount of poker chips.

    current_tournament_place : int
        The player's current tournament place.

    current_table_position : Position
        The player's current position in the table (i. e.: Button, UTG, etc.).

    current_hand : Hand
        The player's current hand.
    """

    name: str

    current_stack_size: int = None
    current_tournament_place: int = None
    current_table_position: Position = None
    current_hand: Hand = None

    def __str__(self) -> str:
        """
        Method to set how the class will be printed.

        Returns
        --------
        str
            The representation of the class in str format.
        """
        name_string = f"Name: {self.name}\n"

        stats_string = ""

        if self.current_stack_size:
            stats_string += f"Current Stack Size: {self.current_stack_size:,d}\n"

        if self.current_tournament_place:
            stats_string += (
                f"Current Tournament Place: {self.current_tournament_place:,d}\n"
            )

        if self.current_table_position.value:
            stats_string += (
                f"Current Table Position: {self.current_table_position.value}\n"
            )

        if self.current_hand:
            stats_string += f"Current Hand: {self.current_hand}\n"

        return name_string + stats_string
