board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]
def display_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def update_board(board, row, col, mark):
    if 0 <= row < 3 and 0 <= col < 3:  # Check if indices are valid
        if board[row][col] == " ":  # Check if the cell is empty
            board[row][col] = mark
            return True
        else:
            print("Cell is already occupied. Try again.")
            return False
    else:
        print("Invalid row or column. Try again.")
        return False


def check_rows(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return True
    return False


def check_colum(board):
    for col in range(3):  # Iterate through each column (0, 1, 2)
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True
    return False


def diagonal(board):
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True
    return False

def check_tie(board):
    for row in board:
        if " " in row:  # If any empty cell is found, no tie
            return False
    return True

while True:
    display_board(board)
    try:
        row = int(input("Enter the row (0, 1, 2): "))
        col = int(input("Enter the column (0, 1, 2): "))
        mark = input("Enter your mark (X or O): ").upper()

        if mark not in ["X", "O"]:
            print("Invalid mark. Please enter X or O.")
            continue

        if update_board(board, row, col, mark):
            if check_rows(board):
                display_board(board)
                print(f"you win {mark}")
                break
            if check_colum(board):
                display_board(board)
                print(f"you win {mark}")
                break
            if diagonal(board):
                display_board(board)
                print(f"you win {mark}")
                break
            if check_tie(board):
                display_board(board)
                print(f"you win {mark}")
                break


    except ValueError:
        print("Invalid input. Please enter numbers for row and column.")


