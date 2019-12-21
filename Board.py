class Board:
    def __init__(self):
        self.board = []
        self.is_board_full = False

    def init_board(self):
        for i in range(0,3):
            self.board.append([])
            for j in range(0,3):
                self.board[i].append('-')

    def display_board(self):
        print()
        for row in self.board:
            display_row = '| '
            for box in row:
                display_row += box + ' | '
            print(display_row)
        print()

    def position_converter(self, position):
        col = int(position % 3 - 1)
        row = int((position-col) / 3 )
        if col == -1:
            col = 2
            row = row - 1
        return [row, col]

    def is_position_available(self, position):
        position = self.position_converter(position)
        if self.board[position[0]][position[1]] == '-':
            return True
        return False

    def set_board(self, position, symbol):
        position = self.position_converter(position)
        self.board[position[0]][position[1]] = symbol

    def check_rows(self):
        for row in self.board:
            if row[0] == row[1] and row[1] == row[2]:
                if row[0] != '-':
                    return row[0]

    def check_columns(self):
        board = self.board
        for i in range(0,3):
            if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
                if board[0][i] != '-':
                    return board[0][i]

    def check_diagonals(self):
        board = self.board
        if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
            if board[0][0] != '-':
                return board[0][0]
        if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
            if board[0][2] != '-':
                return board[0][2]

    def check_sequence(self):
        winner_symbol = [0]*3
        winner_symbol[0] = self.check_rows()
        winner_symbol[1] = self.check_columns()
        winner_symbol[2] = self.check_diagonals()
        for symbol in winner_symbol:
            if symbol:
                return symbol
        return None

    def check_full_board(self):
        self.is_board_full = True
        for row in self.board:
            for col in row:
                if col == '-':
                    self.is_board_full = False