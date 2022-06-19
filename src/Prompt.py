import sys

import CardPrinter

def title(money=''):
    """returns letter command obtained from user"""
    print("""
         .o88b.  .d8b.  .d8888. d888888b d8b   db  .d88b.      
        d8P  Y8 d8' `8b 88'  YP   `88'   888o  88 .8P  Y8.     
        8P      88ooo88 `8bo.      88    88V8o 88 88    88     
        8b      88~~~88   `Y8b.    88    88 V8o88 88    88     
        Y8b  d8 88   88 db   8D   .88.   88  V888 `8b  d8'     
         `Y88P' YP   YP `8888Y' Y888888P VP   V8P  `Y88P'      
                                                               
                                                               
        db   db  .d88b.  db      d8888b. Cb d88888b .88b  d88. 
        88   88 .8P  Y8. 88      88  `8D `D 88'     88'YbdP`88 
        88ooo88 88    88 88      88   88  ' 88ooooo 88  88  88 
        88~~~88 88    88 88      88   88    88~~~~~ 88  88  88 
        88   88 `8b  d8' 88booo. 88  .8D    88.     88  88  88 
        YP   YP  `Y88P'  Y88888P Y8888D'    Y88888P YP  YP  YP 
                                                               
                 ⠀⠀⠀⠀⠀⠀⣀⣤⣴⣄⠀⢀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀ ⠀⣠⣴⣾⣿⣿⣿⣿⣿⣇⢸⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀ ⠀⢿⣿⣿⣿⠛⠿⣿⣿⣿⡀⢻⣿⣿⣿⣿⠀⣸⣿⣶⣦⣄⠀⠀⠀⠀⠀⠀⠀
                ⠀ ⠀⠘⣿⣿⠃⠀⠀⠀⠈⠙⣧⠈⢿⣿⣿⣿⠀⣿⣿⣿⣿⡟⢀⡀⠀⠀⠀⠀⠀
                ⠀ ⠀⠀⢹⡇⠀⠀⠀⠀⣀⣠⣿⣇⠘⣿⣿⣿⠀⣿⣿⣿⡿⠀⣾⣿⣷⣄⠀⠀⠀
                ⠀ ⠀⠀⠀⢿⣦⣤⣾⡆⣹⣿⣿⣿⡄⠹⣿⣿⠀⣿⣿⣿⠃⣸⣿⣿⣿⣿⣷⠀⠀
                ⠀⠀ ⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⠗⢀⣿⡏⠀⣿⣿⡏⢠⣿⣿⣿⣿⠟⠁⠀⠀
                ⠀⠀ ⠀⠀⠀⠸⢿⠿⠟⠋⠉⠁⠀⠐⠚⠛⠃⣰⣿⡿⠀⣾⣿⣿⡿⠃⠀⠀⠀⠀
                ⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠻⠿⠿⠃⣸⣿⣿⠋⠀⠀⠀⠀⠀⠀
                ⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠢⣤⣾⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠁⠀⠀⠀⠀⠀⠀⠀""")
    while True:
        options = ['n', 'x']
        if money:
            print(f"r - Resume Game  Balance: {money.bal}")
            options = ['n', 'x', 'r']
        print("n - New Game")
        print("x - Exit")
        # print("h - how to play")
        ur = input(">")
        if ur.lower() in options:
            return ur
        else:
            print()
            print("-------------------------------------------")
            print(f"'{ur}' is an invalid command")
            print("Please select from the following commands:")
            print("-------------------------------------------")
            print()

def thanks():
    print("""
 ______  __ __   ____  ____   __  _  _____     _____   ___   ____       ____  _       ____  __ __  ____  ____    ____  __ 
|      ||  |  | /    ||    \ |  |/ ]/ ___/    |     | /   \ |    \     |    \| |     /    ||  |  ||    ||    \  /    ||  |
|      ||  |  ||  o  ||  _  ||  ' /(   \_     |   __||     ||  D  )    |  o  ) |    |  o  ||  |  | |  | |  _  ||   __||  |
|_|  |_||  _  ||     ||  |  ||    \ \__  |    |  |_  |  O  ||    /     |   _/| |___ |     ||  ~  | |  | |  |  ||  |  ||__|
  |  |  |  |  ||  _  ||  |  ||     \/  \ |    |   _] |     ||    \     |  |  |     ||  _  ||___, | |  | |  |  ||  |_ | __ 
  |  |  |  |  ||  |  ||  |  ||  .  |\    |    |  |   |     ||  .  \    |  |  |     ||  |  ||     | |  | |  |  ||     ||  |
  |__|  |__|__||__|__||__|__||__|\_| \___|    |__|    \___/ |__|\_|    |__|  |_____||__|__||____/ |____||__|__||___,_||__|""")
    sys.exit(0)

def newGame(balance, anteMax):
    """returns ante amount from user input"""
    """returns an ante amount from the players choice"""
    while True:
        print()
        print(f"Current balance: ${balance}")
        print(f"Enter an ante amount [$1 - ${anteMax}]:")
        ur = input("$")
        if ur.isnumeric():
            ur = int(ur)
            if ur <= anteMax and ur > 0:
                return ur
            else:
                print()
                print("---------------------------------------------")
                print(f"The ante must be [$1 - ${round(anteMax, 3)}]")
                print("---------------------------------------------")
        else:
            print()
            print("--------------------------------------------------")
            print(f"{ur} is not a valid input")
            print(f"Please enter an amount between [$1 - ${anteMax}]:")
            print("--------------------------------------------------")

def printTable(house, table, player,hand='Hand'):
    print("""
_____________________________________________________________   
                                        _____________________
                                       |Royal Flush    |100:1|
                                       |Straight Flush |20:1 |
                                       |Four of a Kind |10:1 |
              =======                  |Full House     |3:1  |
               House                   |Flush          |2:1  |
              =======                  |_______________|_____|""")
    print(CardPrinter.rowStr(house, 11))
    print()
    print(CardPrinter.rowStr(table))
    print(f"""
               ====== 
                {hand}          
               ======""")
    print(CardPrinter.rowStr(player, 11))
    print("_____________________________________________________________")

def action(money):
    """Call, fold"""
    print(f"Balance: ${money.bal}  Total Bet: ${money.ante}")
    print(f"Ante: ${money.ante}")
    print(f"\n(c)all ${money.ante * 2} or (f)old")
    ur = input(">").lower()
    return ur

def result(money, winner='', handTup='', qualify=True):
    print(f"Balance: ${money.bal}  Total Bet: $0")
    print(f"Ante: ${money.ante}")
    if winner:
        print(f"\n{winner} won with a {handTup[1]}")
        print(CardPrinter.rowStr(handTup[0]))
    elif not qualify:
        print("\nThe house did not qualify, bets are pushed")
    print(f"\n(c)ontinue, e(x)it, (a)nte change")
    ur = input(">")
    if ur.lower() in ['c', 'x', 'a']:
        return ur
    else:
        print()
        print("-------------------------------------------")
        print(f"'{ur}' is an invalid command")
        print("Please select from the following commands:")
        print("-------------------------------------------")
        print()


def gameOver():
    print("""   
 ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ 
██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝""")
    sys.exit(0)

if __name__ == '__main__':
    gameOver()