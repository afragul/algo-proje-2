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

istek=int(input())
tahtamatrix= [ [' ',' ',' ',' ',' ',' ',' ']]*7

def board3(game_board):
    print('   A   B   C')
    print('  -----------')
    print('1|' +' '+game_board[0][0]+' '+'|'+' '+game_board[0][1]+' '+'|'+' '+game_board[0][2]+' '+'|')
    print('  -----------')
    print('2|' +' '+game_board[1][0]+' '+'|'+' '+game_board[1][1]+' '+'|'+' '+game_board[1][2]+' '+'|')
    print('  -----------')
    print('3|' +' '+game_board[2][0]+' '+'|'+' '+game_board[2][1]+' '+'|'+' '+game_board[2][2]+' '+'|')

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
    board3(tahtamatrix)
    eski_konum1=tahtamatrix[0][1]
    eski_konum2=tahtamatrix[2][1]

elif istek==5:
    board5(tahtamatrix)
    eski_konum1=tahtamatrix[0][2]
    eski_konum2=tahtamatrix[4][1]

elif istek==7:
    board7(tahtamatrix)
    eski_konum1=tahtamatrix[0][3]
    eski_konum2=tahtamatrix[6][1]

column_letter = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6}
row_num = {'1':0, '2':1, '3':2, '4':3, '5':4, '6':5, '7':6}

def yon(konum_yonu,eski_konum):
    global izin
    global yeni_konum
    if konum_yonu=='N':
        if eski_konum[+0][+1]==' ':
            izin=True
            yeni_konum=eski_konum[+0][+1]

    elif konum_yonu=='S':
        if eski_konum[+1][+0]==' ':
            izin=True
            yeni_konum=eski_konum[+1][+0]
    
    elif konum_yonu=='W':
        if eski_konum[-1][+0]==' ':
            izin=True
            yeni_konum=eski_konum[-1][+0]
    
    elif konum_yonu=='E':
        if eski_konum[+0][-1]==' ':
            izin=True
            yeni_konum=eski_konum[+0][-1]
    
    elif konum_yonu=='NW':
        if eski_konum[-1][+1]==' ':
            izin=True
            yeni_konum=eski_konum[-1][+1]
    
    elif konum_yonu=='NE':
        if eski_konum[+1][+1]==' ':
            izin=True
            yeni_konum=eski_konum[+1][+1]
    
    elif konum_yonu=='SE':
        if eski_konum[+1][-1]==' ':
            izin=True
            yeni_konum=eski_konum[+1][-1]
    
    elif konum_yonu=='SW':
        if eski_konum[-1][-1]==' ':
            izin=True
            yeni_konum=eski_konum[-1][-1]

    return yeni_konum, izin


def konum(user_input, board_size):
    pass
    # column_letter = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7}
    # row_num = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7}
    # row=user_input[1]
    # column =user_input[0].upper()
    # return row_num[row]*board_size-(board_size-column_letter[column])

for i in range(10):
     #8 false tan asonra cilimali
    istenen_konum1= input('gitmek istediginiz yönü yazin: ')
    yon(istenen_konum1,eski_konum1)
    eski_konum1=yeni_konum

    istenen_konum2= input('gitmek istediginiz yönü yazin: ')
    yon(istenen_konum2,eski_konum2)
    eski_konum2=yeni_konum

