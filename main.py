from distutils.versionpredicate import re_paren


def start_title():
    print("DEALER'S CHOICE")
    print("CREATIVE COMPUTING")
    print("MORRISTOWN, NEW JERSEY")
    print()
    print("THIS PROGRAM WILL SIMULATE THE T.V. SHOW, DEALER'S CHOICE.")
    print("YOU HAVE $100 TO START WITH. ENJOY THE GAME.")

def first_game():
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
    if (Z == A):

    print("YOU WIN ON DIAMONDS")
    print("YOU WIN ON SPADES")
    print("YOU WIN ON HEARTS")
    print("YOU WIN ON CLUBS")
    print("YOU LOSE")
    print("AT THE END OF PART 1, YOU HAVE $" + O)
    return O

def second_game():
    for i in range(5):
        print()
    print("THIS IS THE GAME OF IN BETWEEN. THE OBJECT IS: 5 CARDS WILL")
    print("BE DEALT OUT. IF ANY CARD IS LESS THAN A 3 OR GREATER THAN A")
    print("10, THE GAME IS OVER. YOU MAY BET UP TO $30. YOUR MONEY")
    print("WILL BE DOUBLED EACH TIME YOU ARE RIGHT. GOOD LUCK!")
    print()
    while True:
        print("WHAT IS THE BET")
        A = int(input())
        if not
            IF
            A > 30
            break
       print("***YOU BET OVER THE HOUSE LIMIT ***")
    T = T + 1:Z = int(12 * round(1) + 1)
    print("CARD NUMBER " + T + " IS A " + )









    return
def main():
    start_title()
    O = first_game()
    second_game()