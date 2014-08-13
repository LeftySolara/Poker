from player import Player
from deck import Deck

class Poker(object):
    """Poker game object (aces high)

    Attributes:
        players: list of player objects
        pot:     amount of money currently in the pot
        deck:    deck object with cards used for the game
    """

    def __init__(self):
        self.players = []
        self.pot = 0
        self.deck = Deck(True)
        self.deck.shuffle()

    def add_player(self, name):
        """Adds a player to the game with $1000 in wallet"""
        new_player = Player(name, 1000)
        self.players.append(new_player)

    def remove_player(self, name):
        """Removes a player from the game"""
        for player in self.players:
            if player.name == name:
                self.players.remove(player)
                break

    def clear_hands(self):
        """Moves cards from players' hands to the deck"""
        for player in self.players:
            for card in player.hand:
                self.deck.add_card(card)
            player.hand = []

    def deal_hands(self):
        """Replaces each player's hand with five new cards"""
        self.clear_hands()
        for player in self.players:
            for i in range(5):
                card = self.deck.pop_card()
                player.hand.append(card)

    def reset(self):
        """Resets game to initial conditions
        1) Moves players' cards to deck
        2) shuffles deck
        3) Sets pot to $0
        4) Sets players' wallets to $1000
        """
        self.clear_hands()
        self.deck.shuffle()
        self.pot = 0
        for player in self.players:
            player.wallet = 1000
