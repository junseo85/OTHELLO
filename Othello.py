# Author: Jun Seo
# GitHub username: junseo85
# Date: 5/31/2023
# Description: write a class called Othello that allows two people to play text-based Othello.
# The Othello game is a strategy board game. In this game, two players take turns placing their colored pieces on an 8x8 board.
# The objective is to capture the opponent's pieces and have the majority of your own pieces on the board at the end of the game
class Player:
    """A class to represent two players with different color team(white/ black). Each player will store list of boards that contains rows and columns. Used by class Othello"""
    def __init__(self, name, color):
        """The constructor for Player class. Takes name and color parameters. Initializes the required data members. All data members are private."""
        self._name = name
        if color not in ("black", "white"):
            raise TypeError("'color' must be one of 'black' or 'white'.")
        self._color = color
        """either black or white color """

        """this player list will store list of rows and columns"""

    def get_name(self):
        return self._name

    def get_color(self):
        return self._color


class Othello:
    """A class to represent the game Othello, played by two players. Player who choose Black color start first. The objective is to capture the opponent’s pieces and have the majority of your own pieces on the board at the end of the game. Use Player class to store data"""
    def  __init__(self):
        """The constructor for Othello class. Takes player, rows columns and size. Initializes the required data members. All data members are private. Self._board needs to be access each position value on the board by self._board[row][column]"""

        self._players = {'white': None, 'black': None}
        self._black = [(4,5),(5,4)]
        self._white = [(4,4),(5,5)]
        self._board = [['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'], ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'], ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'], ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'], ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'], ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'], ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'], ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'], ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']]
        """access each position value on the board by self._board[row][column]"""
    def get_player_list(self):
        return [self._players[color] for color in self._players]

    def print_board(self):
        """receive information from make_move  and go through board then to the print_board to print out the next move"""

        for i in self._board:
            print(i)

    def create_player(self, player_name, color):
        """Creates a player object with the given name and
color(black or white) and adds it to the player list
"""
        self._players[color] = Player(player_name, color)

    def return_winner(self):
        """the game ends when neither player can move, and the player with the most pieces on the board wins."""
        """when white player wins the game"""
        name = self.get_player_list()
        if range(len(self._white)) > range(len(self._black)):
            print("Winner is white player:",name)
            return "Winner is white player: player's name"
        """when black player wins the game"""
        if range(len(self._black)) > range(len(self._white)):
            print("Winner is black player:", name)
            return "Winner is black player: player’s name"
        if range(len(self._black)) == range(len(self._white)):
            """if black and white player has the same number of pieces on the board when the game ends"""
            print("It's a tie")
            return "It's a tie"

    def return_available_positions(self, color):
        """takes a self, color and scan through the entire board to figure out next possible moves.
If there is no return available position then go to the return_winner and print out the result
Return a list of possible positions for the player with the given color to move on the current board
"""

        available_list = []
        if available_list is []:
            self.return_winner()
        for b in self._black:
            x = b[0]
            y = b[1]
            self._board[x][y] = "X"
        for w in self._white:
            x = w[0]
            y = w[1]
            self._board[x][y] = "O"

        if color == "black":
            print("finding black moves")
            for b in self._black:
                print(available_list)
                x = b[0]
                y = b[1]
                if self._board[x+1][y] == "O":#move temp one right side
                    idx_x = x+2
                    idx_y = y+0
                    while self._board[idx_x][idx_y] == "O":
                        idx_x = idx_x + 1
                    if self._board[idx_x][idx_y] == ".":#temp right side
                        if (idx_x, idx_y) not in available_list:
                            available_list.append((idx_x, idx_y))

                if self._board[x-1][y] == "O":# move temp one left side
                    idx_x = x - 2
                    idx_y = y + 0
                    while self._board[idx_x][idx_y] == "O":
                        idx_x = idx_x - 1
                    if self._board[idx_x][idx_y] == ".":
                        if (idx_x, idx_y) not in available_list:
                            available_list.append((idx_x, idx_y))

                if self._board[x][y-1] == "O":# move temp one above
                    idx_x = x + 0
                    idx_y = y - 2
                    while self._board[idx_x][idx_y] == "O":
                        idx_y = idx_y - 1
                    if self._board[idx_x][idx_y] == ".":  # temp right side
                        if (idx_x, idx_y) not in available_list:
                            available_list.append((idx_x, idx_y))

                if self._board[x][y+1] == "O":# move temp one below
                    idx_x = x + 0
                    idx_y = y + 2
                    while self._board[idx_x][idx_y] == "O":
                        idx_y = idx_y + 1
                    if self._board[idx_x][idx_y] == ".":  # temp right side
                        if (idx_x, idx_y) not in available_list:
                            available_list.append((idx_x, idx_y))

                if self._board[x+1][y-1] == "O": #move temp one right side and one above
                    idx_x = x + 2
                    idx_y = y - 2
                    while self._board[idx_x][idx_y] == "O":
                        idx_x = idx_x + 1
                        idx_y = idx_y - 1
                    if self._board[idx_x][idx_y] == ".":  # temp right side
                        if (idx_x, idx_y) not in available_list:
                            available_list.append((idx_x, idx_y))

                if self._board[x-1][y-1] == "O": #move temp one left side and one above
                    idx_x = x - 2
                    idx_y = y - 2
                    while self._board[idx_x][idx_y] == "O":
                        idx_x = idx_x - 1
                        idx_y = idx_y - 1
                    if self._board[idx_x][idx_y] == ".":  # temp right side
                        if (idx_x, idx_y) not in available_list:
                            available_list.append((idx_x, idx_y))

                if self._board[x+1][y+1] == "O": #move temp one right side and one below
                    idx_x = x + 2
                    idx_y = y + 2
                    while self._board[idx_x][idx_y] == "O":
                        idx_x = idx_x + 1
                        idx_y = idx_y + 1
                    if self._board[idx_x][idx_y] == ".":  # temp right side
                        if (idx_x, idx_y) not in available_list:
                            available_list.append((idx_x, idx_y))

                if self._board[x-1][y+1] == "O": #move temp one left side and one below
                    idx_x = x - 2
                    idx_y = y + 2
                    while self._board[idx_x][idx_y] == "O":
                        idx_x = idx_x - 1
                        idx_y = idx_y + 1
                    if self._board[idx_x][idx_y] == ".":  # temp right side
                        if (idx_x, idx_y) not in available_list:
                            available_list.append((idx_x, idx_y))

        if color == "white":
            print("finding black moves")
            for b in self._white:
                print(available_list)
                x = b[0]
                y = b[1]
                if self._board[x + 1][y] == "X":  # move temp one right side
                    idx_x = x + 2
                    idx_y = y + 0
                    while self._board[idx_x][idx_y] == "X":
                        idx_x = idx_x + 1
                    if self._board[idx_x][idx_y] == ".":  # temp right side
                        if (idx_x, idx_y) not in available_list:
                            available_list.append((idx_x, idx_y))

                if self._board[x - 1][y] == "X":  # move temp one left side
                    idx_x = x - 2
                    idx_y = y + 0
                    while self._board[idx_x][idx_y] == "X":
                        idx_x = idx_x - 1
                    if self._board[idx_x][idx_y] == ".":
                        if (idx_x, idx_y) not in available_list:
                            available_list.append((idx_x, idx_y))

                if self._board[x][y - 1] == "X":  # move temp one above
                    idx_x = x + 0
                    idx_y = y - 2
                    while self._board[idx_x][idx_y] == "X":
                        idx_y = idx_y - 1
                    if self._board[idx_x][idx_y] == ".":  # temp right side
                        if (idx_x, idx_y) not in available_list:
                            available_list.append((idx_x, idx_y))

                if self._board[x][y + 1] == "X":  # move temp one below
                    idx_x = x + 0
                    idx_y = y + 2
                    while self._board[idx_x][idx_y] == "X":
                        idx_y = idx_y + 1
                    if self._board[idx_x][idx_y] == ".":  # temp right side
                        if (idx_x, idx_y) not in available_list:
                            available_list.append((idx_x, idx_y))

                if self._board[x + 1][y - 1] == "X":  # move temp one right side and one above
                    idx_x = x + 2
                    idx_y = y - 2
                    while self._board[idx_x][idx_y] == "X":
                        idx_x = idx_x + 1
                        idx_y = idx_y - 1
                    if self._board[idx_x][idx_y] == ".":  # temp right side
                        if (idx_x, idx_y) not in available_list:
                            available_list.append((idx_x, idx_y))

                if self._board[x - 1][y - 1] == "X":  # move temp one left side and one above
                    idx_x = x - 2
                    idx_y = y - 2
                    while self._board[idx_x][idx_y] == "X":
                        idx_x = idx_x - 1
                        idx_y = idx_y - 1
                    if self._board[idx_x][idx_y] == ".":  # temp right side
                        if (idx_x, idx_y) not in available_list:
                            available_list.append((idx_x, idx_y))


                if self._board[x + 1][y + 1] == "X":  # move temp one right side and one below
                    idx_x = x + 2
                    idx_y = y + 2
                    while self._board[idx_x][idx_y] == "X":
                        idx_x = idx_x + 1
                        idx_y = idx_y + 1
                    if self._board[idx_x][idx_y] == ".":  # temp right side
                        if (idx_x, idx_y) not in available_list:
                            available_list.append((idx_x, idx_y))

                if self._board[x - 1][y + 1] == "X":  # move temp one left side and one below
                    idx_x = x - 2
                    idx_y = y + 2
                    while self._board[idx_x][idx_y] == "X":
                        idx_x = idx_x - 1
                        idx_y = idx_y + 1
                    if self._board[idx_x][idx_y] == ".":  # temp right side
                        if (idx_x, idx_y) not in available_list:
                            available_list.append((idx_x, idx_y))

        available_list = sorted(available_list)
        print("Here are the valid moves:", available_list)
        return available_list

    def chain_moves(self, color, piece_position, delta_x, delta_y):
        if color == "black":
            player = "X"
            opponent = "O"
            add_moves = self._black
            remove_moves = self._white
        elif color == "white":
            player = "O"
            opponent = "X"
            add_moves = self._white
            remove_moves = self._black
        column_item = piece_position[0]
        row_item = piece_position[1]
        if self._board[column_item + delta_x][row_item + delta_y] == opponent:
            flipped_positions = []
            idx_c = column_item + delta_x
            idx_r = row_item + delta_y
            while self._board[idx_c][idx_r] == opponent:
                flipped_positions.append((idx_c, idx_r))
                idx_c = idx_c + delta_x
                idx_r = idx_r + delta_y
            if self._board[idx_c][idx_r] == player:
                for flipped_position in flipped_positions:
                    print(flipped_position)
                    column = flipped_position[0]
                    row = flipped_position[1]
                    self._board[column][row] = player
                    add_moves.append(flipped_position)
                    remove_moves.remove(flipped_position)

    def make_move(self, color, piece_position):
        """after seeing return_available_positions, puts a piece of the specified color at the given position and updates the board accordingly then return the current board(as a 2d list)
Take self, color, piece_position.
Pass information to def print_board with make_move decision.
Return current board(as a 2d list)
"""
        black, white, empty = "X", "O", "."
        print("Make move received ", piece_position)
        for b in self._black:
            x = b[0]
            y = b[1]
            self._board[x][y] = "X"
        for w in self._white:
            x = w[0]
            y = w[1]
            self._board[x][y] = "O"

        column_item = piece_position[0]
        row_item = piece_position[1]

        if color == "black":
            self._board[column_item][row_item] = "X"
            self._black.append(piece_position)

            self.chain_moves("black", piece_position, 0, 0)
            self.chain_moves("black", piece_position, 0, -1)
            self.chain_moves("black", piece_position, 0, 1)
            self.chain_moves("black", piece_position, 1, 0)
            self.chain_moves("black", piece_position, 1, -1)
            self.chain_moves("black", piece_position, 1, 1)
            self.chain_moves("black", piece_position, -1, 0)
            self.chain_moves("black", piece_position, -1, -1)
            self.chain_moves("black", piece_position, -1, 1)
        if color == "white":
            self._board[column_item][row_item] = "O"
            self._white.append(piece_position)
            self.chain_moves("white", piece_position, -1, 0)
            self.chain_moves("white", piece_position, -1, -1)
            self.chain_moves("white", piece_position, -1, 1)
            self.chain_moves("white", piece_position, 0, 0)
            self.chain_moves("white", piece_position, 0, -1)
            self.chain_moves("white", piece_position, 0, 1)
            self.chain_moves("white", piece_position, 1, 0)
            self.chain_moves("white", piece_position, 1, -1)
            self.chain_moves("white", piece_position, 1, 1)
        return self._board

    def play_game(self, player_color, piece_position):
        """Attempts to make a move for the player with the given color at the specified position.
If the position the player wants to move is invalid, the function should not make any move and return “Invalid move” and also print out this message “ Here are the valid moves:” followed by a list of possible positions.
If no valid moves exist then the returned list is empty.
If the position is valid, the function should make that move and update the board.
If the game is ended at that point, the function should print”Game is ended white piece: number black piece: number” and call the return_winner method.
"""
        "if game is over then it should call self.return_winner(), print, 'Game is ended.' and return"
        "if the player had no valid moves(which menas the move they attempted was invalid), it should print, 'Here are the valid moves: []' and return 'invalid move'."
        valid_moves = self.return_available_positions(player_color)
        print("Playing ", piece_position)
        print("Color ", player_color)
        print(valid_moves)
        self.print_board()
        if piece_position is []:
            print("Here are the valid moves:", valid_moves)
            return "Invalid move"
        if piece_position not in valid_moves:
            print("Not Valid")
            print("Here are the valid moves:", valid_moves)
            return "Invalid move"
        self.print_board()
        self.make_move(player_color, piece_position)
        self.print_board()


