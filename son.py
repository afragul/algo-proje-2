import string 
player1 = input('Please enter a letter to represent player 1 (except O): ')
while player1=='O' or not (player1 in string.ascii_letters):
    print('invalid data try again')
    player1=input('Please enter a letter to represent player 1:')

player2 = input('Please enter a letter to represent player 2 (except O): ')
while player2=='O' or not (player2 in string.ascii_letters) or player1==player2:
    print('invalid data try again')
    player2=input('Please enter a letter again to represent player 2: ')
player2=player2.upper()
player1=player1.upper()

boardsize =int(input('Enter the row/column number of the playing field (3, 5, 7): '))
while not boardsize in (3,5,7):
    boardsize =int(input('Please enter 3, 5 or 7 for the row/column number of the playing field: '))

if boardsize==3:
    game_board = [' ' for x in range(10)]
elif boardsize==5:
    game_board = [' ' for x in range(26)]
else:
    game_board = [' ' for x in range(50)]

def board(game_board,boardsize):
    if boardsize==3:
        print('   A   B   C')
        print('  -----------')
        print('1|' +' '+game_board[1]+' '+'|'+' '+game_board[2]+' '+'|'+' '+game_board[3]+' '+'|')
        print('  -----------')
        print('2|' +' '+game_board[4]+' '+'|'+' '+game_board[5]+' '+'|'+' '+game_board[6]+' '+'|')
        print('  -----------')
        print('3|' +' '+game_board[7]+' '+'|'+' '+game_board[8]+' '+'|'+' '+game_board[9]+' '+'|')
    elif boardsize ==5:
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
    else:
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

start_point_1 = boardsize**2 -(boardsize//2)
start_point_2 = (boardsize//2)+1

def move_small(boardsize):
    user_input =input('konum: ')
    hareket=int(konum(user_input,boardsize))
    game_board[hareket] = 'O'
    return board(game_board,boardsize)

def yonler(start,user_input,board_size):
    start_position = start
    if user_input =='N':
        end_position = start_position-board_size
    elif user_input=='S':
        end_position = start_position+board_size
    elif user_input=='E':
        end_position = start_position+1
    elif user_input=='W':
        end_position = start_position-1
    count_doluluk=1
    try:
        while game_board[end_position] != ' ':
            again=input('dolu:')
            count_doluluk+=1
            yonler(start_position,again,board_size)
            if count_doluluk==8:
                print('kaybettiniz :(')
                break

    except IndexError:
        print('taşı oraya götüremezsiniz ')
        again=input('TEKRAR:')
        yonler(start_position,again,board_size)
    return end_position

count=0
game_board[start_point_1]=player1
game_board[start_point_2]=player2
board(game_board,boardsize)
game_board[start_point_1]=' '
game_board[start_point_2]=' '

while True:
    if count % 2==0:
        user_input =input(f'Player {player1}, please enter the direction you want to move your own big stone (N, S, E, W, NE, NW, SE, SW): ')
        hareket1=int(yonler(start_point_1,user_input,boardsize))
        game_board[hareket1] = player1
        board(game_board,boardsize)
        move_small(boardsize)
    else:
       user_input =input(f'Player {player2}, please enter the direction you want to move your own big stone (N, S, E, W, NE, NW, SE, SW): ')
       hareket2=int(yonler(start_point_2,user_input,boardsize))
       game_board[hareket2] = player2
       board(game_board,boardsize)
       move_small(boardsize)
    count+=1
    if count % 2==0:
        start_point_1=hareket1
        game_board[start_point_1]=' '
    elif count == 1:
        pass
    else:
        start_point_2=hareket2
        game_board[start_point_2]=' '
    