from board import Board

class Solver(object):

    def __init__(self, path="board.txt"):
        self.path = path
        self.reset()

    def reset(self):
        self.board = Board(self.path)

    def single_possibles(self):
        for cell, row, col in self.board.iter():
            if len(cell.possibilities) == 1:
                yield row, col

    def possibles_for(self, height, color):
        for cell, row, col in self.board.find(
                lambda cell, r, c: cell.height == height and (color in cell.possibilities) ):
            yield (cell, row, col)

    def all_proposed(self):
        return all(
            [ cell.proposal for cell, row, col in self.board.iter() ]
        )
