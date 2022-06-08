import Deck


class Card:

    VALUES = ['2','3','4','5','6','7','8','9','10','j','q','k','a']

    ASCIIS = { 'blank' :  ['_____', '|\\ ~ /|', '|}}:{{|', '|}}:{{|', '|}}:{{|', '|/_~_\\|'],
               ('spades', 'a'): [' _____ ', '|A .  |', '| /.\\ |', '|(_._)|', '|  |  |', '|____V|'],
               ('spades', 'k'): [' _____ ', '|K  WW|', '| ^ {)|', '|(.)%%|', '| |%%%|', '|_%%%>|'],
               ('spades', 'q'): [' _____ ', '|Q  ww|', '| ^ {(|', '|(.)%%|', '| |%%%|', '|_%%%O|'],
               ('spades', 'j'): [' _____ ', '|J  ww|', '| ^ {)|', '|(.)% |', '| | % |', '|__%%[|'],
               ('spades', '10'): [' _____ ', '|10 ^ |', '|^ ^ ^|', '|^ ^ ^|', '|^ ^ ^|', '|___0I|'],
               ('spades', '9'): [' _____ ', '|9    |', '|^ ^ ^|', '|^ ^ ^|', '|^ ^ ^|', '|____6|'],
               ('spades', '8'): [' _____ ', '|8    |', '|^ ^ ^|', '| ^ ^ |', '|^ ^ ^|', '|____8|'],
               ('spades', '7'): [' _____ ', '|7    |', '| ^ ^ |', '|^ ^ ^|', '| ^ ^ |', '|____L|'],
               ('spades', '6'): [' _____ ', '|6    |', '| ^ ^ |', '| ^ ^ |', '| ^ ^ |', '|____9|'],
               ('spades', '5'): [' _____ ', '|5    |', '| ^ ^ |', '|  ^  |', '| ^ ^ |', '|____S|'],
               ('spades', '4'): [' _____ ', '|4    |', '| ^ ^ |', '|     |', '| ^ ^ |', '|____h|'],
               ('spades', '3'): [' _____ ', '|3    |', '| ^ ^ |', '|     |', '|  ^  |', '|____E|'],
               ('spades', '2'): [' _____ ', '|2    |', '|  ^  |', '|     |', '|  ^  |', '|____Z|'],
               ('clubs', 'a'): [' _____ ', '|A _  |', '| ( ) |', '|(_"_)|', '|  |  |', '|____V|'],
                ('clubs', 'k'): [' _____ ', '|K  WW|', '| o {)|', '|o o%%|', '| |%%%|', '|_%%%>|'],
                ('clubs', 'q'): [' _____ ', '|Q  ww|', '| o {(|', '|o o%%|', '| |%%%|', '|_%%%O|'],
                ('clubs', 'j'): [' _____ ', '|J  ww|', '| o {)|', '|o o% |', '| | % |', '|__%%[|'],
                ('clubs', '10'): [' _____ ', '|10 & |', '|& & &|', '|& & &|', '|& & &|', '|___0I|'],
                ('clubs', '9'): [' _____ ', '|9    |', '|& & &|', '|& & &|', '|& & &|', '|____6|'],
                ('clubs', '8'): [' _____ ', '|8    |', '|& & &|', '| & & |', '|& & &|', '|____8|'],
                ('clubs', '7'): [' _____ ', '|7    |', '| & & |', '|& & &|', '| & & |', '|____L|'],
                ('clubs', '6'): [' _____ ', '|6    |', '| & & |', '| & & |', '| & & |', '|____9|'],
                ('clubs', '5'): [' _____ ', '|5    |', '| & & |', '|  &  |', '| & & |', '|____S|'],
                ('clubs', '4'): [' _____ ', '|4    |', '| & & |', '|     |', '| & & |', '|____h|'],
                ('clubs', '3'): [' _____ ', '|3    |', '| & & |', '|     |', '|  &  |', '|____E|'],
                ('clubs', '2'): [' _____ ', '|2    |', '|  &  |', '|     |', '|  &  |', '|____Z|'],
                ('diamonds', 'a'): [' _____ ', '|A ^  |', '| / \\ |', '| \\ / |', '|  .  |', '|____V|'],
                ('diamonds', 'k'): [' _____ ', '|K  WW|', '| /\\{)|', '| \\/%%|', '|  %%%|', '|_%%%>|'],
                ('diamonds', 'q'): [' _____ ', '|Q  ww|', '| /\{(|', '| \/%%|', '|  %%%|', '|_%%%O|'],
                ('diamonds', 'j'): [' _____ ', '|J  ww|', '| /\{)|', '| \/% |', '|   % |', '|__%%[|'],
                ('diamonds', '10'): [' _____ ', '|10 o |', '|o o o|', '|o o o|', '|o o o|', '|___0I|'],
                ('diamonds', '9'): [' _____ ', '|9    |', '|o o o|', '|o o o|', '|o o o|', '|____6|'],
                ('diamonds', '8'): [' _____ ', '|8    |', '|o o o|', '| o o |', '|o o o|', '|____8|'],
                ('diamonds', '7'): [' _____ ', '|7    |', '|o o o|', '| o o |', '|o o o|', '|____L|'],
                ('diamonds', '6'): [' _____ ', '|6    |', '| o o |', '| o o |', '| o o |', '|____9|'],
                ('diamonds', '5'): [' _____ ', '|5    |', '| o o |', '|  o  |', '| o o |', '|____S|'],
                ('diamonds', '4'): [' _____ ', '|4    |', '| o o |', '|     |', '| o o |', '|____h|'],
                ('diamonds', '3'): [' _____ ', '|3    |', '| o o |', '|     |', '|  o  |', '|____E|'],
                ('diamonds', '2'): [' _____ ', '|2    |', '|  o  |', '|     |', '|  o  |', '|____Z|'],
                ('hearts', 'a'): [' _____ ', '|A_ _ |', '|( v )|', '| \ / |', '|  .  |', '|____V|'],
                ('hearts', 'k'): [' _____ ', '|K  WW|', '|   {)|', '|(v)%%|', '| v%%%|', '|_%%%>|'],
                ('hearts', 'q'): [' _____ ', '|Q  ww|', '|   {(|', '|(v)%%|', '| v%%%|', '|_%%%O|'],
                ('hearts', 'j'): [' _____ ', '|J  ww|', '|   {)|', '|(v)% |', '| v % |', '|__%%[|'],
                ('hearts', '10'): [' _____ ', '|10 v |', '|v v v|', '|v v v|', '|v v v|', '|___0I|'],
                ('hearts', '9'): [' _____ ', '|9    |', '|v v v|', '|v v v|', '|v v v|', '|____6|'],
                ('hearts', '8'): [' _____ ', '|8    |', '|v v v|', '| v v |', '|v v v|', '|____8|'],
                ('hearts', '7'): [' _____ ', '|7    |', '| v v |', '|v v v|', '| v v |', '|____L|'],
                ('hearts', '6'): [' _____ ', '|6    |', '| v v |', '| v v |', '| v v |', '|____9|'],
                ('hearts', '5'): [' _____ ', '|5    |', '| v v |', '|  v  |', '| v v |', '|____S|'],
                ('hearts', '4'): [' _____ ', '|4    |', '| v v |', '|     |', '| v v |', '|____h|'],
                ('hearts', '3'): [' _____ ', '|3    |', '| v v |', '|     |', '|  v  |', '|____E|'],
                ('hearts', '2'): [' _____ ', '|2    |', '|  v  |', '|     |', '|  v  |', '|____Z|']}

    def __init__(self, value, suit):
        self.val = value
        self.suit = suit
        self.used = 0
        if (suit, value) in self.ASCIIS:
            self.ascii = self.ASCIIS[(suit, value)]

    def __len__(self):
        return len(self.ascii)

    def __str__(self):
        return self.art()

    def __eq__(self, other):
        return (self.val == other.val and self.suit == other.suit)

    def __ge__(self, other):
        return (self.VALUES.index(self.val) <= other.VALUES.index(other.val))

    def __lt__(self, other):
        return (self.VALUES.index(self.val) < other.VALUES.index(other.val))

    def __add__(self, other):
        if isinstance(other, int):
            return self.getValInt() + other
        else:
            raise NotImplementedError

    def __sub__(self, other):
        if isinstance(other, int):
            return self.getValInt() - other
        else:
            raise NotImplementedError

    def getValInt(self):
        return self.VALUES.index(self.val) + 2

    def getVal(self): return self.val

    def getSuit(self): return self.suit

    def getUsed(self): return self.used

    def setUsed(self): self.used += 1

    def setNotUsed(self): self.used -= 1

    def resetUsed(self): self.used = 0

    def art(self):
        str = ''
        for l in self.ascii:
            str += f"{l}\n"
        return str

if __name__ == '__main__':

   dk = Deck.Deck()
   card = dk[0]
   print(card)
   print(card.getValInt())
   print(card+0)