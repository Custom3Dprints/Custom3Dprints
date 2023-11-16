Opperation_list = ["Addition", "Subtraction", "Multiplication", "Division"]

def Addition():
  result = num1 + num2
  print(result)
def Subtraction():
  result = num1 - num2
  print(result)
def Multiplication():
  result = num1 * num2
  print(result)
def Division():
  result = num1 / num2
  print(result)

while True:
  print(f"\n1. {Opperation_list[0]}")
  print(f"2. {Opperation_list[1]}")
  print(f"3. {Opperation_list[2]}")
  print(f"4. {Opperation_list[3]}")
  print(f"5. None")

  opperation_Question = input("What operation do you want to perform?: ")

  if int(opperation_Question) in range(1,5) or opperation_Question in Opperation_list:
    num1 = float(input("Number one: "))
    num2 = float(input("Number two: "))
    if opperation_Question.capitalize() == Opperation_list[0] or int(opperation_Question) == 1:
      Addition()

    elif opperation_Question.capitalize() == Opperation_list[1] or int(opperation_Question) == 2:
      Subtraction()

    elif opperation_Question.capitalize() == Opperation_list[2] or int(opperation_Question) == 3:
      Multiplication()

    elif opperation_Question.capitalize() == Opperation_list[3] or int(opperation_Question) == 4:
      Division()
  elif opperation_Question.capitalize() == 'None' or int(opperation_Question) not in range(1,5):
    break


'''
Opp_dict = {Opperation_list[0]: "Addition", "Subtraction": Opperation_list[1]}
print(Opp_dict[Opperation_list[0]])
print(Opp_dict["Subtraction"])
'''
'''
  elif len(opp_list) > 1:
    Join = ' or '.join(opp_list)
    opperation_Question = (f"Do you want to do {Join}? ")
    opperation_Question = opperation_Question.capitalize()
    print(opperation_Question)

    #if opperation_Question in Opperation_list:

'''