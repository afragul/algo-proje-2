
tahtamatrix= [
    ['1','1','1'],
    ['1','1','1'],
    ['1','1','1']
]
def board3(game_board):
    print('   A   B   C')
    print('  -----------')
    print('1|' +' '+game_board[0][0]+' '+'|'+' '+game_board[0][1]+' '+'|'+' '+game_board[0][2]+' '+'|')
    print('  -----------')
    print('2|' +' '+game_board[1][0]+' '+'|'+' '+game_board[1][1]+' '+'|'+' '+game_board[1][2]+' '+'|')
    print('  -----------')
    print('3|' +' '+game_board[2][0]+' '+'|'+' '+game_board[2][1]+' '+'|'+' '+game_board[2][2]+' '+'|')

board3(tahtamatrix)