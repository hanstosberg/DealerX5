import random


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
    Z = int(4 * random.random() + 1)
    print("****", Z, "****")
    if (Z == A):
        if Z == 1:
            O = O + (11 * B8)
            print("YOU WIN ON DIAMONDS")
        elif Z == 2:
            O = O + (1 * B8)
            print("YOU WIN ON SPADES")
        elif Z == 3:
            O = O + (3 * B8)
            print("YOU WIN ON HEARTS")
        else:
            O = O + (3 * B8)
            print("YOU WIN ON CLUBS")
    if (Z != A):
        O = O - (1 * B8)
        print("YOU LOSE")

    print("AT THE END OF PART 1, YOU HAVE $", O)
    for i in range(5):
        print()
    return O
    #


def second_game():

    O = 100 # временно для отладки

    print("THIS IS THE GAME OF IN BETWEEN. THE OBJECT IS: 5 CARDS WILL")
    print("BE DEALT OUT. IF ANY CARD IS LESS THAN A 3 OR GREATER THAN A")
    print("10, THE GAME IS OVER. YOU MAY BET UP TO $30. YOUR MONEY")
    print("WILL BE DOUBLED EACH TIME YOU ARE RIGHT. GOOD LUCK!")
    print()
    while True:
        print("WHAT IS THE BET")
        A = int(input())
        if not (A > 30):
            break
        print("***YOU BET OVER THE HOUSE LIMIT ***")
    T = 0
    B = 0
    while True:

        T = T + 1
        Z = int(12 * random.random() + 1)
        print("CARD NUMBER " , T , " IS A " , Z)
        B += (2 * A)
        if (Z < 3 or Z > 10):
            O = O - A
            print("YOU LOST. AT THE END OF PART 2, YOU HAVE $", O)
            break
        if (T == 5):
            print("YOU WIN. AT THE END OF PART 2, YOU HAVE $", B + O)
            B += O
            break
        print("YOU ARE STILL IN THE GAME. YOU HAVE ", B)
        print("STOP OR GO")
        AA = str(input())
        if (AA == "STOP"):
            print("YOU WIN. AT THE END OF PART 2, YOU HAVE $", B + O)
            B = B + O
            break
        if (AA == "GO"):
            pass

    for i in range(5):
        print()




def third_game():

    O = 100

    print("THIS IS THE GAME OF BLACKJACK <DEALER'S CHOICE STYLE>")
    print("THE OBJECT IS TO BEAT THE DEALER WITH OVER 17 OR 21 OR")
    print("UNDER. YOU MAY BET UP TO $50. YOU MAY STOP WHEN YOU WISH.")
    print("IF YOU MAKE BLACKJACK, YOUR MONEY IS DOUBLED.")
    print("IF THE HOUSE DEALS OUT LESS THAN A TOTAL OF 17 IN 6 TRIES,")
    print("YOU WILL KEEP THE MONEY YOU BET. GOOD LUCK!")
    print()


    print("THE DEALER WILL GET HIS CARDS FIRST")
    print()


    print("HERE I GO")

    Z5 = 0
    C = 0
    while True:
        Q = int(12 * random.random() + 1)
        Z5 = Q + Z5
        print("THE CARD IS A ",Q)
        C=C+1
        print("SO FAR:", Z5)
        if C==6:
            if Z5 < 17:
                print("THE HOUSE DELT OUT LESS THAN 17. NOW YOU MUST TRY TO")
                print("BEAT ME")
                print()
            if Z5 >= 17:
                if Z5 > 21:
                    print("I BLEW IT. YOU WIN THE GREATEST AMOUNT ALLOWED TO BE")
                    print("BET BY THE HOUSE.")
                    O += 50
                    print("YOU KEEP IT WITH OUR BEST WISHES.")
                    break
                if Z5 == 21:
                    print("I GOT BLACKJACK")
                    print()
                if Z5 < 21:
                    print("I STOP. THE TOTAL FOR ME IS ",Z5)
                    print()
                    print("NOW YOU GO")
                    print()
        else:
            if Z5 < 17:
                continue
            if Z5 > 21:
                print("I BLEW IT. YOU WIN THE GREATEST AMOUNT ALLOWED TO BE")
                print("BET BY THE HOUSE.")
                O += 50
                print("YOU KEEP IT WITH OUR BEST WISHES.")
                break
            if Z5 == 21:
                print("YOU BEAT THE DEALER WITH BLACKJACK!!")
                print()
            if Z5 < 21:
                print("I STOP. THE TOTAL FOR ME IS ",Z5)
                print()
                print("NOW YOU GO")
                print()

        while True:
            print("WHAT IS THE BET")
            A = int(input())
            if (A > O):
                print("***YOU BET OVER WHAT YOU HAVE***")
                pass
            if A>50 or A <=0:
                print("***YOU BET OVER THE HOUSE LIMIT***")
                pass
            break

        C3 = 0
        Z1 = 0
        Q1= int(12 * random.random() + 1)
        print("YOUR CARD IS A ",Q1)
        C3 = C3 + 1
        Z1 = Q1 + Z1
        print("SO FAR THE TOTAL FOR YOU IS ",Z1)
        if (C3 == 6):
            if Z1 < 17:
                O += A
                print("THE HOUSE DELT OUT LESS THAN 17 IN")
                print("6 TRIES. YOU GET THE MONEY YOU BET")
                break
            else:
                print("WE ARE THE SAME SO WE WILL PLAY AGAIN")
                pass
        else:
            if Z1 > 21:
                O = O - (1 * A)
                print("THE DEALER BEAT YOU. YOU LOSE")
                break
            else:
                print("STOP OR GO")
                A = str(input())
                if A == "STOP":
                    if Z1 == Z5:
                        print("WE ARE THE SAME SO WE WILL PLAY AGAIN")
                        pass
                    if Z5 < Z1:
                        print("THE DEALER LOST. YOU WIN")
                        break
                    if Z1 < 17:
                        print("THE HOUSE DELT OUT LESS THAN 17 IN")
                        print("6 TRIES. YOU GET THE MONEY YOU BET")
                        break

    print("AT THE END OF PART 3, YOU HAVE $",O)
    if O <=0:
        print("AT THE END OF THE GAME YOU HAVE A GRAND TOTAL OF $",O)
    for i in range(5):
        print()

third_game()