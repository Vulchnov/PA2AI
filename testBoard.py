import board

gameBoard = board.Board([['O','O','O','O','Y','O','O'],
                         ['O','O','O','O','Y','R','O'],
                         ['O','O','O','O','Y','R','Y'],
                         ['O','Y','Y','Y','O','R','O'],
                         ['O','O','O','O','O','O','O'],
                         ['O','O','O','O','O','O','O']])

gameBoard.insertPiece('Y', 6)
print(gameBoard)
print(gameBoard.pieceTracker)
print(gameBoard.getColumn(7))
print(gameBoard.getColumn(5))
print(gameBoard.isWinningRow(gameBoard.getColumn(5)))
print(gameBoard.isWinningRow(gameBoard.getRow(3)))
print(gameBoard.getWinner())
print(gameBoard.util)
print(gameBoard.getValidMoves())