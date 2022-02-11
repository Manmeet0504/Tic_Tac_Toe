from IPython.display import clear_output

def display_board(board):
    clear_output()
    print("     |     |     ")
    print("  "+board[7]+"  |  "+board[8]+"  |  "+board[9]+"  ")
    print("     |     |     ")
    print("-----------------")
    print("     |     |     ")
    print("  "+board[4]+"  |  "+board[5]+"  |  "+board[6]+"  ")
    print("     |     |     ")
    print("-----------------")
    print("     |     |     ")
    print("  "+board[1]+"  |  "+board[2]+"  |  "+board[3]+"  ")
    print("     |     |     ")
    
def player_input():
    marker="WRONG"
    
#     from random import randint
#     l=['1','2']
#     print("player"+l[randint(0,1)]+" goes first !!")
    
    while marker not in ['X','O']:
        marker=input("Player1: Do you want to be X or O ?")
        if marker not in ['X','O']:
            print("Wrong choice enter again")
    if marker=='X':
        return ('X','O')
    else:
        return ('O','X')

def place_marker(board,marker,position):
    board[position]=marker

def win_check(board,mark):
    if board[1]==mark and board[2]==mark and board[3]==mark:
        return True 
    elif board[4]==mark and board[5]==mark and board[6]==mark:
        return True 
    elif board[7]==mark and board[8]==mark and board[9]==mark:
        return True
    
    elif board[1]==mark and board[4]==mark and board[7]==mark:
        return True 
    elif board[2]==mark and board[5]==mark and board[8]==mark:
        return True 
    elif board[3]==mark and board[6]==mark and board[9]==mark:
        return True 
    
    elif board[1]==mark and board[5]==mark and board[9]==mark:
        return True 
    elif board[3]==mark and board[5]==mark and board[7]==mark:
        return True 
    
    else:
        return False

from random import randint

def choose_first():
    l=['1','2']
    return "player"+l[randint(0,1)]+" goes first !!"

def space_check(board,position):
    if board[position] == ' ':
        return True
    else:
        return False

def full_board_check(board):
    for x in range(1,10):
        if board[x] == " ":
            return False
    return True 

def player_choice(board):
    position="WRONG"
    while position.isdigit()==False or position not in range(0,10):
        position = input("Enter your next move (0-9)")
        if position.isdigit()==False:
            print("INVALID CHOICE !! Enter a NUMBER!!")
            continue
        
        elif int(position) not in range(1,10):
            print("INVALID CHOICE !! Enter the in RANGE!!")
            continue
            
        elif space_check(board, int(position))==False:
            print("Space occupied !! Enter again!!")
            continue
            
        else:
            return int(position)

def replay():
    choice="WRONG"
    while choice not in ["yess","no"]:
        choice=input("Do you want to play again ??")
        if choice not in ["yess","no"]:
            print("Sorry! I don't understand. Please choose yess or no !!")
            continue
        
        if choice == "yess":
            return True 
        else:
            return False

print("Welcome to TIC TAC TOE")
while True:
    the_board=[' ']*10
    player1_marker,player2_marker=player_input()
    
    turn =choose_first()
    print(turn + "will go first")
    
    play_game=input("Ready to play? yess or no ?")
    if play_game=='yess':
        game_on =True 
    else:
        game_on=False
    
    while game_on:
        if turn == 'Player1':
            display_board(the_board)
            position=player_choice(the_board)
            place_marker(the_board,player1_marker,position)
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print("Player 1 has WON !!")
                game_on = False 
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Game TIE !!")
                    game_on=False
                else:
                    turn = "Player2"
        else:
            display_board(the_board)
            position=player_choice(the_board)
            place_marker(the_board,player2_marker,position)
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print("Player 2 has WON !!")
                game_on = False 
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Game TIE !!")
                    game_on=False
                else:
                    turn = "Player1"
    if not replay():
        break
            
