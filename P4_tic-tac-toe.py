print('Hello Shiva baba my world')

board = [' ' for i in range(0,10)]

def insertLetter(letter,pos):
    board[pos]= letter

def isFreeSpace(pos):
    return board[pos] == ' '   #returns true or false

def printBoard():
    print('   |   |   ')
    print(f' {board[1]} | {board[2]} | {board[3]}')
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(f' {board[4]} | {board[5]} | {board[6]}')
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(f' {board[7]} | {board[8]} | {board[8]}')
    print('   |   |   ')

def isBoardFull(board):
    if board.count(' ')>1:
        return True
    else:
        return False

def isWinner(b,l):
    return (b[1] == l and b[2] == l and b[3] == l)

def playerMove():
    run = True
    while run:
        move = input('please enter a position to insert X between 1 and 10: ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if isFreeSpace(move):
                    run = False
                    insertLetter('X',move)
                else:
                    print('Sry the space is already occupied')
            else:
                print('Please type a number between 1 and 9')

        except:
            print('please enter a number')










printBoard()
# #main   this all is in a loop
# print('this is.....')
# print('print board')
# playermove = input('enter position')
# print('update board acc to player')
# print('update board acc to comp and print')