// Unit 5 project workbook

#include <iostream>
#include <fstream>
using namespace std;

int main(){
    ifstream myfile("Random.txt");
    if (myfile.is_open()){
        // Specify the path to your text file
        string filename = "Random.txt";

        // Open the file
        ifstream inputFile(filename);

        // Check if the file is successfully opened
        if (!inputFile.is_open()) {
            cerr << "Error opening file: " << filename << std::endl;
            cout<< 1; // Return an error code
        }

        // Vector to store lines from the file
        vector<string> lines;
        int numofnums = 0;
        // Read the file line by line
        string line;
        while (getline(inputFile, line)) {
            lines.push_back(line);
            numofnums++;
        }

        // Close the file
        inputFile.close();
        int sum = 0;
        for (int i=0; i < lines.size(); i++){
            sum = sum+stoi(lines.at(i));
        }
        cout << "\nNumber of numbers: " << numofnums;
        cout << "\nSum of the numbers: "<<sum;
        cout << "\nAverage of the numbers: "<< sum / numofnums<<endl;
    }
}