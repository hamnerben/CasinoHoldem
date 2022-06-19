<<<<<<< HEAD

=======
import Prompt
import Money

STARTING_BAL = 1000

ur = Prompt.title()
if ur == 'x':
    Prompt.thanks()
elif ur == 'n':
    ante = Prompt.newGame(STARTING_BAL, STARTING_BAL/10)

playerMoney = Money.Money(STARTING_BAL,ante)


>>>>>>> 4f09008b40b0b815cb79b4152b9d722d2ecccb3b
