//Unit 4 workbook project 2
/*
#include <iostream>
#include <cmath>
using namespace std;

int main(){
    cout << "Geometry Calculator\n\n";

    cout << "1. Calculate the Area of a Circle\n"
    << "2. Calculate the Area of a Rectangle\n"
    << "3. Calculate the Area of a Triangle\n"
    << "4. Quit\n\n";

    int choice;
    cout << "Enter your choice (1-4): ";
    cin >> choice;
    while (choice < 1 || choice > 4){
        cout << "The valid choices are 1 through 4. Run the \nprogram again and select one of those.\n";
        cout << "Enter your choice (1-4): ";
        cin >> choice;
    }
    
    switch (choice){
        case 1:
            int radius;
            cout << "\nEnter the circle's radius: ";
            cin >> radius;
    
            if (radius < 0){
                cout << "\nThe radius can not be less than zero.\n";
                break;
            }else{
                cout << "\nThe area is " << pow(radius, 2) * 3.14159 << endl;
                break;
            }
        case 2:
            int length, width;
            cout << "\nEnter the rectangle's length: ";
            cin >> length;
            cout << "Enter the rectangle's width: ";
            cin >> width;
    
            if (length < 0 || width < 0){
                cout << "\nOnly enter positive values for length and width.\n";
                break;
            }else{
                cout << "\nThe area is " << length * width << endl;
                break;
            }
        case 3:
            int height, base;
            cout << "Enter the length of the base: ";
            cin >> base;
            cout << "Enter the triangle's height: ";
            cin >> height;
    
            if (height < 0 || base < 0){
                cout << "\nOnly enter positive values for length and width.\n";
                break;
            }else{
                cout << "\nThe area is " << base * height * .5 << endl;
                break;
            }
        default:
            cout << "Program ending.\n";
            break;
    }
}
*/
 