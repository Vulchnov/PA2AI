import board
import sys
import random

boardArray = []

#Take input file, designates algorithm, parameter, create board, execute algorithm
if len(sys.argv) != 3:
    print("Correct usage: main.py <input text file> <information wanted>")
    exit()
textFname = sys.argv[1]

algorithm = ''
param = 0
player=''

#Read the input map file and assign variables
with open(textFname, 'r') as inputFile:
    lineCount = 0
    for line in inputFile:
        line = line.strip()
        splitLine = line.split(" ") #get a row on the inputfile as a list of numeric strings
        if lineCount == 0: #Save the algorithm
            algorithm = splitLine[0]
        elif lineCount == 1: #Save the parameter
            param = int(splitLine[0])
        elif lineCount == 2: #Save starting player
            player = splitLine[0] 
        else:
            boardArray.append(splitLine) #append a list of numbers (A row on the board) to the board
        lineCount+=1
gameBoard = board.Board(boardArray)

#Moves
def URMove(gameBoard): #Uniform Random
    valid_moves = [col for col in gameBoard.pieceTracker if col < 6]
    return random.choice(valid_moves)

def DLMMMove(state, ply): #Depth-Limited MinMax - Returns a move
    #Expand game tree to the depth of ply
    #Evaluate fringe nodes with eval function
    #Compare values, pass Min/Max to the root
    #Choose best move, repeat
    valid_moves = [col for col in state.pieceTracker if col < 6]


    #Return action in random.choice(valid_moves) that is highest for MinValue(a, state, ply)
    pass

def MaxValue(state, ply): #Returns a Utility Value
    if(state.isTerminal or ply == 0):
        return state.getUtil
    
    #v = -infinite
    #for child in state.children:
        #v = max(v,MinValue(child))
    #return v
    pass

def MinValue(state, ply): #Returns a Utility Value
    if(state.isTerminal or ply == 0):
        return state.getUtil
    #v = infinite
    #for child in state.children:
        #v = min(v,MaxValue(child))
    #return v
    pass

def PMCGSMove(gameBoard): #Pure Monte Carlo Game Search
    pass

def UCTMove(gameBoard): #Upper Confidence bound for Trees
    pass

#Game Playing
moveChosen = URMove(gameBoard)
print(moveChosen)
print(gameBoard.pieceTracker)