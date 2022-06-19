import Card
import Deck
import Hand
import CardPrinter
import random
import Prompt

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
    c1 = Card.Card('4', 'hearts')
    c2 = Card.Card('2', 'diamonds')
    c3 = Card.Card('2', 'spades')
    c4 = Card.Card('10', 'clubs')
    c5 = Card.Card('3', 'spades')
    c6 = Card.Card('5', 'spades')
    c7 = Card.Card('a', 'clubs')
    hd = Hand.Hand([c1, c2, c3, c4, c5, c6, c7])
    return hd

def testStraightSpecific():
    c1 = Card.Card('a','spades')
    c2 = Card.Card('a','diamonds')
    c3 = Card.Card('a','hearts')
    c4 = Card.Card('a','clubs')
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
    hd = makeSpecificHand()
    print("=================================================")
    print("=================================================")
    print(hd)
    print(CardPrinter.rowStr(hd.isStraight(hd.cards)))

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

def testRoyalFlush():
    dk = Deck.Deck()
    found = 0
    loop = 1000
    for i in range(loop):
        hd = makeHand(dk, 7)
        string = str(hd)
        x = hd.isPair(hd.cards)
        if x:
            found += 1
            print("=================================================")
            print("=================================================")
            print("--ORIGINAL HAND--")
            print(string)
            print("--two pair--")
            print(CardPrinter.rowStr(x))

    print("XXXXXXXXXXXXXXXXXXXXX")
    print(f"found {found}/{loop}")
    print("XXXXXXXXXXXXXXXXXXXXX")

def testFourofAKind():
    hd = makeSpecificHand()
    print(hd)
    print(CardPrinter.rowStr(hd.isFourofAKind(hd.cards)))

def testFlush():
    dk = Deck.Deck()
    hd = makeHand(dk,7)
    string = str(hd)
    x = hd.isStraight(hd.cards)
    if x:
        print("==============================================")
        print(string)
        print(CardPrinter.rowStr(x))


def testhandName():
    dk = Deck.Deck()
    hd = makeHand(dk, 7)
    print("=========================================")
    print(hd)
    x = hd.determineHand(hd.cards)
    print(x[1])
    print(CardPrinter.rowStr(x[0]))

def countHands(iterations):
    dk = Deck.Deck()
    dict = {}
    for i in range(iterations):
        if i % 10000 == 0:
            print(i)
        hd = makeHand(dk, 5)
        name = hd.determineHand(hd.cards)[1]
        if name in dict:
            dict[name] += 1
        else:
            dict[name] = 1
    print(f"{iterations} iterations\n")
    list = []
    for key in dict:
        list.append((dict[key],key))
    list.sort()
    for i in list:
        print(i)

def winner(hd, hand1, hand2):
    print("======================================================")
    if hd.doesWin(hand1, hand2):
        print("==WINNER==")
    print(CardPrinter.rowStr(hand1))
    if hd.doesWin(hand2, hand1):
        print("==WINNER==")
    print(CardPrinter.rowStr(hand2))

if __name__ == '__main__':
    blank = Card.Card('blank', 'blank')
    dk = Deck.Deck()
    hd = Hand.Hand()
    for i in range(100):
        dk.shuffle()
        house = [dk[0], dk[1]]
        player = [dk[2], dk[3]]
        table = dk[4:9]
        winner(hd,table + house, table + player)