from Card import Card

class Hand:
    def __init__(self, cards):
        self.__cards = cards  # shouldn't be changed
        self.tempCards = cards
        self.flush = False
        self.straight = False
        self.royal = False
        self.topSetSize = 0
        self.sets = 0
        # handName = self.determineHand()


    def __len__(self):
        return len(self.__cards)


    def __str__(self):
        str = ''
        for card in self.__cards:
            str += f"{card}\n"
        return str

    def checkFlush(self, cards):
        """if exists >= 5 suited cards
        stores True on hand for flush
        and puts suited cards in tempCards"""
        newCards = []
        suitsCount = {'clubs': 0, 'spades': 0, 'hearts': 0, 'diamonds': 0}
        # count the suits in the hand
        for card in cards:
            suitsCount[card.getSuit()] += 1
        # if a flush exists
        for suit in suitsCount:
            if suitsCount[suit] >= 5:
                self.flush = True
                for

    #     if there doesnt exits a count >= 5
    #         set flush to False
    #     remove the non suited cards
    #     set flush to True



if __name__ == '__main__':
    card0 = Card('3', 'hearts')
    card1 = Card('4', 'hearts')
    card2 = Card('5', 'hearts')
    card3 = Card('6', 'hearts')
    card4 = Card('7', 'hearts')

    cards = [card0,card1,card2,card3,card4]

    hand = Hand(cards)

    print(hand)