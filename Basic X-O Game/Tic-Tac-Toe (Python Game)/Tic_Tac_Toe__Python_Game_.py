import random


Board = [" - ", " - ", " - ", 
         " - ", " - ", " - ", 
         " - ", " - ", " - ",]
CurrentPlayer = " X "
Winner = None
GameRunning = True


# print the board
def PrintBoard(Board):
    print("")
    print(Board[0] + " | " + Board[1] + " | " + Board[2])
    print("----------------")
    print(Board[3] + " | " + Board[4] + " | " + Board[5])
    print("----------------")
    print(Board[6] + " | " + Board[7] + " | " + Board[8])
    print("")


# take player input
def PlayerInput(Board):
    Input = int(input("Enter a number 1-9:"))
    if Input >= 1 and Input <= 9 and Board[Input-1] == " - ":
        Board[Input-1] = CurrentPlayer
    else:
        print("Spot's already taken, unlucky.")


# check for win, lose or draw
def CheckHorizontal(Board):
    global Winner
    global GameRunning

    if Board[0] == Board[1] == Board[2] and Board[1] != " - ":
        Winner = Board[0]
        GameRunning = False
        return True

    elif Board[3] == Board[4] == Board[5] and Board[4] != " - ":
        Winner = Board[3]
        GameRunning = False
        return True

    elif Board[6] == Board[7] == Board[8] and Board[7] != " - ":
        Winner = Board[6]
        GameRunning = False
        return True


def CheckVertical(Board):
    global Winner
    global GameRunning

    if Board[0] == Board[3] == Board[6] and Board[3] != " - ":
        Winner = Board[0]
        GameRunning = False
        return True

    elif Board[1] == Board[4] == Board[7] and Board[4] != " - ":
        Winner = Board[1]
        GameRunning = False
        return True

    elif Board[2] == Board[5] == Board[8] and Board[5] != " - ":
        Winner = Board[2]
        GameRunning = False
        return True


def CheckDiagonal(Board):
    global Winner
    global GameRunning

    if Board[0] == Board[4] == Board[8] and Board[4] != " - ":
        Winner = Board[0]
        GameRunning = False
        return True

    elif Board[2] == Board[4] == Board[6] and Board[4] != " - ":
        Winner = Board[2]
        GameRunning = False
        return True


def CheckDraw(Board):
    global Winner
    global GameRunning

    if " - " not in Board and Winner == None:
        print("Draw!")
        GameRunning = False


def CheckWin():
    if CheckHorizontal(Board) or CheckDiagonal(Board) or CheckVertical(Board):
        print(f"Winner is: {Winner}")
        GameRunning = False


# switch player
def SwitchPlayer():
    global CurrentPlayer

    if CurrentPlayer == " X ":
        CurrentPlayer = " O "

    elif CurrentPlayer == " O ":
        CurrentPlayer = " X "


# AI Computer
def AIComp2(Board):
    while CurrentPlayer == " O ":
        Position = random.randint(0,8)
        if Board[Position] == " - ":
            Board[Position] = " O "
            SwitchPlayer()


def AIComp1(Board):
    while CurrentPlayer == " X ":
        Position = random.randint(0,8)
        if Board[Position] == " - ":
            Board[Position] = " X "
            SwitchPlayer()


#AI V AI
#while GameRunning:
#    PrintBoard(Board)
#    
#    CheckWin()
#    CheckDraw(Board)
#    
#    AIComp1(Board)
#    PrintBoard(Board)
#    CheckWin()
#    CheckDraw(Board)
#    
#    AIComp2(Board)


#Player V AI
while GameRunning: 
    PrintBoard(Board)
    
    CheckWin()
    CheckDraw(Board)
    
    PlayerInput(Board)
    PrintBoard(Board)
    CheckWin()
    CheckDraw(Board)
    
    SwitchPlayer()
    AIComp2(Board)