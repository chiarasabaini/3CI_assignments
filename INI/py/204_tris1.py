__author__ = "Sabaini Chiara 3CI"
__version__ = "1.0 2020-03-23"

PLAYER_1 = "X"
PLAYER_2 = "O"
EMPTY = "-"

def print_board(board):
    """Prints the play board
    """
    for i in range(3):
        for j in range(3):
            print(board[i][j], end=" ")
        
        print()

def get_input ():
    """Gets the input from the player
    """
    row = int(input("Row [1-3]: "))
    col = int(input("Col [1-3]: "))
    
    return row - 1, col - 1

def set_cell (board, row, col, player):
    """Sets the cell with the current player value
    """
    board[row][col] = player

if __name__ == "__main__":
 board = [[EMPTY, EMPTY, EMPTY],
 [EMPTY, EMPTY, EMPTY],
 [EMPTY, EMPTY, EMPTY]]
 player = PLAYER_1
 print_board(board)
 row, col = get_input()
 set_cell(board, row, col, player)
 print_board(board)