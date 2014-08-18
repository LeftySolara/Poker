from card import Card
import random

DECK_LENGTH = 52

class Deck(object):
    """Represents a standard deck of playing cards (excluding jokers)

    Attributes:
        cards:     list of Card objects (first item is bottom of deck)
    """

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                new_card = Card(suit, rank)
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
        """Adds a new card to the bottom of the deck"""
        self.cards.insert(0, card)

    def remove_card(self, card):
        """Removes a card from the deck"""
        self.cards.remove(card)

    def sort(self):
        """Sorts cards in the deck in ascending order"""
        self.cards.sort()

    def pop_card(self):
        """Removes and returns card from top of deck"""
        return self.cards.pop()