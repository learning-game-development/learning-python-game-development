# Reversegam: a clone of Othello/Reversi

import random
import sys
WIDTH = 8
HEIGHT = 8


def draw_board(board):
    print('  12345678')
    print(' +--------+')
    for y in range(HEIGHT):
        print('%s|' % (y+1), end='')
        for x in range(WIDTH):
            print(board[x][y], end='')
        print('|%s' % (y+1))
    print(' +--------+')
    print('  12345678')


def get_new_board():
    board = []
    for i in range(WIDTH):
        board.append([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
    return board


def is_valid_move(board, tile, xstart, ystart):
    # Return False if the player's move on space xstart, ystart is invalid.
    # If it is a valid move, return a list of spaces that would become the player's if they made a move here.
    if board[xstart][ystart] != ' ' or not is_on_board(xstart, ystart):
        return False

    if tile == 'X':
        otherTile = 'O'
    else:
        otherTile = 'X'

    tilesToFlip = []
    for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        x, y = xstart, ystart
        x += xdirection  # First step in the x direction
        y += ydirection  # First step in the y direction
        while is_on_board(x, y) and board[x][y] == otherTile:
            # Keep moving in this x & y direction.
            x += xdirection
            y += ydirection
            if is_on_board(x, y) and board[x][y] == tile:
                # There are pieces to flip over. Go in the reverse direction until we reach the original space, noting all the tiles along the way.
                while True:
                    x -= xdirection
                    y -= ydirection
                    if x == xstart and y == ystart:
                        break
                    tilesToFlip.append([x, y])

    # If no tiles were flipped, this is not a valid move.
    if len(tilesToFlip) == 0:
        return False
    return tilesToFlip


def is_on_board(x, y):
    # Return True if the coordinates are located on the board.
    return x >= 0 and x <= WIDTH - 1 and y >= 0 and y <= HEIGHT - 1


def get_board_with_valid_moves(board, tile):
    # Return a new board with periods marking the valid moves the player can make.
    boardCopy = get_board_copy(board)

    for x, y in get_valid_moves(boardCopy, tile):
        boardCopy[x][y] = '.'
    return boardCopy


def get_valid_moves(board, tile):
    # Return a list of [x,y] lists of valid moves for the given player on the given board.
    validMoves = []
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if is_valid_move(board, tile, x, y) != False:
                validMoves.append([x, y])
    return validMoves


def get_score_of_board(board):
    # Determine the score by counting the tiles. Return a dictionary with keys 'X' and 'O'.
    xscore = 0
    oscore = 0
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if board[x][y] == 'X':
                xscore += 1
            if board[x][y] == 'O':
                oscore += 1
    return {'X': xscore, 'O': oscore}


def enter_player_tile():
    # Let the player enter which tile they want to be.
    # Return a list with the player's tile as the first item and the computer's tile as the second.
    tile = ''
    while not (tile == 'X' or tile == 'O'):
        print('Do you want to be X or O?')
        tile = input().upper()

    # The first element in the list is the player's tile, and the second is the computer's tile.
    if tile == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def who_goes_first():
    # Randomly choose who goes first.
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


def make_move(board, tile, xstart, ystart):
    # Place the tile on the board at xstart, ystart and flip any of the opponent's pieces.
    # Return False if this is an invalid move; True if it is valid.
    tilesToFlip = is_valid_move(board, tile, xstart, ystart)

    if tilesToFlip == False:
        return False

    board[xstart][ystart] = tile
    for x, y in tilesToFlip:
        board[x][y] = tile
    return True


def get_board_copy(board):
    # Make a duplicate of the board list and return it.
    boardCopy = get_new_board()
    for x in range(WIDTH):
        for y in range(HEIGHT):
            boardCopy[x][y] = board[x][y]

    return boardCopy


def is_on_corner(x, y):
    # Return True if the position is in one of the four corners.
    return (x == 0 or x == WIDTH - 1) and (y == 0 or y == HEIGHT - 1)


def get_player_move(board, playerTile):
    # Let the player enter their move.
    # Return the move as [x, y] (or return the strings 'hints' or 'quit').
    DIGITS1TO8 = '1 2 3 4 5 6 7 8'.split()
    while True:
        print('Enter your move, "quit" to end the game, or "hints" to toggle hints.')
        move = input().lower()
        if move == 'quit' or move == 'hints':
            return move

        if len(move) == 2 and move[0] in DIGITS1TO8 and move[1] in DIGITS1TO8:
            x = int(move[0]) - 1
            y = int(move[1]) - 1
            if is_valid_move(board, playerTile, x, y) == False:
                continue
            else:
                break
        else:
            print('That is not a valid move. Enter the column (1-8) and then the row (1-8).')
            print('For example, 81 will move on the top-right corner.')

    return [x, y]


def get_computer_move(board, computerTile):
    # Given a board and the computer's tile, determine where to
    # move and return that move as an [x, y] list.
    possibleMoves = get_valid_moves(board, computerTile)
    random.shuffle(possibleMoves)  # Randomize the order of the moves.

    # Always go for a corner if available.
    for x, y in possibleMoves:
        if is_on_corner(x, y):
            return [x, y]

    # Find the highest-scoring move possible.
    bestScore = -1
    for x, y in possibleMoves:
        boardCopy = get_board_copy(board)
        make_move(boardCopy, computerTile, x, y)
        score = get_score_of_board(boardCopy)[computerTile]
        if score > bestScore:
            bestMove = [x, y]
            bestScore = score

    return bestMove


def print_score(board, playerTile, computerTile):
    scores = get_score_of_board(board)
    print('You: %s points. Computer: %s points.' % (scores[playerTile], scores[computerTile]))


def play_game(playerTile, computerTile):
    showHints = False
    turn = who_goes_first()
    print('The ' + turn + ' will go first.')

    # Clear the board and place starting pieces.
    board = get_new_board()
    board[3][3] = 'X'
    board[3][4] = 'O'
    board[4][3] = 'O'
    board[4][4] = 'X'

    while True:
        playerValidMoves = get_valid_moves(board, playerTile)
        computerValidMoves = get_valid_moves(board, computerTile)

        if playerValidMoves == [] and computerValidMoves == []:
            return board  # No one can move, so end the game.

        elif turn == 'player':  # Player's turn
            if playerValidMoves != []:
                if showHints:
                    validMovesBoard = get_board_with_valid_moves(board, playerTile)
                    draw_board(validMovesBoard)
                else:
                    draw_board(board)
                print_score(board, playerTile, computerTile)

                move = get_player_move(board, playerTile)
                if move == 'quit':
                    print('Thanks for playing!')
                    sys.exit()  # Terminate the program.
                elif move == 'hints':
                    showHints = not showHints
                    continue
                else:
                    make_move(board, playerTile, move[0], move[1])
            turn = 'computer'

        elif turn == 'computer':  # Computer's turn
            if computerValidMoves != []:
                draw_board(board)
                print_score(board, playerTile, computerTile)

                print_score(board, playerTile, computerTile)
                move = get_computer_move(board, computerTile)
                make_move(board, computerTile, move[0], move[1])
            turn = 'player'


print('Welcome to Reversegam!')

playerTile, computerTile = enter_player_tile()

while True:
    finalBoard = play_game(playerTile, computerTile)

    # Display the final score.
    draw_board(finalBoard)
    scores = get_score_of_board(finalBoard)
    print('X scored %s points. O scored %s points.' % (scores['X'], scores['O']))
    if scores[playerTile] > scores[computerTile]:
        print('You beat the computer by %s points! Congratulations!' % (scores[playerTile] - scores[computerTile]))
    elif scores[playerTile] < scores[computerTile]:
        print('You lost. The computer beat you by %s points.' % (scores[computerTile] - scores[playerTile]))
    else:
        print('The game was a tie!')

    print('Do you want to play again? (yes or no)')
    if not input().lower().startswith('y'):
        break
