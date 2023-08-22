
'''
this is a simple tic tac toe game without GUI
we have X and O as a players 
we have a specific sequence till us who is the winner 
the completed code with detailed functions show below 

'''


board=["_","_","_",
        "_","_","_",
        "_","_","_"]
        
current_player= "X"
winner=None
gameRunning= True

'''
this is a game board consist of "_" represent
empty squares which players will play in 
'''

def showboard(board):
    print(board[0],"|",board[1],"|", board[2],"|")
    print("_________")
    print(board[3],"|",board[4],"|", board[5],"|")
    print("_________")
    print(board[6],"|",board[7],"|", board[8],"|")

'''
every square represent number from 1 to 9 
'''

def playerinp(board):
    inp=int(input("enter a number from 1 to 9 "))
    if inp>=1 and inp<=9and board[inp-1]=="_" :
        board[inp-1]=current_player
    else:
        print("ouuch! this spot isn't empty")

'''
this is just a conditions to make the player on the right road 
or there is a message will be shown on screen till that 
there is something wrong 
'''
    

    
def horizontal(board):
    global winner
    if board[0]==board[1]==board[2]!= "_":
        winner=board[0]
        return True
    elif board[3]==board[4]==board[5]!= "_":
        winner=board[3]
        return True
    elif board[6]==board[7]==board[8]!= "_":
        winner=board[6]
        return True
        
'''
this is a way to win 
if the player enter one symbol three times horizontally
0 1 2 
or 
3 4 5
or 
6 7 8
'''


def checkrow(board):
    global winner
    if board[0]==board[3]==board[6]!= "_":
        winner=board[0]
        return True
    elif board[1]==board[4]==board[7]!= "_":
        winner=board[1]
        return True
    elif board[2]==board[5]==board[8]!= "_":
        winner=board[2]
        return True

'''
as the below function but in rows 

'''


def diagonal(board):
    global winner
    if board[0]==board[4]==board[8]!= "_":
        winner=board[0]
        return True
    elif board[2]==board[4]==board[6]!= "_":
        winner=board[2]
        return True
        
'''
if the square 0 and 4 and 8 
or 2 and 4 and 6 
have the same symbol 
this mean the symbol player won 
in diagonal shape 
'''


def checktie(board):
    showboard(board)
    if "_" not in board:
        print("It's a Tie!")
        return True
    else:
        return False
        
'''
if there is no one achieve the win condisions 
and there isn't empty squares ("_" wasn't found )
so it's a tie 

'''


def checkwin(board):
    if diagonal(board) or horizontal(board) or checkrow(board):
        print("congrats!! the winner is ", winner)
        return True
    else:
        return False
        
'''
 when the one of two players achieve one of the win condisions 
the message congratulation will be shown on screen and the 
symbol of winner 

'''

def switchplayer():
    global current_player
    if current_player=="X":
        current_player="O"
    else:
        current_player="X"
        
'''
this function to switch between X player and O player 
and repeat that while game is on 
'''
        
        
        
while gameRunning:
    
    showboard(board)
    
    playerinp(board)
    if checkwin(board)  or checktie(board):
        gameRunning= False
    else:
        showboard(board)
    switchplayer()
    
    
'''
this condition make the game on 
while all functions on track
'''