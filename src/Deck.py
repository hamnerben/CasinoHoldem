import Card
import CardPrinter
import random

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
        return CardPrinter.gridStr(self.__cards,13)

    def __getitem__(self, n):
        """returns the requested Cards as a list"""
        if isinstance(n,int):
            if len(self) < n+1:
                raise IndexError
            else:
                return self.card(n+1)
        if isinstance(n, list):
            ls = []
            for i in n:
                if len(self) < i+1:
                    raise IndexError
                else:
                    ls.append(self.card(i))
            return ls
        if isinstance(n, slice):
            start, stop, step = n.indices(len(self))
            return [self[i] for i in range(start, stop, step)]

    def __iter__(self):
        self.current_index = 0
        return self

    def __next__(self):
        if self.current_index < len(self.__cards):
            card = self.__cards[self.current_index]
            self.current_index += 1
            return card
        raise StopIteration

    def card(self, n):
        """return the card by the number passed in, starting with 1"""
        if 0 <= n and n <= len(self):
            return self.__cards[n-1]
        else:
            raise IndexError

    def shuffle(self):
        random.shuffle(self.__cards)

    def printGrid(self,cols):
        print(CardPrinter.gridStr(self.__cards,cols))


if __name__ == '__main__':
    dk = Deck()
