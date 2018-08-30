'''
Python tictactoe game as exercise for udemys training
'''
from random import randint

players = []
board = [f" {i+1} " for i in range(0, 9)]
remaining = []
player = 0
game_on = True
again = "Y"
error = "Choose any of {remaining}"
validation_check = False


def replay():

    again = input("Play again? [ y / any key to exit ]: ").upper().strip()

    return again == "Y"


def validate_entry(position):

    global board
    global error

    remaining = [int(x.strip())
                 for x in list(set(board)) if x.strip().isdigit()]

    if not position.isdigit():
        print(f"\n\tInvalid entry. \n\tPlease choose any of {remaining}")
        return False
    elif int(position) not in [x for x in list(range(1, 10))]:
        print(f"\n\tOutside Boundaries. \n\tPlease choose any of {remaining}")
        return False
    elif int(position) not in remaining:
        print(f"\n\tItem taken. \n\tPlease choose any of {remaining}")
        return False
    else:
        return True

    return False


def check_outcome():

    global game_on
    global error
    global player

    # test rows
    if len(set(board[6:9])) == 1:
        game_on = False
    elif len(set(board[3:6])) == 1:
        game_on = False
    elif len(set(board[0:3])) == 1:
        game_on = False

    # test columns
    if len(set(board[0::3])) == 1:
        game_on = False
    elif len(set(board[1::3])) == 1:
        game_on = False
    elif len(set(board[2::3])) == 1:
        game_on = False

    # test diagonals
    elif len(set(board[::4])) == 1:
        game_on = False
    elif len(set(board[2:8:2])) == 1:
        game_on = False

    # test for a tie - Todo: Predict Tie
    elif len(set(board[::])) == 2:
        player = "TIE"
        game_on = False
    else:
        return game_on


def update_board(position):

    global board

    board[position] = f" {players[player - 1]} "


def print_board():

    print("")
    print(" | ".join(board[6:9]))
    print(" | ".join(board[3:6]))
    print(" | ".join(board[0:3]))


def move():

    global player

    if player == 0:
        player = randint(1, 2)
    if player == 1:
        player = 2
    else:
        player = 1

    item = players[player - 1]

    global validation_check
    validation_check = False

    while not validation_check:
        msg = f"\n [ P{player} ] > where do you want to place your {item}?: "
        position = input(f"{msg}").strip()
        validation_check = validate_entry(position)
    else:
        return int(position) - 1


def define_players():

    global players

    options = ["X", "O"]

    while players[0] not in options:
        players[0] = input(
            f"P1 do you want {options[0]} or {options[1]}?: ").upper().strip()

    players[1] = list(set(options) - set(players))[0]

    return players


def reload():

    global players
    global board
    global player
    global game_on
    global again
    global error
    global validation_check

    players = ["", ""]
    board = [f" {i+1} " for i in range(0, 9)]
    player = 0
    game_on = True
    again = "Y"
    error = "Choose any of {remaining}"
    validation_check = False


def main():

    global again

    print("==== \tTIC TAC TOE v1\t ====")

    while True:
        reload()
        define_players()

        while game_on:
            print_board()
            update_board(move())
            check_outcome()

        if player != "TIE":
            print(f"\n\t [ P{player} ] IS THE WINNER!\n")
        else:
            print(f"\n\t DRAW : BOTH LOSERS! ")

        print_board()
        print("\n\t -- end\n")

        if not replay():
            break


main()
