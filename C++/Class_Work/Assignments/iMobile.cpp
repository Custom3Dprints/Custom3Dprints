#include <iostream>
#include <iomanip>
using namespace std;

void Initial(){
    cout << fixed << setprecision(2);
    cout <<"iMobile Bill Calculator ..."
    << "\n\nSelect a subscription package:"
    << "\n\t1. Package A"
    << "\n\t2. Package B"
    << "\n\t3. Package C\n";

    int package_type;
    double gigs;
    double price;
    double given_gigs;
    double cost;

    cout << "Package: ";
	cin >> package_type;
    while (package_type <= 0 || package_type > 3){
        cout << "\nError ... Invalid package. Try again.\n";
        cout << "Package: ";
        cin >> package_type;
    }

    cout << "How many gigabytes of data were used? ";
    cin >> gigs;
    while (gigs < 1){
        cout << "\nError ... Invalid gigabytes entered. Try again.\n";
        cout << "How many gigabytes of data were used? ";
        cin >> gigs;   
    }
    
    switch (package_type){
        case 1:
            price = 39.99;
            given_gigs = 4;
            cost = price + ((gigs - given_gigs)*10);
            cout << "The total amount due is $" << cost;
            break;
        case 2:
            price = 59.99;
            given_gigs = 8;
            cost = price + ((gigs - given_gigs)*5);
            cout << "The total amount due is $" << cost;
        case 3:
            price = 69.99;
            cost = price;
            cout << "The total amount due is $" << cost;
    default:
        break;
    }
}

int main(){
    Initial();
    return 0;
}