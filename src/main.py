import Prompt
import Money

STARTING_BAL = 1000

ur = Prompt.title()
if ur == 'x':
    Prompt.thanks()
elif ur == 'n':
    ante = Prompt.newGame(STARTING_BAL, STARTING_BAL/10)

playerMoney = Money.Money(STARTING_BAL,ante)


