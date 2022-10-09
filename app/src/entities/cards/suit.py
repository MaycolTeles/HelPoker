"""
Module containing the 'Suit' Class.
"""

from enum import Enum


class Suit(Enum):
    """
    Class to represent a Enum containing all the following Poker Cards Suit:

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
