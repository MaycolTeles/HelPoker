"""
Module containing the 'Table' Class.
"""

# TYPING IMPORTS
from __future__ import annotations
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from ..players import Player
    from ..boards import Board

# MODULE IMPORTS
from dataclasses import dataclass


@dataclass
class Table:
    """
    Class to represent a Poker Table.

    Attributes
    ----------
    players : List[Player]
        A list containing all the players that are in this Table.

    total_players : int
        The number of the total players that are currently in this Table.

    board_cards : Board
        The Table's board (cards in flop, turn, river).
    """

    players: List[Player]

    total_players: int = None
    board_cards: Board = None

    def __post_init__(self):
        """
        Method that will be called after the __init__ (constructor) method.

        Used to set the 'total_players' attribute value.
        """
        self.total_players = len(self.players)
