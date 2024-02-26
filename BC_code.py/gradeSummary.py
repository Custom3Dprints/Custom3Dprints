#Marjorie Middlesteadt
#grade Summary

def Get_info():
    get_file = input("Enter file name to process: ") #asks for file

    try:
        file = open(get_file, "r") #tries to open file
        return file
    except FileNotFoundError:
        print(f"Error ... {get_file} file not found.")
        return False

def output():
    get_info = Get_info()

    while get_info == False: #re-prompts
        try_again = input("\nWould you like to process another file (y/n)? ")
        if try_again == "y":
            get_info = Get_info()
        else:
            return False
    else:
        doc = [var.strip() for var in get_info] #gets rid of spaces
        names = [doc[n] for n,c in enumerate(doc) if n % 2 != 0 and n > 1] #list of names
        scores = [int(doc[s]) for s,c in enumerate(doc) if s % 2 == 0 and s > 2] #list of numbers
        passed = [score for score in scores if int(score) >= 70] #list of scores >= 70
        total = sum(scores) #sum of all the scores
        print("Course Grades Summary Report ...")
        print(f"{'-'*55}\n{' '*10}Broward College Grades Summary\n{'-'*55}")
        print(f"{doc[0]}") #name of course
        print(f"{doc[1]}{' '*18}Term: {doc[2]}\n") #professor name and term
        print(f"{'Student Name':30s}{'Grade'}\n{'-'*40}")
        for index in range(len(names)):
            print(f"{names[index]:32s}{int(scores[index])}") # prints -> name : grade
        print("\nStudents' Performance\n"+"-"*40)
        print(f"Passed: {str(len(passed)):20s}Failed: {len(scores) - len(passed)}") #how many passed/failed
        print(f"Passing Percent: {int((len(passed)/len(scores))*100)}%") #percent of passed students
        print(f"Average Grade: {round(total/len(scores))}") #average grade

output_ = output() #calls function

while output_ != False: #re-prompts for another file
    try_again = input("\nWould you like to process another file (y/n)? ")
    if try_again == "y":
        output() #calls function again
    else:
        break