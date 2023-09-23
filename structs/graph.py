"""
    Graph built from maze
"""

from maze import Maze

class Graph:
    def __init__(self, maze : Maze):
        nb_vertices = maze.maze_width * maze.maze_height
        self.vertices = list(range(nb_vertices))
        self.adj_mat : list[list[bool]] = [[False for __ in range(nb_vertices)] for _ in range(nb_vertices)]
    
    def update_adj_mat(self, maze: Maze):
        nb_vertices = len(self.vertices)
        for cell1_id in range(nb_vertices):
            for cell2_id in range(cell1_id + 1, nb_vertices):
                if maze.are_connected_neighbors(cell1_id, cell2_id):
                    self.adj_mat[cell1_id][cell2_id] = True
                    self.adj_mat[cell2_id][cell1_id] = True