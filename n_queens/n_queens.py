import sys

user_input = int(sys.argv[1]) if len(sys.argv) > 1 else 8 # default to 8x8 board


class Boards():
    def __init__(self, n):
        self.n = n
        self.boards = []
        self.simulate(set(), set(), set(), set(), 0)

    def get_boards(self):
        return str(self.boards)

    def generate_board(self, queens_position):
        board = []
        current_row = ""
        for row in range(self.n):
            for col in range(self.n):
                if (row, col) in queens_position:
                    current_row += "Q"
                else:
                    current_row += "."
            board.append(current_row)
            current_row = ""
        self.boards.append(board)

    def simulate(self, queens_position, positive_diagonal, negative_diagonal, cols, row):
        if len(queens_position) == self.n:
            self.generate_board(queens_position)
            return
        for col in range(self.n):
            if (col not in cols) and ((col-row) not in negative_diagonal) and ((row + col) not in positive_diagonal):
                self.simulate(queens_position.union({(row, col)}), positive_diagonal.union({row+col}), 
                negative_diagonal.union({col-row}), cols.union({col}), row+1) # add queen to board

boards = Boards(user_input)
print(boards.get_boards())



