class Board:
    def __init__(self):
        self.board = []

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
