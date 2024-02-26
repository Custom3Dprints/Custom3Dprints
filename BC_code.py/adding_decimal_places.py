#At one college, the tuition for a full-time student is $8,000 per semester. 
# It has been announced that the tuition will increase by 3 percent each year for the next 5 years. 
# Write a program with a loop that displays the projected semester tuition amount for the next 5 years.
#Your program’s output must exactly match the output shown in the sample run below. 
# Notice the wording of the messages and the placement of spaces and punctuation. 
# Also, make sure that the tuition amounts are rounded to two decimal places.
#Sample Run
#In 1 year, the tuition will be $8240.00.
#In 2 years, the tuition will be $8487.20.
#In 3 years, the tuition will be $8741.82.
#In 4 years, the tuition will be $9004.07.
#In 5 years, the tuition will be $9274.19.


tuition = int(input("Enter amount of tuition: ")) #8000
tenth = ''
decimal = ''
for i in range(1, 6):
    tuition = float(tuition)
    tuition = round((tuition * .03) + tuition, 2)
    tuition = str(tuition)
    for c in range(len(tuition)):
        if tuition[c] == ".":
            tenth += tuition[c+1:]

    if len(tenth) != 2:
        for var in range(len(tenth)):
            decimal += '0'
        
        if i == 1:
            print(f"In {i} year, the tuition will be ${(tuition + decimal)}.")
        else:
            print(f"In {i} years, the tuition will be ${(tuition + decimal)}.")
    else:
        print(f"In {i} years, the tuition will be ${(tuition)}.")
    
    tenth = ''
    decimal = ''
