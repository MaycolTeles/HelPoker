"""
Module containing the 'TestRangesEntity' Class.
"""

import unittest

from src.entities import RangesEntity
from src.entities import Hand, Card, Value, Suit


class TestRangesEntity(unittest.TestCase):
    """
    Class to test the 'RangesEntity' Class.
    """

    def setUp(self) -> None:
        """
        Method to set up some variables to the tests.

        This method will execute once and before each test.
        """
        self.ranges = RangesEntity()

    def __get_pairs_hands(self) -> list[Hand]:
        """
        Private Method to return a list containing all the pair hands.

        Returns
        --------
        list[Hand]
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

    def __get_aces_hands(self, suited: bool) -> list[Hand]:
        """
        Private Method to return a list containing all the aces hands
        whether they're suited or not (based on the 'suited' value received as argument).

        Parameters
        ----------
        suited : bool
            - True if the aces are suited;
            - False otherwise.

        Returns
        --------
        list[Hand]
            A list containing all the aces hands.
        """
        return [
            Hand(
                [Card(Value.ACE, Suit.ANY), Card(Value.KING, Suit.ANY)], suited=suited
            ),
            Hand(
                [Card(Value.ACE, Suit.ANY), Card(Value.QUEEN, Suit.ANY)], suited=suited
            ),
            Hand(
                [Card(Value.ACE, Suit.ANY), Card(Value.JACK, Suit.ANY)], suited=suited
            ),
            Hand([Card(Value.ACE, Suit.ANY), Card(Value.TEN, Suit.ANY)], suited=suited),
            Hand(
                [Card(Value.ACE, Suit.ANY), Card(Value.NINE, Suit.ANY)], suited=suited
            ),
            Hand(
                [Card(Value.ACE, Suit.ANY), Card(Value.EIGHT, Suit.ANY)], suited=suited
            ),
            Hand(
                [Card(Value.ACE, Suit.ANY), Card(Value.SEVEN, Suit.ANY)], suited=suited
            ),
            Hand([Card(Value.ACE, Suit.ANY), Card(Value.SIX, Suit.ANY)], suited=suited),
            Hand(
                [Card(Value.ACE, Suit.ANY), Card(Value.FIVE, Suit.ANY)], suited=suited
            ),
            Hand(
                [Card(Value.ACE, Suit.ANY), Card(Value.FOUR, Suit.ANY)], suited=suited
            ),
            Hand(
                [Card(Value.ACE, Suit.ANY), Card(Value.THREE, Suit.ANY)], suited=suited
            ),
            Hand(
                [Card(Value.ACE, Suit.ANY), Card(Value.DEUCE, Suit.ANY)], suited=suited
            ),
        ]

    def __get_suited_aces_hands(self) -> list[Hand]:
        """
        Private Method to return a list containing all the suited aces hands.

        Returns
        --------
        list[Hand]
            A list containing all the suited aces hands.
        """
        return self.__get_aces_hands(True)

    def __get_off_suited_aces_hands(self) -> list[Hand]:
        """
        Private Method to return a list containing all the off-suited aces hands.

        Returns
        --------
        list[Hand]
            A list containing all the off-suited aces hands.
        """
        return self.__get_aces_hands(False)

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

        pair_hands = self.__get_pairs_hands()
        suited_aces_hands = self.__get_suited_aces_hands()

        range.extend(pair_hands)
        range.extend(suited_aces_hands)
        range.extend(custom_range)

        return range

    def test_get_UTG_opening_range(self) -> None:
        """
        Method to test the 'get_UTG_opening_range' method.
        """
        utg_range = [
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

        actual = self.ranges.get_UTG_opening_range()
        expected = self.__get_custom_range(utg_range)

        self.assertCountEqual(actual, expected)

    def test_get_MP_opening_range(self) -> None:
        """
        Method to test the 'get_MP_opening_range' method.
        """
        mp_range = [
            # OFF-SUITED ACES
            Hand([Card(Value.ACE, Suit.ANY), Card(Value.KING, Suit.ANY)], suited=False),
            Hand(
                [Card(Value.ACE, Suit.ANY), Card(Value.QUEEN, Suit.ANY)], suited=False
            ),
            Hand([Card(Value.ACE, Suit.ANY), Card(Value.JACK, Suit.ANY)], suited=False),
            Hand([Card(Value.ACE, Suit.ANY), Card(Value.TEN, Suit.ANY)], suited=False),
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
            # SUITED TENS
            Hand([Card(Value.TEN, Suit.ANY), Card(Value.NINE, Suit.ANY)], suited=True),
            # SUITED NINES
            Hand(
                [Card(Value.NINE, Suit.ANY), Card(Value.EIGHT, Suit.ANY)], suited=True
            ),
        ]

        actual = self.ranges.get_MP_opening_range()
        expected = self.__get_custom_range(mp_range)

        self.assertCountEqual(actual, expected)

    def test_get_HIJ_opening_range(self) -> None:
        """
        Method to test the 'get_HIJ_opening_range' method.
        """
        hij_range = [
            # OFF-SUITED ACES
            Hand([Card(Value.ACE, Suit.ANY), Card(Value.KING, Suit.ANY)], suited=False),
            Hand(
                [Card(Value.ACE, Suit.ANY), Card(Value.QUEEN, Suit.ANY)], suited=False
            ),
            Hand([Card(Value.ACE, Suit.ANY), Card(Value.JACK, Suit.ANY)], suited=False),
            Hand([Card(Value.ACE, Suit.ANY), Card(Value.TEN, Suit.ANY)], suited=False),
            Hand([Card(Value.ACE, Suit.ANY), Card(Value.NINE, Suit.ANY)], suited=False),
            # SUITED KINGS
            Hand(
                [Card(Value.KING, Suit.ANY), Card(Value.QUEEN, Suit.ANY)], suited=True
            ),
            Hand([Card(Value.KING, Suit.ANY), Card(Value.JACK, Suit.ANY)], suited=True),
            Hand([Card(Value.KING, Suit.ANY), Card(Value.TEN, Suit.ANY)], suited=True),
            Hand([Card(Value.KING, Suit.ANY), Card(Value.NINE, Suit.ANY)], suited=True),
            Hand(
                [Card(Value.KING, Suit.ANY), Card(Value.EIGHT, Suit.ANY)], suited=True
            ),
            # OFF-SUITED KINGS
            Hand(
                [Card(Value.KING, Suit.ANY), Card(Value.QUEEN, Suit.ANY)], suited=False
            ),
            Hand(
                [Card(Value.KING, Suit.ANY), Card(Value.JACK, Suit.ANY)], suited=False
            ),
            Hand([Card(Value.KING, Suit.ANY), Card(Value.TEN, Suit.ANY)], suited=False),
            # SUITED QUEENS
            Hand(
                [Card(Value.QUEEN, Suit.ANY), Card(Value.JACK, Suit.ANY)], suited=True
            ),
            Hand([Card(Value.QUEEN, Suit.ANY), Card(Value.TEN, Suit.ANY)], suited=True),
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
            Hand([Card(Value.JACK, Suit.ANY), Card(Value.TEN, Suit.ANY)], suited=True),
            Hand([Card(Value.JACK, Suit.ANY), Card(Value.NINE, Suit.ANY)], suited=True),
            Hand(
                [Card(Value.JACK, Suit.ANY), Card(Value.EIGHT, Suit.ANY)], suited=True
            ),
            # SUITED TENS
            Hand([Card(Value.TEN, Suit.ANY), Card(Value.NINE, Suit.ANY)], suited=True),
            Hand([Card(Value.TEN, Suit.ANY), Card(Value.EIGHT, Suit.ANY)], suited=True),
            # SUITED NINES
            Hand(
                [Card(Value.NINE, Suit.ANY), Card(Value.EIGHT, Suit.ANY)], suited=True
            ),
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

        actual = self.ranges.get_HIJ_opening_range()
        expected = self.__get_custom_range(hij_range)

        self.assertCountEqual(actual, expected)

    def test_get_CO_opening_range(self) -> None:
        """
        Method to test the 'get_CO_opening_range' method.
        """
        co_range = [
            # SUITED KINGS
            Hand(
                [Card(Value.KING, Suit.ANY), Card(Value.QUEEN, Suit.ANY)], suited=True
            ),
            Hand([Card(Value.KING, Suit.ANY), Card(Value.JACK, Suit.ANY)], suited=True),
            Hand([Card(Value.KING, Suit.ANY), Card(Value.TEN, Suit.ANY)], suited=True),
            Hand([Card(Value.KING, Suit.ANY), Card(Value.NINE, Suit.ANY)], suited=True),
            Hand(
                [Card(Value.KING, Suit.ANY), Card(Value.EIGHT, Suit.ANY)], suited=True
            ),
            Hand(
                [Card(Value.KING, Suit.ANY), Card(Value.SEVEN, Suit.ANY)], suited=True
            ),
            Hand([Card(Value.KING, Suit.ANY), Card(Value.SIX, Suit.ANY)], suited=True),
            Hand([Card(Value.KING, Suit.ANY), Card(Value.FIVE, Suit.ANY)], suited=True),
            Hand([Card(Value.KING, Suit.ANY), Card(Value.FOUR, Suit.ANY)], suited=True),
            # OFF-SUITED KINGS
            Hand(
                [Card(Value.KING, Suit.ANY), Card(Value.QUEEN, Suit.ANY)], suited=False
            ),
            Hand(
                [Card(Value.KING, Suit.ANY), Card(Value.JACK, Suit.ANY)], suited=False
            ),
            Hand([Card(Value.KING, Suit.ANY), Card(Value.TEN, Suit.ANY)], suited=False),
            Hand(
                [Card(Value.KING, Suit.ANY), Card(Value.NINE, Suit.ANY)], suited=False
            ),
            # SUITED QUEENS
            Hand(
                [Card(Value.QUEEN, Suit.ANY), Card(Value.JACK, Suit.ANY)], suited=True
            ),
            Hand([Card(Value.QUEEN, Suit.ANY), Card(Value.TEN, Suit.ANY)], suited=True),
            Hand(
                [Card(Value.QUEEN, Suit.ANY), Card(Value.NINE, Suit.ANY)], suited=True
            ),
            Hand(
                [Card(Value.QUEEN, Suit.ANY), Card(Value.EIGHT, Suit.ANY)], suited=True
            ),
            Hand(
                [Card(Value.QUEEN, Suit.ANY), Card(Value.SEVEN, Suit.ANY)], suited=True
            ),
            Hand([Card(Value.QUEEN, Suit.ANY), Card(Value.SIX, Suit.ANY)], suited=True),
            # OFF-SUITED QUEENS
            Hand(
                [Card(Value.QUEEN, Suit.ANY), Card(Value.JACK, Suit.ANY)], suited=False
            ),
            Hand(
                [Card(Value.QUEEN, Suit.ANY), Card(Value.TEN, Suit.ANY)], suited=False
            ),
            # SUITED JACKS
            Hand([Card(Value.JACK, Suit.ANY), Card(Value.TEN, Suit.ANY)], suited=True),
            Hand([Card(Value.JACK, Suit.ANY), Card(Value.NINE, Suit.ANY)], suited=True),
            Hand(
                [Card(Value.JACK, Suit.ANY), Card(Value.EIGHT, Suit.ANY)], suited=True
            ),
            Hand(
                [Card(Value.JACK, Suit.ANY), Card(Value.SEVEN, Suit.ANY)], suited=True
            ),
            Hand([Card(Value.JACK, Suit.ANY), Card(Value.SIX, Suit.ANY)], suited=True),
            # OFF-SUITED JACKS
            Hand([Card(Value.JACK, Suit.ANY), Card(Value.TEN, Suit.ANY)], suited=False),
            # SUITED TENS
            Hand([Card(Value.TEN, Suit.ANY), Card(Value.NINE, Suit.ANY)], suited=True),
            Hand([Card(Value.TEN, Suit.ANY), Card(Value.EIGHT, Suit.ANY)], suited=True),
            Hand([Card(Value.TEN, Suit.ANY), Card(Value.SEVEN, Suit.ANY)], suited=True),
            Hand([Card(Value.TEN, Suit.ANY), Card(Value.SIX, Suit.ANY)], suited=True),
            # SUITED NINES
            Hand(
                [Card(Value.NINE, Suit.ANY), Card(Value.EIGHT, Suit.ANY)], suited=True
            ),
            Hand(
                [Card(Value.NINE, Suit.ANY), Card(Value.SEVEN, Suit.ANY)], suited=True
            ),
            Hand([Card(Value.NINE, Suit.ANY), Card(Value.SIX, Suit.ANY)], suited=True),
            # SUITED EIGHTS
            Hand(
                [Card(Value.EIGHT, Suit.ANY), Card(Value.SEVEN, Suit.ANY)], suited=True
            ),
            Hand([Card(Value.EIGHT, Suit.ANY), Card(Value.SIX, Suit.ANY)], suited=True),
            # SUITED SEVENS
            Hand([Card(Value.SEVEN, Suit.ANY), Card(Value.SIX, Suit.ANY)], suited=True),
            Hand(
                [Card(Value.SEVEN, Suit.ANY), Card(Value.FIVE, Suit.ANY)], suited=True
            ),
            # SUITED SIXES
            Hand([Card(Value.SIX, Suit.ANY), Card(Value.FIVE, Suit.ANY)], suited=True),
            Hand([Card(Value.SIX, Suit.ANY), Card(Value.FOUR, Suit.ANY)], suited=True),
            # SUITED FIVES
            Hand([Card(Value.FIVE, Suit.ANY), Card(Value.FOUR, Suit.ANY)], suited=True),
        ]

        range: list[Hand] = []
        off_suited_aces_hands = self.__get_off_suited_aces_hands()

        range.extend(off_suited_aces_hands)
        range.extend(co_range)

        actual = self.ranges.get_CO_opening_range()
        expected = self.__get_custom_range(range)

        self.assertCountEqual(actual, expected)

    def test_get_BTN_opening_range(self) -> None:
        """
        Method to test the 'get_BTN_opening_range' method.
        """
        btn_range = [
            # SUITED KINGS
            Hand(
                [Card(Value.KING, Suit.ANY), Card(Value.QUEEN, Suit.ANY)], suited=True
            ),
            Hand([Card(Value.KING, Suit.ANY), Card(Value.JACK, Suit.ANY)], suited=True),
            Hand([Card(Value.KING, Suit.ANY), Card(Value.TEN, Suit.ANY)], suited=True),
            Hand([Card(Value.KING, Suit.ANY), Card(Value.NINE, Suit.ANY)], suited=True),
            Hand(
                [Card(Value.KING, Suit.ANY), Card(Value.EIGHT, Suit.ANY)], suited=True
            ),
            Hand(
                [Card(Value.KING, Suit.ANY), Card(Value.SEVEN, Suit.ANY)], suited=True
            ),
            Hand([Card(Value.KING, Suit.ANY), Card(Value.SIX, Suit.ANY)], suited=True),
            Hand([Card(Value.KING, Suit.ANY), Card(Value.FIVE, Suit.ANY)], suited=True),
            Hand([Card(Value.KING, Suit.ANY), Card(Value.FOUR, Suit.ANY)], suited=True),
            Hand(
                [Card(Value.KING, Suit.ANY), Card(Value.THREE, Suit.ANY)], suited=True
            ),
            Hand(
                [Card(Value.KING, Suit.ANY), Card(Value.DEUCE, Suit.ANY)], suited=True
            ),
            # OFF-SUITED KINGS
            Hand(
                [Card(Value.KING, Suit.ANY), Card(Value.QUEEN, Suit.ANY)], suited=False
            ),
            Hand(
                [Card(Value.KING, Suit.ANY), Card(Value.JACK, Suit.ANY)], suited=False
            ),
            Hand([Card(Value.KING, Suit.ANY), Card(Value.TEN, Suit.ANY)], suited=False),
            Hand(
                [Card(Value.KING, Suit.ANY), Card(Value.NINE, Suit.ANY)], suited=False
            ),
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
                [Card(Value.QUEEN, Suit.ANY), Card(Value.JACK, Suit.ANY)], suited=True
            ),
            Hand([Card(Value.QUEEN, Suit.ANY), Card(Value.TEN, Suit.ANY)], suited=True),
            Hand(
                [Card(Value.QUEEN, Suit.ANY), Card(Value.NINE, Suit.ANY)], suited=True
            ),
            Hand(
                [Card(Value.QUEEN, Suit.ANY), Card(Value.EIGHT, Suit.ANY)], suited=True
            ),
            Hand(
                [Card(Value.QUEEN, Suit.ANY), Card(Value.SEVEN, Suit.ANY)], suited=True
            ),
            Hand([Card(Value.QUEEN, Suit.ANY), Card(Value.SIX, Suit.ANY)], suited=True),
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
                [Card(Value.QUEEN, Suit.ANY), Card(Value.JACK, Suit.ANY)], suited=False
            ),
            Hand(
                [Card(Value.QUEEN, Suit.ANY), Card(Value.TEN, Suit.ANY)], suited=False
            ),
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
            Hand([Card(Value.JACK, Suit.ANY), Card(Value.TEN, Suit.ANY)], suited=True),
            Hand([Card(Value.JACK, Suit.ANY), Card(Value.NINE, Suit.ANY)], suited=True),
            Hand(
                [Card(Value.JACK, Suit.ANY), Card(Value.EIGHT, Suit.ANY)], suited=True
            ),
            Hand(
                [Card(Value.JACK, Suit.ANY), Card(Value.SEVEN, Suit.ANY)], suited=True
            ),
            Hand([Card(Value.JACK, Suit.ANY), Card(Value.SIX, Suit.ANY)], suited=True),
            Hand([Card(Value.JACK, Suit.ANY), Card(Value.FIVE, Suit.ANY)], suited=True),
            Hand([Card(Value.JACK, Suit.ANY), Card(Value.FOUR, Suit.ANY)], suited=True),
            Hand(
                [Card(Value.JACK, Suit.ANY), Card(Value.THREE, Suit.ANY)], suited=True
            ),
            Hand(
                [Card(Value.JACK, Suit.ANY), Card(Value.DEUCE, Suit.ANY)], suited=True
            ),
            # OFF-SUITED JACKS
            Hand([Card(Value.JACK, Suit.ANY), Card(Value.TEN, Suit.ANY)], suited=False),
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
            Hand([Card(Value.TEN, Suit.ANY), Card(Value.NINE, Suit.ANY)], suited=True),
            Hand([Card(Value.TEN, Suit.ANY), Card(Value.EIGHT, Suit.ANY)], suited=True),
            Hand([Card(Value.TEN, Suit.ANY), Card(Value.SEVEN, Suit.ANY)], suited=True),
            Hand([Card(Value.TEN, Suit.ANY), Card(Value.SIX, Suit.ANY)], suited=True),
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
            Hand(
                [Card(Value.NINE, Suit.ANY), Card(Value.EIGHT, Suit.ANY)], suited=True
            ),
            Hand(
                [Card(Value.NINE, Suit.ANY), Card(Value.SEVEN, Suit.ANY)], suited=True
            ),
            Hand([Card(Value.NINE, Suit.ANY), Card(Value.SIX, Suit.ANY)], suited=True),
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
                [Card(Value.EIGHT, Suit.ANY), Card(Value.SEVEN, Suit.ANY)], suited=True
            ),
            Hand([Card(Value.EIGHT, Suit.ANY), Card(Value.SIX, Suit.ANY)], suited=True),
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
            # SUITED SEVENS
            Hand([Card(Value.SEVEN, Suit.ANY), Card(Value.SIX, Suit.ANY)], suited=True),
            Hand(
                [Card(Value.SEVEN, Suit.ANY), Card(Value.FIVE, Suit.ANY)], suited=True
            ),
            # OFF-SUITED SEVENS
            Hand(
                [Card(Value.SEVEN, Suit.ANY), Card(Value.SIX, Suit.ANY)], suited=False
            ),
            # SUITED SIXES
            Hand([Card(Value.SIX, Suit.ANY), Card(Value.FIVE, Suit.ANY)], suited=True),
            Hand([Card(Value.SIX, Suit.ANY), Card(Value.FOUR, Suit.ANY)], suited=True),
            # SUITED FIVES
            Hand([Card(Value.FIVE, Suit.ANY), Card(Value.FOUR, Suit.ANY)], suited=True),
        ]

        range: list[Hand] = []
        off_suited_aces_hands = self.__get_off_suited_aces_hands()

        range.extend(off_suited_aces_hands)
        range.extend(btn_range)

        actual = self.ranges.get_BTN_opening_range()
        expected = self.__get_custom_range(range)

        self.assertCountEqual(actual, expected)

    def test_get_SM_opening_range(self) -> None:
        """
        Method to test the 'get_SM_opening_range' method.
        """
        sm_range = [
            # SUITED KINGS
            Hand(
                [Card(Value.KING, Suit.ANY), Card(Value.QUEEN, Suit.ANY)], suited=True
            ),
            Hand([Card(Value.KING, Suit.ANY), Card(Value.JACK, Suit.ANY)], suited=True),
            Hand([Card(Value.KING, Suit.ANY), Card(Value.TEN, Suit.ANY)], suited=True),
            Hand([Card(Value.KING, Suit.ANY), Card(Value.NINE, Suit.ANY)], suited=True),
            Hand(
                [Card(Value.KING, Suit.ANY), Card(Value.EIGHT, Suit.ANY)], suited=True
            ),
            Hand(
                [Card(Value.KING, Suit.ANY), Card(Value.SEVEN, Suit.ANY)], suited=True
            ),
            # OFF-SUITED KINGS
            Hand(
                [Card(Value.KING, Suit.ANY), Card(Value.QUEEN, Suit.ANY)], suited=False
            ),
            Hand(
                [Card(Value.KING, Suit.ANY), Card(Value.JACK, Suit.ANY)], suited=False
            ),
            Hand([Card(Value.KING, Suit.ANY), Card(Value.TEN, Suit.ANY)], suited=False),
            Hand(
                [Card(Value.KING, Suit.ANY), Card(Value.NINE, Suit.ANY)], suited=False
            ),
            # SUITED QUEENS
            Hand(
                [Card(Value.QUEEN, Suit.ANY), Card(Value.JACK, Suit.ANY)], suited=True
            ),
            Hand([Card(Value.QUEEN, Suit.ANY), Card(Value.TEN, Suit.ANY)], suited=True),
            Hand(
                [Card(Value.QUEEN, Suit.ANY), Card(Value.NINE, Suit.ANY)], suited=True
            ),
            Hand(
                [Card(Value.QUEEN, Suit.ANY), Card(Value.EIGHT, Suit.ANY)], suited=True
            ),
            Hand(
                [Card(Value.QUEEN, Suit.ANY), Card(Value.SEVEN, Suit.ANY)], suited=True
            ),
            # OFF-SUITED QUEENS
            Hand(
                [Card(Value.QUEEN, Suit.ANY), Card(Value.JACK, Suit.ANY)], suited=False
            ),
            Hand(
                [Card(Value.QUEEN, Suit.ANY), Card(Value.TEN, Suit.ANY)], suited=False
            ),
            # SUITED JACKS
            Hand([Card(Value.JACK, Suit.ANY), Card(Value.TEN, Suit.ANY)], suited=True),
            Hand([Card(Value.JACK, Suit.ANY), Card(Value.NINE, Suit.ANY)], suited=True),
            Hand(
                [Card(Value.JACK, Suit.ANY), Card(Value.EIGHT, Suit.ANY)], suited=True
            ),
            Hand(
                [Card(Value.JACK, Suit.ANY), Card(Value.SEVEN, Suit.ANY)], suited=True
            ),
            # OFF-SUITED JACKS
            Hand([Card(Value.JACK, Suit.ANY), Card(Value.TEN, Suit.ANY)], suited=False),
            # SUITED TENS
            Hand([Card(Value.TEN, Suit.ANY), Card(Value.NINE, Suit.ANY)], suited=True),
            Hand([Card(Value.TEN, Suit.ANY), Card(Value.EIGHT, Suit.ANY)], suited=True),
            Hand([Card(Value.TEN, Suit.ANY), Card(Value.SEVEN, Suit.ANY)], suited=True),
            # SUITED NINES
            Hand(
                [Card(Value.NINE, Suit.ANY), Card(Value.EIGHT, Suit.ANY)], suited=True
            ),
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
            # SUITED FIVES
            Hand([Card(Value.FIVE, Suit.ANY), Card(Value.FOUR, Suit.ANY)], suited=True),
        ]

        range: list[Hand] = []
        off_suited_aces_hands = self.__get_off_suited_aces_hands()

        range.extend(off_suited_aces_hands)
        range.extend(sm_range)

        actual = self.ranges.get_SM_opening_range()
        expected = self.__get_custom_range(range)

        self.assertCountEqual(actual, expected)
