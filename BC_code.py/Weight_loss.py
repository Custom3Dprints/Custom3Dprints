# Marjorie Middlesteadt
# Weightloss code

def get_input(): #processes for valid input
    user_input = int(input("Choose one of the following options:\n\
    1. Display “10 ways to cut 500 calories” guideline\n\
    2. Generate next semester expected weight table\n\
    3. Quit\nOption: "))
    if user_input in range(1, 4): # if input is 1-3
        return user_input
    else: 
        print("Error... Invalid option. Try Again")
        return False

def Option2(weight): #processes for valid input
    if weight >= 100: #if input >= 100
        return weight
    else:
        print("     Error... Invalid weight. Try Again")
        return False

def Output():
    while True:
        user_input = get_input() #gets valid input

        if user_input == 1:
            print("""Try these 10 ways to cut 500 calories every day.
        * Swap you snack.
        * Cut one high-calorie treat.
        * DO NOT drink your calories.
        * Skip seconds.
        * Make low calorie substitutions.
        * Ask for a doggie bag.
        * Just say “no” to fried food.
        * Build a thinner pizza.
        * Use a smaller plate.
        * Avoid alcohol.
    Source: US National Library of Medicine""")

        elif user_input == 2:
            Op2 = Option2(float(input("Enter weight (>=100): "))) #gets weight
            while Op2 == False: #if invlid weight is inputed
                Op2 = Option2(float(input("Enter weight (>=100): "))) #re-prompt
            else: #if input is valid
                print(f"{'-'*30}\n{'Month':20s}Weight\n{'-'*30}") 
                for i in range(1, 6+1):
                    print(f"  {str(i):18}{Op2 - 4}lb.") #month : weight loss number goal

        elif user_input == 3:
            print("     Good bye ...")
            break #stop code
Output()