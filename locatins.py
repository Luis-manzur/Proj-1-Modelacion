"""Locations Classes"""
from vertex import Vertex

class Location:
    name: str
    vertex: Vertex

    def __init__(self, name, vertex) -> None:
        self.name = name
        self.vertex = vertex