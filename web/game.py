import random


    # start_title()


def main(custom_print=print, custom_input=input):
    # start_title():
    custom_print("                     DEALER'S CHOICE")
    custom_print("                    CREATIVE COMPUTING")
    custom_print("                  MORRISTOWN, NEW JERSEY")
    custom_print()
    custom_print()
    custom_print()
    custom_print("THIS PROGRAM WILL SIMULATE THE T.V. SHOW, DEALER'S CHOICE.")
    custom_print("YOU HAVE $100 TO START WITH. ENJOY THE GAME.")

    # first_game():
    O = 100
    custom_print("FOR THE FIRST GAME, WE WILL PLAY ON THE WHEEL OF CHANCE.")
    custom_print("THE OBJECT IS SIMPLE. GUESS WHAT SUITE WILL APPEAR ON THE")
    custom_print("WHEEL AND YOU WILL GET PAID AT THOSE ODDS IF YOU ARE RIGHT.")
    custom_print("THEY ARE AS FOLLOWS:")
    custom_print()
    custom_print("1=DIAMONDS AT 11 TO 1 ODDS          2=SPADES AT 1 TO 1 ODDS.")
    custom_print("3=HEARTS AT 3 TO 1 ODDS             4=CLUBS AT 3 TO 1 ODDS.")
    custom_print("YOU MAY BET UP TO $25. GOOD LUCK!")
    custom_print()
    while True:
        custom_print("WHAT SUITE DO YOU WANT? ")
        A = custom_input()
        A = int(A)
        if not (A > 4 or A < 1):
            break
        custom_print("***YOU PICKED A WRONG SUITE***")

    while True:
        custom_print("WHAT IS THE BET? ")
        B8 = int(custom_input())

        if not (B8 > 25 or B8 <= 0):
            break
        custom_print("***YOU BET OVER THE HOUSE LIMIT***")

    custom_print("O.K. NOW THAT YOUR BET IS IN, WE WILL SPIN")
    custom_print("THE WHEEL, GOOD LUCK!")
    for B1 in range(10 * 570):
        pass
    custom_print("THE WHEEL IS SLOWING DOWN.")
    for B1 in range(7 * 570):
        pass
    custom_print("THE WHEEL IS STOPPING.")
    for B1 in range(7 * 570):
        pass
    custom_print("THE SUITE IS ")
    for B1 in range(4 * 570):
        pass

    #Z = int(4 * random.random() + 1)
    Z = 2
    custom_print(f"**** {Z} ***")
    if (Z == A):
        if Z == 1:
            O = O + (11 * B8)
            custom_print("YOU WIN ON DIAMONDS")
        elif Z == 2:
            O = O + (1 * B8)
            custom_print("YOU WIN ON SPADES")
        elif Z == 3:
            O = O + (3 * B8)
            custom_print("YOU WIN ON HEARTS")
        else:
            O = O + (3 * B8)
            custom_print("YOU WIN ON CLUBS")
    if (Z != A):
        O = O - (1 * B8)
        custom_print("YOU LOSE")

    custom_print(f"AT THE END OF PART 1, YOU HAVE ${O}")
    for i in range(5):
        custom_print()

    # second_game():
    custom_print("THIS IS THE GAME OF IN BETWEEN. THE OBJECT IS: 5 CARDS WILL")
    custom_print("BE DEALT OUT. IF ANY CARD IS LESS THAN A 3 OR GREATER THAN A")
    custom_print("10, THE GAME IS OVER. YOU MAY BET UP TO $30. YOUR MONEY")
    custom_print("WILL BE DOUBLED EACH TIME YOU ARE RIGHT. GOOD LUCK!")
    custom_print()
    while True:
        custom_print("WHAT IS THE BET? ")
        A = int(custom_input())
        if not (A > 30):
            break
        custom_print("***YOU BET OVER THE HOUSE LIMIT ***")
    T = 0
    B = 0
    while True:

        T = T + 1
        #Z = int(12 * random.random() + 1)
        Z = 11
        custom_print(f"CARD NUMBER {T} IS A {Z}")
        B += (2 * A)
        if (Z < 3 or Z > 10):
            O = O - A
            custom_print(f"YOU LOST. AT THE END OF PART 2, YOU HAVE ${O}")
            break
        if (T == 5):
            custom_print(f"YOU WIN. AT THE END OF PART 2, YOU HAVE ${B + O}")
            B += O
            break
        custom_print(f"YOU ARE STILL IN THE GAME. YOU HAVE {B}")
        custom_print("STOP OR GO")
        AA = str(custom_input())
        if (AA == "STOP"):
            custom_print(f"YOU WIN. AT THE END OF PART 2, YOU HAVE ${B + O}")
            B = B + O
            break
        if (AA == "GO"):
            pass

    for i in range(5):
        custom_print()

    # third game
    custom_print("THIS IS THE GAME OF BLACKJACK <DEALER'S CHOICE STYLE>")
    custom_print("THE OBJECT IS TO BEAT THE DEALER WITH OVER 17 OR 21 OR")
    custom_print("UNDER. YOU MAY BET UP TO $50. YOU MAY STOP WHEN YOU WISH.")
    custom_print("IF YOU MAKE BLACKJACK, YOUR MONEY IS DOUBLED.")
    custom_print("IF THE HOUSE DEALS OUT LESS THAN A TOTAL OF 17 IN 6 TRIES,")
    custom_print("YOU WILL KEEP THE MONEY YOU BET. GOOD LUCK!")
    custom_print()
    custom_print("THE DEALER WILL GET HIS CARDS FIRST")
    custom_print()
    custom_print("HERE I GO")
    Z5 = 0
    C = 0
    while True:
        #Q = int(12 * random.random() + 1)
        Q = 6
        Z5 = Q + Z5
        custom_print(f"THE CARD IS A {Q}")
        C = C + 1
        custom_print(f"SO FAR: {Z5}")
        if C == 6:
            if Z5 < 17:
                custom_print("THE HOUSE DELT OUT LESS THAN 17. NOW YOU MUST TRY TO")
                custom_print("BEAT ME")
                custom_print()
            if Z5 >= 17:
                if Z5 > 21:
                    custom_print("I BLEW IT. YOU WIN THE GREATEST AMOUNT ALLOWED TO BE")
                    custom_print("BET BY THE HOUSE.")
                    O += 50
                    custom_print("YOU KEEP IT WITH OUR BEST WISHES.")
                    break
                if Z5 == 21:
                    custom_print("I GOT BLACKJACK")
                    custom_print()
                if Z5 < 21:
                    custom_print(f"I STOP. THE TOTAL FOR ME IS {Z5}")
                    custom_print()
                    custom_print("NOW YOU GO")
                    custom_print()
        else:
            if Z5 < 17:
                continue
            if Z5 > 21:
                custom_print("I BLEW IT. YOU WIN THE GREATEST AMOUNT ALLOWED TO BE")
                custom_print("BET BY THE HOUSE.")
                O += 50
                custom_print("YOU KEEP IT WITH OUR BEST WISHES.")
                break
            if Z5 == 21:
                custom_print("I GOT BLACKJACK")
                custom_print()
            if Z5 < 21:
                custom_print(f"I STOP. THE TOTAL FOR ME IS {Z5}")
                custom_print()
                custom_print("NOW YOU GO")
                custom_print()

        while True:
            custom_print("WHAT IS THE BET")
            A = int(custom_input())
            if (A > O):
                custom_print("***YOU BET OVER WHAT YOU HAVE***")
                pass
            if A > 50 or A <= 0:
                custom_print("***YOU BET OVER THE HOUSE LIMIT***")
                pass
            break

        C3 = 0
        Z1 = 0

        flag = False
        while True:
            #Q1 = int(12 * random.random() + 1)
            Q1 = 7
            custom_print(f"YOUR CARD IS A {Q1}")
            C3 = C3 + 1
            Z1 = Q1 + Z1
            custom_print(f"SO FAR THE TOTAL FOR YOU IS {Z1}")
            if (C3 == 6):
                if Z1 < 17:
                    O += A
                    custom_print("THE HOUSE DELT OUT LESS THAN 17 IN")
                    custom_print("6 TRIES. YOU GET THE MONEY YOU BET")
                    break
                else:
                    custom_print("WE ARE THE SAME SO WE WILL PLAY AGAIN")
                    continue
            else:
                if Z1 > 21:
                    O = O - (1 * A)
                    custom_print("THE DEALER BEAT YOU. YOU LOSE")
                    flag = True
                    break
                else:
                    custom_print("STOP OR GO")
                    AA = str(custom_input())
                    if AA == "STOP":
                        if Z1 == Z5:
                            custom_print("WE ARE THE SAME SO WE WILL PLAY AGAIN")
                            Z5 = 0
                            C = 0
                            C3 = 0
                            Z1 = 0
                            flag = False
                            break
                        if Z1 < Z5:
                            O = O - (1 * A)
                            custom_print("THE DEALER BEAT YOU. YOU LOSE")
                            flag = True
                            break
                        if Z5 < Z1:
                            O = O + (1 * A)
                            custom_print("THE DEALER LOST. YOU WIN")
                            flag = True
                            break
                        if Z1 < 17:
                            O = O + (1 * A)
                            custom_print("THE HOUSE DELT OUT LESS THAN 17 IN")
                            custom_print("6 TRIES. YOU GET THE MONEY YOU BET")
                            flag = True
                            break

                    if AA == "GO":
                        continue
        if flag == True:
            break
        if flag == False:
            continue

    custom_print(f"AT THE END OF PART 3, YOU HAVE ${O}")
    if O <= 0:
        custom_print(f"AT THE END OF THE GAME YOU HAVE A GRAND TOTAL OF ${O}")
        exit
    for i in range(5):
        custom_print()

    # part four
    custom_print("NOW WE ENTER THE LAST CHANCE ROUND. IF YOU MAKE UP TO")
    custom_print("$300 YOU WILL BE ABLE TO GO INTO THE BONUS ROUND. THE")
    custom_print("OBJECT IS TO GUESS INTO WHICH CATEGORY THE TOTAL OF 5 CARDS")
    custom_print("WILL ADD UP TO. THESE ARE THE CATEGORIES:")
    custom_print()
    custom_print("1=31-40 AT 1 TO 1 ODDS     2=41-50 AT 3 TO 1 ODDS")
    custom_print("3=21-31 AT 3 TO 1 ODDS     4=6-20 AT 20 TO 1 ODDS")
    custom_print("GOOD LUCK!!")
    custom_print()
    custom_print("AT THIS POINT IN THE GAME YOU HAVE ${O}")
    while True:
        custom_print("WHAT CATEGORY DO YOU WANT")
        A = int(custom_input())
        if A > 4 or A < 0:
            custom_print("***YOU BET ON A WRONG CATEGORY***")
            continue
        if A <= 4:
            break

    while True:
        custom_print("WHAT IS THE BET")
        B = int(custom_input())
        if B <= O:
            custom_print("THE CARDS ARE NOW BEING ADDED UP")
            custom_print("GOOD LUCK!")
            break
        if B > O:
            custom_print("***YOU BET OVER WHAT YOU HAVE***")
            continue
    C1 = 0
    Z = 0
    while True:
        Q = int(12 * random.random() + 1)
        C1 = C1 + 1
        custom_print(f"CARD NUMBER {C1} IS A {Q}")
        Z = Z + Q
        custom_print(f"SO FAR: {Z}")
        if C1 == 5:
            if (A == 1 and Z < 31) and (A == 2 and 31 <= Z < 40) and (A == 3 and 40 <= Z < 50) and (A == 4 and 50 <= Z):
                O = O + (1 * B)
                custom_print("YOU WIN")
                break
            else:
                O = O - (1 * B)
                custom_print("YOU LOSE")
                break
        else:
            continue
    custom_print(f"AT THE END OF THE GAME YOU HAVE A GRAND TOTAL OF ${O}")
    if O < 300:
        custom_print("THIS IS THE END OF THE GAME. I HOPE YOU ENJOYED IT.")
        exit
    for i in range(5):
        custom_print(" ")
    custom_print("YOU ARE ELIGIBLE FOR THE BONUS ROUND.")
    custom_print("DO YOU WANT TO PLAY IT")
    A = str(custom_input())
    if A == "NO":
        custom_print("THIS IS THE END OF THE GAME. I HOPE YOU ENJOYED IT.")
        exit
    custom_print("THIS IS THE BONUS ROUND. IF YOU GET A TOTAL OF 1,000")
    custom_print("WITHOUT GETTING A SPADE IN THE ROLLS, YOU WILL GET")
    custom_print("A GRAND PRIZE OF $10,000.00. YOU MAY STOP AT ANY POINT")
    custom_print("DURING THE GAME. YOU WILL KEEP WHAT YOU MADE. GOOD LUCK!")
    custom_print()
    A = [0] * 6
    B = [0] * 5
    A9 = "SPADES"
    B7 = 0
    while True:
        custom_print("THE DICE ARE ROLLING")
        custom_print("GOOD LUCK.")
        custom_print("THE DICE ARE")
        X = int(4 * random.random() + 1)
        A[0] = 50
        A[1] = 100
        A[2] = 150
        A[3] = 200
        A[4] = 0
        Y = int(3 * random.random() + 1)
        B[0] = 50
        B[1] = 100
        B[2] = 150
        B[4] = 200
        if A[X] == 0:
            custom_print(f"**** {A9} {B[Y]} ****")
            custom_print(f"TOTAL {B[Y]}")
        custom_print(f"**** {A[X]} {B[Y]} ****")
        custom_print(f"TOTAL {A[X] + B[Y]}")
        B7 = B7 + A[X] + B[Y]
        custom_print(f"YOU NOW HAVE {B7}")
        if B7 >= 1000:
            for i in range(3):
                custom_print(" ")
            B7 = O + 10000
            custom_print(f"                ****CONGRATULATIONS****")
            custom_print("YOU WON THE GRAND PRIZE. AT THE END OF THE GAME, YOU HAVE")
            for i in range(3):
                custom_print()
            custom_print(f"                   ******* {B7} ******")
            custom_print("THIS IS THE END OF THE GAME. I HOPE YOU ENJOYED IT.")
        custom_print("STOP OR GO")
        BB = str(custom_input())
        if BB == "GO":
            continue
        custom_print("SMART MOVE. YOU GET THE MONEY FROM THE BEGINNING OF")
        custom_print("THE GAME PLUS THE BONUS ROUND. AT THE END OF THE GAME")
        custom_print(f"YOU HAVE THE GRAND TOTAL OF ${B7 + O}")
        custom_print("THIS IS THE END OF THE GAME. I HOPE YOU ENJOYED IT.")
        exit

if __name__ == "__main__":
    main()
