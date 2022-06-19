import Card
import Deck
import Prompt
import Money
import Hand

def mainMenu(money=''):
    STARTING_BAL = 1000
    ur = Prompt.title(money)
    if ur == 'x':
        Prompt.thanks()
    elif ur == 'n':
        ante = Prompt.newGame(STARTING_BAL, int(STARTING_BAL/10))
        money = Money.Money(STARTING_BAL, ante)
    elif ur == 'r':
        ante = Prompt.newGame(money.bal, int(money.bal/10))
        money.setAnte(ante)

    dk = Deck.Deck()
    hd = Hand.Hand()
    rounds(dk,hd,money)



def rounds(dk, hd, pMoney):
    blank = Card.Card('blank', 'blank')
    while True:
        # flop - call or fold
        dk.shuffle()

        house = dk[0:2]
        player = dk[2:4]
        flop = [dk[4], dk[5], dk[6], blank, blank]
        river = dk[4:9]

        pMoney.anteUp()
        Prompt.printTable([blank, blank],flop,player)
        ur = Prompt.action(pMoney)
        # call
        if ur == 'c':
            pMoney.call()
            pHand = hd.determineHand(player + river)
            hHand = hd.determineHand(house + river)
            # house qualifies with pair 4s
            if hd.doesQualify(hHand[0]):
                # win
                if hd.doesWin(player + river, house + river):
                    pMoney.win(pHand[1])
                    Prompt.printTable(house, river, player, "WIN!")
                    result_ur = Prompt.result(pMoney,'you',pHand)
                # lose
                else:
                    Prompt.printTable(house, river, player, "LOSE")
                    result_ur = Prompt.result(pMoney, 'the house', hHand)
            # the house doesn't qualify
            else:
                pMoney.noQualify()
                Prompt.printTable(house,river, player)
                Prompt.result(pMoney,qualify=False)
        # fold
        elif ur == 'f':
            Prompt.printTable(house, river, player, "FOLD")
            result_ur = Prompt.result(pMoney)
        # continue
        if result_ur == 'c':
            continue
        # exit to main menu
        elif result_ur == 'x':
            mainMenu(pMoney)
        elif result_ur == 'a':
            pMoney.setAnte(Prompt.newGame(pMoney.bal, pMoney.bal/10))

if __name__ == '__main__':
    mainMenu()