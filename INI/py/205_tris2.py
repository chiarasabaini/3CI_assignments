__author__ = "Sabaini Chiara 3CI"
__version__ = "1.0 2020-03-23"

def print_board (board):
    """Prints the play board
    """
    for row in board:
        for elem in row:
            print(elem, end=" ")
        print()

def set_cell (board, player, value):
    row = int(input("player {} - Row ".format(player)))
    col = int(input("player {} - Col ".format(player)))
    if (board[row-1][col-1] == "-"):
        board[row-1][col-1] = value
        return True
    else:
        print("Already taken")
        return False

def is_winner (board, value): 
    print_board (board)
    
    for r in range(3):
        if (board[r][0] == value and board[r][1] == value and board[r][2] == value):
            return True
        
    for c in range(3) :
        if (board[0][c]==value and board[1][c] == value and board[2][c] == value):
            return True
        
    if (board[0][0] == value and board[1][1]==value and board[2][2]==value):
        return True
    
    if (board[0][2] == value and board[1][1] == value and board[2][0] == value):
        return True
    
    return False

def game(i, win):
    """The game
    """
    while (i < 9 and win == False):
            if (i % 2 == 0):
                value = "X"
                player = 1
                while set_cell (board, player, value) == False :
                    a = 0
            else:
                value = "O"
                player = 2
                while set_cell (board, player, value) == False :
                    a = 0
                    
            win = is_winner(board, value)
            i += 1
            
            if (win == True):
                if player == 1 :
                    print("Complimenti ha vinto il player {} (X)".format(player))
                else :
                    print("Complimenti ha vinto il player {} (O)".format(player))
            else:
                print("Mi dispiace non ha vinto nessuno")

if __name__ == "__main__" :
    board = [["-","-","-"],["-","-","-"],["-","-","-"]]
    print_board(board)
    win = False
    i = 0
    value = "X"
    player = 0
    game(i, win)