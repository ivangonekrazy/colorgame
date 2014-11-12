class Cell(object):
    """ Stores the possible Pieces for any given Cell. """

    def __init__(self, height):
        self.height = height
        self.colors = list("RGBPYO")
        self.proposal = None

    def set_color(self, color):
        if not color in self.colors:
            raise Exception("color already eliminated from this cell")

        if self.proposal:
            raise Exception("This cell already has a proposal.")

        self.proposal = color
        self.colors = []

    def remove_possible(self, color):
        if color in self.colors:
            self.colors.remove(color)

    @property
    def possibilities(self):
        return self.colors

    def __repr__(self):
        if self.proposal:
            return "%s|(  %s  )" % (self.height, self.proposal)

        return "%s|{%s}" % (self.height, "".join(self.colors))


