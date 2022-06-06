import random
import re

class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        # creating the board
        # helper function
        self.board = self.make_new_board()

        # iniitizalize a set to keep track of which locations we've uncovered
        # we'll save(row,col) tuples into this set
        self.dug = set()  # if we dig at 0, 0, then self.dug = ({0,0})

    def make_new_board(self):

        # construct a new board based on the dim size and num bombs
        # we should construct the list of lists here (or whatever representation  you prefer,
        # but since we have 2D board, list  of lists is most natural)

        # generate a new board
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        # this creates an array like this:0,1
        # [[None, None, ..., None, None],
        # [None, None, ..., None, None]
        # ]

        # plant the bombs
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            # return a random integer N such that a <= N <= b
            loc = random.randint(0, self.num_bombs**2 - 1)
            row = loc // self.dim_size  # we eant the number of times dim_size goes into loc
            # we eant the remainder to tell us whawt index in that row to loc
            col = loc % self.dim_size

            if board[row][col] == '*':
                # this means we've actually planted a bomb there already so keep going
                continue
            board[row][col] = '*'
            bombs_planted += 1
        return board

    def assign_values_to_board(self):
        # now that we have the bombs planted, let's assign aa number 0-8 for all the empry spaces,
        # which represents how many neighboring bombs there are. we can precompute these and it'll save us some
        # effort checking what's around the board later on
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    # if this is already a bomb, then we don't want to calc anything
                    continue
                self.board[r][c] = self.get_num_neighboring_bombs(r, c)

    def get_num_neighboring_bombs(self, row, col):
        # let's iterate through each of the neighboring positions and sum numbers of bombs
        # top left: (row - 1, col - 1)
        # top middle: (row - 1, col)
        # top right: (row - 1, col + 1)
        # left (row, col - 1)
        # right (row, col + 1)
        # bottom left: (row + 1, col - 1)
        # bottom middle: (row + 1, col)
        # bottom right: (row + 1, col + 1)

        # make sure to not go out of bounds

        num_neighboring_bombs = 0
        for r in range(max(0, row - 1), min(self.dim_size-1(row + 1)) + 1):
            for c in range(max(0, col - 1), min(self.dim_size-1, (col + 1)) + 1):
                if r == row and c == col:
                    # our location, dont check
                    continue
                if self.board[r][c] == '*':
                    num_neighboring_bombs += 1
        return num_neighboring_bombs

    def dig(self, row, col):
        # dig at that location
        # return true if successful and false otherwise

        # a few  scenarios
        # hit a bomb -> gameover
        # dig at location with neighboring  bombs
        # dig at location without neighboring bombs

        self.dug.add((row, col))

        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True

        # self.board[row][col] == 0
        for r in range(max(0, row - 1), min(self.dim_size-1(row + 1)) + 1):
            for c in range(max(0, col - 1), min(self.dim_size-1, (col + 1)) + 1):
                if (r, c) in self.dug:
                    continue  # dont dig where you have alreay gdug
                self.dig(r, c)
        return True

    def __str__(self):
        # this is a magic function where if you call print on this object
        # it'll print out what this function returns
        # return a stirng that shows the board to the board

        #first: create a new array that represents what the user would see
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row,col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else: 
                    visible_board[row][col] = ' '
         # put this together in a string
        string_rep = ''
        # get max column widths for printing
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key = len)
                )
            )

        # print the csv strings
        indices = [i for i in range(self.dim_size)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'
        
        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep  

def play(dim_size=10, num_bombs=10):
    # Primeiro crie o tabuleiro e distribua as bombas
    board = Board(dim_size, num_bombs)
    # Mostre o tabuleiro ao usuário e pergunte onde ele quer "cavar"
    # Caso o local não seja uma bomba
    # Se ele, por acaso, escolher uma bomba, mostre a mensagem de game over
    # repita 2 e 3 até não ter mais lugares para cavar
    safe = True
    while len(board.dug) < board.dim_size ** 2 - num_bombs:
        print(board)
        user_input = re.split(',(\\s)*', input("Where do you want to dig? Input as row,col: "))
        row, col = int(user_input[0]), int(user_input[-1])
        if row < 0 or row >= board.dim_size or col < 0 or col >= dim_size:
            print("Invalid location. Try again")
            continue
        
        # if it's vlaid we dig 
        safe = board.dig(row, col)
        if not safe:
            # dug a bomb :(
            break # game over rip

    if safe: 
        print("Congrats") 
    else: 
        print("sorry game over")
        board.dug = [(r,c) for r in range(board.dim_size) for c in range(board.dim_size)] 
        print(board)


if __name__ == '__main__': #good pratice
    play()
