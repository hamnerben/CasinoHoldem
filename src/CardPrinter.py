import Deck

def printCards(cards):
    for card in cards:
        print(card)
        try:
            print(card.ascii)
        except:
            pass
def row(cards):
    longestCard = 0
    for card in cards:
        if len(card) > longestCard:
            longestCard = len(card)
    for l in range(longestCard):
        maxLine = 0
        for card in cards:
            if len(card) > l:
                print(card.ascii[l], end='')
        print()




if __name__ == '__main__':
    dk = Deck.Deck()
    cards = [dk.card(2), dk.card(6), dk.card(23), dk.card(50)]
    row(cards)
