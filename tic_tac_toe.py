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

board_print(board_game)


while True:
    player_1 = "X"
    print("\n")
    turn = input("{} where do you want to move? ".format(player_1))
    # need to choose row and column to move
    for row in board_game:
        for column in row:
            board_game.append(player_1)
        print(board_game)
    # board[turn] = player_1
    board_print(board_game)
    player_2 = "O"
    turn = input("{} where do you want to move? ".format(player_2))
    # board[turn] = player_2
    board_print(board_game)


# def game():
#     game_board = print_board
#     print(game_board)
    # for row in matrix:
    #     for column in row:
    #         print(column)
    #     return(row, column)

# print(row, column())
# game()
