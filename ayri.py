import string 
def stone_type():
    stone=(input('tas secin: '))

    while stone=='O' or not (stone in string.ascii_letters):
        print('invalid data try again')
        stone=input('tas secin: ')
    return stone 

stone_type()

choice=int(input('tahta secin (3,5,7): '))
while not choice in [3,5,7]:
    print('invalid data try again') 
    choice=int(input('tahta secin (3,5,7): '))

def display_board(choice):
    """display the board"""
    list=['A','B','C','D','E','F','G']
    
    for harf in range(choice):
        print('  ' , list[harf] , end='')
    print( ' ')
    
    for x in range(choice):
        print("----"*choice +'--')
        print(x+1 , end=' ')
        for y in range(choice):
            print("|", ' ', end = " ")
        print("|")
    print("----"*choice +'--')
    
    for harf2 in range(choice):
        print('  ' , list[harf2] , end='')

display_board(choice)