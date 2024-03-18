#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

double Price_gallons(){ //gets price of gallons
    double price;
    cout << "\nPaint Job Estimator ...";
    cout << "\n\nPrice per gallon of paint (>=0): ";
    cin >> price;
    while (price < 0){
        cout << "Error ... Invalid price per gallon of paint. Try again.";
        cout << "\nPrice per gallon of paint (>=0): ";
        cin >> price;
    }   
    return price;
}

int Num_ofRooms(){ //gets the number of rooms
    int nrooms;
    cout << "\n\nNumber of rooms to be painted (>=1): ";
    cin >> nrooms;
    while (nrooms < 1){
        cout << "Error ... Invalid number of rooms. Try again.";
        cout << "\nNumber of rooms to be painted (>=1): ";
        cin >> nrooms;
    }
    return nrooms;
}

int SQFT(int nrooms){ // sqft per room
    int sqft;
    int total_sqft = 0;
    cout << "\n\nSquare feet of wall space (>=25)\n";
    for (int i = 0; i < nrooms; i+=1){
        cout << "\tRoom " << i+1 << ": ";
        cin >> sqft;
        while (sqft < 25){
            cout << "\tError ... Incorrect wall space for the room. Try again.";
            cout << "\n\tRoom " << i+1 << ": ";
            cin >> sqft;
        }
        total_sqft += sqft;
    }
    return total_sqft;
}

void Function(double gallonprice, double sqft, double onegallonsqft, double labortime, double laborPrice){ //all output formatting
    double Gallons = sqft/onegallonsqft;
    cout << fixed <<setprecision(2) 
    << "\n\tPaint Job Estimate"
    << "\n\nPaint ..."
    << "\nGallons of Paint:\t" << round(Gallons)  //gallons of paint needed
    << "\nCost of Paint:\t\t$ " << round(Gallons) * gallonprice //Cost of paint 
    << "\n\nLabor ..."
    << "\nHours of Labor:\t\t" << labortime * Gallons //hours of labor
    << "\nCost of Labor:\t\t$ " << laborPrice * labortime * Gallons //cost of labor
    << "\n\t\t\t----------"
    << "\nTotal Cost:\t\t$ " <<  (round(Gallons) * gallonprice) + (laborPrice * labortime * Gallons) <<endl;//Total Cost
}

int main(){ //calling all functions^
    double price_per_gallon = Price_gallons();
    int Rooms = Num_ofRooms();
    int Total_Sqft = SQFT(Rooms);
    
    Function(price_per_gallon, Total_Sqft, 115, 8, 25);
    return 0;
}