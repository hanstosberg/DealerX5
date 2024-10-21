import random

# start_title():
print("DEALER'S CHOICE")
print("CREATIVE COMPUTING")
print("MORRISTOWN, NEW JERSEY")
print()
print("THIS PROGRAM WILL SIMULATE THE T.V. SHOW, DEALER'S CHOICE.")
print("YOU HAVE $100 TO START WITH. ENJOY THE GAME.")

# first_game():
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

# second_game():
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
    print("CARD NUMBER ", T, " IS A ", Z)
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

# third game
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
    print("THE CARD IS A ", Q)
    C = C + 1
    print("SO FAR:", Z5)
    if C == 6:
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
                print("I STOP. THE TOTAL FOR ME IS ", Z5)
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
            print("I GOT BLACKJACK")
            print()
        if Z5 < 21:
            print("I STOP. THE TOTAL FOR ME IS ", Z5)
            print()
            print("NOW YOU GO")
            print()

    while True:
        print("WHAT IS THE BET")
        A = int(input())
        if (A > O):
            print("***YOU BET OVER WHAT YOU HAVE***")
            pass
        if A > 50 or A <= 0:
            print("***YOU BET OVER THE HOUSE LIMIT***")
            pass
        break

    C3 = 0
    Z1 = 0

    flag = False
    while True:
        Q1 = int(12 * random.random() + 1)
        print("YOUR CARD IS A ", Q1)
        C3 = C3 + 1
        Z1 = Q1 + Z1
        print("SO FAR THE TOTAL FOR YOU IS ", Z1)
        if (C3 == 6):
            if Z1 < 17:
                O += A
                print("THE HOUSE DELT OUT LESS THAN 17 IN")
                print("6 TRIES. YOU GET THE MONEY YOU BET")
                break
            else:
                print("WE ARE THE SAME SO WE WILL PLAY AGAIN")
                continue
        else:
            if Z1 > 21:
                O = O - (1 * A)
                print("THE DEALER BEAT YOU. YOU LOSE")
                flag = True
                break
            else:
                print("STOP OR GO")
                AA = str(input())
                if AA == "STOP":
                    if Z1 == Z5:
                        print("WE ARE THE SAME SO WE WILL PLAY AGAIN")
                        Z5 = 0
                        C = 0
                        C3 = 0
                        Z1 = 0
                        flag = False
                        break
                    if Z1 < Z5:
                        O = O - (1 * A)
                        print("THE DEALER BEAT YOU. YOU LOSE")
                        flag = True
                        break
                    if Z5 < Z1:
                        O = O + (1 * A)
                        print("THE DEALER LOST. YOU WIN")
                        flag = True
                        break
                    if Z1 < 17:
                        O = O + (1 * A)
                        print("THE HOUSE DELT OUT LESS THAN 17 IN")
                        print("6 TRIES. YOU GET THE MONEY YOU BET")
                        flag = True
                        break

                if AA == "GO":
                    continue
    if flag == True:
        break
    if flag == False:
        continue

print("AT THE END OF PART 3, YOU HAVE $", O)
if O <= 0:
    print("AT THE END OF THE GAME YOU HAVE A GRAND TOTAL OF $", O)
    exit
for i in range(5):
    print()

# part four
print("NOW WE ENTER THE LAST CHANCE ROUND. IF YOU MAKE UP TO")
print("$300 YOU WILL BE ABLE TO GO INTO THE BONUS ROUND. THE")
print("OBJECT IS TO GUESS INTO WHICH CATEGORY THE TOTAL OF 5 CARDS")
print("WILL ADD UP TO. THESE ARE THE CATEGORIES:")
print()
print("1=31-40 AT 1 TO 1 ODDS     2=41-50 AT 3 TO 1 ODDS")
print("3=21-31 AT 3 TO 1 ODDS     4=6-20 AT 20 TO 1 ODDS")
print("GOOD LUCK!!")
print()
print("AT THIS POINT IN THE GAME YOU HAVE $", O)
while True:
    print("WHAT CATEGORY DO YOU WANT")
    A = int(input())
    if A > 4 or A < 0:
        print("***YOU BET ON A WRONG CATEGORY***")
        continue
    if A <= 4:
        break

while True:
    print("WHAT IS THE BET")
    B = int(input())
    if B <= O:
        print("THE CARDS ARE NOW BEING ADDED UP")
        print("GOOD LUCK!")
        break
    if B > O:
        print("***YOU BET OVER WHAT YOU HAVE***")
        continue
C1 = 0
Z = 0
while True:
    Q = int(12 * random.random() + 1)
    C1 = C1 + 1
    print("CARD NUMBER ", C1, " IS A ", Q)
    Z = Z + Q
    print("SO FAR: ", Z)
    if C1 == 5:
        if (A == 1 and Z < 31) and (A == 2 and 31 <= Z < 40) and (A == 3 and 40 <= Z < 50) and (A == 4 and 50 <= Z):
            O = O + (1 * B)
            print("YOU WIN")
            break
        else:
            O = O - (1 * B)
            print("YOU LOSE")
            break
    else:
        continue
print("AT THE END OF THE GAME YOU HAVE A GRAND TOTAL OF $", O)
if O < 300:
    print("THIS IS THE END OF THE GAME. I HOPE YOU ENJOYED IT.")
    exit
for i in range(5):
    print(" ")
print("YOU ARE ELIGIBLE FOR THE BONUS ROUND.")
print("DO YOU WANT TO PLAY IT")
A = str(input())
if A == "NO":
    print("THIS IS THE END OF THE GAME. I HOPE YOU ENJOYED IT.")
    exit
print("THIS IS THE BONUS ROUND. IF YOU GET A TOTAL OF 1,000")
print("WITHOUT GETTING A SPADE IN THE ROLLS, YOU WILL GET")
print("A GRAND PRIZE OF $10,000.00. YOU MAY STOP AT ANY POINT")
print("DURING THE GAME. YOU WILL KEEP WHAT YOU MADE. GOOD LUCK!")
print()
A = [0] * 6
B = [0] * 5
A9 = "SPADES"
B7 = 0
while True:
    print("THE DICE ARE ROLLING")
    print("GOOD LUCK.")
    print("THE DICE ARE")
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
        print("****", A9, B[Y], "****")
        print("TOTAL ", B[Y])
    print("****", A[X], B[Y], "****")
    print("TOTAL ", A[X] + B[Y])
    B7 = B7 + A[X] + B[Y]
    print("YOU NOW HAVE ", B7)
    if B7 >= 1000:
        for i in range(3):
            print(" ")
        B7 = O + 10000
        print("               ", "****CONGRATULATIONS****")
        print("YOU WON THE GRAND PRIZE. AT THE END OF THE GAME, YOU HAVE")
        for i in range(3):
            print()
        print(("                  ", "*******", B7, "******"))
        print("THIS IS THE END OF THE GAME. I HOPE YOU ENJOYED IT.")
    print("STOP OR GO")
    BB = str(input())
    if BB == "GO":
        continue
    print("SMART MOVE. YOU GET THE MONEY FROM THE BEGINNING OF")
    print("THE GAME PLUS THE BONUS ROUND. AT THE END OF THE GAME")
    print("YOU HAVE THE GRAND TOTAL OF $", B7 + O)
    print("THIS IS THE END OF THE GAME. I HOPE YOU ENJOYED IT.")
    exit