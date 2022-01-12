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

  boardstr = ""
  
  def MakeBoard(boardl, startlist):
    boardstr = ""
    for i in range(3):
        if i != 2:
            boardstr = boardstr + boardl[startlist] + " "
            startlist = startlist + 1
        else:
            boardstr = boardstr + board[startlist]
    return boardstr

  row1 = MakeBoard(board, 6)
  row2 = MakeBoard(board, 3)
  row3 = MakeBoard(board, 0)
  fullboard = row1 + "\n" + row2 + "\n" + row3
  return fullboard


def main():
  board = [ 'O' , 0 , 0 , 'X' , 'O' , 0 , 0 , 0 , 'X' ] 
  assert displayString(board) == "- - X\nX O -\nO - -"
  board = [ 0 , 'O' , 'X' , 'O' , 'O' , 0 , 'X' , 0 , 'X' ] 
  assert displayString(board) == "X - X\nO O -\n- O X"

if __name__ == "__main__":
  main()
