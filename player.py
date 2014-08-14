class Player(object):
    """Represents one poker player

    Attributes:
        name:   player's name; will be shown when displaying player info
        hand:   list of cards held by the player
        wallet: amount of money player has
    """

    def __init__(self, name="player", wallet=0):
        self.name = name
        self.hand = []
        self.wallet = wallet

    def __str__(self):
        return "Player: {}\nWallet: ${}".format(self.name, self.wallet)

    def set_wallet(self, amount):
        """Sets player's wallet to given value"""
        self.wallet = amount

    def show_hand(self):
        """Displays the player's current hand"""
        for card in self.hand:
            print(card, end=" ")
        print()

    def place_bet(self, bet=0):
        """Removes and returns money from wallet"""
        self.wallet -= bet
        return bet

    def add_card(self, card):
        """Adds a card to player's hand"""
        self.hand.append(card)

    def pop_card(self):
        """Removes and returns a card from player's hand"""
        return self.hand.pop()