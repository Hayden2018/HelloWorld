import os
from time import sleep
from game import Board

# Initialize neccessary variables
board = Board()
i = 0
curr_player = 'X'

# Main game loop
while True:
    print('Welcome to Tic-Tat-Toe!')
    print(board)
    pos = input('Player ' + curr_player + ' please input yor move: ')
    # Handle user input
    try:
        board.move(curr_player, pos)
        i += 1
    except:
        print('Please input a valid play.')
        sleep(1)
        os.system('cls')
        continue
    # End the loop if ending condition met else changes side
    if board.have_winner() or i == 9:
        break
    elif curr_player == 'X':
        curr_player = 'O'
    else:
        curr_player = 'X'
    os.system('cls')   # Clear console

# Show final game result
os.system('cls')
print(board)
if i != 9:
    print('Player', curr_player, 'has won the game!')
else:
    print('It\'s a draw!')


