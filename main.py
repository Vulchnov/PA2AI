import board
import sys
import random

boardArray = []

#Take input file, designates algorithm, parameter, create board, execute algorithm
if len(sys.argv) != 3:
    print("Correct usage: PA1.py <input text file> <Search Type>")
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

def URMove(gameBoard): #Uniform Random
    valid_moves = [col for col in gameBoard.peiceTracker if gameBoard.peiceTracker < 6]
    return random.choice(valid_moves)

def DLMMMove(gameBoard): #Depth-Limited MinMax
    pass

def PMCGSMove(gameBoard): #Pure Monte Carlo Game Search
    pass

def UCTMove(gameBoard): #Upper Confidence bound for Trees
    pass
