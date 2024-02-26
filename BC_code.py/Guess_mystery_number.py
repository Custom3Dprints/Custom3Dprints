#Marjorie Middlesteadt
#guess number game

import random
rnum = random.randint(1, 100) #produces a random number 1-100
print(rnum)
print("\nGuess the Mystry Number ...")
def getGuess(first, last):
    user_guess = int(input("Enter your best guess (1-100): "))
    if user_guess in range(first, last + 1): #checks if input is valid
        return user_guess
    else:
        while user_guess not in range(first, last + 1): #if number entered not 1-100 run until input is valid
            print("Error ... Incorrect number. Try again")
            user_guess = int(input(">Enter your best guess (1-100): ")) #re-prompt
            if user_guess in range(first, last + 1): #once input is valid
                return user_guess
                
def guessWin(number, guess):
    if guess == number:
        print("\nCongradulations ... You guessed the Mistery Number!")
        return True
    elif guess > number:
        print(f" ---> {guess} is too High ...")
        return False
    elif guess < number:
        print(f" ---> {guess} is too Low ...")
        return False

def game():
    for i in range(1, 7 + 1): #7 tries to guess the random number
        print(f"\nRound {i} of 7\n{'-'*35}") #amount of times you've tried
        guess = getGuess(1, 100) #prompts user for an input until valid
        guess_win = guessWin(rnum, guess) #checks if input is to high, to low, or correct
        if guess_win == True:
            break #stops the code

def output():
    game() #runs the code

    while True: #asks if user wants to play the game again
        try_again = input("\nDo you want to try again (y/n)? ")
        if try_again == "y":
            game() #plays another game
        else:
            break #stops the code
        
output()