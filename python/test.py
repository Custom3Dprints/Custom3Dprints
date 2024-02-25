def main():
    # display a welcome message
    print("Welcome to the Future Value Calculator\n")

    choice = "y"
    while choice.lower() == "y":

        # get input from the user
        monthly_investment = float(input("Enter monthly investment:\t"))
        while monthly_investment <= 0:
            print("Entry must be greater than 0. Please try again.")
            monthly_investment = float(input("Enter monthly investment:\t"))
            
        yearly_interest_rate = float(input("Enter yearly interest rate:\t"))
        while yearly_interest_rate <= 0 or yearly_interest_rate > 15:
            print("Entry must be greater than 0 and less than or equal to 15.\nPlease try again.")
            yearly_interest_rate = float(input("Enter yearly interest rate:\t"))
            
        years = int(input("Enter number of years:\t\t"))
        while years <= 0 or years > 50:
            print("Entry must be greater than 0 and less than or equal to 50.\nPlease try again.")
            years = int(input("Enter number of years:\t\t\n"))
            
        # convert yearly values to monthly values
        monthly_interest_rate = yearly_interest_rate / 12 / 100 
        months = years * 12  ##Var not used

        # calculate the future value
        future_value = 0
        for i in range(years): ## changed from months to years
            future_value += monthly_investment                               ##Your math is wrong:(
            monthly_interest_amount = future_value * monthly_interest_rate   ##Your math is wrong:(
            future_value += monthly_interest_amount                          ##Your math is wrong:(
            
            # display the result
            ## i == years but technecilly starts counting from 0 so i just add one
            print(f"Year = {i+1}\tFuture value = {round(future_value, 2)}")
            
        # see if the user wants to continue
        choice = input("\nContinue (y/n)?\n")

    print("\nBye!")  ##\n = next line or enter

main() ##this is the correct way to call a function unless specified by ur professor
##Technacally you dont need this code below

#if __name__ == "__main__":   # if this module is the main module
#    main()                   # call the main()function