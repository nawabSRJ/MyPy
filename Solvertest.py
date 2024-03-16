def nQueens(n):
    board = []    
    for i in range(n):
        row = []  # Create a new row and then append 
        for j in range(n):
            row.append(0)  # Add 0 to the row
        board.append(row)
    print(board)

nQueens(4)
