"""
Module containing the 'Card' Class.
"""

# TYPING IMPORTS
from .suits import Suits
from .values import Values

# MODULE IMPORTS
from dataclasses import dataclass


@dataclass
class Card:
    """
    Class to represent a card that contains a Value and a Suit.

    Attributes
    -----------
    card_value : Values
        The card value.

    card_suit : Suits
        The card suit.
    """

    card_value: Values
    card_suit: Suits

    def __init__(self, card_value: Values, card_suit: Suits) -> None:
        """
        Constructor to set up the values.

        Parameters
        -----------
        card_value : Values
            The card value.

        card_suit : Suits
            The card suit.
        """
        self.card_value = card_value
        self.card_suit = card_suit

    def __str__(self) -> str:
        """
        Method to configure how the class will be printed.

        Returns
        --------
        str
            The representation of the class in str format.
        """
        return f"{self.card_value.value} of {self.card_suit.value}"
