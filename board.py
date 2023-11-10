#The board will be stored as an array
import math
import copy
class Board:
    '''
    def __init__(self):
        self.boardArray =   [['O','O','O','O','O','O','O'],
                            ['O','O','O','O','O','O','O'],
                            ['O','O','O','O','O','O','O'],
                            ['O','O','O','O','O','O','O'],
                            ['O','O','O','O','O','O','O'],
                            ['O','O','O','O','O','O','O']])
        self.pieceTracker = [0,0,0,0,0,0,0]
    '''
    def __init__(self, boardArray): #Creates a board based on an existing top-down board array
        self.boardArray = boardArray
        self.pieceTracker = [0] * len(boardArray[0])
        for i in range(0, len(boardArray[0])):
            self.pieceTracker[i] = self.updatePieceTrack(self.getColumn(i))
        self.util = 0
        self.getWinner() #update Util

    def updatePieceTrack(self, column): #Updates the piece tracker for a given column
        for i in range(0, len(column)):
            if column[i] != 'O':
                return i
        return len(column)
    
    def getValidMoves(self):
        validMoves = []
        for i in range(len(self.pieceTracker)):
            if(self.pieceTracker[i] > 0):
                validMoves.append(i)
        return validMoves
    
    def __str__(self): #return the top-down representation of the board
        boardStr = ""
        for row in self.boardArray:
            boardStr += "["
            for num in row:
                boardStr += f"{num},"
            boardStr += "]\n"
        return boardStr
    
    def insertPiece(self, player, column): #insert num into the column on the board, return piece inserted, return -1 if the operation was not completed
        if(self.pieceTracker[column] <= 0):
            return -1
        else:
            self.boardArray[self.pieceTracker[column]-1][column] = player
            self.pieceTracker[column] -= 1
            return player
        
    def exploreMove(self, player, column): #Returns a new board that represents a given move
        exploreBoard = copy.deepcopy(self)
        exploreBoard.insertPiece(player,column)
        return exploreBoard
    
    def getRow(self, num): #Returns the given row of the board, -1 if num is out of range
        if(num in range(0,len(self.boardArray))):
            return self.boardArray[num]
        else:
            return -1
        
    def getColumn(self, num): #Returns the given column of the board, returns -1 if num is out of range
        if(num in range(0,len(self.boardArray[0]))):
            column = []
            for i in range(0,len(self.boardArray)):
                column.append(self.boardArray[i][num])
            return column
        else:
            return -1
        
    def getDiagonals(self): #Returns a list of all diagonals in the board 
        pass

    def isWinningRow(self, row): #Return winner if there are 4 ones or 4 twos in a row. Otherwise, return -1
        if(len(row) < 4): #return -1 if the row (probably a diagonal) is contains less than 4 spaces, as it is impossible to have 4 in a row in less than 4 spaces... obviously...
            return 0
        consecutiveReds = 0
        consecutiveYellows = 0
        for piece in row:
            match piece:
                case 'O':
                    consecutiveReds = 0
                    consecutiveYellows = 0
                case 'Y':
                    consecutiveReds = 0
                    consecutiveYellows += 1
                    self.util += 1 #Update util multiple yellow pieces in a row
                case 'R':
                    consecutiveReds += 1
                    consecutiveYellows = 0   
                    self.util -= 1 #Update util if there are multiple red pieces in a row
                case _:
                    print("Error: invalid key in boardArray")
                    print(self)
                    return 0
            if consecutiveReds >= 4:
                return -1
            elif consecutiveYellows >= 4:
                return 1 
        return 0
    
    def isFull(self): #Returns true if there is a 0 in the board. Otherwise, return false
        for piece in self.boardArray[0]:
            if piece == 'O':
                return False
        return True
    
    def getWinner(self): #Returns winning player if there is a winning row, otherwise, return -1, iterates through entire board, always
        self.util = 0 #Reset util, it will be updated with each call of self.getWinningRow()
        #Check all rows
        for i in range(len(self.boardArray)):
            prospect  = self.isWinningRow(self.getRow(i))
            if prospect  != 0:
                match prospect:
                    case -1:
                        self.util = math.inf * -1
                    case 1:
                        self.util = math.inf
                    case _:
                        print('error, invalid return for self.isWinningRow')
                return prospect
        #Check all columns
        for i in range(len(self.boardArray[0])):
            prospect = self.isWinningRow(self.getColumn(i))
            if prospect  != 0:
                match prospect:
                    case -1:
                        self.util = math.inf * -1
                    case 1:
                        self.util = math.inf
                    case _:
                        print('error, invalid return for self.isWinningRow')
                return prospect
        #Check all diagonals
        '''
        for valid diagonal in board:
            prospect = self.isWinningRow(diagonal)
            if prospect  != 0:
                match prospect:
                    case -1:
                        self.util = math.inf * -1
                    case 1:
                        self.util = math.inf
                    case _:
                        print('error, invalid return for self.isWinningRow')
                return prospect
        '''
        return 0
    
    def isDraw(self): #Returns true if the board is full and there are no winners. Otherwise, return false
        if(self.isFull() and self.getWinner != 0):
            return True
        else:
            return False
        
    def gameOver(self):
        return self.isDraw() or self.getWinner()!=0

    def getUtil(self):
        return self.util