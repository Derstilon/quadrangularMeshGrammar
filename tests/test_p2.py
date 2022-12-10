import matplotlib.pyplot as plt
import networkx as nx
import pytest

from productions import P2


def test_p2_should_be_applied():
    G = nx.Graph()
    G.add_node(1, label='el', pos=(1/2, 1/2), layer=0)
    G.add_node(2, label='I', pos=(1/2, 1/2), layer=1)
    G.add_node(3, label='E', pos=(0, 0), layer=1)
    G.add_node(4, label='E', pos=(1, 0), layer=1)
    G.add_node(5, label='E', pos=(0, 1), layer=1)
    G.add_node(6, label='E', pos=(1, 1), layer=1)
    G.add_edges_from([(2, i) for i in (1, 3, 4, 5, 6)])
    G.add_edges_from([(i, i+1) for i in range(3, 6)])
    G.add_edge(3, 6)

    assert True == P2.apply(G)

    assert [(1, {'label': 'el', 'pos': (0.5, 0.5), 'layer': 0}),
            (2, {'label': 'i', 'pos': (0.5, 0.5), 'layer': 1}),
            (3, {'label': 'E', 'pos': (0, 0), 'layer': 1}),
            (4, {'label': 'E', 'pos': (1, 0), 'layer': 1}),
            (5, {'label': 'E', 'pos': (0, 1), 'layer': 1}),
            (6, {'label': 'E', 'pos': (1, 1), 'layer': 1}),
            (7, {'label': 'I', 'pos': (0.25, 0.5), 'layer': 2}),
            (8, {'label': 'I', 'pos': (0.75, 0.5), 'layer': 2}),
            (9, {'label': 'E', 'pos': (0, 0), 'layer': 2}),
            (10, {'label': 'E', 'pos': (0.5, 0.0), 'layer': 2}),
            (11, {'label': 'E', 'pos': (1, 0), 'layer': 2}),
            (12, {'label': 'E', 'pos': (0, 1), 'layer': 2}),
            (13, {'label': 'E', 'pos': (0.5, 1.0), 'layer': 2}),
            (14, {'label': 'E', 'pos': (1, 1), 'layer': 2})] == list(G.nodes(data=True))

    assert {(1, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 8), (2, 7), (3, 4), (3, 6), (4, 5),
            (5, 6), (7, 9), (7, 10), (7, 12), (7, 13), (8, 10), (8, 11), (8, 13), (8, 14),
            (9, 10), (9, 12), (10, 11), (10, 13), (11, 14), (12, 13), (13, 14)} == set(G.edges)
