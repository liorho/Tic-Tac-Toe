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

    def check_winner(self):
        self.board.check_rows()
        self.board.check_columns()
        self.board.check_diagonals()
        if self.board.winner_symbol:
            print("**** GAME OVER ****")
            if self.player1.symbol == self.board.winner_symbol:
                print(f"** {self.player1.name} is the winner **")
            else:
                print(f"** {self.player2.name} is the winner **")
            self.is_game_still_on = False

    def check_tie(self):
        self.board.check_full_board()
        if self.board.is_board_full:
            print("**** GAME OVER ****")
            print("** It's a tie **")
            self.is_game_still_on = False

    def play_game(self):
        print("*** LETS PLAY TIC-TAC-TOE ***")
        self.init_players()
        self.board.init_board()
        self.board.display_board()
        while self.is_game_still_on:
            self.player1.set_position()
            self.player2.set_position()
            self.player1.toggle_turn()
            self.player2.toggle_turn()
            self.board.display_board()
            self.check_winner()
            if not self.is_game_still_on:
                break
            self.check_tie()