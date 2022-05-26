import Card
import Deck
import math

def rowStr(cards):
    for obj in cards:
        if not isinstance(obj, Card.Card):
            raise TypeError(f"Expected Card object but received {type(obj)}")
    longestCard = 0
    for card in cards:
        if len(card) > longestCard:
            longestCard = len(card)
    str = ''
    for l in range(longestCard):
        maxLine = 0
        for card in cards:
            if len(card) > l:
                str += card.ascii[l]
        str += '\n'
    return str

def grid(cards, cols):
    rows = []
    str =''
    for row in range(math.ceil(len(cards)/cols)):
        rows.append([])
    x = 0
    for l in rows:
        for i in range(x + 0, x + cols):
            if len(cards) > i:
                l.append(cards[i])
        x += cols
    for i in range(math.ceil(len(cards)/cols)):
        str += rowStr(rows[i])
    str += '\n'
    return str


if __name__ == '__main__':
    dk = Deck.Deck()
    cards = [dk.card(2), dk.card(6), dk.card(23), dk.card(50)]
    list = [1,2,1,23]
    print(rowStr(cards))
