class rankedItem:
    def __init__(self, name, rank):
        self.name = name
        self.rank = rank

        return
    def define(self):
        return (f"'{self.name}': {self.rank}")
        