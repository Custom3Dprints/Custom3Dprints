// TicTacToe.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
using namespace std;
// prototypes
void playTTT();
void showBoard(char board[3][3]);
void move(char board[3][3], char playerSymbol);
bool boardFull(char board[3][3]);
int main()
{
	playTTT();
}

void playTTT() {
	char board[3][3]={{' ',' ',' '},{' ',' ',' '},{' ',' ',' '}};
	do {
		showBoard(board);
		move(board, 'X');
		if (boardFull(board) == false) {
			showBoard(board);
			move(board, 'O');
		}
	} while (boardFull(board) == false);
	showBoard(board);
}

// showBoard shows current board state
void showBoard(char board[3][3]) {
	for (int row = 0; row < 3; row++) {
		for (int col = 0; col < 3; col++) {
			cout << "|" << board[row][col];
		}
		cout << "|" << endl;
		
	}
}
// move means playing X or O
void move(char board[3][3], char playerSymbol) {
	int moveRow, moveCol;
	cout << "Enter row and col separated by space:  ";
	cin >> moveRow >> moveCol;
	while (moveRow < 0 || moveRow>2 || moveCol < 0 || moveCol>2 || board[moveRow][moveCol] != ' ') {
		cout << "Invalid move" << endl;
		cout << "Enter row and col separated by space:  ";
		cin >> moveRow >> moveCol;
	}
	board[moveRow][moveCol] = playerSymbol;
}

// boardFull means that there is no more space to play in the board
bool boardFull(char board[3][3]) {
	bool full = true;
	for (int row = 0; row < 3; row++)
		for (int col = 0; col < 3; col++)
			if (board[row][col] == ' ')
				full = false;
	return full;
}

