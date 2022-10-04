"""
Tic Tac Toe
- Classes
- 2D lists
- Computational Thinking

board = [
    ["0, 0", "0, 1", "0, 2"],
    ["1, 0", "1, 1", "1, 2"],
    ["2, 0", "2, 1", "2, 2"],
]
"""
import random

class Board:
    
    def __init__(self):
        self.board = []
        
    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append("-")
            self.board.append(row)
    
    def display_board(self):
        print()
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()
        print()
    
    def has_item(self, row, column):
        return self.board[row][column] != "-"

    def insert_mark(self, row, column, mark):
        self.board[row][column] = mark
        
    def has_complete_row(self):
        for row in self.board:
            if len(set(row)) == 1 and "-" not in row:
                return True
        
        return False

    def has_complete_column(self):
        complete_row = set()
        column_index = 0
        while column_index < len(self.board):
            for row in self.board:
                complete_row.add(row[column_index])
            
            if len(complete_row) == 1 and "-" not in complete_row:
                return True

            complete_row.clear()
            column_index += 1
        
        return False
    
    def has_complete_diagonal(self):
        """
        board = [
            ["0, 0", "0, 1", "0, 2"],
            ["1, 0", "1, 1", "1, 2"],
            ["2, 0", "2, 1", "2, 2"],
        ]
        """
        complete_diagonal = set()
        for i in range(len(self.board)):
            complete_diagonal.add(self.board[i][i])
        
        if len(complete_diagonal) == 1 and "-" not in complete_diagonal:
            return True
        
        complete_diagonal.clear()
        
        column_index = len(self.board) - 1
        for i in range(len(self.board)):
            complete_diagonal.add(self.board[i][column_index])
            column_index -= 1
        
        if len(complete_diagonal) == 1 and "-" not in complete_diagonal:
            return True

        return False
    
    def winner_exists(self):
        return self.has_complete_row() or self.has_complete_column() or self.has_complete_diagonal()
    
    def get_empty_positions(self):
        positions = []
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j] == "-":
                    positions.append([i, j])
        return positions

class TicTacToe:
    def __init__(self):
        self.board = Board()
        self.board.create_board()
        self.user_turn = True
    
    def get_user_input(self):
        while True:
            row = int(input("Enter a row [0, 1, 2]: "))
            column = int(input("Enter a column [0, 1, 2]: "))
            if not self.board.has_item(row, column):
                return row, column
            print("\nThat position is taken!")
            
    def get_ai_input(self):
        free_positions = self.board.get_empty_positions()
        choice = random.choice(free_positions)
        return choice
    
    def switch_turn(self):
        self.user_turn = not self.user_turn
        
    def play(self):
        print("Welcome to TicTacToe!")
        print("You are X")
        while True:
            if self.user_turn:
                row, column = self.get_user_input()
                self.board.insert_mark(row, column, "X")
                if self.board.winner_exists():
                    print("\nCongratulations you have won!\n")
                    break
            else:
                print("The computer is thinking.")
                row, column = self.get_ai_input()
                self.board.insert_mark(row, column, "0")
                if self.board.winner_exists():
                    print("\nYou have lost. Better luck next time!\n")
                    break
            
            if len(self.board.get_empty_positions()) == 0:
                print("\nIt was a draw!")
                break
            
            self.board.display_board()
            self.switch_turn()
        
        self.board.display_board()

tic_tac_toe = TicTacToe()
tic_tac_toe.play()