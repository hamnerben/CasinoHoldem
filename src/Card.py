class Card:



    def __init__(self, value, suit):
        ASCII = { 'blank' :  "_____\n|\ ~ /|\n|}}:{{|\n|}}:{{|\n|}}:{{|\n|/_~_\|",
                 ('spades', 'a'): ' _____\n|A .  |\n| /.\ |\n|(_._)|\n|  |  |\n|____V|',
                 ('spades', 'k'): " _____ \n|K  WW|\n| ^ {)|\n|(.)%%|\n| |%%%|\n|_%%%>|",
                 ('spades', '9'): " _____ \n|9    |\n|^ ^ ^|\n|^ ^ ^|\n|^ ^ ^|\n|____6|",
                 ('diamonds', 'a') : " _____\n|A ^  |\n| / \ |\n| \ / |\n|  .  |\n|____V|",
                 ('diamonds', 'k') : " _____\n|K  WW|\n| /\{)|\n| \/%%|\n|  %%%|\n|_%%%>|",
                 ('hearts', '4'): " _____ \n|4    |\n| v v |\n|     |\n| v v |\n|____h|",
                 ('clubs', '5') : " _____ \n|5    |\n| & & |\n|  &  |\n| & & |\n|____S|"}

        self.val = value
        self.suit = suit
        self.used = False
        if (suit, value) in ASCII:
            self.ascii = ASCII[(suit, value)]

    def __len__(self):
        list = self.ascii.split(sep='\n')
        print(list)
        return len(list)

    def __str__(self):
        return (f"{self.val} of {self.suit}")


    def getVal(self): return self.val


    def getSuit(self): return self.suit


    def setUsed(self): self.used = True


    def setNotUsed(self): self.used = False

if __name__ == '__main__':
    test = Card('a', 'spades')

    print(len(test))
    print(test.ascii)