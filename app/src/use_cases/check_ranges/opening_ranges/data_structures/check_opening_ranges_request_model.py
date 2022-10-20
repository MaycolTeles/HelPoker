"""
Module containing the "CheckRangesRequestModel" Class.
"""

from dataclasses import dataclass

from .....entities import Hand, Position


@dataclass
class CheckOpeningRangesRequestModel:
    """
    Class to represent a Data Structure (DS) to the "CheckOpeningRanges" Use case requests.

    Attributes
    ----------
    hand : Hand
        The player's hand.

    current_position : Position
        The player's current position.
    """

    hand: Hand
    current_position: Position
