#include <iostream>
#include <vector>
#include <string>
using namespace std;

/*
void function(){
    int num;
    cout << "Creating Lo Shu Square"
    << "\n\nEnter Nine Numbers (1-9)\n";

    for (int i = 1; i < 10; i+=1){ //1-9
        cout << "\tNumber " << i << ": ";
        cin >> num;
        while (num < 1 || num > 9){
            cout << "\tNumber " << i << ": ";
            cin >> num;
        }
        grid(7,7,num);
    }
    
}
*/
void grid(const int row, const int column, int num) {
    int count = 1;

    // Declaring a pointer to a 2D array
    string** array1 = new string*[row];

    for (int i = 0; i < row; i++) {
        array1[i] = new string[column];
    }

    //string dashes(1, '-');  // Create a string of 1 dash

    // Initialize 2D array using loop
    for (int i = 0; i < row; i++) {
        if (i % 2 != 1) {  // Check if the row index is odd
            for (int j = 0; j < column; j++) {
                array1[i][j] = "-";
            }
        }else {
            for (int j = 0; j < column; j++) {
                array1[i][j] = to_string(count);
                count++;
            }
        }
        for (int j = 0; j < column; j++){
            if (i % 2 != 0){
                if (j % 2 == 0){
                    array1[i][j] = "|";
                }
                else{
                    array1[i][j] = to_string(num);
                }
        /*
                else if (j % 2 != 0){
                    array1[i][j] = to_string(num);
                }
        */
            }
            
        }
    }

    // Printing the elements of the 2D array
    for (int i = 0; i < row; i++) {
        for (int j = 0; j < column; j++) {
            cout << array1[i][j] << " ";
        }
        cout << endl;
    }

    // free the dynamically allocated memory
    for (int i = 0; i < row; ++i) {
        delete[] array1[i];
    }
    delete[] array1;
}


int main(){
    int num;
    cout << "Creating Lo Shu Square"
    << "\n\nEnter Nine Numbers (1-9)\n";

    for (int i = 1; i < 10; i+=1){ //1-9
        cout << "\tNumber " << i << ": ";
        cin >> num;
        while (num < 1 || num > 9){
            cout << "\tNumber " << i << ": ";
            cin >> num;
        }
        grid(7,7,num);
    }
    return 0;
}