#!python3

def displayString(board):
  """
  function should create a string that can be displayed using a print command
  this function should have no actual print commands in it
  
  input:
  list board: the game board data:
  7 8 9
  4 5 6
  1 2 3
  
  eg 
  board = [ 'O' , 0 , 0 , 'X' , 'O' , 0 , 0 , 0 , 'X' ] 
  should display:
  - - X
  X O -
  O - -
  
  return value
  str the gameboard
  """

  for i in range(len(board)):
    if board[i] == 0:
      board.pop(i)
      board.insert(i, "-")


  print(f"{board[6]}{board[7]}{board[8]}")
  print(f"{board[3]}{board[4]}{board[5]}")
  print(f"{board[0]}{board[1]}{board[2]}")

  return None

def main():
  board = [ 'O' , 0 , 0 , 'X' , 'O' , 0 , 0 , 0 , 'X' ] 
  assert displayString(board) == "- - X\nX O -\nO - -"
  board = [ 0 , 'O' , 'X' , 'O' , 'O' , 0 , 'X' , 0 , 'X' ] 
  assert displayString(board) == "X - X\nO O -\n- O X"

if __name__ == "__main__":
  main()
