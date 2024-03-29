"""
Conway's Game of Life

Imagine a grid where you randomly place cells.

How they grow according to the rules:

  1. Cell with less than 2 neighbours dies
  2. Cell with more than 3 neighbours dies
  3. Empty space with exactly 3 neighbours becomes a new cell
"""

import random
import time
import copy

EMPTY = 0  
ALIVE = 1

board = [
  [EMPTY, ALIVE, EMPTY],
  [EMPTY, ALIVE, EMPTY],
  [EMPTY, ALIVE, EMPTY]
]




def prepare_new_board(w=15, h=15, randomly=True):
  """
  Create a new board filled with random values
  >>> prepare_new_board(2, 2, randomly=False)
  [[0, 0], [0, 0]]
  >>> prepare_new_board(3, 3, randomly=False)
  [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
  """
  board = []
  # for i in range(h):
    

  for i in range(h):
    board.append([])
    for j in range(w):
      if randomly:
        cell_value = random.choice([EMPTY, ALIVE])
      else:
        cell_value = EMPTY
      board[i].append(cell_value)
  return board

  # board = []
  return board

def display_board(board):
  """
  displays the board. No tests written because it doesn't return anything
  """
  board_text = get_board_text(board)
  print(board_text)

def get_board_text(board):
  """
  transforms a board into text which can be displayed
  >>> get_board_text([[EMPTY, EMPTY],[EMPTY, EMPTY]])
  '  \\n  \\n'
  """
  LABELS = {0 :  ' ', 1 : '#' }
  board_text = ''
  for row in board:
    board_text += ''.join([LABELS[cell] for cell in row]) + '\n'
  return board_text

def update_board(board):
  """
  updates all cells based on GOL rules:  
  ***      *-*
  ***  ->  ---
  ***      *-*

  -*-      ---
  -*-  ->  ***
  -*-      ---
  TESTS:
  >>> update_board([[EMPTY, EMPTY], [EMPTY, EMPTY]])
  [[0, 0], [0, 0]]
  >>> update_board([[ALIVE, ALIVE], [ALIVE, ALIVE]])
  [[1, 1], [1, 1]]
  >>> update_board([[ALIVE, ALIVE, ALIVE], [ALIVE, ALIVE, ALIVE], [ALIVE, ALIVE, ALIVE]])
  [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
  >>> update_board([[EMPTY, ALIVE, EMPTY], [EMPTY, ALIVE, EMPTY], [EMPTY, ALIVE, EMPTY]])
  [[0, 0, 0], [1, 1, 1], [0, 0, 0]]
  
  """
  new_board = copy.deepcopy(board)
  for (rowNo, row) in enumerate(board):
    for (cellNo, cell) in enumerate(row):
      if neighbours_count(board, rowNo, cellNo) > 3:
        new_board[rowNo][cellNo] = EMPTY
      if neighbours_count(board, rowNo, cellNo) < 2:
        new_board[rowNo][cellNo] = EMPTY
      if neighbours_count(board, rowNo, cellNo) == 3:
        new_board[rowNo][cellNo] = ALIVE
  return new_board

def neighbours_count(board, rowNo, cellNo):
  """
  >>> neighbours_count([\
                        [EMPTY, EMPTY, EMPTY],\
                        [EMPTY, EMPTY, EMPTY],\
                        [EMPTY, EMPTY, EMPTY]], 1, 1)
  0
  >>> neighbours_count([\
                        [EMPTY, ALIVE, EMPTY],\
                        [EMPTY, EMPTY, EMPTY],\
                        [EMPTY, EMPTY, EMPTY]], 1, 1)
  1
  >>> neighbours_count([\
                        [ALIVE, ALIVE, ALIVE],\
                        [ALIVE, EMPTY, ALIVE],\
                        [ALIVE, ALIVE, ALIVE]], 1, 1)
  8
  >>> neighbours_count([\
                        [EMPTY, ALIVE, ALIVE],\
                        [ALIVE, ALIVE, ALIVE],\
                        [ALIVE, ALIVE, ALIVE]], 0, 0)
  3
  >>> neighbours_count([\
                        [ALIVE, ALIVE, ALIVE],\
                        [ALIVE, ALIVE, ALIVE],\
                        [ALIVE, ALIVE, EMPTY]], 2, 2)
  3
  """
  sum = 0
  if rowNo > 0:
    sum += board[rowNo-1][cellNo] # top
  
  if rowNo < len(board) - 1: # ilosc wierszy
    sum += board[rowNo+1][cellNo] # bottom

  if cellNo > 0:
    sum += board[rowNo][cellNo - 1] # left
  
  if cellNo < len(board[rowNo]) - 1: 
    sum += board[rowNo][cellNo + 1] # right

  if rowNo > 0 and cellNo > 0:
    sum += board[rowNo - 1][cellNo - 1] # top left
  
  if rowNo < len(board) - 1 and cellNo < len(board[rowNo]) - 1: 
    sum += board[rowNo + 1][cellNo + 1] # bottom right
  
  if rowNo > 0 and cellNo < len(board[rowNo]) - 1:
    sum += board[rowNo - 1][cellNo + 1] # Top right
  
  if rowNo < len(board) - 1 and cellNo > 0:
    sum += board[rowNo + 1][cellNo - 1] # bottom left
  
  return sum


def main():
  board = prepare_new_board(3, 3)
  # while True:
  display_board(board)
  update_board(board)
    # time.sleep(0.5)


if __name__ == '__main__':
  main()