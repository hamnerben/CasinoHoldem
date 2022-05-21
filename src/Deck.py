import Card
import CardPrinter
import random
import math

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

    def __getitem__(self, n):
        return self.card(n)

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
        rows = []
        for row in range(math.ceil(len(self)/cols)):
            rows.append([])
        x = 0
        for l in rows:
            for i in range(x + 0, x + cols):
                if len(self) > i:
                    l.append(dk[i])
            x += cols
        for i in range(math.ceil(len(self)/cols)):
            CardPrinter.row(rows[i])

if __name__ == '__main__':
    cols = int(input("how many columns? >"))
    dk = Deck()
    for i in range(4):
        dk.printGrid(cols)
