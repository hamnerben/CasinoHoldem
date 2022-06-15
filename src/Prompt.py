def title():
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
        print("n - New Game")
        print("x - exit")
        ur = input()
        if ur.lower() in ['n', 'x']:
            return ur
        else:
            print()
            print("-------------------------------------------")
            print(f"'{ur}' is an invalid command")
            print("Please select from the following commands:")
            print("-------------------------------------------")
            print()

def newGame(balance, anteMax):
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
                print("The ante must be [$1 - ${round(anteMax, 3)}]")
                print("---------------------------------------------")
        else:
            print()
            print("--------------------------------------------------")
            print(f"{ur} is not a valid input")
            print(f"Please enter an amount between [$1 - ${anteMax}]:")
            print("--------------------------------------------------")




if __name__ == '__main__':
    title()
    newGame(100.20, 30000)