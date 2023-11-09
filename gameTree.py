#import whatever queue we need to use for this tree 

class Node:
    def __init__(self, parent, board, util):
        self.util = util
        self.parent = parent
        self.board = board
        self.util = util #Have Util be a property of the board?
        self.winner = 0
        
    def isTerminal(self): #Determines if the game is in a terminal state, sets the winner if so
        self.winner = self.board.getWinner()
        if(self.board.isDraw() == True or self.winner != 0):
            return True
        return False
    def getGameWinner(self): #Should never be called before isTerminal
        return self.winner