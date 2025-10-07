#count neighbors
#create new board
#rules of da game(4)
#data structures represent the board
#how do we read the game board ouf of the text file

def printBoard(board):
    print(" ", end=" ")
    for col in range(len(board)):
        print(col, end=" ")
    print()
    for row in range(len(board)):
        print(row, end=" ")
        for col in range(len(board)):
            print(board[row][col], end=" ")
        print()

board = []
with open("seed2.txt") as f:
    for line in f:
        board.append([])
        for i in range(len(line)-1):
            board[len(board)-1].append(line[i])

print("Gen 0")
printBoard(board)