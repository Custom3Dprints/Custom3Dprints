/*
#include <iostream>
#include <string>
#include <vector>
using namespace std;

vector <int> numbers;
int getnum(int n){
    int num;
    cout << "\tNumber " << n << ": ";
    cin >> num;

    //bool exists = find(numbers.begin(), numbers.end(), num)
    while (num < 1 || num > 9){
        cout << "\tError ... Invalid number\n\n";
        cout << "\tNumber " << n << ": ";
        cin >> num;
    }
    while (find(numbers.begin(), numbers.end(), num)!=numbers.end()){
        cout << "\tError ... " << num << " is already in the Lo Shu Square. Try again\n\n";
        cout << "\tNumber " << n << ": ";
        cin >> num;
    }
    numbers.push_back(num);
    return num;
}

void grid(const int row, const int column) {
    int count = 1;

    // Declaring a pointer to a 2D array
    string** array1 = new string*[row];

    for (int i = 0; i < row; ++i) {
        array1[i] = new string[column];
    }

    // 2D array formatting
    for (int i = 0; i < row; i++) {
        if (i % 2 != 1) {  // Check if the row index is odd
            for (int j = 0; j < column; j++) {
                array1[i][j] = "-";
            }
        }else {
            for (int j = 0; j < column; j++) {
                if (i % 2 != 0){
                    if (j % 2 == 0){
                        array1[i][j] = "|";
                    }
                    else if (j % 2 != 0){
                        array1[i][j] = to_string(count);
                        count++;
                    }
                }
            }
        }
    }
    

    int lis1[3];
    int lis2[3];
    int lis3[3];
    int total1, total2, total3;
    // number replacement
    int number = 1;
    for (int r = 0; r < row; r++){
        for (int c = 0; c < column; c++){
            //cout <<endl<< array1[r][c];
            if ((array1[r][c] == "|") || (array1[r][c] == "-")){}
            else{
                int gotnum = getnum(number);
                array1[r][c] = to_string(gotnum);
                number++;
                for (int a = 0; a < lis1.size(); a++){

                }
                if (number <= 3){
                    lis1.push_back(gotnum);
                }else if (number <= 6){
                    lis2.push_back(gotnum);
                }else{
                    lis3.push_back(gotnum);
                }
            }
        }
    }
    cout << lis1 << endl;// << lis2 << endl <<lis3;

    // Final display
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

int main() {
    cout << "Creating Lo Shu Square"
    << "\n\nEnter Nine Numbers (1-9)\n";
    grid(7, 7);
    return 0;
}
*/


