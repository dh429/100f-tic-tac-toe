#!python3
from x02_display import displayString
"""
Create a function that will determine if one person is the winner (has 3 in a row)
inputs:
list board : the list that contains the board data

return:
str 'X' if X is the winner
str 'O' if O is the winner
None if there is no winner
"""

def whoWins(board):
  
  if board[8] == "O" and board[4] == "O" and board[0] == "O":
    return "O"
  elif board[8] == "X" and board[4] == "X" and board[0] == "X":
    return "X"
  elif board[6] == "O" and board[4] == "O" and board[2] == "O":
    return "O"
  elif board[6] == "X" and board[4] == "X" and board[2] == "X":
    return "X"
  elif board[7] == "O" and board[4] == "O" and board[1] == "O":
    return "O"
  elif board[7] == "X" and board[4] == "X" and board[1] == "X":
    return "X"
  elif board[6] == "O" and board[3] == "O" and board[0] == "O":
    return "O"
  elif board[6] == "X" and board[3] == "X" and board[0] == "X":
    return "X"
  elif board[8] == "O" and board[5] == "O" and board[2] == "O":
    return "O"
  elif board[8] == "X" and board[5] == "X" and board[2] == "X":
    return "X"
  else:
    return None


def main():
  board = [ 'O','X',0,'X','O',0,'X',0,'O']
  assert whoWins(board) == 'O'
  board = [ 'X','O',0,'X','O','X','O','O','X']
  assert whoWins(board) == 'O'
  board = [ 'X','O',0,'X','X','O','O','X','O']
  assert whoWins(board) == None
  board = [ 'X','O',0,'X','X','X','O','O','X']
  assert whoWins(board) == 'X'

if __name__ == "__main__":
  main()