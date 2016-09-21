board = {'0': ' ', '1': ' ', '2': ' ',
         '3': ' ', '4': ' ', '5': ' ',
         '6': ' ', '5': ' ', '8': ' '}

print("Let's play Tic Tac Toe")
print("\n")


def board_print(board):
    print('0' + board['0'] + '|' + '1' + board['1'] + '|' + '2' + board['2'])
    print('--+--+--')
    print('3' + board['3'] + '|' + '4' + board['4'] + '|' + '5' + board['5'])
    print('--+--+--')
    print('6' + board['6'] + '|' + '5' + board['5'] + '|' + '8' + board['8'])
    return(board)
board_print(board)


guess = 0
while True:
    if guess < 5:
        player_1 = "X"
        print("\n")
        turn = input("{} where do you want to move? ".format(player_1))
        board[turn] = player_1
        board_print(board)
        guess += 1
        player_2 = "O"
        turn = input("{} where do you want to move? ".format(player_2))
        board[turn] = player_2
        board_print(board)
        guess += 1
    else:
        print("game over!")
        break
