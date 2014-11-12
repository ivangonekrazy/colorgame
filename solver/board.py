from itertools import product
from cell import Cell

class Board(object):

    def __init__(self, path):
        self.heights = self.load_board(path)

        self.cells = [
            [Cell(c) for c in r]
            for r in self.heights
        ]

        self.inventory = list(product(range(1,7), "RGBPYO"))

    def load_board(self, path):
        """ Load and verify a board.  Returns a 6x6 list of integers
        """

        with open(path) as f:
            rows = f.readlines()

        cells = [ [int(c) for c in r.split()] for r in rows]

        assert(len(rows) == 6)
        assert(len(cells) == 6)

        return cells

    def iter(self):
        for row, r in enumerate(self.cells):
            for col, cell in enumerate(r):
                yield (cell, row, col)

    def find(self, _callable):
        for cell, row, col in self.iter():
            if _callable(cell, row, col):
                yield cell, row, col

    def iter_row(self, row):
        for cell, r, c in self.find(lambda c, _r, _c: _r == row):
            yield cell

    def iter_col(self, col):
        for cell, r, c in self.find(lambda c, _r, _c: _c == col):
            yield cell

    def get(self, r, c):
        return self.cells[r][c]

    def set_color(self, r, c, color):
        cell = self.cells[r][c]
        height = cell.height

        if color not in cell.possibilities:
            raise Exception("%s already eliminated from this Cell." % color)

        cell.set_color(color)
        self.elim_from_row(r, color)
        self.elim_from_col(c, color)

        for c, _r, _c in self.iter():
            if c.height == height:
                c.remove_possible(color)

        self.inventory.remove((height, color))


    def elim_from_row(self, r, color):
        for c in self.iter_row(r):
            c.remove_possible(color)

    def elim_from_col(self, c, color):
        for c in self.iter_col(c):
            c.remove_possible(color)

    def show(self):
        for r in self.cells:
            for c in r:
                print "\t", c,
            print 

