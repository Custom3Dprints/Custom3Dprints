import random
DEBUG = True
Cat_dict = {
"Football": """Gridiron football, version of the sport of football so named for the vertical yard lines marking the rectangular field. Gridiron football evolved from English rugby and soccer 
(association football); it differs from soccer chiefly in allowing players to touch, throw, and carry the ball with their hands, and it differs from rugby in allowing each side to control the ball 
in alternating possessions. The sport, played with 11 on each side, originated in North America, primarily in the United States, where it eventually became the country’s leading spectator sport. 
It also developed simultaneously in Canada, where it evolved into a 12-man game, though it never achieved the great popularity and status of ice hockey there. Gridiron football has not been taken 
up in the rest of the world to the same degree as other American sports such as basketball and baseball. Since the 1980s, however, primarily through the marketing efforts of the National Football 
League, teams and leagues have been established in Europe, and the game has achieved a degree of international popularity through television.""", 
"Soccer": """Football, also called association football or soccer, game in which two teams of 11 players, using any part of their bodies except their hands and arms, try to maneuver the ball into the 
opposing team's goal. Only the goalkeeper is permitted to handle the ball and may do so only within the penalty area surrounding the goal. The team that scores more goals wins.Football is the world’s 
most popular ball game in numbers of participants and spectators. Simple in its principal rules and essential equipment, the sport can be played almost anywhere, from official football playing fields 
(pitches) to gymnasiums, streets, school playgrounds,parks, or beaches. Football’s governing body, the Fédération Internationale de Football Association (FIFA), estimated that at the turn of the 21st 
century there were approximately 250 million footballplayers and over 1.3 billion people “interested” in football; in 2010 a combined television audience of more than 26 billion watched football’s 
premier tournament, the quadrennial month-long World Cup finals.For a history of the origins of football sport, see football.""",
"Tennis": """Tennis, original name lawn tennis, game in which two opposing players (singles) or pairs of players (doubles) use tautly strung rackets to hit a ball of specified size, weight, and bounce over 
a net on a rectangular court. Points are awarded to a player or team whenever the opponent fails to correctly return the ball within the prescribed dimensions of the court. Organized tennis is played 
according to rules sanctioned by the International Tennis Federation (ITF), the world governing body of the sport.""", 
"Swimming": """Swimming, in recreation and sports, the propulsion of the body through water by combined arm and leg motions and the natural flotation of the body. Swimming as an exercise is popular as an 
all-around body developer and is particularly useful in therapy and as exercise for physically handicapped persons. It is also taught for lifesaving purposes. For activities that involve swimming, see 
also diving, lifesaving, surfing, synchronized swimming, underwater diving, and water polo.""",
"Basketball": """Basketball, game played between two teams of five players each on a rectangular court, usually indoors. Each team tries to score by tossing the ball through the opponent’s goal, an elevated
horizontal hoop and net called a basket. The only major sport strictly of U.S. origin, basketball was invented by James Naismith (1861–1939) on or about December 1, 1891, at the International Young Men’s 
Christian Association (YMCA) Training School (now Springfield College), Springfield, Massachusetts, where Naismith was an instructor in physical education."""
}


Cat_lists = ["Football", "Soccer", "Tennis", "Swimming", "Basketball"]
join = ", ".join(Cat_lists)
print(f"Catigories: {join}")



while True:
  Cat_input = input("Enter a category: ")

  Yes_no_list = ["YES", "Yes", "yes", "Y", "y", "NO", "No", "no", "N", "n"]
  returnedCats = [cat for cat in Cat_lists if Cat_input in cat ]  # cat = for cat in cat_lists and if Cat_input in cat
  #low_Cat_list = [cat.lower() for cat in Cat_lists]


  print(f"Cat_input = {Cat_input}")
  print(f"returnedCats = {returnedCats}")
  print(f"returnedCats length = {len(returnedCats)}")
  #print(f"low_Cat_list = {low_Cat_list[0:]}") # prints list in all lower case

  print(f"cat input >>{Cat_input}\n")
  returnedCats = [cat for cat in Cat_lists if Cat_input in cat ] #by re-coding this list comprehension it redifines returnCats to most recent Cat_input
  print(f"\nreturnedCats ==> {returnedCats}\nCat_input ==> {Cat_input}")
  Random = random.choice(Cat_lists)
  Cat_input = Cat_input.capitalize()

  Or_Join = " or ".join(returnedCats)

  # capitalize the input and if its cat_lists
  if len(returnedCats) == 0:
    Question = input(f"Do you want to read about {Random}? ")
    if Question in Yes_no_list[0:4]:
      print(Cat_dict[Random])



  elif len(returnedCats) > 1:
    Answer = input(f"line 64\nWould you like to read about {Or_Join}? ")
    print(f"Answer.capitalize = {Answer.capitalize()}")
    if Answer.capitalize() in Cat_lists:
      print(f"line 57\n{Cat_dict[Answer.capitalize()]}")
      
    elif Answer not in Cat_lists: # if Answer not in Cat_list or in Yes_no_list
      #print(f"line 59\n{Cat_dict[Random]}")

      if Cat_input in Cat_lists:        #low_Cat_list                                                                     //not printing
        print(f"line 62\n{Cat_dict[Cat_input]}") #cuz if statement has .capitalize need to print .capitalize as well

      elif Cat_input not in Cat_lists:  #                                                                                //not printing when input 1 = ball and 2 = extcfyvg
        #Answer = input(f"line 65\nWould you like to read about {Or_Join}? ") #input here
        Question = input(f"line 69\nDo you want to read about {Random}? ")
        print(f"line 66\nQuestion = {Question}")

        if Answer not in Yes_no_list:

          if Answer in Yes_no_list[0:4]: #if Answer = yes
            print(f"line 66\n{Cat_dict[Random]}")

          elif Answer in Yes_no_list[5:9]:  # if Answer = no
            Question = input(f"line 69\nDo you want to read about {Random}? ")
            print(f"Question = {Question}")

            if Question in Yes_no_list[0:4]:  # if Question = yes
              print(f"line 73\n{Cat_dict[Random]}\n")

            elif Question in Yes_no_list[5:9] or Question not in Yes_no_list:  #if Question = no   //not working
              print(f"line 75\n{Cat_dict[Random]}")

#if type foot code doesnt work