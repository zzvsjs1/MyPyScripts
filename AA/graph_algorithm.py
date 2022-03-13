from abc import ABCMeta, abstractmethod, ABC
from typing import Any
from enum import Enum
from queue import Queue

from LinkedList import LinkList


class VertexColor(Enum):
    WHITE = 0
    GREY = 1
    BLACK = 2


class Vertex:
    label: Any
    distance: int
    color: VertexColor

    def __init__(self, label):
        self.label = label
        self.distance = 0
        self.color = VertexColor.WHITE
        self.parent = None

    def __str__(self):
        return f'{{{self.label}, {self.color}, {self.distance}, {self.parent}}}'

    def __hash__(self) -> int:
        return hash((self.label, self.color, self.parent, self.distance))

    def __eq__(self, other: 'Vertex'):
        return self.label == other.label

    def __ne__(self, other):
        return not (self == other)


class Edge:
    v1: Vertex
    v2: Vertex
    weight: int

    def __init__(self, v1: Vertex, v2: Vertex, weight: int):
        self.v1 = v1
        self.v2 = v2
        self.weight = weight

    def get_swap(self):
        return Edge(self.v2, self.v1, self.weight)

    def __str__(self):
        return f'{{{self.v1}, {self.v2}, {self.weight}}}'

    def __hash__(self):
        return hash((self.v1, self.v2, self.weight))


class AbstractGraph(metaclass=ABCMeta):

    @abstractmethod
    def add_vertex(self, vertex):
        raise NotImplementedError('This method must be implemented.')

    @abstractmethod
    def add_edge(self, edge: Edge):
        raise NotImplementedError('This method must be implemented.')


class MyGraphAdjList(AbstractGraph, ABC):
    vertex_edge_map: dict[Vertex, LinkList]

    def __init__(self):
        self.vertex_edge_map = {}


class GraphAdjListIndirection(MyGraphAdjList):

    def __init__(self):
        MyGraphAdjList.__init__(self)

    def add_vertex(self, vertex: Vertex):
        if vertex in self.vertex_edge_map:
            raise RuntimeError(f'The vertex {vertex}, already in graph.')

        self.vertex_edge_map[vertex] = LinkList()

    def add_edge(self, edge: Edge):
        self.vertex_edge_map[edge.v1].push_back(edge)
        self.vertex_edge_map[edge.v2].push_back(edge.get_swap())

    def do_bfs(self, callable_obj):
        if not callable(callable_obj):
            raise ValueError(f'{callable_obj} is not callable')

        self.__reset_vertexes()
        cur_queue = Queue()
        cur_queue.put()

    def __reset_vertexes(self):
        for k in self.vertex_edge_map.keys():
            k.color = VertexColor.WHITE
            k.parent = None
            k.distance = 0

    def __str__(self):
        temp: list = []
        for k, v in self.vertex_edge_map.items():
            temp.append(f'Vertex: {k}')
            temp.append(' ')
            temp.append('Edge: ')
            temp.append(str(v))
            temp.append('\n')

        return ''.join(temp)


if __name__ == '__main__':
    g: GraphAdjListIndirection = GraphAdjListIndirection()
    v = Vertex('a')
    v2 = Vertex('b')
    v3 = Vertex('c')
    g.add_vertex(v)
    g.add_vertex(v2)
    g.add_vertex(v3)
    g.add_edge(Edge(v, v2, 1))
    g.add_edge(Edge(v2, v3, 1))
    g.add_edge(Edge(v, v3, 1))
    print(g)
