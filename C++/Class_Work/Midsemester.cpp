#include <iostream>
using namespace std;

int input() {
    int num;
    cout << "Enter a positive number: ";
    cin >> num;
    while (num <= 0) {
        cout << "Enter a positive number: ";
        cin >> num;
    }
    return num;
}

// Function to populate the even array
void populateEven(int even[], int n) {
    int length = 0;
    for (int i = 0; length < n; i += 2) {
        even[length] = i;
        length++;
    }
}

// Function to populate the odd array
void populateOdd(int odd[], int n) {
    int length = 0;
    for (int i = 1; length < n; i += 2) {
        odd[length] = i;
        length++;
    }
}

void Sum(int arr[], int n) {
    int total = 0;
    for (int i = 0; i < n; i++) {
        total += arr[i];
    }
    cout << total;
}

void Average(int arr[], int n) {
    int total = 0;
    for (int i = 0; i < n; i++) {
        total += arr[i];
    }
    cout << total / n;
}

// Function to print the elements of an array
void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

// Function to append even and odd numbers to arrays and print them
void Output(int n) {
    int even[n];
    int odd[n];

    populateEven(even, n);
    populateOdd(odd, n);

    cout << "Even sum: ";
    Sum(even, n);
    cout << "\tEven Average: ";
    Average(even, n);
    cout << endl;
    cout << "Odd sum: ";
    Sum(odd, n);
    cout << "\tOdd Average: ";
    Average(odd, n);

    cout << endl;
}

int main() {
    int maxsize = input(); // Get user input for the size of the array
    Output(maxsize);
    return 0;
}

