import Card
import Deck
import Hand
import CardPrinter
import random

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
            hand.checkFlush()
            print(hand.tempCards)
            print("\nSORTED")
            hand.sortHand()
            print(hand)
            print("==========================================")

def checkFlushOrder():
    dk = Deck.Deck()
    for i in range(1000):
        dk.shuffle()
        hd0 = Hand.Hand(dk[0:8])
        hd0.checkFlush(hd0.cards)
        if hd0.flush:
            print("==============")
            print("unsorted flush")
            print(CardPrinter.rowStr(hd0.tempCards))

        hd1 = Hand.Hand(dk[0:8])
        hd1.sortHand()
        hd1.checkFlush(hd1.cards)
        if hd1.flush:
            print("sorted flush")
            print(CardPrinter.rowStr(hd1.tempCards))

def testStraight():
    dk = Deck.Deck()
    for i in range(1000):
        dk.shuffle()
        hd = Hand.Hand(dk[0:7])
        hd.sortHand()
        str1 = str(hd)
        hd.checkStraight(dk[0:7])
        if hd.straight:
            print("=================================================")
            # print("!!!!!!!!!!\n!!!!!!!!!!\n!!!!!!!!!!!")
            print("--sorted HAND--")
            print(str1)
            print("--straightened--")
            print(CardPrinter.rowStr(hd.tempCards))
            print(f"Straight: {hd.straight}")
        ran = random.random()
        # if ran < 0.1:
        #     print("=================================================")
        #     print("--sorted HAND--")
        #     print(str1)
        #     print("--straightened--")
        #     print(CardPrinter.rowStr(hd.tempCards))
        #     print(f"Straight: {hd.straight}")

def testStraightSpecific():
    c1 = Card.Card('a','spades')
    c2 = Card.Card('j','diamonds')
    c3 = Card.Card('4','hearts')
    c4 = Card.Card('5','hearts')
    c5 = Card.Card('5','spades')
    c6 = Card.Card('3','hearts')
    c7 = Card.Card('2','hearts')
    hd = Hand.Hand([c1,c2,c3,c4,c5,c6,c7])
    hd.sortHand()
    print(hd)
    hd.checkStraight(hd.cards)
    print(CardPrinter.rowStr(hd.tempCards))
    print(hd.state())


if __name__ == '__main__':

    testStraight()