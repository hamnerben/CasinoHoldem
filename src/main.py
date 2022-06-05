import Hand
import Deck

dk = Deck.Deck()
dk.shuffle()

print(dk)
print()
for i in range(10):
    dk.shuffle()
    print(dk)
