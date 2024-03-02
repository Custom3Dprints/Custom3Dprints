#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

const int rows = 7;
const int cols = 7;

// Function to print the 2D array
void printArray(vector<vector<string> >& arr) {
    for(int i = 0; i < rows; ++i) {
        for(int j = 0; j < cols; ++j) {
            cout << arr[i][j] << " ";
        }
        cout << endl;
    }
}


void formatting(vector<vector<string> >& arr){
    for(int i = 0; i < rows; ++i) {
        for(int j = 0; j < cols; ++j) {
            if (i %2==0){
                arr[i][j] = "-";
            }else{
                if (j %2 == 0){
                    arr[i][j] ="|";
                }
            }
        }
    }
}
int getinput(vector<vector<string> >& arr){
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
            if (arr[i][j] != "-" && arr[i][j] != "|"){
                arr[i][j] = to_string(inputs[count]);
                count++;
            }
        }
    }
   return 0;
}
/*
void update(string arr[rows][cols]){
    int count = 0;
    for (int i = 0; i < rows; i++){
        for (int j =0; j < cols; j++){
            if (arr[rows][cols] != "-" && arr[rows][cols] != "|"){
                arr[rows][cols] = inputs[count];
                count++;
            }
        }
    }
}
*/

int main() { //board
    //string arr[rows][cols];
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
    formatting(arr);
    getinput(arr);
    //update(arr);
    printArray(arr);
    
    return 0;
}

