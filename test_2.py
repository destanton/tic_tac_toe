
board_game = [[" ", " ", " "],
              [" ", " ", " "],
              [" ", " ", " "]]

            # 0,0 0,1, 0,2
# 			  1,0 1,1 1,2
# 			  2,0 2,1 2,2
def board_print(board):
    print(" 0   1   2")
    print("0  " + board[0][0] + "|" + board[0][1] + " |" + board[0][2])
    print("  --+--+--")
    print("1  " + board[1][0] + "|" + board[1][1] + " |" + board[1][2])
    print("  --+--+--")
    print("2  " + board[2][0] + "|" + board[2][1] + " |" + board[2][2])

board_print(board_game)
#


# def game():
#     game_board = print_board
#     print(game_board)
    # for row in matrix:
    #     for column in row:
    #         print(column)
    #     return(row, column)

# print(row, column())
# game()