"""Vertex class"""

class Vertex:
    name: str
    neighbors: dict
    distance: int
    previous: any

    def __init__(self, name: str) -> None:
        self.name = name
        self.neighbors = {}

    def __repr__(self):
        return f"<Vertex {self.id}>"
