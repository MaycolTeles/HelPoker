"""
Module containing the 'Table' Class.
"""

# TYPING IMPORTS
from __future__ import annotations
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from ..cards import Card
    from ..players import Player

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

    # NO NEED TO PASS WHEN INSTANTIATING. DEFINED IN THE '__post_init__' METHOD.
    total_players: int = field(init=False)

    # NO NEED TO PASS WHEN INSTANTIATING.
    board_cards: List[Card] = field(init=False)

    def __post_init__(self):
        """
        Method that will be called after the __init__ (constructor) method.

        Used to set the 'total_players' attribute value.
        """
        self.total_players = len(self.players)
        self.board_cards = []
