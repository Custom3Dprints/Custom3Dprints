#pythonpracticeproblems

"""
name = str(input("Enter your name: "))
age = int(input("Enter your age: "))
year = 2022 - age + 100
print(f"Hi!, {name} you will turn 100 years old in the year {year}")
"""

################################################################################### Even Odd nums

"""
num = int(input("Enter a number: "))

if num % 4 == 0:
    print(f"{num} is divisable by 4")
elif num % 2 == 0:
    print(f"{num} is a even")
elif num % 2 == 1:
    print(f"{num} is odd")
"""

#################################################################################### if

""" #if num > 5
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

print([x for x in a if x < 5])
"""

###################################################################################

"""
num = int(input("Enter a number: "))

print([i for i in range(1, num) if num % i == 0])
"""

###################################################################################

"""
a = [13, 44, 52, 1, 1, 2, 3, 5, 8, 13]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#[1, 2, 3, 5, 8, 13]
lis = []
for i in a:
    for j in b:
        if i == j and i not in lis:
            lis.append(i)
lis.sort()
print(lis)
"""

####################################################################################

"""
word = input("Enter a word: ")

if word == word[::-1]: #reverse list
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")
"""

#####################################################################################

"""
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print([x for x in a if x % 2 == 0])
"""

#####################################################################################
"""
name = input("Enter name: ")
player1 = input("Rock or Paper or Scissors: ")
name2 = input("Enter name: ")
player2 = input("Rock or Paper or Scissors: ")

def Rock_Paper_Scissors():
    if player1.capitalize() or player2.capitalize() == "Rock" or "Paper" or "Scissors":
        for i in range(3):
            if player1.capitalize() == "Rock":
                if player2.capitalize() == "Paper":
                    return (f"Congrats to {name2} you win!!")
                elif player2.capitalize() == "Scissors":
                    return (f"Congrats to {name} you win!!")
                elif player2.capitalize() == "Rock":
                    return ("Tie")

            elif player1.capitalize() == "Paper":
                if player2.capitalize() == "Paper":
                    return (f"Tie")
                elif player2.capitalize() == "Scissors":
                    return (f"Congrats to {name2} you win!!")
                elif player2.capitalize() == "Rock":
                    return (f"Congrats to {name} you win!!")
                    
            elif player1.capitalize() == "Scissors":
                if player2.capitalize() == "Paper":
                    return (f"Congrats to {name} you win!!")
                elif player2.capitalize() == "Scissors":
                    return (f"Tie")
                elif player2.capitalize() == "Rock":
                    return (f"Congrats to {name2} you win!!")
    return None
print(Rock_Paper_Scissors())
"""

######################################################################################## 
# Guess random number and amount of tries
"""
import random

lis = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random_num = random.choice(lis)
print(random_num)
guess_count = 0
prompt = int(input("Enter a number: "))

while prompt != random_num:
    if random_num > prompt:
        print("Wrong, to low")
    elif random_num < prompt:
        print("Wrong, to high") 
    else:
        print("You guessed the right number")
        
    guess_count += 1
    prompt = int(input("Enter a number: "))
    if prompt == random_num:
        print("You guessed the random number congrats!!")
print(f"it took {guess_count + 1} amount of tries")
"""


########################################################################################
######################################################################################10

"""
import random
a = random.sample(range(1,30), 12)
b = random.sample(range(1,30), 16)
lis = [x for x in set(a) if x in a]
print(lis)
"""

#######################################################################################

"""
num = int(input("Enter a number: "))

factors = [i for i in range(1, num + 1) if num % i == 0]
if len(factors) != 2:
    print(f"{num} is not a prime number")
else:
    print(f"{num} is prime")
"""

#######################################################################################

"""
a = [5, 10, 15, 20, 25]

print([a[0], a[-1]])
"""

########################################################################################

"""
num = int(input("Enter a num: "))
lis = [x for x in range(1, num + 1)]
var = 0
Fibonacci = []
while var < len(lis):
    Fibonacci.append(lis[var] + var)
    var += 1
print(Fibonacci)
"""

########################################################################################

"""
def gen_fib():
    count = int(input("How many fibonacci numbers would you like to generate? "))
    i = 1
    if count == 0:
        fib = []
    elif count == 1:
        fib = [1]
    elif count == 2:
        fib = [1,1]
    elif count > 2:
        fib = [1,1]
        while i < (count - 1):
            fib.append(fib[i] + fib[i-1])
            i += 1

    return fib

print(gen_fib())
"""

#######################################################################################

"""
def name(names):
    new_lis = []
    for n in range(len(names)):
        if names[n] in new_lis:
            n += 1
        else:
            new_lis.append(names[n])
    return new_lis
print(name(["Michele", "Robin", "Sara", "Michele", "Sara"]))
"""

#######################################################################################

"""
sentence = input("Enter a sentence: ").split()
print(" ".join(sentence))
print(' '.join(sentence[::-1]))
"""

#######################################################################################
                #       RANDOM PASSWORD GENERATOR       #
"""
import random
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
alphabet_caps = [letter.upper() for letter in alphabet]
numbers = [num for num in range(1, 100 + 1)]
symbols = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']

char_list = [alphabet, alphabet_caps, numbers, symbols] #list in char_list: [[chars], [chars], [chars]]
num = [num for num in range(len(char_list))]
prompt = int(input("Enter how many charcters you want in your password: "))
numbs = random.choices(num, k = prompt)

def Random_password():
    password_chars = [str(random.choice(char_list[numbs[var]])) for var in range(len(numbs))]
    password = "".join(password_chars)
    return "password: "+ password
print(Random_password())

import string
letters = string.ascii_letters
print(letters) #all letters upper and lower
"""

############################################################################################
#skiped #17

############################################################################################

"""
import random

number = [num for num in range(1000, 9999 + 1)]
random_num = random.choice(number)
print(random_num)

def game():
    cow = 0
    bull = 0
    guesses = 0
    for index in range(4):
        guess = int(input("Enter a 4 diget number: "))
        if len(str(guess)) == 4:
            print(cow, bull)
            if guess == random_num:
                cow += 1
                return "Congrats you guessed the random number!!"
            elif str(random_num)[index] == str(guess)[index]:
                cow += 1
            else:
                bull += 1
    guesses += 1
    return (f"{cow} cows, {bull} bulls")
print(game())
"""

############################################################################################
# skip #19

############################################################################################
# waste of time

############################################################################################
#24
'''
row = int(input("Enter the amount of rows for the grid: "))
col = int(input("Enter the amount of colums for the grid: "))
char = str(input("Enter what the grid characters should be: "))

def board(row, col, char):
    board = []
    for i in range(row + 4):
        try:
            board.extend([(col+4) * [int(char)]])
        except ValueError:
            board.extend([(col+4)*[char]])
    return board
Board = board(row, col, char)

def rows():
    for i, v in enumerate(Board): #rows
        #print(i, v)
        if i%2==0:
            Board[i] = ["-"]*(row+4)
    return Board
Board = rows()

def final_board():
    for i, v in enumerate(Board): #rows
        if i % 2 != 0:
            for i2, v2 in enumerate(v):
                if i2 % 2 == 0:
                    Board[i][i2] = "|"
        print(" ".join([str(x) for x in Board[i]]))
final_board()
'''

############################################################################################

num = 27#int(input("Enter a num: "))
nums = [n for n in range(100+1)] # 0 - 100
guess_count = 1
