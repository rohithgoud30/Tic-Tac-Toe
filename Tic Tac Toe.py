def display_board(board):
  print(board[7]+" | "+board[8]+" | "+board[9])
  print("---------")
  print(board[4]+" | "+board[5]+" | "+board[6])
  print("---------")
  print(board[1]+" | "+board[2]+" | "+board[3])

def player_input():
  marker_choice = ""
  while marker_choice not in ["X","O"]:
    marker_choice = input("Player 1 Choose 'X' or 'O' : ").upper()
  if marker_choice == "X":
    return ("X","O")
  else:
    return ("O","X")

from random import randint as r

def player_choice():
  flip = r(0,1)
  if flip == 0:
    return "Player 1"
  else:
    return "Player 2"  
  
def replacement_choice(board,marker,position):
  board[position] = marker

def space_check(board,position):
  return board[position] == " "

def full_check(board):
  for i in range(1,10):
    if space_check(board,i) == True:
      return False
  return True

def position_choice(board):
  position = 0
  while position not in [1,2,3,4,5,6,7,8,9] or space_check(board,position) == False:
    position = int(input("Enter Position Between (1-9) : "))
  return position

def replay():
  choice = input("Do You Want to Replay?? y or n : ")
  return choice == "y"

def win_check(board,mark):
  return ((board[7]== mark and board[8]== mark and board[9]==mark) or
  (board[4]== mark and board[5]== mark and board[6]==mark) or
  (board[1]== mark and board[2]== mark and board[3]==mark) or
  (board[1]== mark and board[4]== mark and board[7]==mark) or
  (board[2]== mark and board[5]== mark and board[8]==mark) or
  (board[3]== mark and board[6]== mark and board[9]==mark) or
  (board[1]== mark and board[5]== mark and board[9]==mark) or
  (board[3]== mark and board[5]== mark and board[7]==mark))

print("Welcome to Tic Tac Toe")
while True:
  the_board = [" "]*10
  player1_marker,player2_marker = player_input()
  turn = player_choice()
  print(turn + " will play first")
  play_game = input('Are you ready to play? Enter y or n : ')
  if play_game.lower()[0] == 'y':
      game_on = True
  else:
      game_on = False
  while game_on:
    if turn == "Player 1":
      display_board(the_board)
      position = position_choice(the_board)
      replacement_choice(the_board,player1_marker,position)
      if win_check(the_board,player1_marker) == True:
        print("Palyer1 Won the Game")
        game_on = False
      else:
        if full_check(the_board):
          print("Game is Tie !!!")
          break
        else:
          turn = "Player 2"
    else:
      display_board(the_board)
      position = position_choice(the_board)
      replacement_choice(the_board,player2_marker,position)
      if win_check(the_board,player2_marker) == True:
        print("Player 2 Won the Game")
        game_on = False
      else:
        if full_check(the_board):
          print("Game is Tie !!!")
          break
        else:
          turn = "Player 1"
  if not replay():
    break 