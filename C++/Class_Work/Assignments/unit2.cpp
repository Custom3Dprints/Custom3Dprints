#include <iostream>
#include <string>
using namespace std;

void iTrade(string name, string symbol, int nshares, float cost, float price){
    cout << "Stock Investment Performance Calculator ...\n\n"
    << "Company Name (no spaces) & Symbol:     " << name <<" " << symbol
    << "\nNumber of Shares transacted:           " << nshares
    << "\nCost per Share (@ buying):             " << cost 
    << "\nPrice per Share (@ selling):           " << price;
    cout << "\n\nRealized Gains/Losses Report ...\n";
    std::string dashes(40, '-');       // == ["-"]*40.py
    std::cout << dashes << std::endl;  // prints dashes using std::endl
    cout << "Stock:              " << name <<"("<<symbol<<")"; 
    cout << "\nQuantity:           " << nshares << " shares.";
    
    double total_proceeds = nshares * price - price * nshares * .02;
    double total_cost = nshares * cost * .02 + nshares * cost;
    cout << "\n\nTotal Cost:         $" << total_cost;
    cout << "\nTotal Proceeds:     $" << total_proceeds;
    cout << "\nCommissions:        $"; //formula to get commissions?????  << total_proceeds * .02
    cout << "\nGains/Losses:       $";//idk formula for this and percentage
}

int main() {
    iTrade("AppleInc.", "APPL", 100, 150.05, 313.10);
    return 0;
}