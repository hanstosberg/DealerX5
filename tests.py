import subprocess


def process(command):
    return subprocess.Popen(
        command.split(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdin=subprocess.PIPE,
        shell=True
    )


def expect(proc, pattern):
    pattern = pattern.strip("\n")
    buffer = ""
    while True:
        buffer += proc.stdout.read(1).decode()
        buffer = buffer.replace('\r', '')
        if pattern.endswith(buffer):
            return True


def write(proc, text):
    proc.stdin.write(f'{text}\n'.encode())
    proc.stdin.flush()
    return text


def test():
    print("Launching processes")
    try:
        bas = process('D:\\DealerX5\\DealerX5\\dealerx5.bas')
        py = process('python D:\\DealerX5\\DealerX5\\main.py')

        expected_greetings = '''                     DEALER'S CHOICE
                    CREATIVE COMPUTING
                  MORRISTOWN, NEW JERSEY



THIS PROGRAM WILL SIMULATE THE T.V. SHOW, DEALER'S CHOICE.
YOU HAVE $100 TO START WITH. ENJOY THE GAME.

FOR THE FIRST GAME, WE WILL PLAY ON THE WHEEL OF CHANCE.
THE OBJECT IS SIMPLE. GUESS WHAT SUITE WILL APPEAR ON THE
WHEEL AND YOU WILL GET PAID AT THOSE ODDS IF YOU ARE RIGHT.
THEY ARE AS FOLLOWS:

1=DIAMONDS AT 11 TO 1 ODDS          2=SPADES AT 1 TO 1 ODDS.
3=HEARTS AT 3 TO 1 ODDS             4=CLUBS AT 3 TO 1 ODDS.
YOU MAY BET UP TO $25. GOOD LUCK!

WHAT SUITE DO YOU WANT? '''
        print("expecting answers...")
        # приветствие и начало первой игры
        expect(bas, expected_greetings)
        expect(py, expected_greetings)
        print("[+] TEST 1 - PASSED")
        print("sending keys...")
        write(bas, 1)
        write(py, 1)
        print("[+] KEYS SENT")
        instruction = '''WHAT IS THE BET? '''
        print("expecting results")
        expect(bas, instruction)
        expect(py, instruction)
        print("[+] TEST 2 - PASSED")
        print("sending keys...")
        write(bas, 25)
        write(py, 25)
        print("[+] KEYS SENT")
        print("expecting answers...")
        instruction = '''O.K. NOW THAT YOUR BET IS IN, WE WILL SPIN
THE WHEEL, GOOD LUCK!
THE WHEEL IS SLOWING DOWN.
THE WHEEL IS STOPPING.
THE SUITE IS
**** 2 ****
YOU LOSE.
AT THE END OF PART 1, YOU HAVE $ 75





THIS IS THE GAME OF IN BETWEEN. THE OBJECT IS: 5 CARDS WILL
BE DEALT OUT. IF ANY CARD IS LESS THAN A 3 OR GREATER THAN A
10, THE GAME IS OVER. YOU MAY BET UP TO $30. YOUR MONEY
WILL BE DOUBLED EACH TIME YOU ARE RIGHT. GOOD LUCK!

WHAT IS THE BET? '''

        expect(bas, instruction)
        expect(py, instruction)
        print("[+] TEST 3 - PASSED")
        #начало второй игры
        print("sending keys...")
        write(bas, 25)
        write(py, 25)
        print("[+] KEYS SENT")
        instruction = '''CARD NUMBER  1  IS A  11
YOU LOST. AT THE END OF PART 2, YOU HAVE $ 50





THIS IS THE GAME OF BLACKJACK <DEALER'S CHOICE STYLE>
THE OBJECT IS TO BEAT THE DEALER WITH OVER 17 OR 21 OR
UNDER. YOU MAY BET UP TO $50. YOU MAY STOP WHEN YOU WISH.
IF YOU MAKE BLACKJACK, YOUR MONEY IS DOUBLED.
IF THE HOUSE DEALS OUT LESS THAN A TOTAL OF 17 IN 6 TRIES,
YOU WILL KEEP THE MONEY YOU BET. GOOD LUCK!

THE DEALER WILL GET HIS CARDS FIRST

HERE I GO
THE CARD IS A  6
SO FAR: 6
THE CARD IS A  6
SO FAR: 12
THE CARD IS A  6
SO FAR: 18
I STOP. THE TOTAL FOR ME IS
NOW YOU GO

WHAT IS THE BET? '''
        print("expecting results")
        expect(bas, instruction)
        expect(py, instruction)
        print("[+] TEST 4 - PASSED")

        print("sending keys...")
        write(bas, 25)
        write(py, 25)
        print("[+] KEYS SENT")
        print("expecting answers...")
        instruction = '''
YOUR CARD IS A  7
SO FAR THE TOTAL FOR YOU IS  7
STOP OR GO? 
'''
        expect(bas, instruction)
        expect(py, instruction)
        print("[+] TEST 5 - PASSED")

        print("sending keys...")
        write(bas, "GO")
        write(py, "GO")
        print("[+] KEYS SENT")
        instruction = '''
YOUR CARD IS A  7
SO FAR THE TOTAL FOR YOU IS  14
STOP OR GO? 
'''
        print("expecting results")
        expect(bas, instruction)
        expect(py, instruction)
        print("[+] TEST 6 - PASSED")

        print("sending keys...")
        write(bas, "GO")
        write(py, "GO")
        print("[+] KEYS SENT")
        print("expecting answers...")
        instruction = '''
YOUR CARD IS A  7
SO FAR THE TOTAL FOR YOU IS  21
STOP OR GO? 
'''
        expect(bas, instruction)
        expect(py, instruction)
        print("[+] TEST 7 - PASSED")
        print("sending keys...")
        write(bas, "STOP")
        write(py, "STOP")
        print("[+] KEYS SENT")
        print("expecting answers...")

        instruction = '''
NOW WE ENTER THE LAST CHANCE ROUND. IF YOU MAKE UP TO
$300 YOU WILL BE ABLE TO GO INTO THE BONUS ROUND. THE
OBJECT IS TO GUESS INTO WHICH CATEGORY THE TOTAL OF 5 CARDS
WILL ADD UP TO. THESE ARE THE CATEGORIES:

1=31-40 AT 1 TO 1 ODDS     2=41-50 AT 3 TO 1 ODDS
3=21-31 AT 3 TO 1 ODDS     4=6-20 AT 20 TO 1 ODDS
GOOD LUCK!!

AT THIS POINT IN THE GAME YOU HAVE $ 75
WHAT CATEGORY DO YOU WANT? 
'''
        expect(bas, instruction)
        expect(py, instruction)
        print("[+] TEST 8 - PASSED")

        print("sending keys...")
        write(bas, 1)
        write(py, 1)
        print("[+] KEYS SENT")
        print("expecting answers...")
        instruction = '''
WHAT IS THE BET? 
'''
        expect(bas, instruction)
        expect(py, instruction)
        print("[+] TEST 9 - PASSED")

        print("sending keys...")
        write(bas, 25)
        write(py, 25)
        print("[+] KEYS SENT")
        print("expecting answers...")
        instruction = '''
THE CARDS ARE NOW BEING ADDED UP
GOOD LUCK!
CARD NUMBER  1  IS A  10
SO FAR:  10
CARD NUMBER  2  IS A  10
SO FAR:  20
CARD NUMBER  3  IS A  10
SO FAR:  30
CARD NUMBER  4  IS A  10
SO FAR:  40
CARD NUMBER  5  IS A  10
SO FAR:  50
YOU LOSE
AT THE END OF THE GAME YOU HAVE A GRAND TOTAL OF $ 125
THIS IS THE END OF THE GAME. I HOPE YOU ENJOYED IT. 
'''
        expect(bas, instruction)
        expect(py, instruction)
        print("[+] TEST 10 - PASSED")

    except Exception as ex:
        print(ex)


test()