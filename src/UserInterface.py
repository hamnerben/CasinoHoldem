import Deck
import Hand

def testFlush():
    dk = Deck.Deck()
    for i in range(50):
        dk.shuffle()
        p1Hand = Hand.Hand(dk[1, 2, 3, 4, 5])
        bigHand = dk[1, 2, 3, 4, 5, 6, 7, 8]
        p1Hand.checkFlush(bigHand)
        if p1Hand.flush:
            print("!!!!!!!!!!")
            print("!!!!!!!!!!")
            print("!!!!!!!!!!")
        print("--BIG HAND--")
        print(p1Hand.getNames(bigHand))
        p1Hand.state()

def testSort():
    dk = Deck.Deck()
    for s in range(4,15):
        for i in range(10):
            dk.shuffle()
            print("UNSORTED")
            hand = Hand.Hand(dk[0:s])
            print(hand)
            print("\nSORTED")
            hand.sortHand()
            print(hand)
            print("==========================================")

if __name__ == '__main__':

    testSort()