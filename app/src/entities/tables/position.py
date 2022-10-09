"""
Module containing the 'Position' Enum Class.
"""

from enum import Enum


class Position(Enum):
    """
    Class to represent a Enum containing all the Poker Table Position, such as:
    UTG, UTG+1, CutOff, Button, SmallBlind, BigBlind, etc.
    """

    UTG = "UTG"
    UTG_1 = "UTG+1"
    UTG_2 = "UTG+2"
    LOJACK = "LoJack"
    HIJACK = "HiJack"
    CUTOFF = "CutOff"
    BUTTON = "Button"
    SMALL_BLIND = "Small-Blind"
    BIG_BLIND = "Big-Blind"
