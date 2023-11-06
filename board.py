#The board will be stored as an array
class Board:
    '''
    def __init__(self):
        self.boardArray = [[0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0]]
        self.pieceTracker = [0,0,0,0,0,0,0]
    '''
    def __init__(self, boardArray): #Creates a board based on an existing top-down board array
        self.boardArray = boardArray
        self.pieceTracker = [0,0,0,0,0,0,0]
        for i in range(0, len(boardArray)):
            self.pieceTracker[i] = self.getpieceTrack(self.getColumn(i))
    def getpieceTrack(self, row):
        for i in range(0, len(row)):
            if row[i] != 0:
                return i
        return len(row)-1          
    def __str__(self): #return the top-down representation of the board
        boardStr = ""
        for row in self.boardArray:
            boardStr += "["
            for num in row:
                boardStr += f"{num},"
            boardStr += "]\n"
        return boardStr
    def insertPiece(self, num, column): #insert num into the column on the board, return piece inserted, return -1 if the operation was not completed
        if(self.pieceTracker[column] >= len(self.boardArray)-1):
            return -1
        else:
            self.boardArray[self.pieceTracker[column]-1][column] = num
            self.pieceTracker[column] -= 1
            return num
    def getRow(self, num): #Returns the given row of the board, -1 if num is out of range
        if(num in range(0,len(self.boardArray))):
            return self.boardArray[num]
        else:
            return -1
    def getColumn(self, num): #Returns the given column of the board, returns -1 if num is out of range
        if(num in range(0,len(self.boardArray))):
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
            return -1
        consecutiveOnes = 0
        consecutiveTwos = 0
        for num in row:
            match num:
                case 0:
                    consecutiveOnes = 0
                    consecutiveTwos = 0
                case 1:
                    consecutiveOnes += 1
                    consecutiveTwos = 0
                case 2:
                    consecutiveTwos += 1
                    consecutiveOnes = 0   
                case _:
                    print("Error: invalid key in boardArray")
                    print(self)
                    return -1
            if consecutiveOnes >= 4:
                return 1
            elif consecutiveTwos >= 4:
                return 2  
        return -1
    def isFull(self): #Returns true if there is a 0 in the board. Otherwise, return false
        for row in self.boardArray:
            for num in row:
                if num == 0:
                    return False
        return True
    def getWinner(self): #Returns winning player if there is a winning row, otherwise, return -1
        #Check all rows
        for i in range(0,len(self.boardArray)):
            winner = self.isWinningRow(self.boardArray(i))
            if winner > 0:
                return winner
        #Check all columns
        for i in range(0,len(self.boardArray[0])):
            winner = self.isWinningRow(self.getColumn(i))
            if winner > 0:
                return winner
        #Check all diagonals
        return -1
    def isDraw(self): #Returns true if the board is full and there are no winners. Otherwise, return false
        winner = self.isWin()
        if(self.isFull() and winner != 1 and winner != 2):
            return True
        else:
            return False