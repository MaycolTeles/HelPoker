"""
Module containing the 'RangesEntity' Class.
"""

from ..hands import Hand
from ..cards import Card, Value, Suit


class RangesEntity:
    """
    Class to represent a Ranges entity.
    """

    def __get_pairs_hands(self) -> list[Hand]:
        """
        Method to return a list containig all the pair hands.

        Returns
        -------
        list[str]
            A list containing all the pair hands.
        """
        return [
            Hand([Card(Value.ACE, Suit.ANY), Card(Value.ACE, Suit.ANY)]),
            Hand([Card(Value.KING, Suit.ANY), Card(Value.KING, Suit.ANY)]),
            Hand([Card(Value.QUEEN, Suit.ANY), Card(Value.QUEEN, Suit.ANY)]),
            Hand([Card(Value.JACK, Suit.ANY), Card(Value.JACK, Suit.ANY)]),
            Hand([Card(Value.TEN, Suit.ANY), Card(Value.TEN, Suit.ANY)]),
            Hand([Card(Value.NINE, Suit.ANY), Card(Value.NINE, Suit.ANY)]),
            Hand([Card(Value.EIGHT, Suit.ANY), Card(Value.EIGHT, Suit.ANY)]),
            Hand([Card(Value.SEVEN, Suit.ANY), Card(Value.SEVEN, Suit.ANY)]),
            Hand([Card(Value.SIX, Suit.ANY), Card(Value.SIX, Suit.ANY)]),
            Hand([Card(Value.FIVE, Suit.ANY), Card(Value.FIVE, Suit.ANY)]),
            Hand([Card(Value.FOUR, Suit.ANY), Card(Value.FOUR, Suit.ANY)]),
            Hand([Card(Value.THREE, Suit.ANY), Card(Value.THREE, Suit.ANY)]),
            Hand([Card(Value.DEUCE, Suit.ANY), Card(Value.DEUCE, Suit.ANY)]),
        ]

    def __get_suited_aces_hands(self) -> list[Hand]:
        """
        Method to return a list containig all the suited aces hands.

        Returns
        -------
        list[str]
            A list containing all the suited aces hands.
        """
        return [
            Hand([Card(Value.ACE, Suit.ANY), Card(Value.KING, Suit.ANY)], suited=True),
            Hand([Card(Value.ACE, Suit.ANY), Card(Value.QUEEN, Suit.ANY)], suited=True),
            Hand([Card(Value.ACE, Suit.ANY), Card(Value.JACK, Suit.ANY)], suited=True),
            Hand([Card(Value.ACE, Suit.ANY), Card(Value.TEN, Suit.ANY)], suited=True),
            Hand([Card(Value.ACE, Suit.ANY), Card(Value.NINE, Suit.ANY)], suited=True),
            Hand([Card(Value.ACE, Suit.ANY), Card(Value.EIGHT, Suit.ANY)], suited=True),
            Hand([Card(Value.ACE, Suit.ANY), Card(Value.SEVEN, Suit.ANY)], suited=True),
            Hand([Card(Value.ACE, Suit.ANY), Card(Value.SIX, Suit.ANY)], suited=True),
            Hand([Card(Value.ACE, Suit.ANY), Card(Value.FIVE, Suit.ANY)], suited=True),
            Hand([Card(Value.ACE, Suit.ANY), Card(Value.FOUR, Suit.ANY)], suited=True),
            Hand([Card(Value.ACE, Suit.ANY), Card(Value.THREE, Suit.ANY)], suited=True),
            Hand([Card(Value.ACE, Suit.ANY), Card(Value.DEUCE, Suit.ANY)], suited=True),
        ]

    def __get_core_range(self) -> list[Hand]:
        """
        Method to return a list containig all the cards that are core to all ranges.

        Returns
        -------
        list[Hand]
            A list containing all the core cards to any range.
        """
        range: list[Hand] = []
        pairs_hands = self.__get_pairs_hands()
        suited_aces_hands = self.__get_suited_aces_hands()

        range.extend(pairs_hands)
        range.extend(suited_aces_hands)

        return range

    def __get_custom_range(self, custom_range: list[Hand]) -> list[Hand]:
        """
        Method to return a list containig a custom range based on the range received as argument.

        Parameters
        ----------
        custom_range : list[Hand]
            A list containing a custom range to be added into the basic range.

        Returns
        -------
        list[Hand]
            A list containing all the hands present in the current range.
        """
        range: list[Hand] = []
        core_range = self.__get_core_range()

        range.extend(core_range)
        range.extend(custom_range)

        return range

    def get_UTG_opening_range(self) -> list[str]:
        """
        Method to return the UTG opening range list.
        """
        custom_range = [
            # OFF-SUITED ACES
            Hand([Card(Value.ACE, Suit.ANY), Card(Value.KING, Suit.ANY)], suited=False),
            Hand(
                [Card(Value.ACE, Suit.ANY), Card(Value.QUEEN, Suit.ANY)], suited=False
            ),
            Hand([Card(Value.ACE, Suit.ANY), Card(Value.JACK, Suit.ANY)], suited=False),
            # SUITED KINGS
            Hand(
                [Card(Value.KING, Suit.ANY), Card(Value.QUEEN, Suit.ANY)], suited=True
            ),
            Hand([Card(Value.KING, Suit.ANY), Card(Value.JACK, Suit.ANY)], suited=True),
            Hand([Card(Value.KING, Suit.ANY), Card(Value.TEN, Suit.ANY)], suited=True),
            # OFF-SUITED KINGS
            Hand(
                [Card(Value.KING, Suit.ANY), Card(Value.QUEEN, Suit.ANY)], suited=False
            ),
            # SUITED QUEENS
            Hand(
                [Card(Value.QUEEN, Suit.ANY), Card(Value.JACK, Suit.ANY)], suited=True
            ),
            Hand([Card(Value.QUEEN, Suit.ANY), Card(Value.TEN, Suit.ANY)], suited=True),
            # SUITED JACKS
            Hand([Card(Value.JACK, Suit.ANY), Card(Value.TEN, Suit.ANY)], suited=True),
        ]

        range = self.__get_custom_range(custom_range)

        return range

    def get_MP_opening_range(self) -> list[str]:
        """
        Method to return the MP opening range list.
        """
        range: list[Hand] = []

        utg_range = self.get_UTG_opening_range()

        mp_range = [
            # OFF-SUITED ACES
            Hand([Card(Value.ACE, Suit.ANY), Card(Value.TEN, Suit.ANY)], suited=False),
            # SUITED TENS
            Hand([Card(Value.TEN, Suit.ANY), Card(Value.NINE, Suit.ANY)], suited=True),
            # SUITED NINES
            Hand(
                [Card(Value.NINE, Suit.ANY), Card(Value.EIGHT, Suit.ANY)], suited=True
            ),
        ]

        range.extend(utg_range)
        range.extend(mp_range)

        return range

    def get_HIJ_opening_range(self) -> list[Hand]:
        """
        Method to return the HIJ opening range list.
        """
        range: list[Hand] = []

        mp_range = self.get_MP_opening_range()

        hij_range = [
            # OFF-SUITED ACES
            Hand([Card(Value.ACE, Suit.ANY), Card(Value.NINE, Suit.ANY)], suited=False),
            # SUITED KINGS
            Hand([Card(Value.KING, Suit.ANY), Card(Value.NINE, Suit.ANY)], suited=True),
            Hand(
                [Card(Value.KING, Suit.ANY), Card(Value.EIGHT, Suit.ANY)], suited=True
            ),
            # OFF-SUITED KINGS
            Hand(
                [Card(Value.KING, Suit.ANY), Card(Value.JACK, Suit.ANY)], suited=False
            ),
            Hand([Card(Value.KING, Suit.ANY), Card(Value.TEN, Suit.ANY)], suited=False),
            # SUITED QUEENS
            Hand(
                [Card(Value.QUEEN, Suit.ANY), Card(Value.NINE, Suit.ANY)], suited=True
            ),
            Hand(
                [Card(Value.QUEEN, Suit.ANY), Card(Value.EIGHT, Suit.ANY)], suited=True
            ),
            # OFF-SUITED QUEENS
            Hand(
                [Card(Value.QUEEN, Suit.ANY), Card(Value.JACK, Suit.ANY)], suited=False
            ),
            Hand(
                [Card(Value.QUEEN, Suit.ANY), Card(Value.TEN, Suit.ANY)], suited=False
            ),
            # SUITED JACKS
            Hand([Card(Value.JACK, Suit.ANY), Card(Value.NINE, Suit.ANY)], suited=True),
            Hand(
                [Card(Value.JACK, Suit.ANY), Card(Value.EIGHT, Suit.ANY)], suited=True
            ),
            # SUITED TENS
            Hand([Card(Value.TEN, Suit.ANY), Card(Value.EIGHT, Suit.ANY)], suited=True),
            # SUITED NINES
            Hand(
                [Card(Value.NINE, Suit.ANY), Card(Value.SEVEN, Suit.ANY)], suited=True
            ),
            # SUITED EIGHTS
            Hand(
                [Card(Value.EIGHT, Suit.ANY), Card(Value.SEVEN, Suit.ANY)], suited=True
            ),
            # SUITED SEVENS
            Hand([Card(Value.SEVEN, Suit.ANY), Card(Value.SIX, Suit.ANY)], suited=True),
            # SUITED SIXES
            Hand([Card(Value.SIX, Suit.ANY), Card(Value.FIVE, Suit.ANY)], suited=True),
        ]

        range.extend(mp_range)
        range.extend(hij_range)

        return range

    def get_CO_opening_range(self) -> list[Hand]:
        """
        Method to return the CO opening range list.
        """
        range: list[Hand] = []

        hij_range = self.get_HIJ_opening_range()

        co_range = [
            # OFF SUITED ACES
            Hand(
                [Card(Value.ACE, Suit.ANY), Card(Value.EIGHT, Suit.ANY)], suited=False
            ),
            Hand(
                [Card(Value.ACE, Suit.ANY), Card(Value.SEVEN, Suit.ANY)], suited=False
            ),
            Hand([Card(Value.ACE, Suit.ANY), Card(Value.SIX, Suit.ANY)], suited=False),
            Hand([Card(Value.ACE, Suit.ANY), Card(Value.FIVE, Suit.ANY)], suited=False),
            Hand([Card(Value.ACE, Suit.ANY), Card(Value.FOUR, Suit.ANY)], suited=False),
            Hand(
                [Card(Value.ACE, Suit.ANY), Card(Value.THREE, Suit.ANY)], suited=False
            ),
            Hand(
                [Card(Value.ACE, Suit.ANY), Card(Value.DEUCE, Suit.ANY)], suited=False
            ),
            # SUITED KINGS
            Hand(
                [Card(Value.KING, Suit.ANY), Card(Value.SEVEN, Suit.ANY)], suited=True
            ),
            Hand([Card(Value.KING, Suit.ANY), Card(Value.SIX, Suit.ANY)], suited=True),
            Hand([Card(Value.KING, Suit.ANY), Card(Value.FIVE, Suit.ANY)], suited=True),
            Hand([Card(Value.KING, Suit.ANY), Card(Value.FOUR, Suit.ANY)], suited=True),
            # OFF-SUITED KINGS
            Hand(
                [Card(Value.KING, Suit.ANY), Card(Value.NINE, Suit.ANY)], suited=False
            ),
            # SUITED QUEENS
            Hand(
                [Card(Value.QUEEN, Suit.ANY), Card(Value.SEVEN, Suit.ANY)], suited=True
            ),
            Hand([Card(Value.QUEEN, Suit.ANY), Card(Value.SIX, Suit.ANY)], suited=True),
            # SUITED JACKS
            Hand(
                [Card(Value.JACK, Suit.ANY), Card(Value.SEVEN, Suit.ANY)], suited=True
            ),
            Hand([Card(Value.JACK, Suit.ANY), Card(Value.SIX, Suit.ANY)], suited=True),
            # OFF-SUITED JACKS
            Hand([Card(Value.JACK, Suit.ANY), Card(Value.TEN, Suit.ANY)], suited=False),
            # SUITED TENS
            Hand([Card(Value.TEN, Suit.ANY), Card(Value.SEVEN, Suit.ANY)], suited=True),
            Hand([Card(Value.TEN, Suit.ANY), Card(Value.SIX, Suit.ANY)], suited=True),
            # SUITED NINES
            Hand([Card(Value.NINE, Suit.ANY), Card(Value.SIX, Suit.ANY)], suited=True),
            # SUITED EIGHTS
            Hand([Card(Value.EIGHT, Suit.ANY), Card(Value.SIX, Suit.ANY)], suited=True),
            # SUITED SEVENS
            Hand(
                [Card(Value.SEVEN, Suit.ANY), Card(Value.FIVE, Suit.ANY)], suited=True
            ),
            # SUITED SIXES
            Hand([Card(Value.SIX, Suit.ANY), Card(Value.FOUR, Suit.ANY)], suited=True),
            # SUITED FIVES
            Hand([Card(Value.FIVE, Suit.ANY), Card(Value.FOUR, Suit.ANY)], suited=True),
        ]

        range.extend(hij_range)
        range.extend(co_range)

        return range

    def get_BTN_opening_range(self) -> list[Hand]:
        """
        Method to return the BTN opening range list.
        """
        range: list[Hand] = []

        co_range = self.get_CO_opening_range()

        btn_range = [
            # SUITED KINGS
            Hand(
                [Card(Value.KING, Suit.ANY), Card(Value.THREE, Suit.ANY)], suited=True
            ),
            Hand(
                [Card(Value.KING, Suit.ANY), Card(Value.DEUCE, Suit.ANY)], suited=True
            ),
            # OFF-SUITED KINGS
            Hand(
                [Card(Value.KING, Suit.ANY), Card(Value.EIGHT, Suit.ANY)], suited=False
            ),
            Hand(
                [Card(Value.KING, Suit.ANY), Card(Value.SEVEN, Suit.ANY)], suited=False
            ),
            Hand([Card(Value.KING, Suit.ANY), Card(Value.SIX, Suit.ANY)], suited=False),
            Hand(
                [Card(Value.KING, Suit.ANY), Card(Value.FIVE, Suit.ANY)], suited=False
            ),
            Hand(
                [Card(Value.KING, Suit.ANY), Card(Value.FOUR, Suit.ANY)], suited=False
            ),
            # SUITED QUEENS
            Hand(
                [Card(Value.QUEEN, Suit.ANY), Card(Value.FIVE, Suit.ANY)], suited=True
            ),
            Hand(
                [Card(Value.QUEEN, Suit.ANY), Card(Value.FOUR, Suit.ANY)], suited=True
            ),
            Hand(
                [Card(Value.QUEEN, Suit.ANY), Card(Value.THREE, Suit.ANY)], suited=True
            ),
            Hand(
                [Card(Value.QUEEN, Suit.ANY), Card(Value.DEUCE, Suit.ANY)], suited=True
            ),
            # OFF-SUITED QUEENS
            Hand(
                [Card(Value.QUEEN, Suit.ANY), Card(Value.NINE, Suit.ANY)], suited=False
            ),
            Hand(
                [Card(Value.QUEEN, Suit.ANY), Card(Value.EIGHT, Suit.ANY)], suited=False
            ),
            Hand(
                [Card(Value.QUEEN, Suit.ANY), Card(Value.SEVEN, Suit.ANY)], suited=False
            ),
            Hand(
                [Card(Value.QUEEN, Suit.ANY), Card(Value.SIX, Suit.ANY)], suited=False
            ),
            Hand(
                [Card(Value.QUEEN, Suit.ANY), Card(Value.FIVE, Suit.ANY)], suited=False
            ),
            Hand(
                [Card(Value.QUEEN, Suit.ANY), Card(Value.FOUR, Suit.ANY)], suited=False
            ),
            # SUITED JACKS
            Hand([Card(Value.JACK, Suit.ANY), Card(Value.FIVE, Suit.ANY)], suited=True),
            Hand([Card(Value.JACK, Suit.ANY), Card(Value.FOUR, Suit.ANY)], suited=True),
            Hand(
                [Card(Value.JACK, Suit.ANY), Card(Value.THREE, Suit.ANY)], suited=True
            ),
            Hand(
                [Card(Value.JACK, Suit.ANY), Card(Value.DEUCE, Suit.ANY)], suited=True
            ),
            # OFF-SUITED JACKS
            Hand(
                [Card(Value.JACK, Suit.ANY), Card(Value.NINE, Suit.ANY)], suited=False
            ),
            Hand(
                [Card(Value.JACK, Suit.ANY), Card(Value.EIGHT, Suit.ANY)], suited=False
            ),
            Hand(
                [Card(Value.JACK, Suit.ANY), Card(Value.SEVEN, Suit.ANY)], suited=False
            ),
            Hand([Card(Value.JACK, Suit.ANY), Card(Value.SIX, Suit.ANY)], suited=False),
            Hand(
                [Card(Value.JACK, Suit.ANY), Card(Value.FIVE, Suit.ANY)], suited=False
            ),
            # SUITED TENS
            Hand([Card(Value.TEN, Suit.ANY), Card(Value.FIVE, Suit.ANY)], suited=True),
            Hand([Card(Value.TEN, Suit.ANY), Card(Value.FOUR, Suit.ANY)], suited=True),
            Hand([Card(Value.TEN, Suit.ANY), Card(Value.THREE, Suit.ANY)], suited=True),
            Hand([Card(Value.TEN, Suit.ANY), Card(Value.DEUCE, Suit.ANY)], suited=True),
            # OFF-SUITED TENS
            Hand([Card(Value.TEN, Suit.ANY), Card(Value.NINE, Suit.ANY)], suited=False),
            Hand(
                [Card(Value.TEN, Suit.ANY), Card(Value.EIGHT, Suit.ANY)], suited=False
            ),
            Hand(
                [Card(Value.TEN, Suit.ANY), Card(Value.SEVEN, Suit.ANY)], suited=False
            ),
            # SUITED NINES
            Hand([Card(Value.NINE, Suit.ANY), Card(Value.FIVE, Suit.ANY)], suited=True),
            Hand([Card(Value.NINE, Suit.ANY), Card(Value.FOUR, Suit.ANY)], suited=True),
            Hand(
                [Card(Value.NINE, Suit.ANY), Card(Value.THREE, Suit.ANY)], suited=True
            ),
            Hand(
                [Card(Value.NINE, Suit.ANY), Card(Value.DEUCE, Suit.ANY)], suited=True
            ),
            # OFF-SUITED NINES
            Hand(
                [Card(Value.NINE, Suit.ANY), Card(Value.EIGHT, Suit.ANY)], suited=False
            ),
            # SUITED EIGHTS
            Hand(
                [Card(Value.EIGHT, Suit.ANY), Card(Value.FIVE, Suit.ANY)], suited=True
            ),
            Hand(
                [Card(Value.EIGHT, Suit.ANY), Card(Value.FOUR, Suit.ANY)], suited=True
            ),
            Hand(
                [Card(Value.EIGHT, Suit.ANY), Card(Value.THREE, Suit.ANY)], suited=True
            ),
            Hand(
                [Card(Value.EIGHT, Suit.ANY), Card(Value.DEUCE, Suit.ANY)], suited=True
            ),
            # OFF-SUITED EIGHTS
            Hand(
                [Card(Value.EIGHT, Suit.ANY), Card(Value.SEVEN, Suit.ANY)], suited=False
            ),
            Hand(
                [Card(Value.EIGHT, Suit.ANY), Card(Value.SIX, Suit.ANY)], suited=False
            ),
            # OFF-SUITED SEVENS
            Hand(
                [Card(Value.SEVEN, Suit.ANY), Card(Value.SIX, Suit.ANY)], suited=False
            ),
        ]

        range.extend(co_range)
        range.extend(btn_range)

        return range

    def get_SM_opening_range(self) -> list[Hand]:
        """
        Method to return the SM opening range list.
        """
        range: list[Hand] = []

        hij_range = self.get_HIJ_opening_range()

        sm_range = [
            # OFF SUITED ACES
            Hand(
                [Card(Value.ACE, Suit.ANY), Card(Value.EIGHT, Suit.ANY)], suited=False
            ),
            Hand(
                [Card(Value.ACE, Suit.ANY), Card(Value.SEVEN, Suit.ANY)], suited=False
            ),
            Hand([Card(Value.ACE, Suit.ANY), Card(Value.SIX, Suit.ANY)], suited=False),
            Hand([Card(Value.ACE, Suit.ANY), Card(Value.FIVE, Suit.ANY)], suited=False),
            Hand([Card(Value.ACE, Suit.ANY), Card(Value.FOUR, Suit.ANY)], suited=False),
            Hand(
                [Card(Value.ACE, Suit.ANY), Card(Value.THREE, Suit.ANY)], suited=False
            ),
            Hand(
                [Card(Value.ACE, Suit.ANY), Card(Value.DEUCE, Suit.ANY)], suited=False
            ),
            # SUITED KINGS
            Hand(
                [Card(Value.KING, Suit.ANY), Card(Value.SEVEN, Suit.ANY)], suited=True
            ),
            # OFF-SUITED KINGS
            Hand(
                [Card(Value.KING, Suit.ANY), Card(Value.NINE, Suit.ANY)], suited=False
            ),
            # SUITED QUEENS
            Hand(
                [Card(Value.QUEEN, Suit.ANY), Card(Value.SEVEN, Suit.ANY)], suited=True
            ),
            # SUITED JACKS
            Hand(
                [Card(Value.JACK, Suit.ANY), Card(Value.SEVEN, Suit.ANY)], suited=True
            ),
            # OFF-SUITED JACKS
            Hand([Card(Value.JACK, Suit.ANY), Card(Value.TEN, Suit.ANY)], suited=False),
            # SUITED TENS
            Hand([Card(Value.TEN, Suit.ANY), Card(Value.SEVEN, Suit.ANY)], suited=True),
            # SUITED FIVES
            Hand([Card(Value.FIVE, Suit.ANY), Card(Value.FOUR, Suit.ANY)], suited=True),
        ]

        range.extend(hij_range)
        range.extend(sm_range)

        return range
