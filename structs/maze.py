"""
    Maze

    A maze is a collection of cells
"""
from math import sqrt
from random import random as rd
from cell import Cell

MAZE_NORTH = 0
MAZE_SOUTH = 1
MAZE_EAST = 2
MAZE_WEST = 3
MAZE_DIRECTIONS = [MAZE_NORTH, MAZE_SOUTH, MAZE_EAST, MAZE_WEST]

class Maze:
    def __init__(self, width: int, height: int):
        self.maze_width = width
        self.maze_height = height
        self.matrix : list[list[Cell]] = [[Cell(width * row_id + col_id, []) for col_id in range(width)] for row_id in range(height)]
        
    @staticmethod
    def buildRandomMaze(width: int, height: int):
        random_maze = Maze(width, height)
        for row in random_maze.matrix:
            for cell in row:
                cell.doors = [rd() < 0.75 for _ in range(4)]
        return random_maze

    def are_connected_neighbors(self, cell1_id: int, cell2_id: int):
        cell1_row, cell2_row = cell1_id // self.maze_width, cell2_id // self.maze_width
        cell1_col, cell2_col = cell1_id % self.maze_width, cell2_id % self.maze_width
        is_neighbor = abs(cell1_row - cell2_row) + abs(cell1_col - cell2_col) == 1
        if not is_neighbor:
            return False
        
        # Référentiel : PAR RAPPORT À CELL1 !!!*
        direction : int|None = None
        if cell1_row == cell2_row:
            if cell2_col - cell1_col == 1:
                direction = MAZE_EAST
            elif cell2_col - cell1_col == -1:
                direction = MAZE_WEST
            else:
                direction = None
        else:
            assert cell1_col == cell2_col
            if cell2_row - cell1_row == 1:
                direction = MAZE_SOUTH
            elif cell2_row - cell1_row == -1:
                direction = MAZE_NORTH
            else:
                direction = None
        
        assert direction is not None
        
        if direction == MAZE_NORTH:
            # Veut dire que CELL2 est "juste au dessus" de CELL1
            return self.matrix[cell1_row][cell1_col].doors[MAZE_NORTH] and self.matrix[cell2_row][cell2_col].doors[MAZE_SOUTH]
        elif direction == MAZE_SOUTH:
            # Veut dire que CELL2 est "juste au dessous" de CELL1
            return self.matrix[cell1_row][cell1_col].doors[MAZE_SOUTH] and self.matrix[cell2_row][cell2_col].doors[MAZE_NORTH]
        elif direction == MAZE_EAST:
            # Veut dire que CELL2 est "à l'est" de CELL1
            return self.matrix[cell1_row][cell1_col].doors[MAZE_EAST] and self.matrix[cell2_row][cell2_col].doors[MAZE_WEST]
        else:
            # Veut dire que CELL2 est "à l'ouest" de CELL1
            return self.matrix[cell1_row][cell1_col].doors[MAZE_WEST] and self.matrix[cell2_row][cell2_col].doors[MAZE_EAST]
