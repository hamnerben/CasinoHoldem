import Card

class Deck:

    SUITS = ["spades", "clubs", "diamonds", "hearts"]
    VAlUES = ['a', 'k', 'q', 'j', '10', '9', '8', '7', '6', '5', '4', '3', '2']

    def __init__(self):
        self.__cards = []
        for s in self.SUITS:
            for v in self.VAlUES:
                self.__cards.append(Card.Card(v, s))

    def __len__(self):
        return len(self.__cards)

    def __str__(self):
        str = ''
        for i in range(len(self)):
            str += f"{self.__cards[i]}"
        return str

    def card(self, n):
        """return the card by the number passed in, starting with 1"""
        if 0 < n and n <= len(self):
            return self.__cards[n-1]
        else:
            raise IndexError


if __name__ == '__main__':
    dk = Deck()
    print(dk)