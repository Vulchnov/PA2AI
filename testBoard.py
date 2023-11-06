import board

gameBoard = board.Board([[0,0,0,0,2,0,0],
                        [0,0,0,2,0,0,0],
                        [0,0,2,0,0,0,0],
                        [0,2,0,0,0,2,0],
                        [0,1,1,1,1,2,0],
                        [0,0,0,0,0,2,0],
                        [0,0,0,0,0,2,1]])

gameBoard.insertPiece(1, 6)
print(gameBoard)
print(gameBoard.pieceTracker)
print(gameBoard.getColumn(7))
print(gameBoard.getColumn(5))
print(gameBoard.isWinningRow(gameBoard.getColumn(5)))