# adapting the book's version of a tic tac toe game

# building the board
board = {'tl': ' ', 'tm': ' ', 'tr': ' ',
         'ml': ' ', 'mm': ' ', 'mr': ' ',
         'll': ' ', 'lm': ' ', 'lr': ' ', }

# function that prints the board


def print_board(board):
    print(board['tl']+"|"+board['tm']+"|"+board['tr'])
    print('-+-+-')
    print(board['ml']+"|"+board['mm']+"|"+board['mr'])
    print('-+-+-')
    print(board['ll']+"|"+board['lm']+"|"+board['lr'])
# function to check victory


def victory_check(board):
    if board['tl'] == board['tm'] and board['tm'] == board['tr'] and board['tl'] != ' ' or board['tm'] != ' ' or board['tr'] != ' ':
        print(f"{turn} wins! top row victory")
        return True
    elif board['ml'] == board['mm'] and board['mm'] == board['mr'] and board['ml'] != ' ' or board['mm'] != ' ' or board['mr'] != ' ':
        print(f"{turn} wins! mid row victory")
        return True
    elif board['ll'] == board['lm'] and board['lm'] == board['lr'] and board['ll'] != ' ' or board['lm'] != ' ' or board['lr'] != ' ':
        print(f"{turn} wins! low row victory")
        return True
    elif board['tl'] == board['ml'] and board['ml'] == board['ll'] and board['tl'] != ' ' or board['ml'] != ' ' or board['ll'] != ' ':
        print(f"{turn} wins! left column victory")
        return True
    elif board['tm'] == board['mm'] and board['mm'] == board['lm'] and board['tm'] != ' ' or board['mm'] != ' ' or board['lm'] != ' ':
        print(f"{turn} wins! middle column victory")
        return True
    elif board['tr'] == board['mr'] and board['mr'] == board['lr'] and board['tr'] != ' ' or board['mr'] != ' ' or board['lr'] != ' ':
        print(f"{turn} wins! right column victory")
        return True
    elif board['tl'] == board['mm'] and board['mm'] == board['lr'] and board['tl'] != ' ' or board['mm'] != ' ' or board['lr'] != ' ':
        print(f"{turn} wins! diagonal left victory")
        return True
    elif board['tr'] == board['mm'] and board['mm'] == board['ll'] and board['tr'] != ' ' or board['mm'] != ' ' or board['ll'] != ' ':
        print(f"{turn} wins! diagonal right victory")
        return True
    else:
        return False


# add a flag to quit the game
game_over = False
turn = "X"
while game_over != True:
    print_board(board)
    print('Turn for ' + turn + ' Move on which space? ')
    move = input()
    board[move] = turn
    if turn == 'X':
        turn = "O"
    else:
        turn = "X"
     # check for victory:
    victory = victory_check(board)
    if victory == True:
        game_over = True

print_board(board)
