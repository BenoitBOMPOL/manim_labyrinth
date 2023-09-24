"""
    Graph built from maze
"""

from maze import Maze

class Graph:
    def __init__(self, maze : Maze):
        self.dims = maze.maze_width, maze.maze_height
        nb_vertices = maze.maze_width * maze.maze_height
        self.vertices = list(range(nb_vertices))
        self.adj_mat : list[list[bool]] = [[False for __ in range(nb_vertices)] for _ in range(nb_vertices)]
        for cell1_id in range(nb_vertices):
            for cell2_id in range(cell1_id + 1, nb_vertices):
                if maze.are_connected_neighbors(cell1_id, cell2_id):
                    self.adj_mat[cell1_id][cell2_id] = True
                    self.adj_mat[cell2_id][cell1_id] = True
    
    def update_adj_mat(self, maze: Maze):
        nb_vertices = len(self.vertices)
        for cell1_id in range(nb_vertices):
            for cell2_id in range(cell1_id + 1, nb_vertices):
                if maze.are_connected_neighbors(cell1_id, cell2_id):
                    self.adj_mat[cell1_id][cell2_id] = True
                    self.adj_mat[cell2_id][cell1_id] = True

    # Sommets atteignables depuis [origin]
    def dijkstra(self, origin: int):
        dist : dict = {v : float("inf") if v != origin else 0 for v in self.vertices}
        arbo : list = []
        edges : list[tuple[int, int]] = []

        finite_not_in_arbo : list = [v for v in self.vertices if (v not in arbo) and (dist[v] < float("inf"))]

        while len(finite_not_in_arbo) > 0:
            a_min = finite_not_in_arbo[0]
            m_dist = dist[a_min]
            for v in finite_not_in_arbo:
                if dist[v] < m_dist:
                    m_dist = dist[v]
                    a_min = v

            v = a_min

            # On ajoute à l'arborescence
            arbo.append(v)

            # On cherche ses voisins (licites !)
            rr, cc = v // self.dims[0], v % self.dims[0]
            possible_neighbors = [(rr, cc - 1), (rr, cc + 1), (rr - 1, cc), (rr + 1, cc)]
            allowed_neighbors = [(r, c) for (r, c) in possible_neighbors if (r >= 0) and (c >= 0) and (r < self.dims[1]) and (c < self.dims[0])]
            neighbors = [self.dims[0] * r + c for (r, c) in allowed_neighbors if self.adj_mat[self.dims[0]*rr + cc][self.dims[0]*r + c]]

            for u in neighbors:
                if u not in arbo:
                    if dist[u] > dist[v] + 1:
                        dist[u] = dist[v] + 1
                        edges.append((u, v))

            finite_not_in_arbo = [v for v in self.vertices if (v not in arbo) and (dist[v] < float("inf"))]

        print(f"dist = ")
        for u in [v for v in self.vertices if dist[v] < float("inf")]:
            print(f"\t{u} : {dist[u]}")

        return