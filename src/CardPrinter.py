import Card
import Deck


def row(cards):
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


if __name__ == '__main__':
    dk = Deck.Deck()
    cards = [dk.card(2), dk.card(6), dk.card(23), dk.card(50)]
    list = [1,2,1,23]
    print(row(cards))
