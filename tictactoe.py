# Tic Tac Toe  
# by Mike Lewis  
# CSE-210 Section 8  
# 25-Apr-2022

# define some "constants"
clearscreen = chr(27) + '[2J'

# Colors
black =     chr(27) + "[0;30m"
dkgrey =    chr(27) + "[1;30m"
grey =      chr(27) + "[0;37m"
white =     chr(27) + "[1;37m"

dkred =     chr(27) + "[0;31m"
dkyellow =  chr(27) + "[0;33m"
dkgreen =   chr(27) + "[0;32m"
dkcyan =    chr(27) + "[0;36m"
dkblue =    chr(27) + "[0;34m"
dkmagenta = chr(27) + "[0;35m"

red =       chr(27) + "[1;31m"
yellow =    chr(27) + "[1;33m"
green =     chr(27) + "[1;32m"
cyan =      chr(27) + "[1;36m"
blue =      chr(27) + "[1;34m"
magenta =   chr(27) + "[1;35m"

# Color Theme
normal_color = grey
hilite_color = white
error_color = red
player_color = [grey, yellow, green]
game_board_color = grey
sq_num_color = dkblue
score_color = white
title_color = white

# Need to set up some basic variables to track number of moves
# the game board, maybe a running score of games won, lost, tied
# etc.

player = {}
player[0] = {'name': 'Tie Games', 'score': 0 }
player[1] = {'name': 'Player 1', 'score': 0 }
player[2] = {'name': 'Player 2', 'score': 0 }

game_tokens = [' ','X','O']
game_board = {}

for i in range(1,10):
    index = str(i)
    game_board[index] = 0


def pause():
    input("\nPress enter to continue.")
    return True


def get_player_name(player_num):
    """Query a particular player for his or her name."""
    temp_name = input(f"Player {player_num}, please enter your name: ")
    return temp_name


def display_game_board():
    """Displays the current state of the game board."""
    print(clearscreen)
    print(f"{title_color}Game Board:{normal_color}\n")
    for row in range(0, 3):
        print(f"{game_board_color}+---+---+---+")
        print("|",end='')
        for square in range(1+(3*row), 4+(3*row)):
            sq_owner = game_board[ str(square) ]
            temp_token = player_color[sq_owner] + game_tokens[sq_owner] + game_board_color
            if sq_owner == 0:
                temp_token = sq_num_color + str(square) + game_board_color
            print(f" {temp_token} |",end='')
        print()
    print(f"+---+---+---+{normal_color}")
    print()


def title(): 
    """Display a title and welcome screen."""

    print(clearscreen)
    print(f"""
{title_color}TIC TAC TOE

by Mike Lewis - CSE 210 Section 8{normal_color}

Welcome to the classic game of Tic Tac Toe. One player will be {player_color[1]}X{normal_color}
and the other player will be {player_color[2]}O{normal_color}. First one to get three marks in a 
straight line (horizontal, vertical, or diagonal) wins the game... 
... Otherwise, it's a tie.
    """)


def is_open_square(square_num):
    """Simply returns whether the square specified by square_num is unoccupied or not.
    - TRUE if unoccupied
    - FALSE if occupied"""
    return game_board[square_num] == 0
    


def next_turn(player_num):
    """Advance the turn counter to the next player."""
    advanced_turn = int(not player_num)
    return advanced_turn


def get_move(player_num):
    """Prompts the player for a square number. Checks the input to make sure it is valid.
    Once valid input is entered, returns the player's choice."""
    valid_move = False
    while not valid_move:
        player_move = input(f"{player_color[player_num]}{player[player_num]['name']}{normal_color}, please choose a square for your next move: ")
        if player_move < '1' or player_move > '9':
            print(f"{error_color}You need to enter a square numbered 1 through 9. Try again.{normal_color}")
            valid_move = False
        elif game_board[player_move] != 0:
            print(f"{error_color}Sorry, that square is already occupied. Choose an empty square.{normal_color}")
            valid_move = False
        else:
            valid_move = True

    return player_move


def set_square(square_num, player_num):
    game_board[square_num] = player_num
    return True


def check_win(player_num):
    """Examine the board and check to see if the indicated player has won the game."""
    solution = False
    # Check Rows
    for start in range(1,8,3):
        if game_board[str(start)] == player_num and \
           game_board[str(start+1)] == player_num and \
           game_board[str(start+2)] == player_num:
            solution = (player_num, 'row', start)
            return solution
    # Check Columns
    for start in range(1, 4):
        if game_board[str(start)] == player_num and \
           game_board[str(start+3)] == player_num and \
           game_board[str(start+6)] == player_num:
            solution = (player_num, 'column', start)
            return solution
    # Check Diagonals
    # Square 1 Down-Right
    if game_board[str(1)] == player_num and \
       game_board[str(5)] == player_num and \
       game_board[str(9)] == player_num:
        solution = (player_num, 'diagonal (down-right)', 1)
        return solution
    # Square 3 Down-Left
    if game_board[str(3)] == player_num and \
       game_board[str(5)] == player_num and \
       game_board[str(7)] == player_num:
        solution = (player_num, 'diagonal (down-left)', 3)
        return solution

    # If we got to this point, then there is no match for a win.
    return solution


def reset_board():
    for i in range(1,10):
        index = str(i)
        game_board[index] = 0


def play_game():

# Set up a few things
    winner = False      # Flag if there is a winner
    end_game = False    # Flag if we've reached the end of the game
    game_moves = 0      # Track the total moves played. If == 9, then end_game = True
    player_turn = 0
    reset_board()

# BEGIN GAME LOOP between two players
    while not winner and not end_game:
        display_game_board()
        active_player = player_turn + 1 
        player_move = get_move(active_player)
        set_square(player_move, active_player)
        game_moves += 1
        winner = check_win(active_player)
        end_game = game_moves == 9
        player_turn = next_turn(player_turn)

    display_game_board()
    print("Game Over!")
    if winner:
        (winning_player, direction, start_square) = winner
        print("Tic Tac Toe!")
        print()
        print(f"{player[winning_player]['name']} won with three in a {direction} starting on square {start_square}.")
        player[active_player]['score'] += 1
    elif end_game:
        print("Winner: NONE.")
        player[0]['score'] += 1
    print()


def display_score():
    print(title_color + "--- Standings So Far ---" + normal_color)
    for i in range(0,3):
        print(f"{player_color[i]}{player[i]['name']}:\t{hilite_color}{player[i]['score']}{normal_color}".expandtabs(15))
    
      
def play_again():
    valid_choice = False
    while not valid_choice:
        user_choice = input("\nWould you like to play again? ").capitalize()[0]
        if user_choice not in ['N','Y']:
            print(f"{error_color}A Yes or No response is appropriate here...")
            print(f"If that's too hard, just enter a {hilite_color}Y{error_color} or {hilite_color}N{error_color}.{normal_color}\n")
        else:
            valid_choice = True
    return user_choice == 'Y'

def main():
    """The main routine."""
    title()
    quit_game = False

    for p in range(1, 3):
        player[p]['name'] = get_player_name(p)
    
    while not quit_game:
        play_game()
        display_score()
        quit_game = not play_again() 


if __name__ == "__main__":
    main()  
