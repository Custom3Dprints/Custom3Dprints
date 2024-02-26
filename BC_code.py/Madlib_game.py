pnoun1 = input("Enter a plural noun: ")
fname = input("Enter a first name: ")
noun1 = input("Enter a noun: ")
lname = input("Enter a last name: ")
pnoun2 = input("Enter a plural noun: ")
place1 = input("Enter a place: ")
pnoun3 = input("Enter a plural noun: ")
place2 = input("Enter a place: ")
pnoun4 = input("Enter a plural noun: ")
noun2 = input("Enter a noun: ")
adjective1 = input("Enter a adjective: ")
adjective2 = input("Enter a adjective: ")
verb = input("Enter a verb: ")
adjective3 = input("Enter a adjective: ")

def story():
    print(f"""Hello there, sports {pnoun1}!
This is {fname}, talking to you from the press {noun1}
in {lname} Stadium, where 57,000 cheering {pnoun2}
Have gathered to watch (the) {place1} {pnoun3}
take on (the) {place2} {pnoun4}.
Even though the {noun2} is shining, it’s a/an {adjective1}
cold day with the temperature in the {adjective2} 20s.
We’ll be back for the opening {verb} -off after a few words
from our {adjective3} sponsor.""")
story()