class Money:


    def __init__(self,balance=0,ante=50):
        self.PAYCHART = {'High Card':1, 'Pair':1, 'Two Pair':1, 'Three of a Kind':1, 'Straight':1, 'Flush':2, 'Full House':3, 'Four of a Kind':10,'Straight Flush':20,'Royal Flush':100}
        self.bal = balance
        self.ante = ante

    def __sub__(self, other):
        if isinstance(other, (int,float)):
            self.bal -= other
        else:
            raise NotImplementedError

    def __add__(self, other):
        if isinstance(other, (int,float)):
            self.bal += other
        else:
            raise NotImplementedError

    def __str__(self):
        return str(self.bal)

    def setBal(self, amount):
        self.bal = amount

    def setAnte(self,amount):
        self.ante = amount

    # possible outcomes
        # no qualify -- call and ante pushed
        # tie        -- call and ante pushed
        # fold       -- pay ante
        # lose       -- pay ante and call
        # win        -- pay out scale ante, call payout 1:1

    def anteUp(self):
        self.bal -= self.ante

    def call(self):
        self.bal -= self.ante * 2

    def win(self, handName):
        self.bal += (self.ante * 5) + (self.ante * self.PAYCHART[handName])

    def noQualify(self):
        self.bal += self.ante * 3

if __name__ == '__main__':
    mon = Money()
    mon.setBal(500)
    print(mon)
    mon.anteUp()
    print(f"ante up: {mon}")
    mon.call()
    print(f"call: {mon}")
    # mon.win('Royal Flush')
    mon.noQualify()
    print(mon)
