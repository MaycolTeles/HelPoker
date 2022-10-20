"""
Module containing the "CheckRangesRequestModel" Class.
"""

from dataclasses import dataclass


@dataclass
class CheckOpeningRangesResponseModel:
    """
    Class to represent a Data Structure (DS) to all "CheckRanges" Use cases response.

    Attributes
    ----------
    should_open_the_hand : bool
        - True if the player should open the hand;
        - False otherwise (should fold).
    """

    should_open_the_hand: bool
