#include <iostream>
#include <string>
#include <iomanip>
#include <cmath>
using namespace std;

void output(string name, string institution, double nloan, double rate, double time){
    cout << fixed << setprecision(2); //max hundredth place
    cout << "Loan Payment Calculator ..."

    << "\n\nPlease enter the following information:"

    <<"\n\nBorrower's Name:             " << name
    << "\nLoaning Institution:         " << institution

    << "\n\nLoan Amount($):              " << nloan
    << "\nAnnual Interest Rate (%):    " << rate
    << "\nTerm of Loan (years):        " << time

    << "\n\nDate of Report:              " << "April, 2022\n\n"; //not current date

    string dashes(50, '-');       // == ["-"]*40.py
    cout << dashes << std::endl;  // prints dashes using std::endl

    double monthly_intrest = rate / 12;
    double monthly_payment = nloan*(((monthly_intrest/100)*(pow((monthly_intrest/100)+1,360))) / (pow(1+(monthly_intrest/100), 360) -1));
    double total_amount = monthly_payment*time*12; 

    cout 
    << "Loan Payment Summary Report"

    << "\n\n" << institution << "\t\t" << name
    << "\nAnnual Intrest Rate: " << rate <<"%"
    << "\nDate: April, 2022"
    
    << "\n\nLoan Amount:\t\t\t$  " << nloan
    << "\nMonthly Intrest Rate:\t\t\t" << monthly_intrest
    << "\nNumber of Payments:\t\t      " << time * 12
    << "\nMonthly Payment:\t\t$     " << monthly_payment
    
    << "\n\nTotal Amount to Pay:\t\t$  " << total_amount 
    << "\nTotal Intrest:\t\t\t$   " << total_amount - nloan;
}

int main(){
    output("Taylor Davenport", "Davie Bank & Loans", 120000, 3.75, 30);
    return 0;
}