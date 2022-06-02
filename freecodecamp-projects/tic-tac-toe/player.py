import math
import random

class Player:
    def __init__(self, letter):
        #le
        self.letter = letter
    
    def get_move(self, game):
        pass

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8): ')
            # we're going to check that this is a correct value by trying to cast it to an integer
            # and if it's not, then we say its invalid
            # if that spot isn't available on the board, we also say its invalid
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
            except ValueError:
                print('Invalid square. Try again')
        return val
        


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

