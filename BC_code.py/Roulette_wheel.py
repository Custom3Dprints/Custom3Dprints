print("Roulette Wheel Colors App ...")
user_num = int(input("Please enter a number (0-36): "))

def assign_color():
    if user_num in range(1, 10+1) or user_num in range(19, 28+1): #if user_num is 1-11 and 19-29
        if user_num % 2 != 0: #if num even
            return "Red"
        else:
            return "Black"
    elif user_num in range(11, 18+1) or user_num in range(30, 36+1): #if user_num is 11 - 19 and 30-37
        if user_num % 2 != 0: #if num even
            return "Black"
        else:
            return "Red"
color = assign_color()

if user_num not in range(36+1): #if user inputs a number not 0-36
    print("     Error...Invalid number. Try Again")
elif user_num == 0:
    print("Green")
else:
    print(f"The Color of the Wheel Pocket is {color}") #prints color of wheel pocket