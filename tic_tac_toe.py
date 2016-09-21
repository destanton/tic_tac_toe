import sys

board_game = [[" ", " ", " "],
              [" ", " ", " "],
              [" ", " ", " "]]


def board_print(board):
    print(" 0   1   2")
    print("0  " + board[0][0] + "|" + board[0][1] + " |" + board[0][2])
    print("  --+--+--")
    print("1  " + board[1][0] + "|" + board[1][1] + " |" + board[1][2])
    print("  --+--+--")
    print("2  " + board[2][0] + "|" + board[2][1] + " |" + board[2][2])

# board_print(board_game)
player_1 = "X"


def turns(player_1):
    board_print(board_game)
    row, column = input("where do you want to move? \n*enter input as number space number: ").split(" ")
    row, column = int(row), int(column)
    if board_game[row][column] == "X" or board_game[row][column] == "O":
        print("that spot's already taken")
    else:
        board_game[row][column] = player_1  # MAGIC
        win_condition(player_1, turns)
    while True:
        if player_1 == "X":
            player_1 = "O"

        else:
            player_1 = "X"
        turns(player_1)
        # (board_print(board_game))


def win_condition(player_1, turns):
    winner = [player_1, player_1, player_1]
    column_0 = [row[0] for row in board_game]
    column_1 = [row[1] for row in board_game]
    column_2 = [row[2] for row in board_game]
    # print(winner)
    # while True:
    if board_game[0] == winner or board_game[1] == winner or board_game[2] == winner:
        print("You win!")
        replay()
    elif column_0 == winner or column_1 == winner or column_2 == winner:
        print("You win!")
        replay()
    else:
        pass


def replay():
    play_again = input("would you like to play again? Y/n ")
    if play_again != "n":
        turns(player_1)
    else:
        print("Bye!")
        sys.exit()


turns(player_1)
