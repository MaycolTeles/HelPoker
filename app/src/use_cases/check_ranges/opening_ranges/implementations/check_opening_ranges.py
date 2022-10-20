"""
Module containing the 'CheckOpeningRangesUseCase' Class.
"""

from dataclasses import dataclass

from ..data_structures import (
    CheckOpeningRangesRequestModel,
    CheckOpeningRangesResponseModel,
)
from ..factories.check_opening_ranges_factory import CheckOpeningRangesFactory
from ....interfaces import UseCaseInterface
from .....entities import Hand, Suit


@dataclass
class CheckOpeningRangesUseCase(UseCaseInterface):
    """
    Class to represent an Use Case.

    This use case is used to check if the player is in the opening range.

    Attributes
    ----------
    request_model : CheckRangesRequestModel
        The check ranges request model.
    """

    request_model: CheckOpeningRangesRequestModel
    # presenter: CheckRangesPresenter

    def __get_opening_range(self) -> list[Hand]:
        """
        Private Method to return the opening range.

        Returns
        -------
        list[Hand]
            The opening range.
        """
        ranges_factory = CheckOpeningRangesFactory()

        position = self.request_model.current_position
        factory_function = ranges_factory.get_function(position)

        return factory_function()

    def __get_generic_hand(self) -> Hand:
        """
        Private Method to return the generic hand (the suit setted to "ANY").

        Returns
        -------
        Hand
            The new Hand, with the generic suits.
        """
        new_hand = self.request_model.hand

        for card in new_hand.cards:
            card.suit = Suit.ANY

        return new_hand

    def __get_response_model(
        self, should_open_the_hand: bool
    ) -> CheckOpeningRangesResponseModel:
        """
        Private Method to build and return the response model, based on the arguments.

        should_open_the_hand : bool
            - True if the player should open the hand;
            - False otherwise (should fold).
        """
        response_model = CheckOpeningRangesResponseModel(
            should_open_the_hand=should_open_the_hand
        )

        return response_model

    def execute(self):
        """
        Method to execute the use case.

        In other words, this method will check if the player is in the opening range
        and give the user a response whether he should open or fold this hand.
        """
        hand = self.__get_generic_hand()
        opening_range = self.__get_opening_range()

        should_open_the_hand = hand in opening_range

        response_model = self.__get_response_model(should_open_the_hand)

        return should_open_the_hand

        return self.presenter.execute(response_model)
