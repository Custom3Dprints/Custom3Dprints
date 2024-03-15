#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <typeinfo>
#include <iomanip>
#include <ios>
using namespace std;

//get initial input and checks if valid
int get_option(){
    int option;
    
    cout << "\nChoose one of the following options"
    << "\n\t1. Process Grades Summary report."
    << "\n\t2. Quit."

    << "\nOption: ";
    cin >> option;

    while (true){
        if (option < 1 || option > 2){
            cout << "Option: ";
            cin >> option;
            return option;
        }if (option == 2){
            cout << "\nGood Bye ...\n";
            return 0;
        }
        return option;
    }
}

//get file name
string get_file(){
    cout << "\nGrades Summary Report ...\n\n";
    string file;
    cout << "Enter file name: ";
    cin >> file;
    
    return file;
}

//formatting
int Function(string file, int option){
    string dashes(50, '-');       // == ["-"]*50.py
    cout <<endl<< dashes << endl;  // displays dashes using std::endl

    ifstream myfile(file);
    if (myfile.is_open() && option == 1){
        // Specify the path to your text file
        string filename = file;
    
        // Open the file
        ifstream inputFile(filename);
    
        // Check if the file is successfully opened
        if (!inputFile.is_open()) {
            cerr << "Error opening file: " << filename << std::endl;
            cout<< 1; // Return an error code
        }
    
        // Vector to store lines from the file
        vector<string> lines;
    
        // Read the file line by line
        string line;
        while (getline(inputFile, line)) {
            //store each line in the vector
            lines.push_back(line);
        }
    
        // Close the file
        inputFile.close();
    
        cout <<endl<< lines[0]<<endl<<endl
        <<lines[1]<<"\t\tTerm: "<<lines[2];
        cout<<"\n\n\nList of Students\n";

        cout << dashes << endl;  // prints dashes
        
        //array of all names and grades without spaces
        vector <string> name_grade;
        for (size_t i = 0; i < lines.size(); i += 1) {
            if ((i > 2) && (lines[i]!="")){
                name_grade.push_back(string(lines[i]));
            }
        }

        //organized to seperate arrays/vectors
        vector <string> names;
        vector <int> grades;
        for (size_t n = 0; n < name_grade.size(); n+=1){
            if (n%2==0){
                names.push_back(name_grade[n]);
            }
            else{
                double grade = stod(name_grade[n]); 
                grades.push_back(grade);
            }
        }
        
        //name        grade
        for(size_t j = 0;j<names.size(); j+=1){
            if (j == 4 || j == 10 || j==11){
                cout<<names[j] << "\t\t" << grades[j]<<endl; 
            }else{
                cout<< names[j] << "\t\t\t" << grades[j]<<endl;
            }
        }

        double largest = grades[0];
        double lowest = grades[0];
        double sum = grades[0];
    
        // Iterate through the array to find largest, lowest, and calculate sum
        for (int i = 1; i < grades.size(); ++i) {
            if (grades[i] > largest) {
                largest = grades[i];
            }
            if (grades[i] < lowest) {
                lowest = grades[i];
            }
            sum += grades[i];
        }
    
        // Calculate average
        double average = sum / grades.size();

        cout << "\nHighest Grade: " << largest
        << "\nLowest Grade:  " << lowest
        <<fixed << setprecision(1)
        << "\nAverage Grade: " << average<<endl<<endl;
    }

    cout << dashes << endl;
    return 0;
}

//final output
int main(){
    cout << "\nCourse Summary App ...\n";

    while (int Option = get_option() == 1){
        string filename = get_file();
        Function(filename,Option);
    }
    return 0;
}
