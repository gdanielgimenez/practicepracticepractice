# tic tac toe example from the book - doesn't check who wins
# doesn't have a way to quit
# building the board
board = {'tl': ' ', 'tm': ' ', 'tr': ' ',
         'ml': ' ', 'mm': ' ', 'mr': ' ',
         'll': ' ', 'lm': ' ', 'lr': ' ', }
# printing the board


def print_board(board):
    print(board['tl']+"|"+board['tm']+"|"+board['tr'])
    print('-+-+-')
    print(board['ml']+"|"+board['mm']+"|"+board['mr'])
    print('-+-+-')
    print(board['ll']+"|"+board['lm']+"|"+board['lr'])


# function call to print the board
# print_board(board)
turn = "X"
for i in range(9):
    print_board(board)
    print('Turn for ' + turn + 'Move on which space? ')
    move = input()
    board[move] = turn
    if turn == 'X':
        turn = "O"
    else:
        turn = "X"
print_board(board)
