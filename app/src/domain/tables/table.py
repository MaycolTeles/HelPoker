"""
Module containing the 'Table' Class.
"""

# TYPING IMPORTS
from typing import List

from src.domain.players import Player

from ..cards import Card

# MODULE IMPORTS
from dataclasses import dataclass, field


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

    board_cards : List[Card]
        The cards that are on the board (Flop, Turn, River).
    """

    players: List[Player]
    total_players: int = field(
        init=False
    )  # NOT NEEDED TO PASS WHEN INSTANTIATING. DEFINED IN THE '__post_init__' METHOD.
    board_cards: List[Card] = field(
        init=False
    )  # NOT NEEDED TO PASS WHEN INSTANTIATING.

    def __post_init__(self):
        """
        Method that will be called after the __init__ (constructor) method.

        Used to set the 'total_players' attribute value.
        """
        self.total_players = len(self.players)
        self.board_cards = []
