from random import randrange

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    for i in range(3):
        print(3*('+'+8*'-')+'+')
        print(3*('|'+8*' ')+'|')
        print('|'+3*' ',board[i][0],2*' ',end='')
        print('|'+3*' ',board[i][1],2*' ',end='')
        print('|'+3*' ',board[i][2],2*' '+'|')
        print(3*('|'+8*' ')+'|')
    print(3*('+'+8*'-')+'+')

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    free_cells = make_list_of_free_fields(board)
    while True:
        try:
            choice = int(input('Choose a free cell :'))
            if choice < 1 or choice > 9:
                continue
            row = (choice-1) // 3
            col = (choice-1) % 3 
            tuple_choice = (row, col)
            #print(tuple_choice)
            if tuple_choice in free_cells:
                board[row][col]='O'
                break
            else:
                print('Cell occupied')
        except ValueError:
            print('invalid input')

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free = []
    for i in range(3):
        for j in range(3):
            if board[i][j] not in ['O','X']:
                #print('Cell ',i,':',j,' is free')
                free.append((i,j))
    return free
    

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    for i in range(3):
        if board[0][i]==sign and board[1][i]==sign and board[2][i]==sign:
            return True
    
        if board[i][0]==sign and board[i][1]==sign and board[i][2]==sign:
            return True
    
    if board[0][0]==sign and board[1][1]==sign and board[2][2]==sign:
        return True
    
    if board[2][0]==sign and board[1][1]==sign and board[0][2]==sign:
        return True
    
    return False

def draw_move(board):
    # The function draws the computer's move and updates the board.
    free_cells = make_list_of_free_fields(board)
    choice = randrange(len(free_cells))
    board[free_cells[choice][0]][free_cells[choice][1]]='X'

# board=[['E' for col in range(3)] for line in range(3)]
# counter = 1
# for i in range(3):
#     for j in range(3):
#         board[i][j] = counter
#         counter +=1
board = [[3*i + j + 1 for j in range(3)] for i in range(3)]

counter = 0

victory = False
while victory == False:
    display_board(board)
    if len(make_list_of_free_fields(board)) == 0:
      print('No winner')
      break

    if counter % 2 == 0:
        draw_move(board)
    else:
        enter_move(board)
    
    if victory_for(board,'O'):
        display_board(board)
        victory = True
        print('Bravo O')
    elif victory_for(board,'X'):
        display_board(board)
        victory = True
        print('Bravo X')
    else:
        counter += 1
        print('tour ',counter)
    
