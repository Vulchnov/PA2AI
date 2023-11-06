#The board will be stored in an array that is a representation of the board
class Board:
    def __init__(self):
        self.boardArray = [[0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0]]
        self.pieceTracker = [0,0,0,0,0,0,0]
    def __init__(self, boardArray): #Creates a board based on an existing top-down board array
        self.boardArray = boardArray
        self.pieceTracker = [0,0,0,0,0,0,0]
        for i in range(0, len(boardArray)-1):
            self.pieceTracker[i] = self.getpieceTrack(self.getColumn(i))
    def __getpieceTrack(self, row):
        for i in range(0, len(row)-1):
            if row[i] != 0:
                return i
        return len(row)-1            
    def __str__(self): #return the top-down representation of the board
        boardStr = ""
        for rowNum in self.boardArray:
            boardStr += "["
            for num in self.getRow(rowNum):
                boardStr += f"{num},"
            boardStr += "]\n"
        return boardStr
    def insertPiece(self, num, column): #insert num into the column on the board, return piece inserted, return -1 if the operation was not completed
        if(self.pieceTracker[column] >= 7):
            return -1
        else:
            insertRow = self.pieceTracker[column]
            self.boardArray[insertRow][column] = num
            insertRow += 1
            return num
    def getRow(self, num): #Returns the given row of the board, -1 if num is out of range
        if(num in range(0,len(self.boardArray)-1)):
            return self.boardArray[num]
        else:
            return -1
    def getColumn(self, num): #Returns the given column of the board, returns -1 if num is out of range
        if(num in range(0,len(self.boardArray)-1)):
            column = []
            for i in range(0,len(self.boardArray)-1):
                column.append(self.boardArray[i][num])
            return column
        else:
            return -1
    def getDiagonal(self, cord, isNeg): #Returns the diagonal for a given coordinate in the direction ordained by isNeg (Top Right -> Bottom Left if false, Top Left -> Bottom Right if true)
        pass
    def isWinningRow(self, row): #Return winner if there are 4 ones or 4 twos in a row. Otherwise, return -1
        #oneWin = [1,1,1,1] in row
        #twoWin = [2,2,2,2] in row
        consecutiveOnes = 0
        consecutiveTwos = 0
        for num in row:
            if consecutiveOnes >= 4:
                return 1
            elif consecutiveTwos >= 4:
                return 2
            elif num == 1:
                consecutiveOnes += 1
                consecutiveTwos = 0
            elif num == 2:
                consecutiveTwos += 1
                consecutiveOnes = 0
            elif num == 0:
                consecutiveOnes = 0
                consecutiveTwos = 0
            else:
                print("Error: invalid key in boardArray")
                print(self)
        return -1
    def isFull(self): #Returns true if there is a 0 in the board. Otherwise, return false
        for row in self.boardArray:
            for num in row:
                if num == 0:
                    return False
        return True
    def isWin(self): #Returns winning player if there is a winning row, otherwise, return -1
        #Check all rows
        #Check all columns
        #Check all diagonals
        return False
    def isDraw(self): #Returns true if the board is full and there are no winners. Otherwise, return false
        winner = self.isWin()
        if(self.isFull() and winner != 1 and winner != 2):
            return True
        else:
            return False