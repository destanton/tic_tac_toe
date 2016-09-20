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


# board = [["_", "_", "_"],
#          ["_", "_", "_"],
#          ["_", "_", "_"]]

# used idea for board from dictionary section of book
board = {'0': ' ', '3': ' ', '6': ' ',
         '1': ' ', '4': ' ', '7': ' ',
         '2': ' ', '5': ' ', '8': ' '}


def board_print(board):
    print('0' + board['0'] + '|' + '3' + board['3'] + '|' + '6' + board['6'])
    print('--+--+--')
    print('1' + board['1'] + '|' + '4' + board['4'] + '|' + '7' + board['7'])
    print('--+--+--')
    print('2' + board['2'] + '|' + '5' + board['5'] + '|' + '8' + board['8'])
    return(board)
board_print(board)

print("Let's play Tic Tac Toe")


while True:
    player_1 = "X"
    turn = input("where do you want to move?")
    board[turn] = player_1
    board_print(board)
