//optimized version:
/*
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string_view>

using namespace std;

struct Player {
    string name;
    int number;
    int goals;
};

int getOption() {
    cout << "Choose one of the following options\n"
         << "\t1. Load team's information.\n"
         << "\t2. Display team's roster.\n"
         << "\t3. Display team's goals.\n"
         << "\t4. Display team's star(s).\n"
         << "\t5. Quit.\n";
    int option;
    cout << "Option: ";
    cin >> option;
    while (option < 1 || option > 5) {
        cout << "Invalid option. Please enter a valid option (1-5): ";
        cin >> option;
    }
    cout << endl;
    return option;
}

string getFileName() {
    string file;
    cout << "Enter File Name: ";
    cin >> file;
    return file;
}

void readFile(const string& file, vector<string>& lines) {
    ifstream myfile(file);
    if (myfile.is_open()) {
        string line;//
        while (getline(myfile, line)) {
            lines.push_back(line);
        }
        myfile.close();
    }
}

void parseData(const vector<string>& lines, vector<Player>& players) { //
    for (size_t i = 0; i < lines.size(); i += 3) {
        Player player;                      
        player.name = lines[i];               
        player.number = stoi(lines[i + 1]);    
        player.goals = stoi(lines[i + 2]);    
        players.push_back(player);
    }
}

void displayRoster(const vector<Player>& players) {
    cout << "\nPlayer Name\t\tNumber\t  Goals\n";
    string dashes(45, '-');
    cout << dashes << endl;
    for (const auto& player : players) { //
        if (player.name.size() >= 8) {
            cout << player.name << "\t\t  " << player.number << "\t\t" << player.goals << endl;
        } else {
            cout << player.name << "\t\t\t  " << player.number << "\t\t" << player.goals << endl;
        }
    }
}

void displayTotalGoals(const vector<Player>& players) {
    int totalGoals = 0;
    for (const auto& player : players) {
        totalGoals += player.goals;
    }
    cout << "\nTotal goals scored: " << totalGoals << endl;
}

void displayTopPlayers(const vector<Player>& players) {
    int maxGoals = 0;
    for (const auto& player : players) {
        maxGoals = max(maxGoals, player.goals);
    }

    cout << "\nTop team player(s): ";
    for (const auto& player : players) {
        if (player.goals == maxGoals) {
            cout << player.name << ", ";
        }
    }
    cout << " (" << maxGoals << " goals)" << endl;
}

int main() {
    cout << "\nSoccer Team Goals ...\n\n";
    
    int option = getOption();
    
    if (option == 5) {
        cout << "Good Bye ...\n";
    } else {
        string filename = getFileName();
        vector<string> lines;
        readFile(filename, lines);
        vector<Player> players;
        parseData(lines, players);
        
        switch (option) {
            case 2:
                displayRoster(players);
                break;
            case 3:
                displayTotalGoals(players);
                break;
            case 4:
                displayTopPlayers(players);
                break;
            default:
                break;
        }
    }
    
    return 0;
}

*/