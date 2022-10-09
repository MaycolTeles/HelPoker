"""
Module containing the 'Board' Class.
"""

# TYPING IMPORTS
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..cards import Card

# MODULE IMPORTS
from dataclasses import dataclass


@dataclass
class Board:
    """
    Class to represent a board.
    """

    cards: list[Card]
