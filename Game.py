from Player import *
from Board import *

class Game:
    def __init__(self):
        self.is_game_still_on = True
        self.board = Board()
        self.player1 = Player('human', True, self.board)
        self.player2 = Player('computer', False, self.board)

    def init_players(self):
        self.player1.set_name()
        self.player1.set_symbol()
        self.player2.set_name('Tici')
        if self.player1.symbol == 'X':
            self.player2.set_symbol('O')
        else:
            self.player2.set_symbol('X')

    def check_if_game_over(self):
        pass



    def play_game(self):
        self.init_players()
        self.board.init_board()
        self.board.display_board()
        while self.is_game_still_on:
            self.player1.set_position()
            self.player2.set_position()
            self.player1.toggle_turn()
            self.player2.toggle_turn()
            self.board.display_board()
            self.check_if_game_over()
        print('BYE BYE')