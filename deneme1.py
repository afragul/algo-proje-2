
game_board = [' ' for x in range(50)]

def board3(game_board):
    print('   A   B   C')
    print('  -----------')
    print('1|' +' '+game_board[1]+' '+'|'+' '+game_board[2]+' '+'|'+' '+game_board[3]+' '+'|')
    print('  -----------')
    print('2|' +' '+game_board[4]+' '+'|'+' '+game_board[5]+' '+'|'+' '+game_board[6]+' '+'|')
    print('  -----------')
    print('3|' +' '+game_board[7]+' '+'|'+' '+game_board[8]+' '+'|'+' '+game_board[9]+' '+'|')

def board5(game_board):
    print('   A   B   C   D   E')
    print('  -------------------')
    print('1|' +' '+game_board[1]+' '+'|'+' '+game_board[2]+' '+'|'+' '+game_board[3]+' '+'|'+' '+game_board[4]+' '+'|'+' '+game_board[5]+' '+'|')
    print('  -------------------')
    print('2|' +' '+game_board[6]+' '+'|'+' '+game_board[7]+' '+'|'+' '+game_board[8]+' '+'|'+' '+game_board[9]+' '+'|'+' '+game_board[10]+' '+'|')
    print('  -------------------')
    print('3|' +' '+game_board[11]+' '+'|'+' '+game_board[12]+' '+'|'+' '+game_board[13]+' '+'|'+' '+game_board[14]+' '+'|'+' '+game_board[15]+' '+'|')
    print('  -------------------')
    print('4|' +' '+game_board[16]+' '+'|'+' '+game_board[17]+' '+'|'+' '+game_board[18]+' '+'|'+' '+game_board[19]+' '+'|'+' '+game_board[20]+' '+'|')
    print('  -------------------')
    print('5|' +' '+game_board[21]+' '+'|'+' '+game_board[22]+' '+'|'+' '+game_board[23]+' '+'|'+' '+game_board[24]+' '+'|'+' '+game_board[25]+' '+'|')
    print('  -------------------')


def board7(game_board):
    print('   A   B   C   D   E   F   G')
    print('  ---------------------------')
    print('1|' +' '+game_board[1]+' '+'|'+' '+game_board[2]+' '+'|'+' '+game_board[3]+' '+'|'+' '+game_board[4]+' '+'|'+' '+game_board[5]+' '+'|'+' '+game_board[6]+' '+'|'+' '+game_board[7]+' '+'|')
    print('  ---------------------------')
    print('2|' +' '+game_board[8]+' '+'|'+' '+game_board[9]+' '+'|'+' '+game_board[10]+' '+'|'+' '+game_board[11]+' '+'|'+' '+game_board[12]+' '+'|'+' '+game_board[13]+' '+'|'+' '+game_board[14]+' '+'|')
    print('  ---------------------------')
    print('3|' +' '+game_board[15]+' '+'|'+' '+game_board[16]+' '+'|'+' '+game_board[17]+' '+'|'+' '+game_board[18]+' '+'|'+' '+game_board[19]+' '+'|'+' '+game_board[20]+' '+'|'+' '+game_board[21]+' '+'|')
    print('  ---------------------------')
    print('4|' +' '+game_board[22]+' '+'|'+' '+game_board[23]+' '+'|'+' '+game_board[24]+' '+'|'+' '+game_board[25]+' '+'|'+' '+game_board[26]+' '+'|'+' '+game_board[27]+' '+'|'+' '+game_board[28]+' '+'|')
    print('  ---------------------------')
    print('5|' +' '+game_board[29]+' '+'|'+' '+game_board[30]+' '+'|'+' '+game_board[31]+' '+'|'+' '+game_board[32]+' '+'|'+' '+game_board[33]+' '+'|'+' '+game_board[34]+' '+'|'+' '+game_board[35]+' '+'|')
    print('  ---------------------------')
    print('6|' +' '+game_board[36]+' '+'|'+' '+game_board[37]+' '+'|'+' '+game_board[38]+' '+'|'+' '+game_board[39]+' '+'|'+' '+game_board[40]+' '+'|'+' '+game_board[41]+' '+'|'+' '+game_board[42]+' '+'|')
    print('  ---------------------------')
    print('7|' +' '+game_board[43]+' '+'|'+' '+game_board[44]+' '+'|'+' '+game_board[45]+' '+'|'+' '+game_board[46]+' '+'|'+' '+game_board[47]+' '+'|'+' '+game_board[48]+' '+'|'+' '+game_board[49]+' '+'|')
    print('  ---------------------------')

def konum(user_input,board_size):
    column_letter = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7}
    row_num = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7}
    row=user_input[1]
    column =user_input[0].upper()
    return row_num[row]*board_size-(board_size-column_letter[column])

player1 = input('Please enter a capital letter to represent player 1 (except O): ')

boardsize =int(input('Enter the row/column number of the playing field (3, 5, 7): '))
while not boardsize in (3,5,7):
    boardsize =int(input('Please enter 3, 5 or 7 for the row/column number of the playing field: '))

def move(boardsize):
    if boardsize==3:
        user_input =input('konum: ')
        hareket=int(konum(user_input,boardsize))
        game_board[hareket] = player1
        return board3(game_board)
    elif boardsize==5:
        user_input =input('konum: ')
        hareket=int(konum(user_input,boardsize))
        game_board[hareket] = player1
        return board5(game_board)
    else:
        user_input =input('konum: ')
        hareket=int(konum(user_input,boardsize))
        game_board[hareket] = player1
        return board7(game_board)
for i in range(10):
    move(boardsize)
    

def empty_control(konum):
    return game_board[konum] == ' '      # True dönerse boş ,false sa dolu


#player1 = input('Please enter a capital letter to represent player 1 (except O): ')
#player2 = input('Please enter a capital letter to represent player 2 (except O): ')
#
#if board_choice=='3':
#    show3()
#    motion_choice = input(f'Player {player1}, please enter the direction you want to move your own big stone (N, S, E, W, NE, NW, SE, SW): ')
#    motion(player1,motion_choice)
#elif board_choice=='5':
#    show5()
#elif board_choice=='7':
#    show7()
#    

