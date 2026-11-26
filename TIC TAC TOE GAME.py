print("Welcome to the TIC TAC TOE GAME")
board = ["1","2","3",
         "4","5","6",
         "7","8","9"]
players = {
"X": "Player-1",
"O":"Player-2"
    }
winning_combintions = (
    (0,1,2),
    (3,4,5),
    (6,7,8),
    (0,3,6),
    (1,4,7),
    (2,5,8),
    (0,4,8),
    (2,4,6)
    )

def display_board():
    print()
    print(board[0],"|",board[1],"|",board[2],)
    print("--+---+--")
    print(board[3],"|",board[4],"|",board[5])
    print("--+---+--")
    print(board[6],"|",board[7],"|",board[8])
    print("--+---+--")
    print()
    

current_player = "X"
occupied = set()

def check_winner(symbol):
    for a,b,c in winning_combintions:
        if board[a] == symbol and board[b] == symbol and board[c] == symbol:
            print(f"{current_player} is the winner")
            return False


def game_start(symbol):
    while True:
        choice = int(input(
            f"{players[symbol]}-{symbol}-> Choose between 1-9: "
            ))
        position = choice - 1
        
        if position in occupied:
            print(f"\nINVALID CHOICE \t You already made this choice\n")
            continue
        if choice > 9:
            print(f"\nINVALID CHOICE \t Choose between 1-9:\n")
            continue
            
        occupied.add(position)
        board[position] = symbol
        break
    
while True:
    display_board()
    game_start(current_player)
    if len(occupied) == 9:
            print("It's a Draw")
            break
    if check_winner(current_player) == False:
        break
    current_player = "O" if current_player == "X" else "X"



























    
