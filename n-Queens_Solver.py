''' Alert : This n-Queens Solver follows 0-based Indexing,make sure you align with it while cross
checking. Also -> 0 -> Empty ; 1->Queen.'''
print(__doc__)
# 0 -> Empty ; 1->Queen
ans_board = []  # list with the right board

def print_board(board):
    n = int(len(board) ** 0.5)  # Assuming board is a square matrix
    for i in range(0, len(board), n):
        row = board[i:i + n]
        print(row)

def printBoard(board):
    for row in board:
        for element in row:
            print(element , end = '')
        print()
def addSolution(board , n):
    global ans_board
    temp = []
    for i in range(n):
        for j in range(n):
            temp.append(board[i][j])    # filling rows

    ans_board = temp    # filling answer board (with correct rows)

def isSafe(row , col, board, n) -> bool :
    r = row
    c = col

    # check for same row    ~ todo - hash map optimization (use dict)
    while(c>=0):
        if board[r][c] == 1:
            return False
        c -= 1
    # while ends

    r = row
    c = col
    # (Out of 4 Diagonal Movements, you have to check only 2-> left-up/down)
    # check for diagonal    
    while(r >= 0 and c >= 0):
        if(board[r][c] == 1):
            return False
        c -= 1
        r -= 1      # left-up (col/row both decrease)
    # while ends
    
    r = row
    c = col
    # check for diagonal
    while(r < n and c >= 0):
        if(board[r][c] == 1):
            return False
        c -= 1
        r += 1      # left-down (col decrease ; row increase)
        
    # while ends

    return True     # All izz Well
        
        

    
def solve(col , board , n):
    if(col == n):   # if all columns are filled
        addSolution(board , n)
        return

    # solve one case manually , rest recursion
    for row in range(n):
        if(isSafe(row,col,board,n) == True):            
            # if placing queen is safe
            board[row][col] = 1     # Queen Place Kardo
            solve(col + 1 , board , n)  # recursion call

            # backtrack?
            board[row][col] = 0


def nQueens(n):
    board = []    
    for i in range(n):
        row = []  # Create a new row and then append 
        for j in range(n):
            row.append(0)  # Add 0 to the row
        board.append(row)
    print('Board Before : \n')
    printBoard(board)
    
    solve(0, board, n)
            

n = int(input('Enter the size of NxN board : '))
nQueens(n)
# printing the board
print('Board After : \n') 
#printBoard(ans_board)
#printBoard(ans_board)   Ayein ? Not working 2nd time

print_board(ans_board)
