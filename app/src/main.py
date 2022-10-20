"""
Main module.
"""

from .entities.tables import Position
from .entities.cards.suit import Suit
from .entities.cards.value import Value
from .entities.cards import Card
from .entities.hands import Hand
from .entities.players import Player


def main() -> None:
    """Main Function."""
    card_1 = Card(Value.ACE, Suit.CLUB)
    card_2 = Card(Value.KING, Suit.CLUB)

    hand1 = Hand([card_1, card_2])

    card_3 = Card(Value.QUEEN, Suit.HEART)
    card_4 = Card(Value.QUEEN, Suit.SPADE)
    hand2 = Hand([card_3, card_4])

    card_5 = Card(Value.SEVEN, Suit.CLUB)
    card_6 = Card(Value.DEUCE, Suit.HEART)
    hand3 = Hand([card_5, card_6])

    player1 = Player(
        name="Maycol",
        current_stack_size=10_000,
        current_tournament_place=1,
        current_table_position=Position.BUTTON,
    )

    player2 = Player(
        name="Anna",
        current_stack_size=9_900,
        current_tournament_place=2,
        current_table_position=Position.SMALL_BLIND,
    )

    player3 = Player(
        name="Carlos",
        current_stack_size=9_800,
        current_tournament_place=3,
        current_table_position=Position.BIG_BLIND,
    )

    print(player1)
    print(player2)
    print(player3)

    player1.current_hand = hand1
    player2.current_hand = hand2
    player3.current_hand = hand3

    print(player1)
    print(player2)
    print(player3)


if __name__ == "__main__":
    main()
