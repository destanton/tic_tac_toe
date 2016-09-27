import sys
import os


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

board_game_global = [[" ", " ", " "],
              [" ", " ", " "],
              [" ", " ", " "]]


def board_print(board):
    clear()
    print(" 0   1   2")
    print("0  " + board[0][0] + "|" + board[0][1] + " |" + board[0][2])
    print("  --+--+--")
    print("1  " + board[1][0] + "|" + board[1][1] + " |" + board[1][2])
    print("  --+--+--")
    print("2  " + board[2][0] + "|" + board[2][1] + " |" + board[2][2])


def turns(player_1, board_game):
    row, column = input("\nwhere do you want to move? \n*enter input as NUMBER space NUMBER: \n").split(" ")
    row, column = int(row), int(column)
    if board_game[row][column] == "X" or board_game[row][column] == "O":
        print("That spot's already taken")
        row, column = input("Guess again! ").split(" ")
        row, column = int(row), int(column)
    board_game[row][column] = player_1  # MAGIC
    return win_condition(player_1, board_game)


def win_condition(player_1, board_game):
    winner = [player_1, player_1, player_1]
    column_0 = [row[0] for row in board_game]
    column_1 = [row[1] for row in board_game]
    column_2 = [row[2] for row in board_game]
    if board_game[0] == winner or board_game[1] == winner or board_game[2] == winner or column_0 == winner or column_1 == winner or column_2 == winner:
        print("You win! {}".format(player_1))
        return replay(board_game)
    else:
        return board_game


def replay(board_game):
    play_again = input("would you like to play again? Y/n ").lower()
    if play_again != "n":
        return clear_board(board_game)
    else:
        print("Bye!")
        sys.exit()


def clear_board(board_game):
    board_game = [[" ", " ", " "],
                  [" ", " ", " "],
                  [" ", " ", " "]]
    return board_game


player_1 = "X"
while True:
    board_print(board_game_global)
    board_game_global = turns(player_1, board_game_global)
    if player_1 == "X":
        player_1 = "O"
    else:
        player_1 = "X"
