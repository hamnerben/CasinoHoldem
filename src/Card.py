

class Card:

    ASCII = {('ace','spades'): ' _____\n|A .  |\n| /.\ |\n|(_._)|\n|  |  |\n|____V|\n'}


    def __init__(self, value, suit):
        self.val = value
        self.suit = suit
        self.used = False
        self.ascii = ASCII[(value,suit)]

    def __str__(self):
        return (f"{self.val} of {self.suit}")


    def getVal(self): return self.val


    def getSuit(self): return self.suit


    def setUsed(self): self.used = True


    def setNotUsed(self): self.used = False