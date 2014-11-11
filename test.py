from solver.board import Board

b = Board("board.txt")

b.set(0, 2, "R")

for r in b.cells:
    for c in r:
        print "\t", c,
    print 
