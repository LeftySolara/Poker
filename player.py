from deck import Deck

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

	def show_hand(self):
		"""Displays the player's current hand"""
		for card in self.hand:
			print(card, end=" ")
		print()

	def place_bet(bet=0):
		"""Removes and returns money from wallet"""
		self.wallet -= bet
		return bet