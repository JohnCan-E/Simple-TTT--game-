# simple Tic tac toe
def make_board(board):
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])

def play_game():
    board=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ' ]
    current_player='X'
    game_over= False

    while game_over:
        make_board(board)
        position=int(input('Pls, pick a position from 1-9:  '))
        if board[position]==' ':
            board[position]=current_player
            if current_player=='X':
                current_player='O'
            else:
                current_player='O'

        else:
            print('Sorry! This position has already been occupied')

        if board[1]==board[2]==board[3]!=' '  or \
            board[4] == board[5] == board[6] != ' ' or\
            board[7] == board[8] == board[9] != ' '  or\
            board[1] == board[5] == board[9] != ' '  or\
            board[3] == board[5] == board[7] != ' '  or\
            board[1] == board[4] == board[7] != ' ' or\
            board[2] == board[5] == board[8] != ' '  or\
            board[3] == board[6] == board[9] != ' ':
                make_board()

                print(current_player + 'WINS!')
                game_over=True

        if '' not in board:
            make_board(board)
            print('The game is a tie!')
            game_over=True

