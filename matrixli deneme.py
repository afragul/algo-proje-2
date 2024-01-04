import string 

first_player=input('1. oyuncu tas secin: ')
while first_player=='O' or not (first_player in string.ascii_letters):
    print('invalid data try again')
    first_player=input('1. oyuncu tas secin: ')

second_player= input('2. oyuncu tas secin: ')
while second_player=='O' or not (second_player in string.ascii_letters) or first_player==second_player:
    print('invalid data try again')
    second_player=input('2, oyuncu tas secin: ')
second_player=second_player.upper()
first_player=first_player.upper()

istek=int(input('tahta secin: '))
gameboard= [ [' ',' ',' ',' ',' ',' ',' ']]*7

def board3(gameboard):
    print('   A   B   C')
    print('  -----------')
    print('1|' +' '+gameboard[0][0]+' '+'|'+' '+gameboard[0][1]+' '+'|'+' '+gameboard[0][2]+' '+'|')
    print('  -----------')
    print('2|' +' '+gameboard[1][0]+' '+'|'+' '+gameboard[1][1]+' '+'|'+' '+gameboard[1][2]+' '+'|')
    print('  -----------')
    print('3|' +' '+gameboard[2][0]+' '+'|'+' '+gameboard[2][1]+' '+'|'+' '+gameboard[2][2]+' '+'|')

def board5(game_board):
    print('   A   B   C   D   E')
    print('  -------------------')
    print('1|' +' '+game_board[0][0]+' '+'|'+' '+game_board[0][1]+' '+'|'+' '+game_board[0][2]+' '+'|'+' '+game_board[0][3]+' '+'|'+' '+game_board[0][4]+' '+'|')
    print('  -------------------')
    print('2|' +' '+game_board[1][0]+' '+'|'+' '+game_board[1][1]+' '+'|'+' '+game_board[1][2]+' '+'|'+' '+game_board[1][3]+' '+'|'+' '+game_board[1][4]+' '+'|')
    print('  -------------------')
    print('3|' +' '+game_board[2][0]+' '+'|'+' '+game_board[2][1]+' '+'|'+' '+game_board[2][2]+' '+'|'+' '+game_board[2][3]+' '+'|'+' '+game_board[2][4]+' '+'|')
    print('  -------------------')
    print('4|' +' '+game_board[3][0]+' '+'|'+' '+game_board[3][1]+' '+'|'+' '+game_board[3][2]+' '+'|'+' '+game_board[3][3]+' '+'|'+' '+game_board[3][4]+' '+'|')
    print('  -------------------')
    print('5|' +' '+game_board[4][0]+' '+'|'+' '+game_board[4][1]+' '+'|'+' '+game_board[4][2]+' '+'|'+' '+game_board[4][3]+' '+'|'+' '+game_board[4][4]+' '+'|')
    print('  -------------------')

def board7(game_board):
    print('   A   B   C   D   E   F   G')
    print('  ---------------------------')
    print('1|' +' '+game_board[0][0]+' '+'|'+' '+game_board[0][1]+' '+'|'+' '+game_board[0][2]+' '+'|'+' '+game_board[0][3]+' '+'|'+' '+game_board[0][4]+' '+'|'+' '+game_board[0][5]+' '+'|'+' '+game_board[0][6]+' '+'|')
    print('  ---------------------------')
    print('2|' +' '+game_board[1][0]+' '+'|'+' '+game_board[1][1]+' '+'|'+' '+game_board[1][2]+' '+'|'+' '+game_board[1][3]+' '+'|'+' '+game_board[1][4]+' '+'|'+' '+game_board[1][5]+' '+'|'+' '+game_board[1][6]+' '+'|')
    print('  ---------------------------')
    print('3|' +' '+game_board[2][0]+' '+'|'+' '+game_board[2][1]+' '+'|'+' '+game_board[2][2]+' '+'|'+' '+game_board[2][3]+' '+'|'+' '+game_board[2][4]+' '+'|'+' '+game_board[2][5]+' '+'|'+' '+game_board[2][6]+' '+'|')
    print('  ---------------------------')
    print('4|' +' '+game_board[3][0]+' '+'|'+' '+game_board[3][1]+' '+'|'+' '+game_board[3][2]+' '+'|'+' '+game_board[3][3]+' '+'|'+' '+game_board[3][4]+' '+'|'+' '+game_board[3][5]+' '+'|'+' '+game_board[3][6]+' '+'|')
    print('  ---------------------------')
    print('5|' +' '+game_board[4][0]+' '+'|'+' '+game_board[4][1]+' '+'|'+' '+game_board[4][2]+' '+'|'+' '+game_board[4][3]+' '+'|'+' '+game_board[4][4]+' '+'|'+' '+game_board[4][5]+' '+'|'+' '+game_board[4][6]+' '+'|')
    print('  ---------------------------')
    print('6|' +' '+game_board[5][0]+' '+'|'+' '+game_board[5][1]+' '+'|'+' '+game_board[5][2]+' '+'|'+' '+game_board[5][3]+' '+'|'+' '+game_board[5][4]+' '+'|'+' '+game_board[5][5]+' '+'|'+' '+game_board[5][6]+' '+'|')
    print('  ---------------------------')
    print('7|' +' '+game_board[6][0]+' '+'|'+' '+game_board[6][1]+' '+'|'+' '+game_board[6][2]+' '+'|'+' '+game_board[6][3]+' '+'|'+' '+game_board[6][4]+' '+'|'+' '+game_board[6][5]+' '+'|'+' '+game_board[6][6]+' '+'|')
    print('  ---------------------------')

if istek==3:
    eski_konum1=[0,1]
    eski_konum2=[2,1]
    first_player = gameboard[eski_konum1[0]][eski_konum1[1]]
    board3(gameboard)

elif istek==5:
    board5(gameboard)
    eski_konum1=(0,2)
    eski_konum2=(4,2)

elif istek==7:
    board7(gameboard)
    eski_konum1=(0,3)
    eski_konum2=(6,3)

def yenikonum(board,eski,player):
    yon=input('yön seçin: ')
    if yon=='S':
        yeni_konum=(eski[0]+1,eski[1])
        player = board[eski[0]][eski[1]]
        board[eski[0]][eski[1]] = ' '
        board[yeni_konum[0]][yeni_konum[1]] = player
    return board[yeni_konum]

first_player = gameboard[eski_konum1[0]][eski_konum1[1]]

yenikonum((gameboard), eski_konum1 , first_player)

print(eski_konum1)
print(board3(gameboard))
