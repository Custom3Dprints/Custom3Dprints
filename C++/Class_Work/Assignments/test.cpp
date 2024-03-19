"""
Project 1: Tic-Tac-Toe

This program is a simple Tic-Tac-Toe game using the console.

Pseudocode:
    1) Define printBoard(board) function, which first prints a constant board header, then uses a for loop to print the rows
    2) Defines the resetBoard() function, which XXX
    3) Defines XXX
    4) XXX
    5) XXX
    6) ...
    ....
    
    
"""

'''

# this function prints the board
def printBoard(board):
    board = [["-", "-", "-", "-"], ["|"]]
    for i,r in enumerate(board):



# this function resets the board 
def resetBoard():
    


# this function validates the user's entry
def validateEntry(row, col, board):


    


# this function checks if the board is full
def checkFull(board):

    

# this function checks if the game has met an end condition by calling XXX
def checkEnd(board, turn):
   


# this function checks for a winner
def checkWin(board, turn):
    




# main function
def main():



    
# call to main() function
if __name__ == "__main__":
    main()
'''

def Board():

    board = [([v]*3) for v in range(3)]
    for rnum, row in enumerate(board):
        for cnum, col in enumerate(row):
            if cnum % 2 != 0 and board[rnum][cnum] != "-":
                board[rnum][cnum] = "|" # column = "|"
    return board

def printBoard(board):
    for rnum, row in enumerate(board):
        print(" ".join(["-"]*6))
        print (row)
    
    print(" ".join(["-"]*6))

printBoard(Board())
"""
def numerical(num):
    board = Board()
    for a,b in enumerate(board):
        for c,d in enumerate(b):
            if type(board[a][c]) == int:
                board[a][c] = num
                num += 1
    return board

def determineWinner(board, last_play):
    print(board)
    Wins = [last_play] * 3
    for index in range(3):
        row = board[index]
        column = [board[i][index] for i in range(3)]
        diagonal = [board[i][i] for i in range(3)]
        diagonal2 = [board[2-i][i] for i in range(3)]

        if column == Wins or row == Wins or diagonal == Wins or diagonal2 == Wins:
            return(f"{last_play} Won")

def get_turn(i):
    if i % 2 == 0:
        return "X"
    else:
        return "O"

plays = []
def True_iput(turn):
    value = False
    while value == False:
        try:
            play = int(input(f"Enter where you want {turn} to go: "))
            if play in range(1, 10) and play not in plays:
                plays.append(play)
                value = True
                return play
            else:
                value = False
        except ValueError:
            value = False
board = numerical(1)

def get_place(play, placer):
    for a, b in enumerate(board):
        for c,d in enumerate(b):
            if board[a][c] == play:
                board[a][c] = placer

    for n in board:
        print(" ".join([str(a) for a in n]))

    b2 = []
    for n, r in enumerate(board):
        for a, b in enumerate(r):
            if n % 2 == 0 and board[n][a] != "|":
                b2.append(board[n][a])
    check_board = [b2[:3], b2[3:6], b2[6:]]
    return check_board

def play_game():
    
    for i in board:
        print(" ".join([str(a) for a in i]))

    for i in range(9):
        turn = get_turn(i)
        true_input = True_iput(turn)
        game = get_place(true_input, turn)
        winner = determineWinner(game,turn)
        if type(winner) == str:
            return (winner)
        if i == 8 and type(winner) == None: #idk
            return("\nCongrats you both lost losers")

#print(play_game())
        
"""
