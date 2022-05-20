class Card:



    ASCIIS = { 'blank' :  "_____\n|\ ~ /|\n|}}:{{|\n|}}:{{|\n|}}:{{|\n|/_~_\|",
              #('spades', 'a'): [' _____', '|A .  |', '| /.\\ |', '|(_._)|', '|  |  |', '|____V|'],
              ('spades', 'k'): " _____ \n|K  WW|\n| ^ {)|\n|(.)%%|\n| |%%%|\n|_%%%>|",
              ('spades', '9'): " _____ \n|9    |\n|^ ^ ^|\n|^ ^ ^|\n|^ ^ ^|\n|____6|",
              ('diamonds', 'a') : " _____\n|A ^  |\n| / \ |\n| \ / |\n|  .  |\n|____V|",
              ('diamonds', 'k') : " _____\n|K  WW|\n| /\{)|\n| \/%%|\n|  %%%|\n|_%%%>|",
              ('hearts', '4'): " _____ \n|4    |\n| v v |\n|     |\n| v v |\n|____h|",
              ('clubs', '5') : " _____ \n|5    |\n| & & |\n|  &  |\n| & & |\n|____S|"}
    def __init__(self, value, suit):

        self.val = value
        self.suit = suit
        self.used = False
        if (suit, value) in self.ASCIIS:
            self.ascii = self.ASCIIS[(suit, value)]

    def __len__(self):
        print(self.ascii)
        return len(self.ascii)

    def __str__(self):
        return (f"{self.val} of {self.suit}")


    def getVal(self): return self.val


    def getSuit(self): return self.suit


    def setUsed(self): self.used = True


    def setNotUsed(self): self.used = False

    def temp(self):
        for card in self.ASCIIS:
            print(f"{card} : {self.ASCIIS[card]}")
            list = self.ASCIIS[card].split('\n')
            print(list)
            print()

if __name__ == '__main__':
    cd = Card('k', 'spades')

    cd.temp()