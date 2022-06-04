import Hand
import Deck

dk = Deck.Deck()
dk.shuffle()

hd = Hand.Hand(dk[0:5])
print(hd)
print("\n\n")

hd.sortHand()
print(hd)
