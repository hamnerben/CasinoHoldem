class Money:

    def __init__(self,balance=0,ante=50):
        self.bal = balance
        self.ante = ante

    def __sub__(self, other):
        if isinstance(other, (int,float)):
            self.bal -= other
        else:
            raise NotImplementedError

    def __add__(self, other):
        if is