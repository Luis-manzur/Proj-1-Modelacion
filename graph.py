"""Graph class"""

from vertex import Vertex

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex: Vertex):
        if vertex.name not in self.vertices:
            self.vertices[vertex.id] = vertex

    def add_edge(self, u, v, weight):
        if u not in self.vertices:
            raise ValueError(f"Vertex {u} not in graph")
        if v not in self.vertices:
            raise ValueError(f"Vertex {v} not in graph")

        if v not in u.neighbors:
            u.neighbors[v] = 0

        u.neighbors[v] = weight

    def dijkstra(self, source):
        source.distance = 0

        unvisited = set(self.vertices.values())

        while unvisited:
            current = min(unvisited, key=lambda vertex: vertex.distance)

            for neighbor, weight in current.neighbors.items():
                new_distance = current.distance + weight

                if new_distance < neighbor.distance:
                    neighbor.distance = new_distance
                    neighbor.previous = current

            unvisited.remove(current)

        return {vertex.id: vertex.distance for vertex in self.vertices.values()}