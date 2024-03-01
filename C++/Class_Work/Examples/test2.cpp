//Chapter 6 programming project
#include <iostream>
using namespace std;


void isPrime(int number){
    int numofFactors = 0;
    
    for (int r = 1; r <= number; r++){
        if (number%r == 0){
            numofFactors++;
        }
    }
    if (numofFactors == 2 || numofFactors == 1){
        cout << number << " is prime." << endl;
    }else if (numofFactors > 2){
        cout << number << " is NOT prime." << endl;
    }else{
        cout << "Invalid";
    }
} 

int main(){
    int number;
    cout << "\nEnter a number and I'll tell you whether it is prime: ";
    cin >> number;

    isPrime(number);
    return 0;
}