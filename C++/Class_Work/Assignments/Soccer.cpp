// Unit 8 Lab Assignment

#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

int getOption(){
    cout << "Choose one of the following options\n"
    << "\t1. Load team's information.\n"
    << "\t2. Display team's roster.\n"
    << "\t3. Display team's goals.\n"
    << "\t4. Display team's star(s).\n"
    << "\t5. Quit.";
    int get_option;
    cout << "\nOption: ";
    cin >> get_option;
    while (get_option < 1 || get_option > 5){
        cout << "\nOption: ";
        cin >> get_option;
    }
    cout << endl;
    return get_option;
}

string getFileName(){
    string file;
    cout << "Enter File Name: ";
    cin >> file;
    return file;
}

string line;
vector<string>lines;

vector<string>playerName;
vector<int>number;
vector<int>goals;

void readfile(string file){
    fstream myfile(file);
    if (myfile.is_open()){
        while (getline(myfile, line)){
            lines.push_back(line);
        }
    }
    myfile.close();
}
void append(){
    for (int i=0; i < lines.size(); i+=3){
        playerName.push_back(lines[i]);
        number.push_back(stoi(lines[i+1]));
        goals.push_back(stoi(lines[i+2]));
    }
}
void output(){
    cout << endl 
    << "Player Name\t\tNumber\t  Goals\n";
    string dashes(45, '-');
    cout << dashes << endl;
    for (int i=0; i < lines.size(); i+=3){
        if (i == 18 || i == 21){
            cout << lines[i] << "\t  " << lines[i+1] << "\t\t" << lines[i+2] << endl;
        }else{
            cout <<lines[i] << "\t\t  " << lines[i+1] << "\t\t" << lines[i+2] << endl;
        }
    }

}

void totalgoals(){
    int total = 0;
    for (int i=0; i < goals.size(); i++){
        total += goals[i];
    }
    cout <<  "\nTotal goals scored: "<<total<<endl;
}

void topPlayer(){
    auto maxScore = max_element(goals.begin(), goals.end());

    cout << "\nTop team player(s): ";
    for (size_t i = 0; i < goals.size(); ++i) {
        if (goals[i] == *maxScore) {
            cout << playerName[i] << ", ";
        }
    }
    cout << " ("<<*maxScore<<" goals)"<<endl;
}


int main(){
    cout << "\nSoccer Team Goals ...\n\n";
    
    int option = getOption();
    
    if (option == 5){
        cout << "Good Bye ...\n";
    }else{
        string filename = getFileName();
        readfile(filename);
        append();
        switch (option){
            case 2:
                output();
                break;
            case 3:
                totalgoals();
                break;
            case 4:
                topPlayer();
                break;
        default:
            break;
        }
    }
    
    return 0;
}
