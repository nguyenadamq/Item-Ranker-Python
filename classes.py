class RankedItem:
    def __init__(self, name, rank):
        self.name = name
        self.rank = rank
    def define(self):
        print(f"Item Name: {self.name}")
        print(f"Item rank : {self.rank}")