"""Detailed Text Descriptions of how to handle the scenarios

1. Initializing the Player and Othello classes
Player class will store the 2d list. Player class will take name and color as parameter
Othello class will take player, rows, columns, size as parameter
All data members must be private
2. Determining how to implement create_player method
Creates a player object with the given name and 
color(black or white) and adds it to the player list in Player class.
Black color player will always start the game.
All data members must be private


3. Determining how to implement print_board method
Each player will take their own turn to play the game.
Board is 10 X10 grid
One player is marked “0”
Other player is marked “X”
Empty space is marked as “.”
Border line is marked as “*”
Each position on the board is represented by a (row, column) pair.
The game starts with four pieces placed in the middle of the board, forming a square with same-colored pieces on a diagonal.
At first, white pieces(“0”) are at position (4,4) and (5,5) and black pieces are at (4,5) and (5,4)

Each Player will always receive information from Def return_available_position for the next move then player will decide next move and enter Def make_move which then pass
information from make_move  and go through board then to the print_board to print out the next move. Once player enters the next move as (row, column) then new number needs to change empty spot(“.” Dot) to either “0” or “X” depends on color of the player.
4.Determining how to implement return_available_positions method
Return_available_position must place their piece(either white color or black color) adjacent to an opponent’s piece, forming a straight line of adjacent pieces(horizontal, vertical, or diagonal) with their piece at each end.
Return_available_position can not touch the border or pass the border.
Range of return_available_position is 8X8 grid
Only empty space”.” Can be return as return_available_position.
Each player will take their turn and receive information on return_available_position as list of (row, column)
List can be none- if list is none then there is no next possible move which means game is not able to continue so it will pass to the return_winner method and print_board.
Return a list of possible positions(row, column) for the player with the given color(white or black) to move on the current board- pass information to make_move and print_board method

5. Determining how to implement return_winner method

Take information from play_game method.
the game ends when neither player can move, and the player with the most pieces on the board wins.
Check and see if both player(white and black) has no next move to make.
Count the number of  pieces for both Black and White.
Determine which color has more pieces.
If white color has more pieces than black pieces, then white color player wins.
If Black color has more pieces then white pieces, then black color player wins.
If they have equal amount of pieces, then they are tie.
When white player wins the game, 
returns ”Winner is white player: Player’s name”
When black player wins the game, 
returns “Winner is black player: player’s name”
If black and white player has the same number of pieces on the board when the game ends, 
return “It’s a tie”

6.Determining how to implement make_move method.

after seeing return_available_positions, puts a piece of the specified color at the given position and updates the board accordingly then return the current board(as a 2d list). Pass information to def play_game method
Also, Pass information to def print_board with make_move decision.
Once a piece is placed, it cannot be moved to a new square.
Multiple chains/directions of pieces can be captured all at once in a single move, and the captured pieces are converted to the capturing player’s color.
Player can not enter the number that matches the border line.
Player can not reenter the same number that previously entered.
Player can only enter the number from the lists that were given from return_available_positions.
If a player cannot make a valid move(a capturing move), their turn passes to the other player.( If there is no available move to make, press “none” to skip the turn)

7. Determining how to implement play_game method; how to validate a move. Determine how to detect the end of the game.

Attempts to make a move for the player with the given color at the specified position.
If the position the player wants to move is invalid, the function should not make any move and return “Invalid move” and also print out this message “ Here are the valid moves:” followed by a list of possible positions which passed from the return_available_position.
If no valid moves exist then the returned list is empty.
If the position(from return_available_position) is valid, the function should make that move and update the board.(pass to print_board and print the updated board)
If the game is ended at that point, the function should print”Game is ended white piece: number black piece: number” and call the return_winner method.

"""

