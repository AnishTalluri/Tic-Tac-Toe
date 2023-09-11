# author: Anish Talluri
# date: 2/7/2023
# file: player.py a Python program that creates the tic-tac-toe players, which are a user who inputs moves manually
      # or AI who plays the game on its own
# input:  Takes in the input of asking the player (or AI/MiniMax input) of where they want to place their sign on the
      # board
# output: Runs the functions in the board if the user/AI/MiniMax chose correctly. If the user specificallty does not input
      # the right thing then it will keep asking them to input the right thing until they do so

import random

class Player:
      def __init__(self, name, sign):
            self.name = name  # player's name
            self.sign = sign  # player's sign O or X
      def get_sign(self):
            # return an instance sign
            return self.sign

      def get_name(self):
            # return an instance name
            return self.name

      def choose(self, board):
            # prompt the user to choose a cell
            # if the user enters a valid string and the cell on the board is empty, update the board
            # otherwise print a message that the input is wrong and rewrite the prompt
            # use the methods board.isempty(cell), and board.set(cell, sign)
            valid_choices = ['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3']
            while True: 
                  cell = input(f'{self.name}, {self.sign}: Enter a cell [A-C][1-3]:').upper()
                  if cell in valid_choices:
                        if board.isempty(cell):
                              board.set(cell, self.sign)
                              break
                        else:
                              print("You did not choose correctly.")
                              
                  else:
                        print("You did not choose correctly.")
                        
class AI(Player):
      def __init__(self, name, sign, board):
            super().__init__(name, sign)
            self.board = board
      
      def choose(self,board):
            valid_choices = ['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3']
            while True: 
                  cell = random.choice(valid_choices)
                  if board.isempty(cell):
                        board.set(cell, self.sign)
                        break
                        


class MiniMax(AI):

      def __init__(self, name, sign, board):
            super().__init__(name, sign, board)
            if self.sign == 'X':
                  self.opponent_sign = "O"
            if self.sign == "O":
                  self.opponent_sign = "X"

      def choose(self, board):
            valid_choices = ['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3']
            topScore = -9999
            topMove = None

            for i in valid_choices:
                  if board.isempty(i):
                        board.set(i, self.sign)
                        current_score = MiniMax.minimax(self, board, False)
                        board.set(i, ' ')
                        if current_score > topScore:
                              topScore = current_score
                              topMove = i
            print(topMove)
            board.set(topMove, self.sign)

      def minimax(self, board, self_player):
            valid_choices = ['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3']
        # check the base conditions
            if board.isdone():
            # self is a winner
                  if board.get_winner() == self.sign:
                        return 1
            # is a tie
                  elif board.get_winner() == 'tie':
                        return 0
            # self is a looser (opponent is a winner)
                  else:
                        return -1

        # make a move (choose a cell) recursively
        # use the pseudocode given to you above to implement the missing code
            if self_player:
                  topScore = -9999

                  for i in valid_choices:
                        if board.isempty(i):
                              board.set(i, self.sign)
                              current_score = MiniMax.minimax(self, board, False)
                              board.set(i, ' ')
                              if current_score > topScore:
                                    topScore = current_score
                  
                  return topScore
            
            else:
                  lowScore = 9999

                  for i in valid_choices:
                        if board.isempty(i):
                              board.set(i, self.opponent_sign)
                              current_score = MiniMax.minimax(self, board, True)
                              board.set(i, ' ')
                              if current_score < lowScore:
                                    lowScore = current_score
                        
                  return lowScore

