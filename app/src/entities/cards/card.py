"""
Module containing the 'Card' Class.
"""

# TYPING IMPORTS
from .suit import Suit
from .value import Value

# MODULE IMPORTS
from dataclasses import dataclass


@dataclass
class Card:
    """
    Class to represent a card that contains a Value and a Suit.

    Attributes
    -----------
    value : Value
        The card value.

    suit : Suit
        The card suit.
    """

    value: Value
    suit: Suit

    def __str__(self) -> str:
        """
        Method to set how the class will be printed.

        Returns
        --------
        str
            The representation of the class in str format.
        """
        return f"{self.value.value} of {self.suit.value}"
