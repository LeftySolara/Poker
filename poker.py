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
        self.deck = Deck()
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


    ####################################
    ##  Methods for evaluating hands  ##
    ####################################

    def isFlush(self, hand):
        """Determines if given hand is a flush"""
        hand.sort(key=lambda card: card.suit)
        if hand[0].suit == hand[-1].suit:
            return True
        else:
            return False

    def isRoyal(self, hand):
        """Determines if hand has a 10, J, Q, and K"""
        ranks = [card.rank for card in hand[1:]]
        ranks.sort()
        if ranks == ['10','J','K','Q']:
            return True
        else:
            return False

    def isStraight(self, hand):
        """Determines if given hand is a straight"""
        hand.sort(key=lambda card: card.value)
        if hand[0].rank == "A":
            ranks = [card.rank for card in hand[1:]]
            ranks.sort()
            if ranks == ['2','3','4','5'] or ranks == ['10','J','K','Q']:
                return True
            else:
                return False
        else:
            for i in range(1,5):
                if hand[i].value - 1 == hand[i-1].value:
                    continue
                else:
                    return False
            return True

    def isStraightFlush(self, hand):
        """Determines if given hand is a straight flush"""
        if self.isStraight(hand) and self.isFlush(hand):
            return True
        else:
            return False

    def isRoyalFlush(self, hand):
        """Determines if given hand is a royal flush"""
        if self.isStraightFlush(hand) and self.isRoyal(hand):
            return True
        else:
            return False

    def isFourOfKind(self, hand):
        """Determines if given hand is a four-of-a-kind"""
        hand.sort(key=lambda card: card.rank)

        # four matches + higher unmatched card
        test1 = hand[0].rank == hand[1].rank and hand[1].rank == hand[2].rank and hand[2].rank == hand[3].rank and hand[3].rank != hand[4].rank
        # lower unmatched card + four matches
        test2 = hand[0].rank != hand[1].rank and hand[1].rank == hand[2].rank and hand[2].rank == hand[3].rank and hand[3].rank == hand[4].rank
        return test1 or test2

    def isFullHouse(self, hand):
        """Determines if given hand is a full house"""
        hand.sort(key=lambda card: card.rank)

        # three matches + two matches
        test1 = hand[0].rank == hand[1].rank == hand[2].rank and hand[3].rank == hand[4].rank
        # two matches + three matches
        test2 = hand[0].rank == hand[1].rank and hand[2].rank == hand[3].rank == hand[4].rank
        return test1 or test2

    def isThreeOfKind(self, hand):
        """Determines if hand is three-of-a-kind"""
        if self.isFourOfKind(hand) or self.isFullHouse(hand):
            return False
        else:
            test1 = hand[0].rank == hand[1].rank and hand[1].rank == hand[2].rank
            test2 = hand[1].rank == hand[2].rank and hand[2].rank == hand[3].rank
            test3 = hand[2].rank == hand[3].rank and hand[3].rank == hand[4].rank
            return test1 or test2 or test3

    def isTwoPairs(self, hand):
        """Determines if hand is two pairs"""
        if self.isFourOfKind(hand) or self.isFullHouse(hand) or self.isThreeOfKind(hand):
            return False

        hand.sort(key=lambda card: card.rank)

        test1 = hand[0].rank == hand[1].rank and hand[2].rank == hand[3].rank
        test2 = hand[0].rank == hand[1].rank and hand[3].rank == hand[4].rank
        test3 = hand[1].rank == hand[2].rank and hand[3].rank == hand[4].rank
        return test1 or test2 or test3

    def isOnePair(self, hand):
        """Determines if hand is one pair"""
        if self.isFourOfKind(hand) or self.isFullHouse(hand) or self.isThreeOfKind(hand) or self.isTwoPairs(hand):
            return False
        else:
            hand.sort(key=lambda card: card.rank)

            test1 = hand[0].rank == hand[1].rank
            test2 = hand[1].rank == hand[2].rank
            test3 = hand[2].rank == hand[3].rank
            test4 = hand[3].rank == hand[4].rank

            return test1 or test2 or test3 or test4