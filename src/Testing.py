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
        hd0 = Hand.Hand(dk[0:7])
        string = str(hd0)
        hd0.checkFlush(hd0.cards)
        if hd0.flush:
            print("==============")
            print("unsorted flush")
            print(string)
            print("sorted flush")
            print(CardPrinter.rowStr(hd0.tempCards))


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

def makeHand(dk,amount):
    dk.shuffle()
    hd = Hand.Hand(dk[0:amount])
    return hd

def makeSpecificHand():
    c1 = Card.Card('a', 'hearts')
    c2 = Card.Card('k', 'diamonds')
    c3 = Card.Card('q', 'diamonds')
    c4 = Card.Card('j', 'diamonds')
    c5 = Card.Card('10', 'spades')
    c6 = Card.Card('9', 'spades')
    c7 = Card.Card('9', 'clubs')
    hd = Hand.Hand([c1, c2, c3, c4, c5, c6, c7])
    return hd

def testStraightSpecific():
    c1 = Card.Card('a','spades')
    c2 = Card.Card('j','diamonds')
    c3 = Card.Card('10','hearts')
    c4 = Card.Card('q','hearts')
    c5 = Card.Card('10','spades')
    c6 = Card.Card('3','hearts')
    c7 = Card.Card('2','hearts')
    hd = Hand.Hand([c1,c2,c3,c4,c5,c6,c7])
    hd.sortHand()
    print(hd)
    hd.checkStraight(hd.cards)
    print(CardPrinter.rowStr(hd.tempCards))
    print(hd.state())


def testRoyal():
    dk = Deck.Deck()
    for i in range(100000):
        hd = makeHand(dk, 7)
        hd.sortHand()
        # string = str(hd)
        hd.checkRoyal(hd.tempCards)
        if hd.royal:
            # print("========================")
            # print("--RAW HAND--")
            # print(string)
            print("--ROYAL HAND--")
            print(CardPrinter.rowStr(hd.tempCards))


def testSpecificthing():
    dk = Deck.Deck()
    hd = makeHand(dk, 7)
    print("=================================================")
    print("=================================================")
    print(hd)
    hd.countSets(hd.tempCards)
    print(CardPrinter.rowStr(hd.tempCards))

def testCountSets():
    dk = Deck.Deck()
    hd = makeHand(dk, 7)
    string = str(hd)
    hd.countSets(hd.tempCards)
    if hd.topSetSize > 2 and hd.numSets > 1:
        print("=================================================")
        print("=================================================")
        print(string)
        print(CardPrinter.rowStr(hd.tempCards))
        print(f"TopSetSize: {hd.topSetSize}")
        print(f"numSets: {hd.numSets}")

if __name__ == '__main__':
    for i in range(1000):
        testCountSets()