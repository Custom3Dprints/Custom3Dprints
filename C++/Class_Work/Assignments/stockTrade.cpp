#include <iostream>
#include <string>
using namespace std;

void iTrade(string name, string symbol, int nshares, float cost, float price){  //function
    cout << "Stock Investment Performance Calculator ...\n\n"                // format display information
    << "Company Name (no spaces) & Symbol:     " << name <<" " << symbol     // format display information
    << "\nNumber of Shares transacted:           " << nshares                // format display information
    << "\nCost per Share (@ buying):             " << cost                   // format display information
    << "\nPrice per Share (@ selling):           " << price;                 // format display information
    cout << "\n\nRealized Gains/Losses Report ...\n";
    std::string dashes(40, '-');       // == ["-"]*40.py
    std::cout << dashes << std::endl;  // prints dashes using std::endl
    cout << "Stock:              " << name <<"("<<symbol<<")"; //displayed info under dashed line
    cout << "\nQuantity:           " << nshares << " shares."; //displayed info under dashed line
    
    double total_cost = nshares * cost * .02 + nshares * cost;                                  //float variables 
    double total_proceeds = nshares * price - price * nshares * .02;                            //float variables     
    double gains_losses = (price * nshares - cost * nshares) - (cost *.02 + price * .02) * 100; //float variables
    cout << "\n\nTotal Cost:         $" << total_cost;                                                      //displayed final math info 
    cout << "\nTotal Proceeds:     $" << total_proceeds;                                                    //displayed final math info   
    cout << "\nCommissions:        $" << (cost + price) * 200 / 100;                                        //displayed final math info               
    cout << "\nGains/Losses:       $" << gains_losses << " (" << (gains_losses / total_cost) * 100 <<"%)";  //displayed final math info                                                     
}

//call the function
int main() { 
    iTrade("AppleInc.", "APPL", 100, 150.05, 313.10);
    return 0;
}