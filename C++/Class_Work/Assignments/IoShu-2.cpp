#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

const int rows = 3;
const int cols = 3;

// Function to print the 2D array
void printArray(vector<vector<string> >& arr) {
    for(int i = 0; i < rows; ++i) {
        cout << "- - - - - - -\n| ";
        for(int j = 0; j < cols; ++j) {
            cout << arr[i][j] << " | ";
        }
        cout << endl;
    }
    cout << "- - - - - - -\n";
}

//gets input
void getinput(vector<vector<string> >& arr){
    vector <int>inputs;
    int number;
    cout << "Enter Nine Numbers (1-9)\n";
    for(int n = 1; n < 10; n++){
        cout << "\tNumber " << n << ": ";
        cin >> number;

        while (number < 1 || number > 9){
            cout << "\tNumber " << n << ": ";
            cin >> number;
        }
        while (find(inputs.begin(), inputs.end(), number) != inputs.end()){
            cout << "\tNumber " << n << ": ";
            cin >> number;
        }
        inputs.push_back(number);
    }

    int count = 0;
    for (int i = 0; i < rows; i++){
        for (int j =0; j < cols; j++){
            arr[i][j] = to_string(inputs[count]);
            count++;
        }
    }
}

bool check(const vector<vector<string> >& arr) {
    // Calculate the sum of the first row to use it as a reference
    int sum_ref = 0;
    for (int j = 0; j < cols; ++j) {
        sum_ref += stoi(arr[0][j]);
    }

    // Check rows
    for (int i = 1; i < rows; ++i) {
        int sum_row = 0;
        for (int j = 0; j < cols; ++j) {
            sum_row += stoi(arr[i][j]);
        }
        if (sum_row != sum_ref) {
            return false; // Rows have different sums
        }
    }

    // Check columns
    for (int j = 0; j < cols; ++j) {
        int sum_col = 0;
        for (int i = 0; i < rows; ++i) {
            sum_col += stoi(arr[i][j]);
        }
        if (sum_col != sum_ref) {
            return false; // Columns have different sums
        }
    }

    // Check main diagonal
    int sum_diag_main = 0;
    for (int i = 0; i < rows; ++i) {
        sum_diag_main += stoi(arr[i][i]);
    }
    if (sum_diag_main != sum_ref) {
        return false; // Main diagonal has different sum
    }

    // Check secondary diagonal
    int sum_diag_sec = 0;
    for (int i = 0; i < rows; ++i) {
        sum_diag_sec += stoi(arr[i][cols - 1 - i]);
    }
    if (sum_diag_sec != sum_ref) {
        return false; // Secondary diagonal has different sum
    }

    return true; // All sums are equal
}

//verify T or F
int finaloutput(bool torf){
    if (torf == true){
        cout<< "This is a Lo Shu Magic Square!!!";
    }else{
        cout<< "Sorry ... this is not a Lo Shu Magic Square";
    }
    return 0;
}

//Starts game
void play(){
    vector<vector<string> > arr(rows, vector<string>(cols));

    int count = 1;
    for(int i = 0; i < rows; ++i) {
        for(int j = 0; j < cols; ++j) {
            arr[i][j] = to_string(count);
            count++;
        }
    }

    
    // Print the array from the main function
    cout << "\nArray from main function:" << endl;

    getinput(arr);
    printArray(arr);
    finaloutput(check(arr));
}

//Final output for game
int main() { //board
    play();
    string choice;
    cout << "\nWould you like to try again (y/n)? ";
    cin >> choice;
    while (choice == "y"){
        play();
        cout << "\nWould you like to try again (y/n)? ";
        cin >> choice;
    }
}

