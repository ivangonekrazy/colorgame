import unittest
from solver.board import Board
from solver.solver import Solver

class TestSolverUtilities(unittest.TestCase):
    """ Verify solver utility methods. """

    def setUp(self):
        self.solver = Solver()
        self.board = self.solver.board

    def test_find_possibles(self):

        self.board.set_color(0, 0, 'R')
        self.board.set_color(1, 1, 'R')
        self.board.set_color(5, 5, 'R')

        self.assertEquals( 2, len(list(self.solver.possibles_for(5, 'R'))),
            "only 2,2 and 4,4 should remain as options for cells with height 5")

class TestBoard(unittest.TestCase):
    """ Verify board utilities. """

    def setUp(self):
        self.board = Board("board.txt")

    def test_iter_row(self):
        self.assertEquals( 6, len(list(self.board.iter_row(0))) )

    def test_iter_col(self):
        self.assertEquals( 6, len(list(self.board.iter_col(0))) )

class TestElimination(unittest.TestCase):
    """ Verify constraint propagation. """

    def setUp(self):
        self.board = Board("board.txt")
        self.board.set_color(0, 2, 'R')
        self.this_cell = self.board.get(0, 2)

    def test_set_color(self):
        self.assertEquals('R', self.this_cell.proposal)

    def test_set_color_failures(self):
        with self.assertRaisesRegexp(Exception, "already eliminated"):
            self.board.set_color(0, 2, 'R')

        with self.assertRaisesRegexp(Exception, "already eliminated"):
            self.board.set_color(0, 2, 'G')

    def test_row_elimination(self):
        for c in self.board.iter_row(0):
            self.assertFalse( 'R' in c.possibilities )

    def test_column_elimination(self):
        for c in self.board.iter_col(2):
            self.assertFalse( 'R' in c.possibilities )

    def test_shared_height_elimination(self):
        for c, _row, _col in self.board.iter():
            if c.height == self.this_cell.height:
                self.assertFalse( 'R' in c.possibilities )


if __name__ == "__main__":
    unittest.main()
