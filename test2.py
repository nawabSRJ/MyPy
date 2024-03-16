def print_board(board):
    # board -> nested list hai
    for row in board:
        for element in row:
            print(element, end='')
        print()

# Example usage:
sample_board = [[1, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [0, 1, 0, 0]]

print_board(sample_board)
