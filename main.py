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
    Z = 1 + int(random.random() * 4)
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
    T = T + 1
    Z = 1 + int(random.random() * 12)
    print("CARD NUMBER " + T + " IS A " + Z)
    B = 0
    B += (2 * A)
    if (Z < 3 or Z > 10):
        O -= A
    if (T == 5):
        print("YOU WIN. AT THE END OF PART 2, YOU HAVE $", B + O)
        B = B + O

    print("YOU ARE STILL IN THE GAME. YOU HAVE ", B)

    print("STOP OR GO")
    A = str(input())
    if (A == "GO"):  #$
        560 #T=T+1:Z=INT(12*RND(1)+1)
    if (A == "STOP"):
       print("YOU WIN. AT THE END OF PART 2, YOU HAVE $",B+O)
       B = B + O
    O = O - A
    print("YOU LOST. AT THE END OF PART 2, YOU HAVE $", O)
    660

    for i in range(5):
        print()

    # Инициализация переменных
    T = 0
    Z = 0
    B = 0
    O = 0

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
#     C = 0
#     C3 = 0
#     print("HERE I GO")
#     Q = int(12 * round(1) + 1)
#     Z5 = Q + Z5
#     print("THE CA
#     RD IS A ", Q)
#     C = C + 1
#     print("SO FAR:", Z5)
#     if (C=6):
#         THEN
#         850)

        # IF
        # Z5 < 17
        # THEN
        # 760
        #
        # if Z5 < 17:
        #     THEN
        # 760
        # if Z5 > 21:
        #     THEN
        # 910
        # if Z5 == 21:
        #     THEN
        # 880
        # if Z5 < 21:
        #     THEN
        # 870
        # if Z5 >= 17: THEN
        # 870
        # if Z5 < 17: THEN
        # 890
        # if Z5 >= 17: THEN
        # 800
        # print("I STOP. THE TOTAL FOR ME IS ");
        # Z5: print
        # "NOW YOU GO": print:GOTO930
        # print("I GOT BLACKJACK"): print:GOTO
        # 930
        # print("THE HOUSE DELT OUT LESS THAN 17. NOW YOU MUST TRY TO")
        # print("BEAT ME");:print: GOTO
        # 930
        # print("I BLEW IT. YOU WIN THE GREATEST AMOUNT ALLOWED TO BE")
        # print("BET BY THE HOUSE."): GOTO1160
        # print("WHAT IS THE BET");:INPUT
        # A
        # if A > O:
        #     THEN
        # 980
        # if A > 50
        # OR
        # A <= 0:
        # THEN
        # 970
        # if A <= 50: THEN
        # 990
        #
        # Q1 = int(12 * random.random()) + 1:print("YOUR CARD IS A ", Q1);
        # Q1:
        # C3 = C3 + 1
        # Z1 = Q1 + Z1:print("SO FAR THE TOTAL FOR YOU IS ", Z1);
        # Z1:
        # if C3 == 6 THEN 1090
        # if Z1 > 21 THEN 1120
        # print "STOP OR GO";:INPUT
        # A$
        # if A$="STOP" THEN 1050
        # if A$="GO" THEN 990
        # if Z1=Z5 THEN 1100
        # if Z1 < Z5 THEN 1120
        # if Z1=21 THEN 1110
        # if Z5 < Z1 THEN 1130
        # if Z1 < 17 THEN 1140
        # O=O+(2 * A):print
        # "YOU BEAT THE DEALER WITH BLACKJACK!!": GOTO1170
        # O = O - (1 * A):print
        # "THE DEALER BEAT YOU. YOU LOSE": GOTO1170
        # O = O + (1 * A):print
        # "THE DEALER LOST. YOU WIN": GOTO1170
        # O = O + (1 * A):print
        # "THE HOUSE DELT OUT LESS THAN 17 IN"
        # print
        # "6 TRIES. YOU GET THE MONEY YOU BET": GOTO1170
        # O = O + 50:print
        # "YOU KEEP IT WITH OUR BEST WISHES.": GOTO1170
        # print
        # "AT THE END OF PART 3, YOU HAVE $";
        # O
        # if O <= 0
        # THEN
        # 1580
        # FOR
        # P = 1
        # TO
        # 5: print:NEXT
        # P
        # print
        # "NOW WE ENTER THE LAST CHANCE ROUND. if YOU MAKE UP TO"
        # print
        # "$300 YOU WILL BE ABLE TO GO INTO THE BONUS ROUND. THE"
        # print
        # "OBJECT IS TO GUESS INTO WHICH CATEGORY THE TOTAL OF 5 CARDS"
        # print
        # "WILL ADD UP TO. THESE ARE THE CATEGORIES:"
        # print
        # "1=31-40 AT 1 TO 1 ODDS     2=41-50 AT 3 TO 1 ODDS"
        # print
        # "3=21-31 AT 3 TO 1 ODDS     4=6-20 AT 20 TO 1 ODDS"
        # print
        # "GOOD LUCK!!": print
        # print
        # "AT THIS POINT IN THE GAME YOU HAVE $";
        # O
        # print
        # "WHAT CATEGORY DO YOU WANT";:INPUT
        # A
        # if A <= 4
        # THEN
        # 1320
        # if A > 4
        # THEN
        # 1310
        # print
        # "***YOU BET ON A WRONG CATEGORY***": GOTO1280
        # print
        # "WHAT IS THE BET";:INPUT
        # B
        # if B <= O
        # THEN
        # 1360
        # if B > O
        # THEN
        # 1350
        # print
        # "***YOU BET OVER WHAT YOU HAVE***": GOTO1320
        # print
        # "THE CARDS ARE NOW BEING ADDED UP": print
        # "GOOD LUCK!"
        # Q = INT(12 * RND(1) + 1):C1 = C1 + 1
        # print
        # "CARD NUMBER ";
        # C1;
        # " IS A ";
        # Q
        # Z = Z + Q:print
        # "SO FAR: ";
        # Z
        # if C1 = 5
        # THEN
        # 1420
        # ON
        # A
        # GOTO
        # 1430, 1460, 1490, 1520
        # if Z < 31
        # THEN
        # 1540
        # if Z < 40
        # THEN
        # 1550
        # if Z > 40
        # THEN
        # 1540
        # if Z < 41
        # THEN
        # 1540
        # if Z < 50
        # THEN
        # 1560
        # if Z > 50
        # THEN
        # 1540
        # if Z < 21
        # THEN
        # 1540
        # if Z < 31
        # THEN
        # 1560
        # if Z > 31
        # THEN
        # 1540
        # if Z < 6
        # THEN
        # 1540
        # if Z < 20
        # THEN
        # 1570
        # O = O - (1 * B):print
        # "YOU LOSE": GOTO1580
        # O = O + (1 * B):print
        # "YOU WIN": GOTO1580
        # O = O + (3 * B):GOTO1580
        # O = O + (20 * B):print
        # "YOU WIN": GOTO1580
        # print
        # "AT THE END OF THE GAME YOU HAVE A GRAND TOTAL OF $";
        # O
        # if O < 300
        # THEN
        # 1940
        # FOR
        # X = 1
        # TO
        # 6: print
        # CHR$(7);:FOR
        # B1 = 1
        # TO
        # 570: NEXT
        # B1: NEXT
        # X
        # print
        # "YOU ARE ELIGIBLE FOR THE BONUS ROUND."
        # print
        # "DO YOU WANT TO PLAY IT";:INPUT
        # A$
        # if A$="NO" THEN 1940
        # print "THIS IS THE BONUS ROUND. if YOU GET A TOTAL OF 1,000"
        # print "WITHOUT GETTING A SPADE IN THE ROLLS, YOU WILL GET"
        # print "A GRAND PRIZE OF $10,000.00. YOU MAY STOP AT ANY POINT"
        # print "DURING THE GAME. YOU WILL KEEP WHAT YOU MADE. GOOD LUCK!"
        # print
        # DIM A(5), B(4):A9$="SPADES"
        # print
        # "THE DICE ARE ROLLING": print
        # "GOOD LUCK."
        # print
        # "THE DICE ARE"
        # FOR
        # B1 = 1
        # TO
        # 570 * 5: NEXT
        # B1
        # X = INT(5 * RND(1) + 1)
        # A(1) = 50:A(2) = 100:A(3) = 150:A(4) = 200:A(5) = 0
        # Y = INT(4 * RND(1) + 1)
        # B(1) = 50:B(2) = 100:B(3) = 150:B(4) = 200
        # if A(X) = 0
        # THEN
        # 1790
        # print
        # "****";
        # A(X);
        # B(Y);
        # "****": print
        # "TOTAL ";
        # A(X) + B(Y): GOTO1810
#