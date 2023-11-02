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
    def __init__(self, boardArray): #Creates a board based on an existing top-down board array
        self.boardArray = boardArray.reverse()
    def __str__(self): #return the top-down representation of the board
        boardStr = ""
        for rowNum in self.boardArray.reverse():
            boardStr += "["
            for num in self.getRow(rowNum):
                boardStr += f"{num},"
            boardStr += "]\n"
        return boardStr
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
    def isFull(): #Returns true if there is a 0 in the board. Otherwise, return false
        pass
    def isWin(self, player): #Returns true if there is a winning row.
        pass
    def isDraw(self): #Returns true if the board is full and there are no winners. Otherwise, return false
        if(self.isFull() and not self.isWin(1) and not self.isWin(2)):
            return True
        else:
            return False