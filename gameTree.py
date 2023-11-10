class Node:
    def __init__(self, parent, board):
        self.parent = parent
        self.board = board
        self.winner = self.board.getWinner()    
    def isTerminal(self): #Determines if the game is in a terminal state, sets the winner if so
        if(self.board.isDraw() == True or self.winner != 0):
            return True
        return False
    def getGameWinner(self):
        return self.winner
    def getUtil(self):
        return self.board.getUtil()