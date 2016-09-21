# Create matrix with Pattern and numbers
#
# create ability to take a turn (loop)
# 	player 1 (x) takes a turn
# 	is it a good guess, is it a bad guess
# 	matrix updates with guess
# 	check to see if there’s a winner
#
# 	player 2 (o) takes a turn
# 	is it a good guess, is it a bad guess
# 	matrix updates with guess
# 	check to see if there’s a winner
#
# possible moves: 0,0 0,1, 0,2
# 			  1,0 1,1 1,2
# 			  2,0 2,1 2,2

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
    row, column = input("where do you want to move? ").split(" ")
    row, column = int(row), int(column)
    board_game[row][column] = player_1  # MAGIC

    while True:
        if player_1 == "X":
            player_1 = "O"

        else:
            player_1 = "X"
        turns(player_1)
        # (board_print(board_game))

turns(player_1)
#
# if row, column of board_game == "x" or "o"
# then print("that spot's already taken ")
