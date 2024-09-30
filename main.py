


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
    print()
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

        if not (B8 > 25 or B8 <= 0):
            break
        print("***YOU BET OVER THE HOUSE LIMIT***")

    print("O.K. NOW THAT YOUR BET IS IN, WE WILL SPIN")
    print("THE WHEEL, GOOD LUCK!")
    print("THE WHEEL, GOOD LUCK!")
    for B1 in range(10 * 570):
        pass
    print("THE WHEEL IS SLOWING DOWN.")
    for B1 in range(7 * 570):
        pass
    print("THE WHEEL IS STOPPING.")
    for B1 in range(7 * 570):
        pass
    print("THE SUITE IS ", )
    for B1 in range(4 * 570):
        pass
    Z = int(4*random(1)+1)
    print("****" + Z + "****")
    if (Z == A):
        return 0
    print("YOU WIN ON DIAMONDS")
    print("YOU WIN ON SPADES")
    print("YOU WIN ON HEARTS")
    print("YOU WIN ON CLUBS")
    print("YOU LOSE")
    print("AT THE END OF PART 1, YOU HAVE $" + O)
    for i in range(5):
        print()
    return O
    #
# # def second_game():
#     print("THIS IS THE GAME OF IN BETWEEN. THE OBJECT IS: 5 CARDS WILL")
#     print("BE DEALT OUT. IF ANY CARD IS LESS THAN A 3 OR GREATER THAN A")
#     print("10, THE GAME IS OVER. YOU MAY BET UP TO $30. YOUR MONEY")
#     print("WILL BE DOUBLED EACH TIME YOU ARE RIGHT. GOOD LUCK!")
#     print()
#     while True:
#         print("WHAT IS THE BET")
#         A = int(input())
#         if not (A > 30):
#             break
#        print("***YOU BET OVER THE HOUSE LIMIT ***")
#     # T = T + 1:Z = int(12 * round(1) + 1)
#     # print("CARD NUMBER " + T + " IS A " + Z:B=B+(2*A))
#     if (Z < 3 OR Z > 10):
#         HEN 630
#     if(T == 5):
#         650
#     print("YOU ARE STILL IN THE GAME. YOU HAVE " , B)
#     print("STOP OR GO")
#     A = str(input())
#     if(A =="GO"):
#         560
#     if(A == "STOP"):
#         650
#
#     O = O-A
#     print("YOU LOST. AT THE END OF PART 2, YOU HAVE $", O) 660
#     print("YOU WIN. AT THE END OF PART 2, YOU HAVE $", B+O) B=B+O
#
#     for i in range(5):
#         print()
#
#     return O
#
# def third_game():
#     print("THIS IS THE GAME OF BLACKJACK <DEALER'S CHOICE STYLE>")
#     print("THE OBJECT IS TO BEAT THE DEALER WITH OVER 17 OR 21 OR")
#     print("UNDER. YOU MAY BET UP TO $50. YOU MAY STOP WHEN YOU WISH.")
#     print("IF YOU MAKE BLACKJACK, YOUR MONEY IS DOUBLED.")
#     print("IF THE HOUSE DEALS OUT LESS THAN A TOTAL OF 17 IN 6 TRIES,")
#     print("YOU WILL KEEP THE MONEY YOU BET. GOOD LUCK!")
#     print()
#     Z5 = 0
#     Z1 = 0
#     print("THE DEALER WILL GET HIS CARDS FIRST")
#     print()
#     C=0
#     C3 =0
#     print("HERE I GO")
#     Q = int(12*round(1)+1)
#     Z5 = Q+Z5
#     print("THE CARD IS A ", Q)
#     C = C+1
#     print("SO FAR:",Z5)
#     if(C=6):
#         THEN 850)








def main():
    start_title()
    first_game()
    #second_game()