from player import Player
from deck import Deck


OPPONENT_NAME = "Lisa"
WALLET_START = 1000        # amount of money players begin with


class Poker(object):
    """Poker game object (aces high)

    Attributes:
        player:   player object holding data for user
        opponent: player object holding data for AI opponent
        pot:      amount of money currently in the pot
        deck:     deck object with cards used for the game
    """

    def __init__(self, player_name):
        self.player = Player(player_name, WALLET_START)
        self.opponent = Player(OPPONENT_NAME, WALLET_START)
        self.pot = 0
        self.deck = Deck(True)
        self.deck.shuffle()

    def show_game(self):
        """Displays game information"""
        print(self.player)
        print()
        print(self.opponent)
        print()
        print("Current pot: ${}".format(self.pot))

    def clear_hands(self):
        """Moves cards from player and AI hands to the deck"""
        for i in range(len(self.player.hand)):
            card = self.player.pop_card()
            self.deck.add_card(card)
        assert len(self.player.hand) == 0

        for i in range(len(self.opponent.hand)):
            card = self.opponent.pop_card()
            self.deck.add_card(card)
        assert len(self.opponent.hand) == 0
            
        assert len(self.deck.cards) == 52

    def deal_hands(self):
        """Adds five new cards to player and opponent hands"""
        for i in range(5):
            card = self.deck.pop_card()
            self.player.add_card(card)
        assert len(self.player.hand) == 5

        for i in range(5):
            card = self.deck.pop_card()
            self.opponent.add_card(card)
        assert len(self.opponent.hand) == 5

        assert len(self.deck.cards) == 42

    def reset(self):
        """Resets game to initial conditions
        1) Moves players' cards to deck
        2) shuffles deck
        3) Sets pot to $0
        4) Sets players' wallets to $1000
        """
        if len(self.player.hand) > 0 and len(self.opponent.hand) > 0:
            self.clear_hands()
        self.deck.shuffle()
        self.pot = 0
        self.player.set_wallet(WALLET_START)
        self.opponent.set_wallet(WALLET_START)
