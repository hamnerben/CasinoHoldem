import CardPrinter
from Card import Card
from CardPrinter import rowStr

class Hand:
    def __init__(self, cards):
        for obj in cards:
            if not isinstance(obj, Card):
                raise TypeError(f"Expected Card object but received {type(obj)}")
        self.cards = cards  # shouldn't be changed
        self.tempCards = cards
        self.flush = False
        self.straight = False
        self.royal = False
        self.topSetSize = 0
        self.sets = 0
        # handName = self.determineHand()

    def __len__(self):
        return len(self.cards)

    def __str__(self):
        return CardPrinter.rowStr(self.cards)

    def __getitem__(self, n):
        """returns the requested Card from the hand"""
        if len(self) < n+1:
            raise IndexError
        else:
            return self.cards[n]

    def __setitem__(self, key, value):
        if not isinstance(key,int):
            raise TypeError
        self.cards[key] = value


    def getNames(self, cards):
        str = ''
        for i in cards:
            str += (f"<{i.getVal()} of {i.getSuit()}>\n")
        str += '\n'
        return str

    def state(self):
        print("--HAND--")
        print(self.getNames(self.cards))
        print("--TEMPCARDS--")
        print(self.getNames(self.tempCards))
        print(f"Is Flush: {self.flush}")
        print(f"Is Straight: {self.straight}")
        print(f"Is Royal: {self.royal}")
        print(f"Top set size: {self.topSetSize}")
        print(f"number of sets: {self.sets}")
        print("===============\n")

    def sortHand(self):
        """Sorts the cards in the hand
          'a' is set as highest"""
        self.sortingHand(0,0,0)

    def sortingHand(self, pos, scan, highPos):
        # the cards are sorted
        if (pos+1) >= len(self):
            return
        # stores the highest card found to the first position
        elif scan >= len(self):
            tempCard = self[pos]
            self[pos] = self[highPos]
            self[highPos] = tempCard
            self.sortingHand(pos+1, pos+1, pos+1)
        # the scan finds a higher card and stores it
        elif self[scan] > self[highPos]:
            highPos = scan
            self.sortingHand(pos, scan+1, highPos)
        else:
            self.sortingHand(pos, scan+1, highPos)



    def checkFlush(self, cards):
        """if exists >= 5 suited cards
        stores True on hand for flush
        and puts suited cards first in tempCards, with unsuited cards after
        suited cards are marked as used"""

        newCards = []
        suitsCount = {'clubs': 0, 'spades': 0, 'hearts': 0, 'diamonds': 0}
        flushSuit = ''
        # count the suits in the hand
        for card in cards:
            suitsCount[card.getSuit()] += 1
        # if a flush exists
        self.flush = False
        for suit in suitsCount:
            if suitsCount[suit] >= 5:
                self.flush = True
                flushSuit = suit
        if self.flush:
            # append all the suited cards at the beginning
            for card in cards:
                if card.getSuit() == flushSuit:
                    newCards.append(card)
                    card.setUsed()  # set the flush cards as used
            # append all the unsuited cards after
            for card in cards:
                if card.getSuit() != flushSuit:
                    newCards.append(card)
            self.tempCards = newCards

    def checkStraight(self, cards):
        """if straight of >=5 cards exists
          stores them in tempCards
          puts straight cards first in descending order
          sets straight to True
          marks straight cards as used"""
        self.straight = False
        aces = []
        hd = Hand(cards)  # this isn't ideal, but I need to make a Hand object
        hd.sortHand()     # in order to sort the cards
        sorted = hd.cards
        straightCards = []
        for i in range(1,len(sorted)):
            current = sorted[i-1]
            next = sorted[i]
            straightCards.append(current)
            current.setUsed()
            if current.getVal() == 'a':
                aces.append(current)
            # if the next card is NOT one step down or equal to the current card
            if not current.getValInt() == next+1 or current.getValInt() == next.getValInt():
                # there exists a straight
                firstCVal = straightCards[0].getValInt()
                lastCVal = straightCards[-1].getValInt()
                if firstCVal - lastCVal >= 4:
                    self.__straightExists(straightCards, sorted)
                    return
                # reset the straight card collection
                for card in straightCards:
                    card.setNotUsed()
                straightCards = []
                continue
            # if it's the last iteration add next card
            if i+1 == len(sorted):
                straightCards.append(next)
                next.setUsed()



        # if low ace would contribute to a straight, add aces if present
        for card in straightCards:
            if card.getVal() == '2':
                for c in aces:
                    straightCards.append(c)
        # there exists a straight
        if straightCards:
            firstCVal = straightCards[0].getValInt()
            lastCVal = straightCards[-1].getValInt()
            if firstCVal - lastCVal >= 4:
                self.__straightExists(straightCards, sorted)
                return
        else:
            self.straight = False



    def __straightExists(self,straightCards,sorted):
        # there exists a straight
        self.straight = True
        self.tempCards = []
        # append all the straight cards first
        for card in sorted:
            if card in straightCards:
                self.tempCards.append(card)
        # append all the non-straight cards
        for card in sorted:
            if card not in straightCards:
                self.tempCards.append(card)
        return








if __name__ == '__main__':
    card0 = Card('3', 'hearts')
    card1 = Card('4', 'diamonds')
    card2 = Card('5', 'clubs')
    card3 = Card('6', 'hearts')
    card4 = Card('7', 'hearts')
    card5 = Card('8', 'hearts')
    card6 = Card('9', 'hearts')

    cards = [card0, card1, card2, card3, card4, card5, card6]

    hand = Hand(cards)

    hand.checkFlush(hand.tempCards)
    print(hand)
    hand.sortHand()
    print(hand)