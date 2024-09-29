
def start_title():
    print("DEALER'S CHOICE")
    print("CREATIVE COMPUTING")
    print("MORRISTOWN, NEW JERSEY")
    print()
    print("THIS PROGRAM WILL SIMULATE THE T.V. SHOW, DEALER'S CHOICE.")


def main():
    start_title()
    print("YOU HAVE $100 TO START WITH. ENJOY THE GAME.")
    O = 100
    print("FOR THE FIRST GAME, WE WILL PLAY ON THE WHEEL OF CHANCE.")
    print("THE OBJECT IS SIMPLE. GUESS WHAT SUITE WILL APPEAR ON THE")
    print("WHEEL AND YOU WILL GET PAID AT THOSE ODDS IF YOU ARE RIGHT.")
    print("THEY ARE AS FOLLOWS:")
    print("1=DIAMONDS AT 11 TO 1 ODDS          2=SPADES AT 1 TO 1 ODDS.")
    print("3=HEARTS AT 3 TO 1 ODDS             4=CLUBS AT 3 TO 1 ODDS.")
    print("YOU MAY BET UP TO $25. GOOD LUCK!")
    while True:
        print("WHAT SUITE DO YOU WANT")
        A = int(input())
        if not (A > 4 or A < 1):
            break
        print("***YOU PICKED A WRONG SUITE***")

    while True:
        print("WHAT IS THE BET")
        B8 = int(input())
        if not (B8 <= 25):
            break
        print("***YOU BET OVER THE HOUSE LIMIT***")

    print("O.K. NOW THAT YOUR BET IS IN, WE WILL SPIN")
    print("THE WHEEL, GOOD LUCK!")
    #:FOR B1=1 TO 10*570:NEXT B1
    B1 = 1
    #for B1 in range(10*570):
     #   B1 =
    print("THE WHEEL IS SLOWING DOWN.")
    print("THE WHEEL IS STOPPING.")
    print("THE SUITE IS ", " ")

    Z = int(4*round(1)+1)
    print("****" + Z + "****")
