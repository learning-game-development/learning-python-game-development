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
        other_tile = 'O'
    else:
        other_tile = 'X'

    tiles_to_flip = []
    for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        x, y = xstart, ystart
        x += xdirection  # First step in the x direction
        y += ydirection  # First step in the y direction
        while is_on_board(x, y) and board[x][y] == other_tile:
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
                    tiles_to_flip.append([x, y])

    # If no tiles were flipped, this is not a valid move.
    if len(tiles_to_flip) == 0:
        return False
    return tiles_to_flip


def is_on_board(x, y):
    # Return True if the coordinates are located on the board.
    return x >= 0 and x <= WIDTH - 1 and y >= 0 and y <= HEIGHT - 1


def get_board_with_valid_moves(board, tile):
    # Return a new board with periods marking the valid moves the player can make.
    board_copy = get_board_copy(board)

    for x, y in get_valid_moves(board_copy, tile):
        board_copy[x][y] = '.'
    return board_copy


def get_valid_moves(board, tile):
    # Return a list of [x,y] lists of valid moves for the given player on the given board.
    valid_moves = []
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if is_valid_move(board, tile, x, y) != False:
                valid_moves.append([x, y])
    return valid_moves


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
    tiles_to_flip = is_valid_move(board, tile, xstart, ystart)

    if tiles_to_flip == False:
        return False

    board[xstart][ystart] = tile
    for x, y in tiles_to_flip:
        board[x][y] = tile
    return True


def get_board_copy(board):
    # Make a duplicate of the board list and return it.
    board_copy = get_new_board()
    for x in range(WIDTH):
        for y in range(HEIGHT):
            board_copy[x][y] = board[x][y]

    return board_copy


def is_on_corner(x, y):
    # Return True if the position is in one of the four corners.
    return (x == 0 or x == WIDTH - 1) and (y == 0 or y == HEIGHT - 1)


def get_player_move(board, player_tile):
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
            if is_valid_move(board, player_tile, x, y) == False:
                continue
            else:
                break
        else:
            print('That is not a valid move. Enter the column (1-8) and then the row (1-8).')
            print('For example, 81 will move on the top-right corner.')

    return [x, y]


def get_computer_move(board, computer_tile):
    # Given a board and the computer's tile, determine where to
    # move and return that move as an [x, y] list.
    possible_moves = get_valid_moves(board, computer_tile)
    random.shuffle(possible_moves)  # Randomize the order of the moves.

    # Always go for a corner if available.
    for x, y in possible_moves:
        if is_on_corner(x, y):
            return [x, y]

    # Find the highest-scoring move possible.
    best_score = -1
    for x, y in possible_moves:
        board_copy = get_board_copy(board)
        make_move(board_copy, computer_tile, x, y)
        score = get_score_of_board(board_copy)[computer_tile]
        if score > best_score:
            best_move = [x, y]
            best_score = score

    return best_move


def print_score(board, player_tile, computer_tile):
    scores = get_score_of_board(board)
    print('You: %s points. Computer: %s points.' % (scores[player_tile], scores[computer_tile]))


def play_game(player_tile, computer_tile):
    turn = who_goes_first()
    print('The ' + turn + ' will go first.')

    # Clear the board and place starting pieces.
    board = get_new_board()
    board[3][3] = 'X'
    board[3][4] = 'O'
    board[4][3] = 'O'
    board[4][4] = 'X'

    while True:
        player_valid_moves = get_valid_moves(board, player_tile)
        computer_valid_moves = get_valid_moves(board, computer_tile)

        if player_valid_moves == [] and computer_valid_moves == []:
            return board  # No one can move, so end the game.

        elif turn == 'player':  # Player's turn
            if player_valid_moves != []:
                move = get_computer_move(board, player_tile)
                make_move(board, player_tile, move[0], move[1])
            turn = 'computer'

        elif turn == 'computer':  # Computer's turn
            if computer_valid_moves != []:
                move = get_computer_move(board, computer_tile)
                make_move(board, computer_tile, move[0], move[1])
            turn = 'player'


NUM_GAMES = 250
xWins = oWins = ties = 0
print('Welcome to Reversegam!')

playerTile, computerTile = enter_player_tile()

for i in range(NUM_GAMES):
    finalBoard = play_game(playerTile, computerTile)

    scores = get_score_of_board(finalBoard)
    print('#%s: X scored %s points. O scored %s points.' % (i + 1, scores['X'], scores['O']))
    if scores[playerTile] > scores[computerTile]:
        xWins += 1
    elif scores[playerTile] < scores[computerTile]:
        oWins += 1
    else:
        ties += 1


print('X wins: %s (%s%%)' % (xWins, round(xWins / NUM_GAMES * 100, 1)))
print('O wins: %s (%s%%)' % (oWins, round(oWins / NUM_GAMES * 100, 1)))
print('Ties: %s (%s%%)' % (ties, round(ties / NUM_GAMES * 100, 1)))
