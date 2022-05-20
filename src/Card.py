class Card:



    ASCIIS = { 'blank' :  ['_____', '|\\ ~ /|', '|}}:{{|', '|}}:{{|', '|}}:{{|', '|/_~_\\|'],
              ('spades', 'a'): [' _____', '|A .  |', '| /.\\ |', '|(_._)|', '|  |  |', '|____V|'],
              ('spades', 'k'): [' _____ ', '|K  WW|', '| ^ {)|', '|(.)%%|', '| |%%%|', '|_%%%>|'],
              ('spades', '9'): [' _____ ', '|9    |', '|^ ^ ^|', '|^ ^ ^|', '|^ ^ ^|', '|____6|'],
              ('diamonds', 'a') : [' _____', '|A ^  |', '| / \\ |', '| \\ / |', '|  .  |', '|____V|'],
              ('diamonds', 'k') : [' _____', '|K  WW|', '| /\\{)|', '| \\/%%|', '|  %%%|', '|_%%%>|'],
              ('hearts', '4'): [' _____ ', '|4    |', '| v v |', '|     |', '| v v |', '|____h|'],
              ('clubs', '5') : [' _____ ', '|5    |', '| & & |', '|  &  |', '| & & |', '|____S|']}

    def __init__(self, value, suit):

        self.val = value
        self.suit = suit
        self.used = False
        if (suit, value) in self.ASCIIS:
            self.ascii = self.ASCIIS[(suit, value)]

    def __len__(self):
        return len(self.ascii)

    def __str__(self):
        return (f"{self.val} of {self.suit}")


    def getVal(self): return self.val


    def getSuit(self): return self.suit


    def setUsed(self): self.used = True


    def setNotUsed(self): self.used = False

    def art(self):
        for l in self.ascii:
            print(l)

if __name__ == '__main__':
   cd = Card('k','spades')
   cd.art()