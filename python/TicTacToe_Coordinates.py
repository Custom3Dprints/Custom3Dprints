#Formatting the board
def Board():
    #board = [([v]*9) for v in range(4)] #the way i make 2d lists#
    board = [[" " for _ in range(4)] for _ in range(4)] #smart chatgpt way of makeing 2d list for this special situation#

    board[0][0] = "R/C" 
    board[0][1] = "0"   
    board[0][2] = "1"   
    board[0][3] = "2"   
    board[1][0] = "0"   
    board[2][0] = "1"   
    board[3][0] = "2"   
    
    return board

#prints board
def printBoard(board):
    for row in board:
        print(" ".join(["-"]*9))
        print("| " + " | ".join(row) + " |")

#Determines whos turn it is
def get_turn(i):
    if i % 2 == 0:
        return "X"
    else:
        return "O"

#takes input and only outputs valid input
plays = []
def True_input(turn):
    print(f"{turn}'s turn.")
    play = (input(f"Where do you want your {turn} placed?\nPlease enter row number and column number separated by a comma.\n"))
    print(f"You have entered row #{play[0]}\n\t  and column #{play[2]}")
    
    if int(play[0]) in range(0,3) and int(play[2]) in range(0,3) and (play[0], play[2]) not in plays:
        print("Thank you for your selection.")
        plays.append((play[0], play[2]))
        return (play[0], play[2])
    else:
        while (play[0], play[2]) in plays:
            play = (input(f"Where do you want your {turn} placed?\nPlease enter row number and column number separated by a comma.\n"))
            print("Invalid entry: try again\nThat cell is already taken.\nPlease make another selection.")
        while int(play[0]) not in range(0,3) or int(play[2]) not in range(0,3):
            print("Invalid entry: try again\nRow & column numbers must be either 0, 1, or 2.")
            play = (input(f"Where do you want your {turn} placed?\nPlease enter row number and column number separated by a comma.\n"))

#Gets the valid input and updates the board
def place(board, validinput, turn):
    x = validinput[0]
    y = validinput[1]
    var1 = 0
    var2 = 0
    for rnum, row in enumerate(board):
        if str(y) == board[rnum][0]:
            var1 = rnum
        for cnum, col in enumerate(row):
            if str(x) == board[0][cnum]:
                var2 = cnum
    
    board[var1][var2] = turn
    return board

#creates smaller lists to help determine winner
def determineWinner(board, turn):
    board = [board[1][1:], board[2][1:], board[3][1:]]
    Wins = [turn] * 3
    for index in range(3):
        row = board[index]
        column = [board[i][index] for i in range(3)]
        diagonal = [board[i][i] for i in range(3)]
        diagonal2 = [board[2-i][i] for i in range(3)]

        if column == Wins or row == Wins or diagonal == Wins or diagonal2 == Wins:
            return True

#runs all the function
def playing():
    print(f"New game: X goes first.")
    board = Board()
    for i in range(9):
        turn = get_turn(i)
        validinput = True_input(turn)
        placer = place(board, validinput, turn)

        if  determineWinner(placer, turn) == True:
            print(f"\n{turn} IS THE WINNER!!!")
            return True
        else:
            printBoard(placer)

#loops the playing function and askes for another game
def main():
    play = playing()
    
    while play == True:
        anothergame = input("Another game? Enter Y or y for yes.\n")
        if anothergame == "Y" or anothergame == "y" or anothergame == "yes":
            playing()

main()
