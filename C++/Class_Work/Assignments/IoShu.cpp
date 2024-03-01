//Unit 7
#include <iostream>
#include <vector>
#include <string>
using namespace std;


vector <int> inputs;

int getnum(){
    int numin;
    int num = 1;

    cout << "\n\nEnter Nine Numbers (1-9)\n";
    for (int i = 0; i < 9; i++){
        cout << "\tNumber " << num << ": ";
        cin >> numin;

        while (numin < 1 || numin > 9){
            cout << "\tNumbers " << num << ": ";
            cin >> numin;
        }
        inputs.push_back(numin);
        num++;
    }
    return 0;
}

/**/
void grid(const int row, const int column) {
    
    int count = 1;

    // Declaring a pointer to a 2D array
    string** array1 = new string*[row];

    for (int i = 0; i < row; i++) {
        array1[i] = new string[column];
    }
    
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
            }
        }
    }

    //for (int p = 0; p < inputs.size(); p++){
    //    cout << inputs[p]<<endl;
    //}    
    /*
    for (int i = 0; i < row; i++){
        for (int j = 0; j < column; j++){
            //array1[i][j] = inputs[c]; //number inputted  
        }
    }
    */

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
    cout << "Creating Lo Shu Square\n";
    //getnum();
    grid(7, 7);
    return 0;
}