"""
Module containing the 'CheckOpeningRangesUseCase' Class.
"""

from dataclasses import dataclass
from typing import Callable

from .....entities import RangesEntity, Position, Hand


@dataclass
class CheckOpeningRangesFactory:
    """
    Class to represent a factory to the opening ranges.

    This use case is used to check if the player is in the opening range.
    """

    def get_function(self, position: Position) -> Callable[[], list[Hand]]:
        """
        Method to return the function accordingly to the position received as argument.

        Parameters
        ----------
        position : Position
            The player's position.

        Returns
        -------
        Callable[[], list[Hand]]
            The function to return the range - mapped by the factory.
        """
        ranges_entity = RangesEntity()

        ranges_factory: dict[Position, Callable[[], list[Hand]]] = {
            Position.UTG: ranges_entity.get_UTG_opening_range,
            Position.UTG_1: ranges_entity.get_UTG_opening_range,
            Position.UTG_2: ranges_entity.get_MP_opening_range,
            Position.LOJACK: ranges_entity.get_MP_opening_range,
            Position.HIJACK: ranges_entity.get_HIJ_opening_range,
            Position.CUTOFF: ranges_entity.get_CO_opening_range,
            Position.BUTTON: ranges_entity.get_BTN_opening_range,
            Position.SMALL_BLIND: ranges_entity.get_SM_opening_range,
        }

        return ranges_factory[position]
