#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

//Open, read and appended into vector
string line;
vector<int>lines;
void readfile(string file){
    fstream myfile(file);
    if (myfile.is_open()){
        while (getline(myfile, line)){
            lines.push_back(stoi(line));
        }
        myfile.close();
    }
}

//calculate average grade
double averageGrade(){
    int Sum = 0;
    for (int i=0; i < lines.size(); i++){
        Sum += lines[i];
    }
    return Sum/lines.size();
}

//create file, write in file, close file
void Createfile(){
    ofstream Myfile("result.txt");
    
    Myfile << lines.size()<<endl;
    Myfile << averageGrade()<<endl;

    Myfile.close();
}

int main(){
    readfile("Scores.txt");
    Createfile();
    return 0;
}