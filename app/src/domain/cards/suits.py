"""
Module containing the 'Suits' Class.
"""

from enum import Enum


class Suits(Enum):
    """
    Class to represent a Enum containing all the following Poker Cards Suits:

    Types
    ------
    - CLUB = 'Clubs';
    - HEART = 'Hearts';
    - DIAMOND = 'Diamonds';
    - SPADE = 'Spades'.
    """

    CLUB = "Clubs"
    HEART = "Hearts"
    DIAMOND = "Diamonds"
    SPADE = "Spades"
