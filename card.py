class SuitException(Exception):
    pass

class RankException(Exception):
    pass

class ColorException(Exception):
    pass

class Card(object):
    """Represents a standard playing card.

    Attributes:
        suit:   card object's assigned suit
        rank:   card object's assigned rank
        color:  card object's assigned color
        value:  integer value of card object's rank (aces are low)
    """

    def __init__(self, suit=0, rank=0):
        suit_list  = ["C", "S", "D", "H"]
        color_list = ["b", "r"]
        rank_list  = [None, "A", "2", "3", "4", "5", "6", "7", "8",
           "9", "10", "J", "Q", "K"]

        if suit in range(len(suit_list)):
            self.suit = suit_list[suit]

            if suit in (0,1):
                self.color = color_list[0]
            elif suit in (2,3):
                self.color = color_list[1]
        else:
            raise SuitException

        if rank in range(len(rank_list)):
            self.rank  = rank_list[rank]
            self.value = rank_list.index(self.rank)
        else:
            raise RankException

    def __str__(self):
        return self.rank + self.suit