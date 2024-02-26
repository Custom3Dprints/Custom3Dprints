#Marjorie Middlesteadt
#grades quiz with 15 questions

print("\nQuiz Grading App ...\n")
def get_file(): #gets valid file
    ans_file = input('  "   quiz answer file: ') #asks for the file
    try:
        file = open(ans_file, "r") #tries to open the file
        return file
    except FileNotFoundError: #if file can't be opened File() == False
        print(f"Error ... could not process {ans_file}")
        return False

def doc(): #formatting and validity
    name = input("Enter name of student: ")
    file = get_file()
    ans_key = ['A', 'C', 'A', 'B', 'B', 'D', 'D', 'A', 'C', 'A', 'B', 'C', 'D', 'C', 'B']

    while file == False: #reprompt for valid file
        try_again = input("\nDo you have another student (y/n)? ")
        if try_again == "y":
            file = get_file()
        else:
            return False
    else:
        file = [v.strip() for v in file] #strips the file of spaces
        correct = [] # correct letter choices
        wrong = [] #number of the questions wrong
        for i, j in enumerate(ans_key):
            for n, c in enumerate(file):
                if i == n and j == c:
                    correct.append(c) #c = correct answers
                if i == n and j != c:
                    wrong.append(i) #wring question number

        wrong_join = " ".join([str(x) for x in wrong]) #makes wrong list to string with space format
        title = f"\n{name} Quiz Results\n{'-'*40}"

        print(f"{title}\nCorrect Answers:{len(correct)}\nIncorrect Answers: {len(wrong)} ({wrong_join})")

        if len(correct) in range(11, 15+1): #passed or failed quiz
            print("\nStudent PASSED the quiz.")
        else:
            print("\nStudent FAILED the quiz.")
doc()

while True: #re-prompts for another file
    try_again = input("\nDo you have another student (y/n)? ")
    if try_again == "y":
        doc() #calls function again
    else:
        break