# author: Anish Talluri
# date: 2/7/2023
# file: board.py a Python program that creates the tic-tac-toe board and win-lose conditions for the game
# input:  Takes in the player(s) sign that they place on the board
# output: creates a blank tic-taco-board and updates the board every time one of the player makes a move. 
      # It also checks the conditions on the board to see if either player has 3 in a row or the whole board is 
      # filled then they tie.

class Board:
      def __init__(self):
            # board is a list of cells that are represented 
            # by strings (" ", "O", and "X")
            # initially it is made of empty cells represented 
            # by " " strings
            self.sign = " "
            self.size = 3
            self.board = list(self.sign * self.size**2)
            # the winner's sign O or X
            self.winner = ""

      def get_size(self): 
             # optional, return the board size (an instance size)
            return self.size

      def get_winner(self):
            # return the winner's sign O or X (an instance winner)     
            return self.winner

      def set(self, cell, sign):
            # mark the cell on the board with the sign X or O
            valid_choices = ['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3']
            index = valid_choices.index(cell)
            self.board[index] = sign
            
      def isempty(self, cell):
            # return True if the cell is empty (not marked with X or O)
            valid_choices = ['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3']
            index = valid_choices.index(cell)
            if self.board[index] != 'X' and self.board[index] != 'O':
                  return True
            else:
                  return False

      def isdone(self):
            done = False
            # check all game terminating conditions, if one of them is present, assign the var done to True
            # depending on conditions assign the instance var winner to O or X

            for i in range(3):            # for checking the columns
                  if self.board[i] == self.board[i+3] == self.board[i+6]:
                        if self.board[i] in ['X', 'O']:
                              done = True
                              self.winner = self.board[i]

            for i in range(0, 7, 3):            # for checking the rows
                  if self.board[i] == self.board[i+1] == self.board[i+2]:
                        if self.board[i] in ['X', 'O']:
                              done = True
                              self.winner = self.board[i]

            if self.board[0] == self.board[4] == self.board[8]:         # for checking diagonals
                  if (self.board[0] and self.board[4] and self.board[8]) in ['X', 'O']:
                        done = True
                        self.winner = self.board[0]
            if self.board[2] == self.board[4] == self.board[6]:
                  if (self.board[2] and self.board[4] and self.board[6]) in ['X', 'O']:
                        done = True
                        self.winner = self.board[2]

            if ' ' not in self.board:           # for if the game ends up being a tie
                  self.winner = "tie"
                  done = True

            return done


      def show(self):
            # draw the board
            # need to complete the code
            print('   A   B   C') 
            print(' +---+---+---+')
            print('1| {} | {} | {} |'.format(self.board[0], self.board[1], self.board[2]))
            print(' +---+---+---+')
            print('2| {} | {} | {} |'.format(self.board[3], self.board[4], self.board[5]))
            print(' +---+---+---+')
            print('3| {} | {} | {} |'.format(self.board[6], self.board[7], self.board[8]))
            print(' +---+---+---+')