from IPython.display import clear_output

player1 = player2 = whoseturn = winner = ''
board = {x:" " for x in range(1,10)}
gameover = False

def intro_actions():
    import random

    global whoseturn, xo, player1, player2

    player1 = input("Player one, please enter your name: ")   # get player names
    player2 = input("Player two, please enter your name: ")
#    clear_output() #use if in jupyter notebook
    print('\n'*100)  #use otherwise

    coinchoice = False
    options = ["heads","tails"]
    while coinchoice == False:              # ask for a heads/tails call for a coin flip and verify input
        headtail = input(f"\nLet's flip a coin to see who will be X and who will be O.\n{player1}, please enter 'heads' or 'tails': ")
        if headtail in options:
            coinchoice = True
            options.remove(headtail)
        else:
            continue
    xo = {player1:None,player2:None}
    if random.randint(1,11) % 2 == 0:        # if random number is even, player 1's choice wins, and vice versa
        xo[player1] = "X"
        xo[player2] = "O"
        whoseturn = player1
        print(f"\nIt's {headtail}. Congrats, {player1}! You're X!")
    else:
        xo[player1] = "O"
        xo[player2] = "X"
        whoseturn = player2
        print(f"\nIt's {options[0]}. Congrats, {player2}! You're X!")
    print("You'll choose your square by pressing the corresponding key on the number pad.")
    print("To help you visualize it, here's the board layout, with each square containing its corresponding number:\n")
    print(f"     |     |     \n  7  |  8  |  9  \n_____|_____|_____\n")
    print(f"     |     |     \n  4  |  5  |  6  \n_____|_____|_____\n")
    print(f"     |     |     \n  1  |  2  |  3  \n     |     |     \n")
    input("Ready? Hit enter to begin")
    return player1, player2, xo, whoseturn # return player names, letter assignments, and who goes first

def display_board():
    global board
    print(f"     |     |     \n  {board[7]}  |  {board[8]}  |  {board[9]}  \n_____|_____|_____\n")
    print(f"     |     |     \n  {board[4]}  |  {board[5]}  |  {board[6]}  \n_____|_____|_____\n")
    print(f"     |     |     \n  {board[1]}  |  {board[2]}  |  {board[3]}  \n     |     |     \n")

def make_move():
    global whoseturn
    token = xo[whoseturn]
    movemade = False
    while movemade == False:     # ask what square to fill in and verify input
        move = input(f"{whoseturn}, please make your move by entering the space you would like to fill: ")
        if move.isdigit():
            move = int(move)
        else:
            continue
        if move in range(1,10) and board[move] == ' ':
            movemade = True
        else:
            continue
    if movemade == True:
        board[move] = token
    return board

def game_over():
    global gameover, winner, whoseturn
    vertical = horizontal = diagUp = diagDown = False

    if any(board[x] == board[x + 1] == board[x + 2] != " " for x in [1,4,7]):
        vertical = True
    elif any(board[x] == board[x + 3] == board[x + 6] != " " for x in [1,2,3]):
        horizontal = True
    elif board[1] == board[5] == board[9] != " ":
        diagUp = True
    elif board[3] == board[5] == board[7] != " ":
        diagDown = True
    else:
        pass

    if vertical or horizontal or diagUp or diagDown:
        gameover = True
        winner = whoseturn
#        clear_output() #use if in jupyter notebook
        print('\n'*100)  #use otherwise
        display_board()
        print(f"{winner} wins!\n\nCongrats {winner}!\n")
    elif all(board[x] != " " for x in range(1,10)):
        gameover = True
#        clear_output() #use if in jupyter notebook
        print('\n'*100)  #use otherwise
        display_board()
        print("It's a draw.\n")
    else:
        if whoseturn == player1:
            whoseturn = player2
        else:
            whoseturn = player1
    return gameover, winner
################################################################
intro_actions()

for player in xo:
    if xo[player] == "X":
        whoseturn = player

while gameover == False:
#    clear_output() #use if in jupyter notebook
    print('\n'*100)  #use otherwise

    display_board()

    make_move()

    game_over()
