

class Card:
    def __init__(self, value, suit):
        self.val = value
        self.suit = suit
        self.used = False


    def __str__(self):
        return (f"{self.val} of {self.suit}")


    def getVal(self): return self.val


    def getSuit(self): return self.suit


    def setUsed(self): self.used = True


    def setNotUsed(self): self.used = False