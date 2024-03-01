#include <iostream>
using namespace std;

const int rows = 7;
const int cols = 7;

// Function to print the 2D array
void printArray(int arr[][cols]) {
    for(int i = 0; i < rows; ++i) {
        for(int j = 0; j < cols; ++j) {
            cout << arr[i][j] << " ";
        }
        cout << endl;
    }
}

void formatting(int arr[][cols]){
    for(int i = 0; i < rows; ++i) {
        for(int j = 0; j < cols; ++j) {
            if (i %2!=0){
                arr[i][j] = '-';
            }
            
        }
    }
}

int Board() { //main
    int arr[rows][cols];

    // Initialize elements of the array
    int count = 1;
    for(int i = 0; i < rows; ++i) {
        for(int j = 0; j < cols; ++j) {
            arr[i][j] = count++;
        }
    }

    // Print the array from the main function
    cout << "Array from main function:" << endl;
    printArray(arr);

    return 0;
}

