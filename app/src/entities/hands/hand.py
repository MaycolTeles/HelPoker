"""
Module containing the 'Hand' Class.
"""

# TYPING IMPORTS
from typing import List

from ..cards import Card

# MODULE IMPORTS
from dataclasses import dataclass


# TODO: SUPPORT MORE CARDS IN HAND
# THIS CLASS IS CURRENTLY ONLY SUPPORTING TWO (2) CARDS ON HAND (Texas Hold'em).


@dataclass
class Hand:
    """
    Class to represent a Poker Hand.

    Attributes
    ----------
    cards : List[Card]
        A list containing all the cards in hand.
    """

    cards: List[Card]
    suited: bool = None

    def __post_init__(self) -> None:
        """
        Method to determine whether the hand is suited or not.
        """
        self.__set_suit()

    def __str__(self) -> str:
        """
        Method to set how the class will be printed.

        Returns
        --------
        str
            The representation of the class in str format.
        """
        hand = f"{self.cards[0]} and {self.cards[1]}"
        suit = f"SUITED: {'SUITED HAND' if self.suited else 'OFF-SUITED HAND'}"

        return hand + suit

    def __set_suit(self) -> None:
        """
        Private Method to set whether the hand is suited or not (off-suited).
        """
        if self.suited:
            return

        # SAME CARDS, IMPOSSIBLE TO BE SUITED.
        if self.cards[0].value == self.cards[1].value:
            self.suited = False
            return

        # DIFFERENT CARDS, CHECKING THEIR SUIT.
        self.suited = True if self.cards[0].suit == self.cards[1].suit else False
