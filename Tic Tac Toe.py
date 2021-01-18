def display_board(board):
  print(board[7]+" | "+board[8]+" | "+board[9])
  print("-"*9)
  print(board[4]+" | "+board[5]+" | "+board[6])
  print("-"*9)
  print(board[1]+" | "+board[2]+" | "+board[3])

def player_input():
  marker_choice = " "
  while marker_choice not in ["X","O"]:
    marker_choice = input("Player 1 choose the marker X or O : ").upper()
  if marker_choice == "X":
    return ("X","O")
  else:
    return ("O","X")

def player_marker(board,marker,position):
  board[position] = marker

from random import randint as r
def choose_first():
  flip = r(0,1)
  if flip == 0:
    return "Player 1"
  else:
    return "Player 2"

def win_check(board,marker):
  return ((board[7]==marker and board[5]==marker and board[3]==marker) or
  (board[7]==marker and board[8]==marker and board[9]==marker) or
  (board[4]==marker and board[5]==marker and board[6]==marker) or 
  (board[1]==marker and board[2]==marker and board[3]==marker) or 
  (board[7]==marker and board[4]==marker and board[1]==marker) or 
  (board[8]==marker and board[5]==marker and board[2]==marker) or 
  (board[9]==marker and board[6]==marker and board[3]==marker) or 
  (board[1]==marker and board[5]==marker and board[9]==marker))

def space_check(board,position):
  return board[position] == " "

def position_choice(board):
  position = 0
  while position not in range(1,10) or not space_check(board,position):
    position = int(input("Enter the postion (1-9) : "))
  return position

def full_board_check(board):
  for i in range(1,10):
    if space_check(board,i) == True:
      return False
  return True

def replay():
  choice = " "
  while choice not in ["Y","N"]:
    choice = input("Do you want to continue Y or N : ").upper()
  return choice == "Y"

while True:
  print("Welcome to Tic Tac Toe")
  the_board = [" "]*10
  player1_marker, player2_marker = player_input()
  turn = choose_first()
  print(turn + " will Play First ")
  play_game = input("Ready to Play Y or N : ").upper()
  if play_game == "Y" :
    game_on = True
  else: 
    game_on = False
  while game_on:
    if turn == "Player 1":
      display_board(the_board)
      position = position_choice(the_board)
      player_marker(the_board,player1_marker,position)
      if win_check(the_board,player1_marker):
        print("Player 1 Won the Game!!")
        game_on = False
      else:
        if full_board_check(the_board):
          print("Game is Draw!!")
          break
        else:
          turn = "Player 2"
    else:
      display_board(the_board)
      position = position_choice(the_board)
      player_marker(the_board,player2_marker,position)
      if win_check(the_board,player2_marker):
        print("Player 2 Won the Game!!")
        game_on = False
      else:
        if full_board_check(the_board):
          print("Game is Draw!!")
          break
        else:
          turn = "Player 1"
  if not replay():
    break  
