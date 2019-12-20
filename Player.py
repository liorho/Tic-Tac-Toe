from random import random

class Player:
    def __init__(self, type, is_turn, board):
        self.name = None
        self.symbol = None
        self.position = None
        self.is_turn = is_turn
        self.type = type
        self.board = board

    def set_name(self, name=None):
        if name is None:
            self.name = input("Hi! Insert your name: ")
        else:
            self.name = name

    def set_symbol(self, symbol=None):
        if symbol is None:
            self.symbol = input("Please insert what symbol would you like to play (X or O): ")
            while self.symbol != 'X' and self.symbol != 'O':
                self.symbol = input("Wrong action! You need to pick X or O:  ")
        else:
            self.symbol = symbol

    def toggle_turn(self):
        self.is_turn = not self.is_turn

    def position_generator(self):
        if self.type == 'human':
            return input("Choose a position from 1-9: ")
        else:
            return int(random() * 10)

    def is_position_valid(self):
        try:
            self.position = int(self.position)
            if self.position > 9 or self.position < 1:
                return False
            return True
        except:
            return False

    def set_position(self):
        if self.is_turn:
            print(f"It's {self.name} turn:")
            self.position = self.position_generator()
            while not self.is_position_valid() or not self.board.is_position_available(self.position):
                self.position = self.position_generator()
            self.board.set_board(self.position, self.symbol)
            print(f"{self.name} chose to mark {self.symbol} at position {self.position}")