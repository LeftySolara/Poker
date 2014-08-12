from card import Card
import random

DECK_LENGTH = 52
ACE_HIGH = 11
ACE_LOW = 1


class Deck(object):
    """Represents a standard deck of playing cards (excluding jokers)

    Attributes:
        cards:     list of Card objects (first item is bottom of deck)
        aces_high: If true, every ace has a value of 11. Otherwise, value is 1.
    """

    def __init__(self, aces_high = False):
        self.cards = []
        self.aces_high = aces_high
        for suit in range(4):
            for rank in range(1,14):
                new_card = Card(suit, rank)
                if aces_high and card.rank == "A":
                    new_card.value = ACE_HIGH
                self.cards.append(new_card)
        assert len(self.cards) == DECK_LENGTH, "Incorrect deck length after initialization"

    def __str__(self):
        for i in self.cards:
            print(i)
        return ''

    def shuffle(self):
        """Shuffles the cards in the deck"""
        random.shuffle(self.cards)

    def add_card(self, card):
        """Adds a new card to the top of the deck"""
        if self.aces_high and rank == 1:
            new_card.value = ACE_HIGH
        self.cards.append(card)

    def remove_card(self, card):
        """Removes a card from the deck"""
        self.cards.remove(card)

    def sort(self):
        """Sorts cards in the deck in ascending order"""
        self.cards.sort()

    def pop_card(self):
        """Removes and returns card from top of deck"""
        return self.cards.pop()

    def change_aces(self):
        """Changes value of aces in deck.
        If aces are low (value 1), all become high (value 11)
        and vice-versa.
        """
        self.aces_high = not self.aces_high
        for card in self.cards:
            if card.rank == "A" and self.aces_high:
                card.value = ACE_HIGH
            elif card.rank == "A" and not self.aces_high:
                card.value = ACE_LOW