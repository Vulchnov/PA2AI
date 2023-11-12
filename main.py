import board
import sys
import random
import math
import gameTree
import mcts
import UCT


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
    valid_moves = gameBoard.getValidMoves()
    return random.choice(valid_moves)

def DLMMMove(gameBoard, player, ply): #Depth-Limited MinMax - Returns a move for a given player - NEED TO MAKE IT UNIVERSAL (Have DLMM Assume the player is always yellow? invert board every turn?)
    valid_moves = gameBoard.getValidMoves()
    #print(valid_moves)
    bestMove = -1
    #Return action in random.choice(valid_moves) that is highest for MinValue(a, state, ply)
    root = gameTree.Node(None, gameBoard) #instantiate root node
    if (player == 'Y'):
        maxUtil = (math.inf * -1)
        for move in valid_moves:
            #print(f"Placing piece in row: {move}")
            minVal = MinValue(gameTree.Node(root, root.board.exploreMove(player, move)), ply-1)
            if (minVal > maxUtil):
                bestMove = move
    elif(player == 'R'):
        maxUtil = (math.inf)
        for move in valid_moves:
            #print(f"Placing piece in row: {move}")
            minVal = MaxValue(gameTree.Node(root, root.board.exploreMove(player, move)), ply-1)
            if (minVal < maxUtil):
                bestMove = move
    #print(f"Move Selected, Column: {bestMove}")
    return bestMove

def MaxValue(state, ply): #Returns a Utility Value
    if(state.isTerminal() or ply <= 0):
        #print(f"Terminal State Reached, ply = {ply}, util = {state.getUtil()}, Board:\n{state.board}")
        return state.getUtil()
    v = math.inf * -1
    valid_moves = gameBoard.getValidMoves()
    for move in valid_moves:
        #print(f"Exploring move: {move}")
        v = max(v,MinValue(gameTree.Node(state, state.board.exploreMove('Y', move)), ply-1)) #Replace player with 'Y'?
    return v

def MinValue(state, ply): #Returns a Utility Value
    if(state.isTerminal() or ply <= 0):
        #print(f"Terminal State Reached, ply = {ply}, util = {state.getUtil()}, Board:\n{state.board}")
        return state.getUtil()
    v = math.inf
    valid_moves = gameBoard.getValidMoves()
    for move in valid_moves:
        #print(f"Exploring move: {move}")
        v = min(v,MaxValue(gameTree.Node(state, state.board.exploreMove('R', move)), ply-1)) #Replace player with 'R'?
    return v

def PMCGSMove(gameBoard, player): #Pure Monte Carlo Game Search
    mct = mcts.MCTS(gameBoard, player, 1)
    mct.search(5)
    move = mct.best_move()
    return move

def UCTMove(gameBoard, player): #Upper Confidence bound for Trees
    uctT = UCT.UCT(gameBoard, player, 1)
    uctT.search(5)
    move = uctT.best_move()
    return move

#Game Playing
'''
moveChosen = URMove(gameBoard)
print(moveChosen)
print(gameBoard.pieceTracker)
'''
#gameBoard.insertPiece(player, DLMMMove(gameBoard, player, 5))
#print(gameBoard)

#Tournament
gameBoard = board.Board([['O','O','O','O','O','O','O'],
                         ['O','O','O','O','O','O','O'],
                         ['O','O','O','O','O','O','O'],
                         ['O','O','O','O','O','O','O'],
                         ['O','O','O','O','O','O','O'],
                         ['O','O','O','O','O','O','O']])
currPlayer = 'Y'
while(gameBoard.gameOver() == False):
    match currPlayer:
        case 'Y':
            gameBoard.insertPiece('Y', DLMMMove(gameBoard, 'Y', 5))
            print(gameBoard)
            currPlayer = 'R'
        case 'R':
            gameBoard.insertPiece('R', DLMMMove(gameBoard, 'R', 5))
            print(gameBoard)
            currPlayer = 'Y'
        case _:
            print("Error, shits fucked, yo")
print(f"Game End: \n{gameBoard}\nWinner: {gameBoard.getWinner()}")