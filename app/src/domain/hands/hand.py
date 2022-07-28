"""
Module containing the 'Hand' Class.
"""

# TYPING IMPORTS
from typing import List

from ..cards import Card

# MODULE IMPORTS
from dataclasses import dataclass


@dataclass
class Hand:
    """
    Class to represent a Poker Hand.

    Attributes
    ----------
    cards : List[Card]
        A list containing all the hand cards.
    """

    cards: List[Card]

    def __str__(self) -> str:
        """
        Method to configure how the class will be printed.

        Returns
        --------
        str
            The representation of the class in str format.
        """
        # TODO: SUPPORT MORE CARDS IN HAND
        return f"{self.cards[0]} and {self.cards[1]}"
