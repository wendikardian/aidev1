import numpy as np
import random

board = np.zeros((3, 3)).astype(int)
turn = 1
move = 9

def check_win():
    if any(np.sum(board, 1)==3) or any(np.sum(board, 0)==3) or sum(np.diag(board))==3 or sum(np.diag(board[::-1]))==3:
        return True
    if any(np.sum(board, 1)==-3) or any(np.sum(board, 0)==-3) or sum(np.diag(board))==-3 or sum(np.diag(board[::-1]))==-3:
        return True
    return False


def play_turn():
    # If player using input
    if(turn ==1):
        x = int(input(f"What is player {turn}'s x position?"))
        y = int(input(f"What is player {turn}'s y position?"))
    # Computer using random
    else:
        x = random.randint(0,2);
        y = random.randint(0,2);
    # Try using exception if the input is right or not
    try:
        # If the input right
        if board[y, x]==0:
            board[y, x]=turn
        else:
            # If the column and row already filled
            if(turn == 1):
                print("The board already contains")
            # Draw again
            play_turn()
    # If the input out of the range of board
    except IndexError:
        print("Input error")
        play_turn()


while move >0:
    # Draw the board
    print (board)
    play_turn()
    if check_win():
        print (f"Player {turn} has won!")
        break
    turn = turn*-1
    move = move -1