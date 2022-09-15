# Tic Tac Toe Game

import os

gameon = False
playerturn = False  # Player one's turn if False
playerone = "X"
playertwo = "O"
winner = ""

# Create Game Board

row1 = ["1", "1", "1"]
row2 = ["2", "2", "2"]
row3 = ["3", "3", "3"]


# Clear screen

def clear():
    os.system("cls")


def reset_game():
    global row1, row2, row3, winner
    row1 = ["1", "1", "1"]
    row2 = ["2", "2", "2"]
    row3 = ["3", "3", "3"]
    winner = ""

    return

def game_board(row1, row2, row3):
    print("\n")
    print("  A    B    C")
    print(row1)
    print(row2)
    print(row3)
    print("\n")


def check_winner():
    for mark in row1:
        if len(set(row1)) == 1:
            return row1[0]
    for mark in row2:
        if len(set(row2)) == 1:
            return row2[0]
    for mark in row3:
        if len(set(row3)) == 1:
            return row3[0]
    if row1[0] == row2[1] == row3[2]:
        return row1[0]
    if row1[2] == row2[1] == row3[0]:
        return row1[2]
    if row1[0] == row2[0] == row3[0]:
        return row1[0]
    if row1[1] == row2[1] == row3[1]:
        return row1[1]
    if row1[2] == row2[2] == row3[2]:
        return row1[2]


def tie_game():
    while winner != "X" and winner != "Y":
        if ((row1[0] != "1") and (row1[1] != "1") and (row1[2] != "1")
        and (row2[0] != "2") and (row2[1] != "2") and (row2[2] != "2")
        and (row3[0] != "3") and (row3[1] != "3") and (row3[2] != "3")):
            print("Tie Game - Nobody wins.")
            quit()
        else:
            return

def game_start(gameon):
    while not gameon:
        playgame = ""
        while playgame != "YES":
            playgame = input("Start game? Yes/No ").upper()
            if playgame == "NO":
                print("Shutting down...")
                quit()
        gameon = True
    return gameon


def player_one():
    pone_col_int = 0
    pone_row_int = 0
    while pone_col_int < 1 or pone_col_int > 3:
        player_one_col = input("Player One, please select your column: A, B, or C ").upper()
        if player_one_col == "A":
            pone_col_int = 1
        if player_one_col == "B":
            pone_col_int = 2
        if player_one_col == "C":
            pone_col_int = 3

    while pone_row_int < 1 or pone_row_int > 3:
        pone_row_int = int(input("Player One, please select your row: 1, 2, or 3 "))

    if pone_row_int == 1:
        if row1[pone_col_int-1] != playerone and row1[pone_col_int-1] != playertwo:
            row1[pone_col_int-1] = playerone
        else:
            print("That spot is already taken, try again!")
            player_one()
    if pone_row_int == 2:
        if row2[pone_col_int-1] != playerone and row2[pone_col_int-1] != playertwo:
            row2[pone_col_int-1] = playerone
        else:
            print("That spot is already taken, try again!")
            player_one()
    if pone_row_int == 3:
        if row3[pone_col_int-1] != playerone and row3[pone_col_int-1] != playertwo:
            row3[pone_col_int-1] = playerone
        else:
            print("That spot is already taken, try again!")
            player_one()


def player_two():
    ptwo_col_int = 0
    ptwo_row_int = 0
    while ptwo_col_int < 1 or ptwo_col_int > 3:
        player_two_col = input("Player Two, please select your column: A, B, or C ").upper()
        if player_two_col == "A":
            ptwo_col_int = 1
        if player_two_col == "B":
            ptwo_col_int = 2
        if player_two_col == "C":
            ptwo_col_int = 3

    while ptwo_row_int < 1 or ptwo_row_int > 3:
        ptwo_row_int = int(input("Player Two, please select your row: 1, 2, or 3 "))

    if ptwo_row_int == 1:
        if row1[ptwo_col_int-1] != playerone and row1[ptwo_col_int-1] != playertwo:
            row1[ptwo_col_int-1] = playertwo
        else:
            print("That spot is already taken, try again!")
            player_two()
    if ptwo_row_int == 2:
        if row2[ptwo_col_int-1] != playerone and row2[ptwo_col_int-1] != playertwo:
            row2[ptwo_col_int-1] = playertwo
        else:
            print("That spot is already taken, try again!")
            player_two()
    if ptwo_row_int == 3:
        if row3[ptwo_col_int-1] != playerone and row3[ptwo_col_int-1] != playertwo:
            row3[ptwo_col_int-1] = playertwo
        else:
            print("That spot is already taken, try again!")
            player_two()


# Main Game Loop

gameon = game_start(gameon)
print("This is your game board:")
game_board(row1, row2, row3)


while gameon:
    while not playerturn:
        player_one()
        game_board(row1, row2, row3)
        winner = check_winner()
        tie_game()

        if winner == "X":
            print("Player One has won the game!")
            playagain = ""

            while playagain !="YES":
                playagain = input("Do you want to play again? Yes/No ").upper()
                if playagain == "NO":
                    print("Shutting down...")
                    quit()
            if playagain == "YES":
                reset_game()
                print("Player One (Winner) will go first")
                game_board(row1, row2, row3)
        else:
            playerturn = True

    while playerturn:
        player_two()
        game_board(row1, row2, row3)
        winner = check_winner()
        tie_game()

        if winner == "O":
            print("Player Two has won the game!")
            playagain = ""

            while playagain != "YES":
                playagain = input("Do you want to play again? Yes/No ").upper()
                if playagain == "NO":
                    print("Shutting down...")
                    quit()
            if playagain == "YES":
                reset_game()
                print("Player Two (Winner) will go first")
                game_board(row1, row2, row3)
        else:
            playerturn = False
