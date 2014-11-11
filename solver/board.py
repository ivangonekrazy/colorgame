from itertools import product

class Cell(object):
    """ Stores the possible Pieces for any given Cell. """

    def __init__(self, height):
        self.height = height
        self.colors = list("RGBPYO")
        self.solution = None

    def set(self, color):
        if not color in self.colors:
            raise Exception("color already eliminated from this cell")

        self.solution = color

    def remove_possible(self, color):
        if color in self.colors:
            self.colors.remove(color)

    def possibilities(self):
        return len(self.colors)

    def __repr__(self):
        if self.solution:
            return "%s: __ %s __" % (self.height, self.solution)

        return "%s: <%s>" % (self.height, "".join(self.colors))


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

    def cell_iter(self):
        for r in self.cells:
            for c in r:
                yield c

    def set(self, r, c, color):
        cell = self.cells[r][c]
        height = cell.height

        cell.set(color)
        self.clear_row(r, color)
        self.clear_col(c, color)

        for c in self.cell_iter():
            if c.height == height:
                c.remove_possible(color)

        self.inventory.remove((height, color))

    def clear_row(self, r, color):
        for c in self.cells[r]:
            c.remove_possible(color)

    def clear_col(self, c, color):
        for r in self.cells:
            r[c].remove_possible(color)
