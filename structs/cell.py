"""
    Cell class
    A maze is a matrix of cells
"""

class Cell:
    def __init__(self, cell_id: int, doors: list[bool]):
        self.cell_id = cell_id
        self.doors = doors